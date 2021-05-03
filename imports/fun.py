import os,requests
from time import sleep
from random import choice,randint
from imports import notcmd

baseurl=os.environ['BASE_URL']

def dice(aid:str,iid:str,token:str):
  dice = [1,2,3,4,5,6,"**The dice got stuck against the wall. Try Again!** :exploding_head:","**The dice got lost. Try Again!** :thinking:"]
  roll = choice(dice)
  emojis = ["<:dice_1:755891608859443290>", "<:dice_2:755891608741740635>", "<:dice_3:755891608251138158>", "<:dice_4:755891607882039327>", "<:dice_5:755891608091885627>", "<:dice_6:755891607680843838>"]
  rolling = {
    "type": 4,
    "data": {
        "content": "<a:loading:747680523459231834> Rolling the Dice…"
    }
  }
  requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=rolling)
  dicerolled = {
        "content": f"The dice rolled {roll}! {emojis[roll-1]}" if type(roll) == int else roll
  }
  sleep(1)
  requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=dicerolled)
  return

def echo(text:str,uname:str,id:str,disc:str,av):
  um=notcmd.analyse(cont=text)
  if um is not None:
    return um
  else:
    return {
      "type": 4,
      "data": {
          "embeds":[
            {
              "color": "3092791",
              "description": text,
              "author":{
                "name": f"{uname}'s Echo!",
                "icon_url": notcmd.usav(id=id,discid=disc,av=av)
              }
            }
          ]
      }
    }

def simon(text:str):
  um=notcmd.analyse(cont=text)
  if um is not None:
    return um
  else:
    return {
      "type": 4,
      "data": {
          "content": f"Simon says {text}"
      }
    }

def guessnum(guess:int,aid:str,iid:str,token:str):
  if guess not in range(1,11):
    return {
      "type": 4,
      "data": {
        "flags": 64,
        "content": "> <:tickNo:315009174163685377> Your choice must be an integer between 1 and 10. (*including them*)\n ***If you really think you can guess numbers in a longer range with this bot, contact the bot developers with a proof showing them at least 10 correct number guesses…***"
      }
    }
  else:
    requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":4,"data":{"content":f":thinking: You guessed {guess}. My guess is..."}})
    jsr={
      "content": f":confetti_ball: You guessed it right! :confetti_ball:\n:thinking: The number I thought of was {num}!" if (guess==(num:=randint(1,10))) else f"Aah! You have guessed it wrong. :thumbdown:\nThe number was {num}."
    }
    sleep(1)
    requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsr)
    return
