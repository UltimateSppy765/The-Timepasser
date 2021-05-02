import os,requests
from time import sleep
from random import choice
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
        "content": f"The dice rolled {roll} {emojis[roll-1]}" if type(roll) == int else roll
  }
  sleep(1)
  requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=dicerolled)
  
def echo(text:str,uname:str,id:str,disc:str,av):
  if notcmd.analyse(cont=text):
    return {
      "type": 4,
      "data": {
        "flags": 64,
        "content": f"> <:tickNo:315009174163685377> Sorry, your command usage was blocked as harmful text was detected in your input \n> If you think it is a mistake, please contact the bot developers. (You can see them through `/aboutme devs`.\n> :confused: Your input: (*just in case you forgot what you wrote...*)\n```\n{text}\n```"
      }
    }
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
