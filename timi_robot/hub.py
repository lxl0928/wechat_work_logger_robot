# coding: utf-8

from timi_robot.robot import WechatWorkRobot

settings = {
    "url": "",
    "phones": ""
}


def init_sdk(robot_url, mentioned_mobiles):
    settings['url'] = robot_url
    settings['phones'] = mentioned_mobiles
    return WechatWorkRobot(robot_url=settings.get('url'), mentioned_mobiles=settings.get('phones'))


def capture_message(text):
    assert settings.get('url'), "请init_sdk, 填入正确的企业微信机器人回调地址!"
    assert settings.get('phones'), "请init_sdk, 填入正确的@联系人手机号!"
    WechatWorkRobot(
        robot_url=settings.get('url'),
        mentioned_mobiles=settings.get('phones')
    ).send_requests(text=text)


async def async_capture_message(text):
    assert settings.get('url'), "请init_sdk, 填入正确的企业微信机器人回调地址!"
    assert settings.get('phones'), "请init_sdk, 填入正确的@联系人手机号!"
    await WechatWorkRobot(
        robot_url=settings.get('url'),
        mentioned_mobiles=settings.get('phones')
    ).async_send_requests(text=text)
