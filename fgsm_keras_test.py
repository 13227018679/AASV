import sys
import os
import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

from PIL import Image

from keras.models import Sequential
from keras.models import load_model
from keras.metrics import categorical_accuracy

from cleverhans.attacks import SaliencyMapMethod
from cleverhans.attacks import FastGradientMethod
from cleverhans.utils_keras import KerasModelWrapper
from cleverhans.utils import AccuracyReport

from keras import backend as K

def loadImg(path): # 1.读取图像，并转换为灰度图像
    print("加载 "+ str(path))
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray

def binary(image): # 1.将图像二值化，并显示

    img_thre = image
    cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV, img_thre)
    #cv2.imshow('threshold', img_thre)
    #cv2.waitKey(0)
    return img_thre

def plot_img(x):
    """
    x is a BGR image with shape (? ,224, 224, 3) 
    """
    t = np.zeros_like(x[0])
    t[:,:,0] = x[0][:,:,2]
    t[:,:,1] = x[0][:,:,1]
    t[:,:,2] = x[0][:,:,0]  
    plt.imshow(np.clip((t+[123.68, 116.779, 103.939]), 0, 255)/255)
    plt.grid('off')
    plt.axis('off')
    plt.show()



epochs = 400
epsilon = 0.01
target_class = 2 # cucumber
prev_probs = []
TEST_PATH = 'C:/Luty/code/AASV/data/test-set/'

x = binary(loadImg(TEST_PATH + '1.bmp')).reshape(1,40,32,1)


# Get current session (assuming tf backend)
sess = K.get_session()
# Initialize adversarial example with input image
x_adv = x
# Added noise
x_noise = np.zeros_like(x)

model = load_model('my_model.h5')
model.summary()
preds = model.predict(x)
print(preds)


for i in range(epochs): 
    # One hot encode the target class
    target = K.one_hot(target_class, 40)
    # Get the loss and gradient of the loss wrt the inputs
    loss = -1*K.categorical_crossentropy(target, model.output)
    grads = K.gradients(loss, model.input)

    # Get the sign of the gradient
    delta = K.sign(grads[0])
    x_noise = x_noise + delta
    # Perturb the image
    x_adv = x_adv + epsilon*delta
    
    # Get the new image and predictions
    x_adv = sess.run(x_adv, feed_dict={model.input:x})
    preds = model.predict(x_adv)
    plot_img(x_noise)
    # Store the probability of the target class
    prev_probs.append(preds[0][target_class])

    if i%20==0:
        print(i, preds[0])

plot_img(x_adv)

'''
result = model.predict(binary(loadImg(TEST_PATH + '2.bmp')).reshape(1,40,32,1),batch_size=1)

print(int(np.argwhere(result[0] == 1)))

sess = K.get_session()
write = tf.summary.FileWriter('C://TensorBoard//test',sess.graph)
write.close()



wrap_model = KerasModelWrapper(model)
#fgsm = FastGradientMethod(wrap_model, sess=sess)

jsma = SaliencyMapMethod(wrap_model, sess=sess)
jsma_params = {'theta': 1., 'gamma': 0.1,
                'clip_min': 0., 'clip_max': 1.,
                'y_target': None}


model.summary()


image = binary(loadImg(TEST_PATH + '1.bmp')).reshape(1,40,32,1)

adv_x = fgsm.generate_np(image, **jsma_params)
#x_adv = fgsm.generate_np(image, **fgsm_params)
im = Image.fromarray(np.uint8(adv_x.reshape(40,32,1)))
im.show()
'''