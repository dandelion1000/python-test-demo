# python-test-demo
python简单获取目标网页的图片并下载到本地目标文件夹

##### 以爬取https://zhuanlan.zhihu.com/p/26019553该网页的图片和小标题为例

> 一：获取网页的源代码

```python
#首先将urllib.request引入，
#使用urllib.request.urlopen().read()方法请求url所返回的网页源代码,返回值是bytes类型时，要将其转换成utf-8才能正常显示在python程序中，所以还要调用decode()方法进行解码。
import urllib.request 
```

这个方法是获取到请求的这个url所返回的网页源代码信息数据，返回值是bytes类型时，要将其转换成utf-8才能正常显示在python程序中，所以还要调用decode()方法进行解码。

```python
url = "https://zhuanlan.zhihu.com/p/26019553"
htmlCode = urllib.request.urlopen(url).read().decode("utf-8", "ignore")

```

> 二：过滤图片url

使用正则表达式匹配，每个网站目标图片是不一样的，匹配的模式也不一样，本例网页

**re.compile()**  根据包含的正则表达式的字符串创建模式对象（直接拿来用就好）

**findall()**  返回string中所有与pattern相匹配的全部字串，返回形式为数组

```python
imgRex = '<img src="(http.*?\.png)"'
imgReList = re.compile(imgRex).findall(html)
```

> 三：定义图片保存路径

新建文件夹需要调用**os.makedirs()**方法，所以先引入os

**os.getcwd()**:获取当前目录

```python
import os
path = os.getcwd() + '/' + 'test'
os.makedirs(path)
```

**urllib.request.urlretrieve(imgurl, filename)**  这个方法就是将远程数据下载到本地

imgurl即图片的url，filename即如何命名下载的图片

本例得到的imgReList是一个数组，所以需要for循环，另外我将以循环的index作为命名图片的依据

```python
for index in range(len(imgReList)):
urllib.request.urlretrieve(imgReList[index], os.getcwd() + '/test/' + str(index) + '.png')

```

执行之后就会发现目标路径出现一个test文件夹，且里面有目标图片

![图片](https://coding-net-production-pp-ci.codehub.cn/971b1aa7-2174-4413-a02b-b0ef5d6cf2f4.png)













