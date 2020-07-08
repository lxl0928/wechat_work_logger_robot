# wechat_work_logger_robot
基于企业微信机器人，封装统一的Logger。

# 安装方式
```
pip3 install timi-robot==1.0.1
```

# 使用方法
```python
# coding: utf-8
import asyncio
from timi_robot import SensoroLoggerClient

if __name__ == '__main__':
    loop = asyncio.get_event_loop() 
    logger = SensoroLoggerClient(
            url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxxx-xxxx-xxxxxxxx",
            phones=["17623076764"]
    )
    loop.run_until_complete(
        logger.async_log(err={"code": 40010, "message": "参数错误!"})
    )
```


# 使用方法
http://qiniucdn.timilong.com/timi-robot-1.0.1.png

![图片](http://qiniucdn.timilong.com/timi-robot-1.0.1.png)


# 使用效果
http://qiniucdn.timilong.com/timi-robot.png

![图片](http://qiniucdn.timilong.com/timi-robot.png)


# 说明
上述模块是基于HTTP请求完成的数据传输及回调，在发生异常时，务必会阻塞Web服务器端的业务，请按自身业务，酌情考虑是否要使用此工具。
