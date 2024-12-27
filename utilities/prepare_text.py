# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import re
import textwrap


def remove_markdown(text):
    """
    Remove Markdown and HTML formatting while preserving newlines and tabs.

    Args:
        text (str): Input text containing Markdown/HTML formatting

    Returns:
        str: Clean text with formatting removed but newlines/tabs preserved
    """
    # Store newlines and tabs by replacing them temporarily
    text = text.replace('\n', 'NEWLINE_PLACEHOLDER')
    text = text.replace('\t', 'TAB_PLACEHOLDER')

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove Markdown headers
    text = re.sub(r'#{1,6}', '', text, flags=re.MULTILINE)
    # text = re.sub(r'^\s*#{1,6}\s*', '', text, flags=re.MULTILINE)

    # Remove bold and italic (both * and _ variations)
    text = re.sub(r'\*\*(.+?)\*\*|__(.+?)__', lambda m: m.group(1) or m.group(2), text)  # Bold
    text = re.sub(r'\*(.+?)\*|_(.+?)_', lambda m: m.group(1) or m.group(2), text)  # Italic

    # Remove blockquotes
    text = re.sub(r'^\s*>\s*', '', text, flags=re.MULTILINE)

    # Remove code blocks and inline code
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`(.+?)`', r'\1', text)

    # Remove Markdown links
    text = re.sub(r'\[([^]]+)]\([^)]+\)', r'\1', text)  # [text](url)
    text = re.sub(r'\[([^]]+)]\[[^]]*]', r'\1', text)  # [text][reference]

    # Remove Markdown images
    text = re.sub(r'!\[([^]]*)\]\([^)]+\)', '', text)   # ![alt](url)

    # Remove horizontal rules
    text = re.sub(r'^\s*[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)

    # Remove list markers
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)  # Unordered lists
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)  # Ordered lists

    # Restore newlines and tabs
    text = text.replace('NEWLINE_PLACEHOLDER', '\n')
    text = text.replace('TAB_PLACEHOLDER', '\t')

    # Clean up extra whitespace
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)  # Max 2 consecutive newlines
    text = text.strip()

    return text


def preprocess_text(text, max_chars=60):
    """
        Preprocess the given text into wrapped lines of no more than max_chars per line.
    """
    lines = []
    for paragraph in text.split('\n'):
        # Handle tabs by replacing them with spaces
        paragraph = paragraph.replace('\t', '    ')

        if not paragraph.strip():
            # Preserve empty lines
            lines.append('')
            continue

        # Wrap text to fit within max_chars
        wrapped_lines = textwrap.wrap(paragraph, width=max_chars,
                                      expand_tabs=False,
                                      replace_whitespace=False,
                                      drop_whitespace=False)
        lines.extend(wrapped_lines)
    return lines