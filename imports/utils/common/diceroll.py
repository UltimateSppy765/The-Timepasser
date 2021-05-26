from random import choice

def droll():
    dice=[1,2,3,4,5,6,"**The dice got stuck against the wall. Try Again!** :exploding_head:","**The dice got lost. Try Again!** :thinking:"]
    roll=choice(dice)
    emojis=["<:dice_1:755891608859443290>","<:dice_2:755891608741740635>","<:dice_3:755891608251138158>","<:dice_4:755891607882039327>","<:dice_5:755891608091885627>","<:dice_6:755891607680843838>"]
    return f"The dice rolled {roll}! {emojis[roll-1]}" if type(roll) == int else roll
