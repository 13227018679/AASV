#coding=utf-8
import os
import time
import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import HyperLPR as pr

from PIL import Image
from keras.models import *
from keras.utils import *
from keras.metrics import *
from keras import backend as K

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
fontC = ImageFont.truetype("./Font/platech.ttf", 14, 0)

os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' 

chars = [u"京", u"沪", u"津", u"渝", u"冀", u"晋", u"蒙", u"辽", u"吉", u"黑", u"苏", u"浙", u"皖", u"闽", u"赣", u"鲁", u"豫", u"鄂", u"湘", u"粤", u"桂",
             u"琼", u"川", u"贵", u"云", u"藏", u"陕", u"甘", u"青", u"宁", u"新", u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"A",
             u"B", u"C", u"D", u"E", u"F", u"G", u"H", u"J", u"K", u"L", u"M", u"N", u"P", u"Q", u"R", u"S", u"T", u"U", u"V", u"W", u"X",
             u"Y", u"Z",u"港",u"学",u"使",u"警",u"澳",u"挂",u"军",u"北",u"南",u"广",u"沈",u"兰",u"成",u"济",u"海",u"民",u"航",u"空"
             ]
results = dict()
epochs = 15
epsilon = 0.8
target_class = 2 # cucumber
prev_probs = []
sess = K.get_session()
model = pr.LPR("model/cascade.xml","model/model12.h5","model/ocr_plate_all_gru.h5")
cls_model = model.modelSeqRec

def fastdecode(y_pred):
    results = ""
    confidence = 0.0
    table_pred = y_pred.reshape(-1, len(chars)+1)
    res = table_pred.argmax(axis=1)
    for i,one in enumerate(res):
        if one<len(chars) and (i==0 or (one!=res[i-1])):
            results+= chars[one]
            confidence+=table_pred[i][one]
    confidence/= len(results)
    return results,confidence

def np2img(x):
    t = np.zeros_like(x[0])
    t[:,:,0] = x[0][:,:,2]
    t[:,:,1] = x[0][:,:,1]
    t[:,:,2] = x[0][:,:,0]
    new_img = np.clip(t, 0, 255)/255
    return new_img

def plot_img(x,name):
    plt.imshow(x.transpose(1,0,2))
    plt.grid('off')
    plt.axis('off')
    plt.savefig(name, bbox_inches='tight',pad_inches=0.0)


def drawRectBox(image,rect,addText):
    cv2.rectangle(image, (int(rect[0]), int(rect[1])), (int(rect[0] + rect[2]), int(rect[1] + rect[3])), (0,0, 255), 2,cv2.LINE_AA)
    #cv2.rectangle(image, (int(rect[0]-1), int(rect[1])-16), (int(rect[0] + 115), int(rect[1])), (0, 0, 255), -1,
    #             cv2.LINE_AA)
    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)
    draw.text((int(rect[0]+1), int(rect[1]-16)), addText, (255, 255, 255), font=fontC)
    imagex = np.array(img)
    return imagex, (int(rect[0]), int(rect[1])),  (int(rect[0] + rect[2]), int(rect[1] + rect[3]))

def dect(image):
    res_set, b_img =  model.SimpleRecognizePlateByE2E(image)
    for pstr,confidence,rect in res_set:
        if confidence>0.7:
            image, start, end = drawRectBox(image, rect, pstr+" "+str(round(confidence,3)))
            print(str(pstr) + '  ' + str(confidence))
            results['class'] = str(pstr)
            results['confidence'] = str(confidence)[:5]            
            return image, b_img


def fgsm(model,sess,sample):

    x = cv2.resize(sample,(164,48))  # 固定大小164.48
    x = np.array([x.transpose(1, 0, 2)])
    x_adv = x
    x_noise = np.zeros_like(x)

    saver = tf.train.Saver()
    if os.path.exists('noise.npy') == True:
        noise = np.load("noise.npy")
        x_adv = x_adv + noise
        
    else:
        for i in range(epochs): 
            target = K.one_hot(target_class, 84)
            loss = -1*K.categorical_crossentropy(target, model.output)
            grads = K.gradients(loss, model.input)
            delta = K.sign(grads[0])
            x_noise = x_noise + delta
            x_adv = x_adv + epsilon*delta
            x_adv = sess.run(x_adv, feed_dict={model.input:x})
            
            y_pred = model.predict(x_adv)
            y_pred = y_pred[:,2:,:]
            result, confidence = fastdecode(y_pred)
            #prev_probs.append(preds[0][target_class])

            print("Epoch "+ str(i+1) + "：", end='')
            print(str(result) + '  ' + str(confidence))
            noise = x_adv-x
            pass
        # saver.save(sess, './checkpoint_dir/MyModel')
    
    plot_img(np2img(x_adv),'./images_out/adv_img.jpg')
    plot_img(np2img(noise),'./images_out/noise_img.jpg')
    print('\n对抗结果：')
    y_pred = model.predict(x_adv)
    y_pred = y_pred[:,2:,:]
    result, confidence = fastdecode(y_pred)
    print(str(result) + '  ' + str(confidence))
    np.save("noise.npy",noise)
    np.save("adv.npy",x_adv)
    return [str(result),str(confidence)[:5]]

def predict(imgName):
    print('[-] PREDICT START.')
    img = cv2.imread(imgName)
    rect_img, bound_img = dect(img)
    x = cv2.resize(bound_img,(164,48))  # 固定大小164.48
    x = np.array([x.transpose(1, 0, 2)])
    x = np2img(x)
    plot_img(x,'./images_out/b_img.jpg')
    print('[-] PREDICT FINISH.')
    return results

    
def attack(imgName):
    print('[x] ATTACK START.')
    img = cv2.imread(imgName)
    rect_img, bound_img = dect(img)
    result,confidence = fgsm(sess=sess, model=cls_model,sample=bound_img)
    print('[x] ATTACK FINISH.')
    return [result,confidence]

if __name__ =='__main__':
    img = cv2.imread("images_in/4.jpg")
    #model.modelSeqRec.summary()

    rect_img, bound_img = dect(img)
    result,confidence = fgsm(sess=sess, model=cls_model,sample=bound_img)
    print('[o] ALL DONE.')