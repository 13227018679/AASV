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
	``fgsm.py`` 是车牌攻击的实现
	``HyperLPR.py``是车牌LPR API
	``*_test.py``是测试代码，传上来当保存
	``/model``存放LPR model
- 大致效果
![image-20191202225801698.png](https://i.loli.net/2019/12/02/npQls86KT52cOth.png)
![image-20191202225815868.png](https://i.loli.net/2019/12/02/r8t439Hanyq71WU.png)
- 相关资源
	
	- 识别模型：HyperLPR 高性能开源中文车牌识别框架
	
		https://github.com/zeusees/HyperLPR
	
	- HikVision SDK 简单使用
	
		https://www.ryannn.com/archives/hikvision
	
	  