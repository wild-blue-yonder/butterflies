# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import os
import yaml

# Location of the file that is running
WHERE_ARE_WE = os.path.dirname(__file__)


def go_configure(config_file: str = 'config.yaml'):
    config_path = os.path.join(WHERE_ARE_WE, 'config.yaml')
    with open(config_path, 'r') as yaml_file:
        config_yaml = yaml_file.read()
        config = yaml.load(config_yaml, Loader=yaml.FullLoader)
    return config


def load_jwt():
    jwt_path = os.path.join(WHERE_ARE_WE, 'jwt.yaml')
    with open(jwt_path, 'r') as jwt_file:
        jwt = yaml.load(jwt_file, Loader=yaml.FullLoader)
    return jwt


def save_jwt(jwt):
    jwt_path = os.path.join(WHERE_ARE_WE, 'jwt.yaml')
    with open(jwt_path, 'w') as jwt_file:
        yaml.dump(jwt, jwt_file)
