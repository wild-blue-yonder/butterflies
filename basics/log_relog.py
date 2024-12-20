# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import yaml
from blue_yonder import Actor

"""
    Make sure that your environment variables are set
    or uncomment the following two lines to load them 
    from a .env file (see the .env_example file).
"""
# import dotenv
# dotenv.load_dotenv()

# Path to the file where JASON Web Token will be stored.
JWT_PATH = './configuration/jwt.yaml'  # Path to the JWT file


def log_in():
    # Instantiate the client
    my_actor = Actor()

    # The session parameters are in a JASON Web Token,
    # or JWT for short.
    jwt = my_actor.jwt

    # We will save it in a yaml file.
    with open(JWT_PATH, 'w') as jwt_file:
        yaml.dump(jwt, jwt_file)

    return my_actor


def relogin():
    with open(JWT_PATH, 'r') as jwt_file:
        jwt = yaml.load(jwt_file, Loader=yaml.BaseLoader)

    # Instantiate a client with the old session (jwt).
    previous_actor = Actor(jwt=jwt)
    return previous_actor


if __name__ == '__main__':
    """ 
        This is a simple example of how to log in and relog in.
    """
    my_actor = log_in()
    my_restored_actor = relogin()
    # You can compare the JWT properties of the two actors
    # my_actor.jwt() and my_restored_actor.jwt()

    """ 
        I created a couple of convenience functions in the
        configuration 'sub-package'. Namely:
        save_jwt(jwt) and load_jwt(). They will save and load
        in that directory as a yaml file.
        I will be using them in what follows.
    """

    from configuration import save_jwt, load_jwt

    another_restored_actor = Actor(jwt=load_jwt())
    save_jwt(another_restored_actor.jwt)

    ...  # this is for setting a breakpoint.