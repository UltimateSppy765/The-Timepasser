import os,json,requests
from time import sleep
from imports.utils.common import diceroll
baseurl=os.environ['BASE_URL']

def btn(usid:str,iid:str,aid:str,token:str,binfo):
    if usid!=binfo["userid"]:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> You can't reroll someone else's dice can you?"
            }
        }
    rolling={
        "type": 7,
        "data": {
            "flags": 64,
            "content": "<a:loading:747680523459231834> Rerolling the Dice…",
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "style": 2,
                            "custom_id": json.dumps(binfo),
                            "disabled": True,
                            "label": "Rerolling..."
                        }
                    ]
                }
            ]
        }
    }
    requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=rolling)
    sleep(1)
    dicerolled={
        "content": diceroll.droll(),
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "style": 1 if binfo["rolls"]<5 else 4,
                        "custom_id": json.dumps({"bfn":"diceroll","rolls":binfo["rolls"]+1,"userid":binfo["userid"]}),
                        "disabled": False if binfo["rolls"]<5 else True,
                        "label": "Reroll Dice" if binfo["rolls"]<5 else "You can't reroll more than 5 times."
                    }
                ]
            }
        ]
    }
    requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=dicerolled)
    return
