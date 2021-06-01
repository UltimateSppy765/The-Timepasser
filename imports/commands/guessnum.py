from time import sleep
from random import randint
import os,requests,json

baseurl=os.environ['BASE_URL']

def cmd(guess:int,aid:str,iid:str,token:str):
    if guess==42:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "> **You chose 42, and…**\n> <:tickYes:315009125694177281> Bingo! It's correct, I don't need to think of this number for your guess to be correct… \n> *It's always correct!*\nDidn't understand? Click the button below.",
                "components": [{
                    "type": 1,
                    "components": [{
                        "type": 2,
                        "style": 5,
                        "url": "https://en.m.wikipedia.org/wiki/42_(number)",
                        "label": "Read this!"
                      },
                      {
                        "type": 2,
                        "style": 1,
                        "label": "What does this do?",
                        "emoji": {"name":"umm","id":"847712983517233152"},
                        "custom_id": json.dumps({"bfn":"shhguess"})
                    }]
                }]
            }
        }
    if guess not in range(1,11):
        return {
            "type": 4,
            "data": {
              "flags": 64,
              "content": "> <:tickNo:315009174163685377> Your choice must be an integer between 1 and 10. (*including them*)\n ***If you really think you can guess numbers in a longer range with this bot, contact the bot developers with a proof showing them at least 10 correct number guesses…***"
            }
        }
    else:
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":4,"data":{"content":f":thinking: You guessed {guess}. Hmm..."}})
        jsr={
            "content": f":confetti_ball: You guessed it right! :confetti_ball:\n:thinking: The number I thought of was {num}!" if (guess==(num:=randint(1,10))) else f"Aah! You have guessed it wrong. :thumbdown:\nThe number was {num}."
        }
        sleep(1)
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsr)
        return
