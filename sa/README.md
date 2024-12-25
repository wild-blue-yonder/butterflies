# Simple automations
Almost immediately you bump into the limitations of the Bluesky network, which is why I created a package called 'blue-yonder'. It allows you to program your own simple automations (SA) of routine tasks on BlueSky.

<br>1. The first and most obvious need that requires automation is [posting a long text](./post_long_text.py) as a thread. The text is split into as many chunks as necessary and each chunk is posted as a separate post, but all of them are organized into a continuous thread. You can also set the rules of interaction with this thread (allow only the 'mentions', 'follows' or 'list members' to respond).

<br>2. If the text is many pages long you can create a [thread of images](./post_threadof_images.py) with your text, split into numbered and ordered pages. I didn't make it particularly flexible, but you can add your own ways to depict your text with a little bit of a `pillow` magic, the code is there for grabs.