# coding: utf-8

import json
import logging
import asyncio
import requests

from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest


class WechatWorkRobot(object):

    def __init__(self, robot_url, mentioned_mobiles):
        self.webhooks_url = robot_url
        self.mentioned = mentioned_mobiles if isinstance(mentioned_mobiles, list) else [mentioned_mobiles]
        self.client = AsyncHTTPClient()
        self.msg = {
            "msgtype": "text",
            "text": {
                "content": "",
                "mentioned_list": [""],
                "mentioned_mobile_list": self.mentioned
            }
        }

    async def async_send_requests(self, text):

        logging.error(msg="{}".format(text))
        self.msg['text']['content'] = json.dumps(text) if not isinstance(text, str) else text
        request = HTTPRequest(
            url=self.webhooks_url,
            body=json.dumps(self.msg),
            method="POST",
            validate_cert=False
        )
        await self.client.fetch(request)

    def send_requests(self, text):
        logging.error(msg="{}".format(text))
        self.msg['text']['content'] = json.dumps(text) if not isinstance(text, str) else text
        requests.post(url=self.webhooks_url, data=json.dumps(self.msg))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    robot = WechatWorkRobot(
        robot_url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxx-xxx-xxxx",
        mentioned_mobiles=["17623076764"]
    )
    loop.run_until_complete(robot.async_send_requests(text={"code": 0, "message": "Ok.", "debug": "async"}))
    robot.send_requests(text={"code": 0, "medthod": "Ok", "debug": "sync"})
