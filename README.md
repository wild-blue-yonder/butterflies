# Butterflies
This is a **template repository** for using the 'blue-yonder' and 'wild-blue-yonder' packages. If you want to create a repository with this template in your account or the account of your organization just click the 'Use this template' button on the top of this page and the copy of this repo will appear in your account where you will be able to use and modify it the way you want.

![The depiction of use template button](./pictures/use_template.png)
<br>The `blue-yonder` [package](https://pypi.org/project/blue-yonder/) is a pypi Python package that allows you to program your own ['simple automation'](./sa/README.md) (SA) of routine tasks on BlueSky.

## The idea of `blue-yonder` package
The Bluesky network creators were so busy with their own perception of their enterprise as 'an implementation of a protocol' that they didn't separate in their code and documentation the different logical levels of participation of entities in the network. In this package I tried to set apart the 'active participation' which consists of the actions (posts, uploads, likes, follows, blocks, mutes, etc.) by a (_logged in_) **Actor**... sorry for the reiteration of the 'act' root bounding with tautology... from the 'passive observation' of **Another** entity, its profile, posts, likes, followers, lists, feeds, etc. that can be done by a _not logged into the Bluesky and, hence, 'anonymous'_ computer with Internet connection. Besides that, on a yet another level, there are pure functions of the network/environment too - the search functions and other utilities of the environment, which I stored in the **yonder** module, where you can import them from as a whole or individually. The package is a work in progress and will keep changing without notice.

<br>If you are experimenting with instructing Language Models and would like to see whether _they_ will make your 'social presence' less stressful and more meaningful by assessing whether the content that you are about to see is worth looking at or it is something that you will wish you would be able to 'unsee' later...

<br>The `wild-blue-yonder` [package](https://pypi.org/project/wild-blue-yonder/) makes it possible for you to instruct a Language Model how to manage your Actor on Bluesky network. Here you will find several useful examples of this new type of ['intelligent automation'](./ia/README.md) (IA).

## Begin with the basics!
But first I recommend you to [start reading there](./basics/README.md). These simple examples will help you start your programmatic interactions with the Bluesky network.