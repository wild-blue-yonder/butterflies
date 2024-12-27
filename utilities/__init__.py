# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from .prepare_text import remove_markdown, preprocess_text
from .long_text_as_images import create_text_images


__all__ = [
    'remove_markdown',
    'preprocess_text',
    'create_text_images'
]

__version__ = '0.0.1'