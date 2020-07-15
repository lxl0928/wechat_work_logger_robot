# coding: utf-8

import traceback
from timi_robot.hub import init_sdk, capture_message, async_capture_message


class SensoroLogger(object):

    def __init__(self, url, phones):
        init_sdk(robot_url=url, mentioned_mobiles=phones)

    def log(self, err=None, common_msg=None):
        msg = "{}".format(traceback.format_exc())
        if err:
            msg = "traceback: {}\n\n error: {}".format(traceback.format_exc(), err)

        if common_msg:
            msg = common_msg

        capture_message(text=msg)

    async def async_log(self, err=None, common_msg=None):
        msg = "{}".format(traceback.format_exc())
        if err:
            msg = "traceback: {}\n\n error: {}".format(traceback.format_exc(), err)

        if common_msg:
            msg = common_msg

        await async_capture_message(text=msg)
