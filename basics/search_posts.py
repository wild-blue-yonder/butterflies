# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from configuration import load_jwt, save_jwt
from blue_yonder import Actor
from blue_yonder.yonder import search_100_posts


query = {
        'q': 'AI',
        'sort': 'latest',
        'since': '2024-11-05T21:44:46Z',
        'until': '2024-12-10T21:44:46Z',
        'limit': 25,
        'cursor': None
}
my_actor = Actor(jwt=load_jwt())
save_jwt(my_actor.jwt)

found_posts = my_actor.search_posts(query=query, max_results=200 - query['limit'])


# posts = search_100_posts(query=query)
...