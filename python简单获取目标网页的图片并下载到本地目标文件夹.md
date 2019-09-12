python简单获取目标网页的图片并下载到本地目标文件夹

> 第一步：获取网页的源代码

```python
urllib.request.urlopen().read()
```

这个方法是获取到请求的这个url所返回的网页源代码信息数据，返回值是bytes类型时，要将其转换成utf-8才能正常显示在python程序中，所以还要调用decode()方法进行解码。

```python
def getPageCode(url):
    html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return html
```



