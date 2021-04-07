# coding: utf-8

import traceback
from timi_robot.hub import init_sdk, capture_message, async_capture_message


class SensoroLogger(object):

    def __init__(self, url, phones):
        self.url = url
        self.phones = phones

    def log(self, err=None, common_msg=None):
        msg = f"{traceback.format_exc()}" if not err else f"traceback: {traceback.format_exc()}\n\n error: {err}"
        msg = msg if not common_msg else common_msg

        if self.url and self.phones:
            init_sdk(robot_url=self.url, mentioned_mobiles=self.phones)
            capture_message(text=msg)

    async def async_log(self, err=None, common_msg=None):
        msg = f"{traceback.format_exc()}" if not err else f"traceback: {traceback.format_exc()}\n\n error: {err}"
        msg = msg if not common_msg else common_msg
        if self.url and self.phones:
            init_sdk(robot_url=self.url, mentioned_mobiles=self.phones)
            await async_capture_message(text=msg)
