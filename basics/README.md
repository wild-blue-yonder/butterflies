# Basics
In order to start making your own automations you need to know a bit about the sequence of actions the Bluesky network expects from your program, which I will loosely call an **Actor** or **Automaton** in the texts below.
### Log-in
Your program will need to log into the Bluesky network. The network issues your Actor a **JWT** (JSON Web Token) that it will be using in its communications with the network. The number of 'log-ins' you can make in a day is limited, that's why it is _really_ helpful to have a JWT saved in a file if you are going to launch your automaton many times a day. Here's the first useful piece of code for you:

<br>1. How to [log and relog](./log_relog.py) your Actor into the Bluesky network.

<br>2. How to post text, reply to it with text and set the rules of interaction for a thread: [lifecycle of a post](./post_lifecycle.py). If you need more automatons generating threads for you, check out the [simple automations](./sa/README.md).

<br>3. How to [upload and post images](./post_images.py).

<br>4. How to [post quotes](./post_quote.py) of other posts.

<br>3. How to read the lists of Another:[get the lists of another person](./lists_of_another.py)