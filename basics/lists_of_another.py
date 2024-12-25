# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
import yaml
from blue_yonder import Another


PROFILE_PATH = './data/another.yaml'  # Path to the profile file


another = Another(bluesky_handle=getenv('BLUESKY_OTHER_ACTOR'))

# We will save it in a yaml file.
with open(PROFILE_PATH, 'w') as profile_file:
    yaml.dump(another, profile_file)

associated_of_another = another.associated
lists_of_another = another.get_lists()
list_members = another.read_list(uri='at://did:plc:x7lte36djjyhereki5avyst7/app.bsky.graph.list/3ldckd6tqsk2j')
...