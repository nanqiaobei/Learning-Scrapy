# Learning-Scrapy

 Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 其可以应用在数据挖掘，信息处理或存储历史数据等一系列的程序中。 其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的， 也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。

# Scrapy 使用了 Twisted异步网络库来处理网络通讯。整体架构大致如下

![image](https://github.com/nanqiaobei/Learning-Scrapy/raw/master/image/img01.png)

# Scrapy主要包括了以下组件：

## 引擎(Scrapy)
    用来处理整个系统的数据流处理, 触发事务(框架核心)
## 调度器(Scheduler)
    用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取  的网址是什么, 同时去除重复的网址
## 下载器(Downloader)
    用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)
## 爬虫(Spiders)
    爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面项目管道(Pipeline)
    负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的 次序处理数据。
## 下载器中间件(Downloader Middlewares)
    位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应。
## 爬虫中间件(Spider Middlewares)
    介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出。
## 调度中间件(Scheduler Middewares)
    介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应。
# Scrapy运行流程大概如下：
    1.引擎从调度器中取出一个链接(URL)用于接下来的抓取
    2.引擎把URL封装成一个请求(Request)传给下载器
    3.下载器把资源下载下来，并封装成应答包(Response)
    4.爬虫解析Response
    5.解析出实体（Item）,则交给实体管道进行进一步的处理
    6.解析出的是链接（URL）,则把URL交给调度器等待抓取
# 2. 基本命令
1. scrapy startproject 项目名称
   - 在当前目录中创建中创建一个项目文件（类似于Django）
2. scrapy genspider [-t template] <name> <domain>
   - 创建爬虫应用
   如：
      scrapy gensipider -t basic oldboy oldboy.com
      scrapy gensipider -t xmlfeed autohome autohome.com.cn
   PS:
      查看所有命令：scrapy gensipider -l
      查看模板命令：scrapy gensipider -d 模板名称
3. scrapy list
   - 展示爬虫应用列表
4. scrapy crawl 爬虫应用名称
   - 运行单独爬虫应用
# 3.项目结构以及爬虫应用简介
 >project_name/   <br>
    scrapy.cfg   <br>
    project_name/ <br>
      >> __init__.py<br>
       >>items.py<br>
       >>pipelines.py<br>
       >>settings.py<br>
       >>spiders/<br>
          >>> __init__.py<br>
           >>>爬虫1.py<br>
           >>>爬虫2.py<br>
           >>>爬虫3.py<br>
文件说明：
scrapy.cfg  项目的主配置信息。（真正爬虫相关的配置信息在settings.py文件中）<br>
items.py    设置数据存储模板，用于结构化数据，如：Django的Model<br>
pipelines    数据处理行为，如：一般结构化的数据持久化<br>
settings.py 配置文件，如：递归的层数、并发数，延迟下载等<br>
spiders      爬虫目录，如：创建文件，编写爬虫规则<br>
注意：一般创建爬虫文件时，以网站域名命名<br>
# 破解滑动验证码的方法
 一些网站加入了滑动验证码，最典型的要属于极验滑动认证了，极验官网：http://www.geetest.com/，下图是极验的登录界面<br>
![image](https://github.com/nanqiaobei/Learning-Scrapy/raw/master/image/img02.png)<br>
 
我们可以用selenium驱动浏览器来解决这个问题，大致分为以下几个步骤<br>
  步骤一:点击按钮，弹出没有缺口的图片<br>
  步骤二：获取步骤一的图片<br>
  步骤三：点击滑动按钮，弹出带缺口的图片<br>
  步骤四：获取带缺口的图片<br>
  步骤五：对比两张图片的所有RBG像素点，得到不一样像素点的x值，即要移动的距离<br>
  步骤六：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹<br>
  步骤七：按照轨迹拖动，完全验证<br>
  步骤八：完成登录<br>
 # 爬虫技术与反爬虫技术直接的关系
![image](https://github.com/nanqiaobei/Learning-Scrapy/raw/master/image/img03.png)<br>
# 爬虫验证码破解之输进式验证码
解决思路：这种是最简单的一种，只要识别出里面的内容，然后填入到输入框中即可。这种识别技术叫OCR，这里我们推荐使用Python的第三方库，tesserocr。对于没有什么背影影响的验证码如图2，直接通过这个库来识别就可以。但是对于有嘈杂的背景的验证码这种，直接识别识别率会很低，遇到这种我们就得需要先处理一下图片，先对图片进行灰度化，然后再进行二值化，再去识别，这样识别率会大大提高。
# 关于cnblog的说明
上面部分详细介绍了scrapy的工作流程，以及如何创建一个爬虫和运行一个爬虫
cnblog是基于爬虫框架scray爬取cnblog一些帖子的相关信息，爬取了每个帖子的作者，标题，以及URL连接，使用json格式存放的
![image]()
