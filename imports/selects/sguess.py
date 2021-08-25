import json

def select(usguess,msg):
    usguess=json.loads(usguess)
    if usguess["pos"] in [2,4]:
        a=msg["components"][0]
        a["components"][0]["disabled"]=True
        return {
            "type": 7,
            "data": {
                "embeds": [],
                "content": f":tada: Congrats!, you've completed the legendary `Guess the Number!` challenge! `{usguess["number"]}` was the right number!\n🏆 Click on the button below to claim your mysterious prize!",
                "components": [a,{
                    "type": 1,
                    "components": [{
                        "type": 2,
                        "style": 1,
                        "label": "Your Prize!",
                        "emoji": {
                            "name": "🏆"
                        },
                        "custom_id": json.dumps({"bfn":"shhguess","state":True})
                    }]
                }]
            }
        }
    else:
        a=msg["components"]
        a[0]["components"][0]["disabled"]=True
        return {
            "type": 7,
            "data": {
                "content": f":pensive: Sorry my friend, but alas glory wasn't yours today.\nI wasn't thinking of `{usguess['number']}`.\n_For maintaining the secret of this challenge, I can't tell you the answer. My advice is to just..._ **Try Again**",
                "embeds": [],
                "components": a
            }
        }
