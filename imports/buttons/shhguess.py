import random,json

def btn(usid:str):
    List=random.sample(range(1,76),4)
    List2=["Choose me because I am a great number.","If you choose me, you get a 🍪!","This number perhaps may let you win...","Don't choose me."]
    random.shuffle(List2)
    random.shuffle(List)
    Options=[]
    for i in range(0,4):
        Options.append({"label":f"{List[i]}","description":List2[i],"value":json.dumps({"pos":i+1,"number":List[i]}),"emoji":{"name":"umm","id":"847712983517233152"}})
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": f"Hey <@!{usid}>, you've found the hidden and **legendary** challenge of `Guess the Number`!\nTry your luck and see if you can win this challenge!\n_On winning you'll get a prize._ :trophy:",
            "embeds": [{
                "color": 3092791,
                "fields": [{
                    "name": "🤔 Guess the Number!",
                    "value": "4 *random* numbers are given in the drop-down menu below. Choose ***one*** number from the menu.\nIf you're lucky, you win! **Good Luck!** 👍"
                }]
            }],
            "components": [{
                "type": 1,
                "components": [{
                    "type": 3,
                    "placeholder": "🤔 Guess the number!",
                    "disabled": False,
                    "custom_id": json.dumps({"sfn":"shhguess"}),
                    "options": Options
                }]
            }]
        }
    }
