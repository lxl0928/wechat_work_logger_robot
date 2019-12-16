# wechat_work_logger_robot
基于企业微信机器人，封装统一的Logger。

# 使用方法
```
# coding: utf-8

from timi_robot import SensoroLoggerClient

logger = SensoroLoggerClient(
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxxx-xxxx-xxxxxxxx",
        phones=["17623076764"]
)

logger.log(err={"code": 40010, "message": "参数错误!"})
```

# 安装方式
```
pip3 install timi-robot==1.0.1
```

# 使用方法
![图片](http://qiniucdn.timilong.com/timi-robot-1.0.1.png)

# 使用效果
![图片](http://qiniucdn.timilong.com/timi-robot.png)
