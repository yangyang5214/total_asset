> [且慢](https://qieman.com/)

一个买基金的平台。。。

> charles 抓包

![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/uPic/xWFI4p.png)

> 经测试，最终只和这两个参数有关

![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/uPic/VdXxKY.png)

- Authorization. Token 认证 => 需要知道 token 是怎么生成的
- x-sign. 比较常见的 x-sign 算法

#### Authorization

> 盲猜是 微信平台的 token。我是微信登录的

本来想模拟微信登录的，但是自己手机还要用，所以这个参数就抓包获取吧。只要不退出登录一般会自己续命。。。

APi: 

```
https://api.qieman.com/pmdj/v1/wechat/login

body:
# code 参数没找到怎么获取的。。。可能是 tcp 协议传输生成的，因为api 会校验 code （或者一些算法校验的，没解决）
{
	"code": "001fT8ll2XEP984QLonl21nR7U1fT8l7",
	"type": "mobile"
}

header:
# 以下两个是必填的
x-sign: xxx
Content-Type: application/json
```

#### x-sign

> 借助  jadx 轻松拿下 **x-sign** 生成方式

![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/uPic/TDaf4I.png)



![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/uPic/UhKVTK.png)

![](https://beef-1256523277.cos.ap-chengdu.myqcloud.com/uPic/IltMBX.png)

可以看到算法的核心是  时间戳 + 时间戳运算得到的 sha256。所以这个字段不能乱传，需要按照上面的算法生成。

> 但是，目前看来，只会校验格式是否对，并没有校验时间是否过期。。。所以那就接着用。。。

总结: 抓到 **https://api.qieman.com/pmdj/v2/asset/summary** 的请求就行了。。。

