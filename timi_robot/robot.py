# coding: utf-8

import json
import logging
import asyncio

from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest


class WechatWorkRobot(object):

    def __init__(self, robot_url, mentioned_mobiles):
        self.webhooks_url = robot_url
        self.mentioned = mentioned_mobiles if isinstance(mentioned_mobiles, list) else [mentioned_mobiles]
        self.client = AsyncHTTPClient()

    async def send_requests(self, text):
        msg = {
            "msgtype": "text",
            "text": {
                "content": "{}".format(json.dumps(text) if not isinstance(text, str) else text),
                "mentioned_list": [""],
                "mentioned_mobile_list": self.mentioned
            }
        }
        logging.error(msg="{}".format(text))
        request = HTTPRequest(url=self.webhooks_url, body=json.dumps(msg), method="POST")
        await self.client.fetch(request)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    robot = WechatWorkRobot(
        robot_url="http://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxxx-xxxx-xxx",
        mentioned_mobiles=["17623076764"]
    )
    loop.run_until_complete(robot.send_requests(text={"code": 0, "message": "Ok."}))
