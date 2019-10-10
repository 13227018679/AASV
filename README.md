## Adversarial Attack on Smart Vehicle

- 编码环境

  - python 3.6.*
  - pip 19.*

- 依赖库

  ```bash
  # 参考requirements.txt
  pip install -r requirements.txt
  ```

- 目前功能
	 - [x] 车牌识别 + 攻击
	 - [ ] LOGO识别 + 攻击
	 - [ ] 检测攻击
	 - [ ] 监控场景
	 - [x] FGSM
	 - [ ] DeepFool
	 - [ ] JSMA
	 - [ ] black-box
- 目录简介
	``fgsm.py`` 是车牌攻击的实现
	``HyperLPR.py``是车牌LPR API
	``*_test.py``是测试代码，传上来当保存
	``/model``存放LPR model
- 相关资源
	
	- 识别模型：HyperLPR 高性能开源中文车牌识别框架
	
		https://github.com/zeusees/HyperLPR
	
	- HikVision SDK 简单使用
	
		https://www.ryannn.com/archives/hikvision
	
	  