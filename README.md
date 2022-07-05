# PyMath Game (Placeholder name)

PyMath Game is a program developed to test your quick thinking math skills, starting with simple addition. As you continue play through, the questions will get progressively more difficult adding in larger numbers, different operations and even more questions to answer at a time. Before we get too in depth on the program itself there are a couple of things that need to be done to run this game, read more below. 


## Pre-requisites:

This program requires [Python 3.0](https://www.python.org/downloads/) or higher to run, please install python using the appropirate installation methods.

On top of that please install firebase, a cloudbased data center, which will save your data for later, and your best scroes to a server; this can be done by using the following command in your terminal once you have Python installed.

	pip install firebase

# Info

## The player
Your goal as the player is simple, don't let any enemies get past you! Defend against numerous enemies, and the only way you can stop them is to shoot the enemy ships down! This will be done by firing off projectiles that are meant to deal with the enemies that are ahead of you! Below is a picture of the player ship. Note: This is what will be firing your projectiles!
<p align="center">
   <img src="/images/shipOrange.png" alt="Player"/>
</p>


You can aim your ship with your mouse and click shoot, do note that the laser speed is constant and will not change, but your enemy position will! So be sure to line up your shots just right to deal with the enemies accordingly! 

## The Enemy
These are what your target(s) will look like:

<p align="center">
   <img src="/images/ship.png" alt="drawing" width="100"/>
</p>


Please note that all shots you make are important, your enemies are smart and have shields to defend themselves, but they do have a weakness! You can see their formula for their shield generation, and with that you can set your shots to break through their shields individual weaknesses! Not only will you see their formula, but you'll also see a few possible settings to break through their shields, input them on your keyboard to match the option that can break through their shields. If your answer matches their weakness it'll destroy the tagrget! If not you'll temporarily supercharge their shields, and that'll look like as follows

<p align="center">
   <img src="/images/shield1.png" alt="drawing" width="250"/>
</p>
When the shields are supercharged they will block **ALL** projectiles in a wide area, so make sure your shots are hitting the right answers and targets!


# Game Mechanics

Playing the game will earn you points based on the amount of enemies shot down, so basically the more enemies you take down the more points you get. As you push further into the enemies, you'll find that they get more advanced, leading to more difficult shield structures (aka more difficult math problems), and more plentiful enemies, take out as many as you can before you let any get by. You have 3 "lives" in this game so make them count, and achieve the highest scores you can. You'll be competing against your own personal scores as well as the scores of other players. 
