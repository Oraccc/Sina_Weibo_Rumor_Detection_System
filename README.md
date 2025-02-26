## Sina Weibo Rumor Detection System

>  第十四届全国大学生信息安全竞赛作品赛参赛作品：微博虚假新闻智能辅助检测系统

>  The 14th National College Student Information Security Competition Entry: "Sina Weibo Rumor Detection System"



### 1. Project Introduction

In the age of Internet, fake news (or rumors) spreads widely and has a wide range of audiences, which causes wrong public opinion orientation easily, and ultimately harm the credibility of news public opinion. At present, the detection of fake news on Weibo mainly relies on *"users' independent reporting"*, and there is no automatic detection system for fake news on Weibo, which not only causes serious misreporting, but also has low efficiency and accuracy. 

In view of this background and demand, our project innovatively proposes an intelligent auxiliary detection system for fake news on Sina Weibo. Our system is mainly divided into five modules: **"Irrelevant Microblog Filtering Module"**, **"Known Fake News Discrimination Module"**, **"Fake News Detection Module of Tracing Stolen Image"**, **"Image Tampering Detection Module"**, and **"Comment Semantic Analysis Module"**.



- **System Structure**

  ![flow chart](https://raw.githubusercontent.com/oraccc/Sina-Weibo-Rumor-Detection-System/master/images/flow%20chart.jpg)

- **Modules and Algorithms**

  | Modules                                                      | Algorithms Used                                              |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | **1**: Irrelevant Microblog Filtering Module（无关微博过滤模块） | [BERT-DPCNN](https://link.springer.com/chapter/10.1007/978-981-15-8599-9_60) |
  | **2**: Known Fake News Discrimination Module （已知虚假新闻检测模块） | [CARMN](https://www.sciencedirect.com/science/article/abs/pii/S0306457320309304) |
  | **3**: Image Tampering Detection Module （图片篡改检测模块） | [RGB-N](https://openaccess.thecvf.com/content_cvpr_2018/papers/Zhou_Learning_Rich_Features_CVPR_2018_paper.pdf), [ResNet](https://arxiv.org/abs/1512.03385) |
  | **4**: Fake News Detection Module of Tracing Stolen Image （基于溯源的盗图新闻检测模块） | [SimNet](https://www.paddlepaddle.org.cn/modelbasedetail/SimNet) (by PaddlePaddle) |
  | **5**: Comment Semantic Analysis Module （评论语义分析模块） | [TextCNN](https://arxiv.org/abs/1408.5882)                   |



### 2. Usage

* **Environment**
  * Django >= 3.0
  * wagtail >= 2.9
* **Run System**
  * `python manage.py makemigrations`
  * `python manage.py migrate`
  * `python manage.py runserver`
  * open browser and visit `127.0.0.1:8000/login`
    * username: admin
    * password: 123456

### 3. System Screenshot Samples

* **Main Panel**

  <img src="https://raw.githubusercontent.com/oraccc/Sina-Weibo-Rumor-Detection-System/master/images/system1.png" style="zoom: 50%;" />

* **Keywords Association Graph**

  <img src="https://raw.githubusercontent.com/oraccc/Sina-Weibo-Rumor-Detection-System/master/images/system2.png" style="zoom: 50%;" />

* **Single Post Detection Page**

  <img src="https://raw.githubusercontent.com/oraccc/Sina-Weibo-Rumor-Detection-System/master/images/system3.png" style="zoom: 50%;" />

* **Detection Result Detail Panel**

  <img src="https://raw.githubusercontent.com/oraccc/Sina-Weibo-Rumor-Detection-System/master/images/system4.png" style="zoom: 67%;" />

* **Built-in Fake News Database**

  <img src="https://raw.githubusercontent.com/oraccc/Sina-Weibo-Rumor-Detection-System/master/images/system5.png" style="zoom: 67%;" />