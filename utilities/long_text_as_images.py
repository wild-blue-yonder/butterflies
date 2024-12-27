# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'  # Process the text


def create_text_images(text,
                       image_size=(620, 620),
                       font_path=FONT_PATH,
                       font_size=18,
                       margin=25,
                       max_chars=60,
                       max_lines=20,
                       output_dir='images'):
    """
    Create multiple PNG images from a long text, storing them in a specified directory.

    Args:
        text (str): Input text to render
        output_dir (str): Directory to save output PNG files
        image_size (tuple): Size of the output image in pixels (width, height)
        margin (int): Margin size in pixels
        max_chars (int): Maximum characters per line
        font_size (int): Font size in pixels
        max_lines (int): Maximum number of lines per page

    Returns:
        list: Paths to created image files
    """

    # Use the defined truetype font
    font = ImageFont.truetype(font=font_path, size=font_size)
    # Calculate line spacing based on font size
    line_spacing = int(font_size * 1.5)  # 1.5 times the font size

    # Preprocess lines first
    all_lines = preprocess_text(text, max_chars=max_chars)

    # Calculate line spacing based on font size
    line_spacing = int(font_size * 1.5)  # 1.5 times the font size

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create images
    images = []
    page_num = 1

    while all_lines:
        # Create a new image with white background
        img = Image.new('RGB', image_size, color='white')
        draw = ImageDraw.Draw(img)

        # Draw text on this page
        y = margin
        lines_on_page = 0

        while all_lines and lines_on_page < max_lines:
            line = all_lines.pop(0)
            draw.text((margin, y), line, font=font, fill='black')
            y += line_spacing
            lines_on_page += 1

        # Draw page number
        page_number_text = f'- {page_num} -'
        # Get text width using font.getlength()
        page_number_width = font.getlength(page_number_text)
        draw.text(
            ((image_size[0] - page_number_width) // 2, image_size[1] - margin - font_size),
            page_number_text,
            font=font,
            fill='black'
        )

        # Save the image
        output_path = os.path.join(output_dir, f'page_{page_num:03d}.png')
        img.save(output_path, 'PNG')
        images.append(output_path)
        page_num += 1

    return images


if __name__ == "__main__":
    sample_text = """LLAMA 3.1-405B: Please provide a specific task or problem you'd like to solve.
    
    ALEX: I want to see a productive discussion of a problem in which there will be three participants - intelligent agents - each advocating for a particular point of view.
    First, let me formulate the problem, it is specified as a following story: The boy who, when asked how many legs his calf would have if he called its tail a leg, replied, ”Five”.
    Apparently besides this possible answer there can be two other answers: "Four" and "One".
    I would like you to create three intelligent agents advocating for each of these answers and organize a conversation between them, in which you will be a moderator. I would like you to print the transcript of this argument when it ends.
    
    LLAMA 3.1-405B: Welcome to the Great Calf Leg Debate!
We have three intelligent agents, each advocating for a different answer to the question: "How many legs would the calf have if its tail were called a leg?"
Let's meet our agents:

Agent 1: Literal Larry
Functionality: Language Analysis
Competences: Linguistics, Semantics
Special Tools: Dictionary, Thesaurus
"Hello! I'm Literal Larry. I believe the answer is Five. If we call the tail a leg, we're essentially redefining the term 'leg.' In this new context, the calf would indeed have five legs."

Agent 2: Logical Lucy
Functionality: Logical Reasoning
Competences: Philosophy, Critical Thinking
Special Tools: Syllogism, Argumentation Theory
"Hi! I'm Logical Lucy. I think the answer is Four. Just because we call the tail a leg doesn't change its fundamental nature. The calf still has four limbs, regardless of what we call them."

Agent 3: Creative Chris
Functionality: Lateral Thinking
Competences: Cognitive Science, Creativity
Special Tools: Analogies, Metaphors
"Hey! I'm Creative Chris. I'd argue the answer is One. If we start calling the tail a leg, we're blurring the lines between language and reality. In this thought experiment, the calf's 'legs' become a matter of interpretation. Perhaps the only true leg is the one we traditionally consider a leg – the one that's not a tail?"

Now, let's begin the discussion. I'll moderate and ensure each agent gets a chance to respond.

    Moderator (Me): Literal Larry, you're first. How do you respond to Logical Lucy's assertion that the calf still has four limbs, regardless of what we call them?
    
    Literal Larry: Ah, but that's precisely the point – we're redefining what a leg is. If we accept this new definition, the calf's tail becomes a leg, and we must count it as such.
    
    Logical Lucy: But, Literal Larry, just because we change the label doesn't change the underlying reality. The tail is still a tail, not a leg in the classical sense.
    
    Creative Chris: I think you're both missing the point. This thought experiment is not about the physical properties of the calf but about how we perceive and describe reality. By calling the tail a leg, we're challenging our assumptions about language and meaning.
    
    Moderator (Me): Interesting perspectives. Logical Lucy, how do you respond to Creative Chris's idea that this is more about language and perception than physical reality?
    
    Logical Lucy: While I see Chris's point, I still believe we must ground our understanding in objective reality. The calf's physical properties don't change just because we play with language.
    
    Creative Chris: But, Lucy, that's exactly the problem – we're assuming a fixed, objective reality. What if our perception of reality is more fluid than that?
    
    Literal Larry: I think Chris is taking this too far. We're not questioning the nature of reality; we're simply redefining a term.
    
    Moderator (Me): Alright, let's summarize. We have three distinct perspectives: Literal Larry advocating for Five, Logical Lucy arguing for Four, and Creative Chris proposing One. Each agent has presented their case and responded to counterarguments.

Now it's your turn! Which agent do you think presents the most compelling argument? Do you have any modifications or suggestions for the agents?

    ALEX: I would like to add an expert Socrates who will reconcile all the points of view and pronounce the final decision on the matter.
    
    LLAMA 3.1-405B: The Great Calf Leg Debate: The Socratic Reconciliation
We welcome Expert Socrates, a master of dialectics and critical thinking, to reconcile the perspectives of our three agents and provide a final verdict.

    Expert Socrates:
Functionality: Dialectical Reasoning
Competences: Philosophy, Critical Thinking, Rhetoric
Special Tools: Socratic Method, Elenchos
"Ah, esteemed agents, I've been following your discussion with great interest. I must say, each of you has presented compelling arguments. However, let us not be satisfied with mere opinions. We must strive for wisdom, for the truth that lies beneath the surface."

    Expert Socrates: Literal Larry, you assert that the calf has Five legs if we call its tail a leg. But tell me, dear Larry, what is the essence of a leg? Is it not a limb that serves a specific function, such as supporting the body or facilitating movement?
    
    Literal Larry: Ah, yes, that's correct.
    
    Expert Socrates: And does the tail, even if we call it a leg, serve the same function as the other four limbs?
    
    Literal Larry: Well, not exactly...
    
    Expert Socrates: I see. Then, perhaps, the tail is not a leg in the same sense as the others, despite our linguistic gymnastics?
    
    Logical Lucy: (excitedly) Ah, yes! That's precisely my point!
    
    Expert Socrates: Not so fast, dear Lucy. Your assertion that the calf has Four legs, regardless of what we call the tail, assumes a rigid definition of a leg. But what if our understanding of 'leg' is not as fixed as we think?
    
    Logical Lucy: (thoughtfully) I suppose that's possible...
    
    Expert Socrates: And Creative Chris, your proposal that the calf has One leg, because we're blurring the lines between language and reality, is intriguing. However, does this not lead to a kind of linguistic nihilism, where words lose all meaning?
    
    Creative Chris: (defensively) Not necessarily! I'm just highlighting the complexities of language and perception.
    
    Expert Socrates: I see. Well, dear agents, it seems we've reached an impasse. But fear not, for I shall offer a reconciliation...
    
    Expert Socrates: The truth lies not in the number of legs, but in our understanding of language and reality. We must acknowledge that our words and concepts are mere approximations of the world. The calf's tail, regardless of what we call it, serves a distinct function, different from the other four limbs.
    
    Expert Socrates: Therefore, I pronounce the final verdict: the calf has Four legs, in the classical sense, but our understanding of 'leg' is indeed flexible and context-dependent. We must be mindful of the complexities of language and reality, lest we become trapped in our own linguistic constructs.

** Agents:** (in unison) Ah, we see!

    And so, the Great Calf Leg Debate comes to a close. Expert Socrates has reconciled the perspectives, and we have gained a deeper understanding of the intricate relationships between language, reality, and our perceptions.

    Now, dear user, do you have any further questions or modifications to propose?
    
    ALEX: I agree with Socrates.
    
    LLAMA 3.1-405B: The Great Calf Leg Debate: Conclusion
With Expert Socrates' reconciliation and your agreement, we have reached a satisfying conclusion to the debate. The calf, indeed, has Four legs in the classical sense, but our understanding of 'leg' is nuanced and context-dependent.

Summary:
Literal Larry advocated for Five legs, emphasizing the redefinition of 'leg.'
Logical Lucy argued for Four legs, focusing on the physical properties of the calf.
Creative Chris proposed One leg, highlighting the complexities of language and perception.
Expert Socrates reconciled the perspectives, emphasizing the importance of understanding language and reality.

Key Takeaways:
Language and reality are intertwined, but distinct.
Our understanding of concepts, like 'leg,' is flexible and context-dependent.
Critical thinking and dialectical reasoning are essential for resolving complex debates.

Final Thoughts:
The Great Calf Leg Debate has demonstrated the value of collaborative critical thinking and the importance of considering multiple perspectives. By engaging with different viewpoints and subjecting them to scrutiny, we can arrive at a deeper understanding of the issues at hand.

Thank you for participating in this thought-provoking exercise! If you have any more questions or topics you'd like to explore, feel free to ask.
(And, of course, the calf is still happy to have its four legs, regardless of what we call its tail!)."""
    font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'  # or '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
    # Create images
    image_paths = create_text_images(sample_text,
                                     image_size=(620, 620),
                                     margin=25,
                                     max_chars=60,
                                     font_path=font_path,
                                     font_size=18,
                                     max_lines=20)
    ...