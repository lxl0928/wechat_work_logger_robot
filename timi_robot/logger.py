# coding: utf-8

import traceback
from timi_robot.hub import init_sdk, capture_message


class SensoroLogger(object):

    def __init__(self, url, phones):
        init_sdk(robot_url=url, mentioned_mobiles=phones)

    def log(self, err=None):
        if err:
            msg = "error: {}, traceback: {}".format(err, traceback.format_exc())
        else:
            msg = "{}".format(traceback.format_exc())

        capture_message(text=msg)
