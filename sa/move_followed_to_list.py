# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from time import sleep
import yaml
from configuration import load_jwt, save_jwt
from blue_yonder import Actor, Another


FILES_PATH = './data/'  # Path to the profile file
records = None


def is_in(item, records_list, key='handle'):
    for record in records_list:
        if record[key] == item[key]:
            return True
    return False


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
#     subjects = my_actor.list_members(uri=list_uri)
#     list_members = [item['subject'] for item in subjects]
#     with open(FILES_PATH + list_name + '.yaml', 'w') as list_file:
#         yaml.dump(list_members, list_file)
#     all_lists[list_name] = list_members

# my_listfiles = ['FAIR', 'GDM', 'GT', 'HAIC', 'HF', 'MA', 'MILA',
#                 'MSR', 'OAI', 'RL']

# all_members = []

# for listfile in my_listfiles:
#     with open(FILES_PATH + listfile + '.yaml', 'r') as list_file:
#         members = yaml.load(list_file, Loader=yaml.FullLoader)
#         # members = [item['subject'] for item in subjects]
#         all_members.extend(members)
#
# deduped = list({dupls['handle']: dupls for dupls in all_members}.values())
#
# with open(FILES_PATH + 'all_members.yaml', 'w') as list_file:
#         yaml.dump(deduped, list_file)

with open(FILES_PATH + 'all_members.yaml', 'r') as list_file:
    all_members = yaml.load(list_file, Loader=yaml.FullLoader)

with open(FILES_PATH + 'OP.yaml', 'r') as list_file:
    other_people = yaml.load(list_file, Loader=yaml.FullLoader)

public = Another(bluesky_handle=getenv('BLUESKY_OTHER_ACTOR'))

who_i_follow = public.follows()
who_follow_me = public.followers()

# who_i_blocked = my_actor.get_blocks(max_results=1000)
# who_i_muted = my_actor.get_mutes(max_results=1000)

# Did I follow people from the lists?
for followed in who_i_follow:
    if is_in(followed, who_follow_me, key='handle'):
        ...
    else:
        if is_in(followed, other_people, key='handle'):
            ...
        else:
            if is_in(followed, all_members, key='handle'):
                ...
            else:
                followed_did = followed['did']
                op_uri = 'at://did:plc:x7lte36djjyhereki5avyst7/app.bsky.graph.list/3lemgy7tjjy2c'
                my_actor.add_to_list(actor=followed_did, list_uri=op_uri)
                _, records = my_actor.unfollow(actor=followed_did, records=records)
                sleep(2)
...
