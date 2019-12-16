# coding: utf-8

import json
import logging
import requests


class WechatWorkRobot(object):

    def __init__(self, robot_url, mentioned_mobiles):
        self.webhooks_url = robot_url
        self.mentioned = mentioned_mobiles if isinstance(mentioned_mobiles, list) else [mentioned_mobiles]

    def send_requests(self, text):
        msg = {
            "msgtype": "text",
            "text": {
                "content": "{}".format(json.dumps(text) if not isinstance(text, str) else text),
                "mentioned_list": [""],
                "mentioned_mobile_list": self.mentioned
            }
        }
        logging.error(msg="{}".format(text))
        requests.post(url=self.webhooks_url, data=json.dumps(msg))


if __name__ == '__main__':
    robot = WechatWorkRobot(
        robot_url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=bb6c4d40-309d-4d7d-b585-95f6d876a206",
        mentioned_mobiles=["17623076764"]
    )
    robot.send_requests(text={"code": 0, "message": "Ok."})
