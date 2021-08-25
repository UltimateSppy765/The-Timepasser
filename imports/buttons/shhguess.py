import random

def btn(usid:str):
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": f"Hey <@!{usid}>, you've found the hidden and **legendary** challenge of `Guess the Number`!\nTry your luck and see if you can win this challenge!\n_On winning you'll get a prize.__ :trophy:",
            "components": []
        }
    }
