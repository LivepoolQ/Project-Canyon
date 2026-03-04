"""
@Author: Ziqian Zou
@Date: 2026-02-05 16:26:58
@LastEditors: Ziqian Zou
@LastEditTime: 2026-03-04 16:29:27
@Description: file content
@Github: https://github.com/LivepoolQ
@Copyright 2026 Ziqian Zou, All Rights Reserved.
"""

import sys

import kayak
import qpid

"""
This repo is compatible with our previous models.
Put their model folders (not the whole repo) into this folder to enable them.

File structures:

(root)
    |___qpid
    |___dataset_original
    |___dataset_configs
    |___dataset_processed
    |___main.py
    |___kayak            
    |___...
"""


if __name__ == '__main__':
    qpid.entrance(sys.argv)
