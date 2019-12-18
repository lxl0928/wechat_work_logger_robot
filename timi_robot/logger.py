# coding: utf-8

import traceback
from timi_robot.hub import init_sdk, capture_message


class SensoroLogger(object):

    def __init__(self, url, phones):
        init_sdk(robot_url=url, mentioned_mobiles=phones)

    async def log(self, err=None):
        if err:
            msg = "traceback: {}\n\n error: {}".format(traceback.format_exc(), err)
        else:
            msg = "{}".format(traceback.format_exc())

        await capture_message(text=msg)
