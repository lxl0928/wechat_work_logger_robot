# coding: utf-8

from setuptools import setup

setup(
    name="timi-robot",
    version="1.2.0",
    url='https://github.com/lxl0928/wechat_work_logger_robot',
    author='Timi long',
    author_email='lixiaolong@smuer.cn',
    description='基于机器微信机器人实现的线上日志错误回调。',
    long_description="""基于机器微信机器人实现的线上日志错误回调。使用方法见README.md""",
    packages=['timi_robot'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    extras_require={
        "requests": ["tornado", "request"],
    },
    install_requires=["tornado==6.0.2", "requests==2.24.0"]
)
