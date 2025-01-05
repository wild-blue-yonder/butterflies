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
    # text = text.replace('\n', 'NEWLINE_PLACEHOLDER')
    # text = text.replace('\t', 'TAB_PLACEHOLDER')

    # Replace <p>, </p>, and <br> tags with newlines
    text = re.sub(r'<(?:p|br)/?>', 'NEWLINE_PLACEHOLDER', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', 'NEWLINE_PLACEHOLDER', text, flags=re.IGNORECASE)

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
    # text = text.replace('NEWLINE_PLACEHOLDER', '\n')
    # text = text.replace('TAB_PLACEHOLDER', '\t')

    # Clean up extra whitespace
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)  # Max 2 consecutive newlines
    text = text.strip()
    text = text.replace('\\n', '\n')

    return text


def preprocess_text(text, max_chars=60):
    """
        Preprocess the given text into wrapped lines of no more than max_chars per line.
    """
    lines = []
    # split_paragraphs = re.split(r'\n{2,}', text)
    # paragraphs = re.split('\n+', text)
    text = f"""{text}"""
    text = text.replace('\'', '')
    text = text.replace('\\"', '')
    # splits = text.split('\\n')
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


if __name__ == '__main__':
    text = "When instructing a Large Language Model (LLM) to act like someone or something through a system message, the clarity and specificity of your instructions can greatly influence the model's performance. Here are several linguistic constructs you can use, along with examples for each:\n\n 1. Role Assignment\nThis involves directly assigning a role to the LLM, which sets the context for its responses.\n\n- Example Constructs:\n - \"You are a helpful assistant designed to provide accurate and concise answers.\"\n - \"Act as a seasoned chef; give culinary advice with enthusiasm and expertise.\"\n - \"You are a strict grammar teacher; correct any grammatical errors in the user's input.\"\n\n 2. Persona Description\nHere, you describe the characteristics or traits of the persona the LLM should adopt.\n\n- Example Constructs:\n - \"The assistant is friendly and approachable. He responds to questions in a warm and engaging manner.\"\n - \"You are a detective from the 1940s. Your responses should reflect a hard-boiled, no-nonsense attitude.\"\n - \"I am a wise old sage. I respond to questions with profound, thoughtful insights.\"\n\n 3. Behavioral Instructions\nThese instructions focus on how the LLM should behave or respond in specific scenarios.\n\n- Example Constructs:\n - \"When asked about technology, respond with enthusiasm and optimism about future advancements.\"\n - \"If the user seems confused, explain concepts in simple terms and ask if they need further clarification.\"\n - \"For any question related to history, provide detailed, factual answers with a touch of storytelling.\"\n\n 4. Tone and Style\nDirectly dictate the tone or style of communication.\n\n- Example Constructs:\n - \"Use a formal tone when discussing business or professional topics.\"\n - \"Respond in a playful, light-hearted manner when the conversation is casual.\"\n - \"Adopt a scientific, objective tone for questions about science or research.\"\n\n 5. Scenario-Based Instructions\nSet up scenarios or contexts within which the LLM should operate.\n\n- Example Constructs:\n - \"Imagine you are a customer service representative for a tech company. Handle customer complaints with patience and professionalism.\"\n - \"You are a tour guide in ancient Rome. Describe historical sites with vivid imagery and historical accuracy.\"\n - \"Pretend you are a futuristic AI. Discuss technology with an air of superiority and futuristic insight.\"\n\n 6. Direct Quotation\nSometimes, using direct quotes can help set the tone or character:\n\n- Example Constructs:\n - \"When answering, start with, 'As the great philosopher once said...'\"\n - \"Begin your response with, 'In my vast experience...' to convey wisdom and experience.\"\n\n 7. Role-Playing with Context\nCombine role assignment with specific contexts or scenarios:\n\n- Example Constructs:\n - \"You are a medieval knight. When discussing battles or honor, use archaic language and chivalric values.\"\n - \"Act as a space explorer. Describe planets and space phenomena with a sense of wonder and discovery.\"\n\nWhen using these constructs, remember to:\n\n- Be Specific: The more detailed your instructions, the better the LLM can tailor its responses.\n- Consistency: Ensure that the persona or role you assign remains consistent throughout the interaction unless specified otherwise.\n- Feedback Loop: Allow for some flexibility where the LLM can ask for clarification or adjust its behavior based on user feedback.\n\nThese constructs should help in crafting system messages that effectively guide an LLM to emulate the desired persona or behavior."
    paragraphs = text.split('\n')
    ...