# coding: utf-8

from timi_robot import SensoroLoggerClient

logger = SensoroLoggerClient(
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxxx-xxxx-xxxxxxxx",
        phones=["17623076764"]
)

logger.log(err={"code": 40010, "message": "参数错误!"})
