

## Adversarial Attack on Smart Vehicle

- 编码环境

  - python 3.6.*

- 依赖

  ```bash
  pip install -r requirements.txt
  ```

- 目前功能
	 - [x] 车牌识别攻击
	 - [x] 演示GUI
	 - [x] 监控场景
	 - [x] FGSM
	 - [ ] DeepFool
	 - [ ] JSMA
	 - [ ] 检测攻击

- 目录简介
	
	
	
	``LPR_fgsm.py`` 攻击实现
	
	
	
	``HyperLPR.py`` 车牌LPR API
	
	
	
	``GUI_demo.py`` 演示GUI
	
	
	
	``/model`` 模型文件
	
	
	
- 效果
- ![result.png](https://i.loli.net/2019/12/10/7NumiVAKyptlkhz.png)
  ![video.jpg](https://i.loli.net/2019/12/10/DLQbwdoYxg1KCUW.jpg)
  
- 相关资源
	
	- 识别模型：HyperLPR 高性能开源中文车牌识别框架
	
		https://github.com/zeusees/HyperLPR
	
	- HikVision SDK 简单使用
	
		https://www.ryannn.com/archives/hikvision
	
	  