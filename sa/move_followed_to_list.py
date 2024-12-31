# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
import yaml
from configuration import load_jwt, save_jwt
from blue_yonder import Actor, Another


FILES_PATH = './data/'  # Path to the profile file


my_actor = Actor(
    bluesky_handle=getenv('BLUESKY_OTHER_ACTOR'),
    jwt=load_jwt())
save_jwt(my_actor.jwt)

# lists_of_my_actor = my_actor.get_lists()
#
# all_lists = {}  # All members of all lists.
# for one_list in lists_of_my_actor:
#     list_uri = one_list['uri']
#     list_name = one_list['value']['name']
#     list_members = my_actor.list_members(uri=list_uri)
#     with open(FILES_PATH + list_name + '.yaml', 'w') as list_file:
#         yaml.dump(list_members, list_file)
#     all_lists[list_name] = list_members

public = Another(bluesky_handle=getenv('BLUESKY_OTHER_ACTOR'))

who_i_follow = public.follows()
who_follow_me = public.followers()

who_i_blocked = my_actor.get_blocks(max_results=1000)
who_i_muted = my_actor.get_mutes(max_results=1000)

records = None
# Did I block somebody who I follow? Then - unfollow them.
for followed in who_i_follow:
    did = followed['did']
    for blocked in who_i_blocked:
        if blocked['did'] == did:
            _, records = my_actor.unfollow(did=did, records=records)
...