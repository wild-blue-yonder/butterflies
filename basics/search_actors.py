# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from blue_yonder import yonder


actors = yonder.search_actors(query={'q': 'ML/AI', 'limit': 50}, max_results=1000)
...