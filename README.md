Leap Motion RockPaperScissors
=============================

Play Rock Paper Scissors against the computer with your Leap Motion!

This project was built at a Leap Motion-sponsored hackathon at my school. This means that the code is still very buggy, and I no longer have a Leap Motion to test it.

The code tracks two things primarily:

1. **Position of your hands** - When you play Rock, Paper, Scissors in real life, you pump your first as you say "Rock, Paper, Scissors!"  We track the pumping motion as well by watching the changing velocity of your palm.  On the third downward stroke, we look for what sign you threw (see below).
2. **Number of fingers** - The Leap Motion can only detect your fingers if they are moderately extended and positioned directly over the device.
  * If we see no fingers, we assume your hand is in a fist and figure you are showing Rock.
  * If we see 1-2 fingers, we assume you're throwing scissors.
  * If we see =< 3 fingers, we assume you're throwing paper.

Usage
-----
1. Download the Leap Motion SDK, then run gamelogic from the command line with the following command:

<code>python3 -i gamelogic.py


2. Show the device how many players you want to play by extending a finger. Only single player is supported right now, although the Leap Motion can track two hands at once, so theoretically multiplayer can happen.
3. Pump your hands up and down as you count off "Rock, Paper, Scissors!"
4. Flash your sign  over the Leap Motion.

