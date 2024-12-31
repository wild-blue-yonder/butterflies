# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from blue_yonder import Actor, Another


handle = 'shay0147.bsky.social'

my_actor = Actor(bluesky_handle=getenv('BLUESKY_OTHER_ACTOR'))

intruder = Another(bluesky_handle=handle)

result = my_actor.block(block_actor=intruder.did)
...