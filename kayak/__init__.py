"""
@Author: Ziqian Zou
@Date: 2026-03-04 14:57:40
@LastEditors: Ziqian Zou
@LastEditTime: 2026-03-04 16:01:03
@Description: file content
@Github: https://github.com/LivepoolQ
@Copyright 2026 Ziqian Zou, All Rights Reserved.
"""
import qpid

from .__args import KayakArgs
from .model import Kayak, KayakModel

qpid.register(kk=[Kayak, KayakModel])
qpid.register_args(KayakArgs, 'kayak args')
