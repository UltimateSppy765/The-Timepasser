from imports.utils.common import diceroll
from time import sleep
import os,requests,json

baseurl=os.environ['BASE_URL']

def cmd(usid:str,aid:str,iid:str,token:str):
    rolling={
        "type": 4,
        "data": {
            "content": "<a:loading:747680523459231834> Rolling the Dice…"
        }
    }
    requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=rolling)
    dicerolled={
        "content": diceroll.droll(),
        "components": [{
            "type": 1,
            "components": [{
                "type": 2,
                "style": 1,
                "emoji": {
                    "name": "dice",
                    "id": "847687299688824942"
                },
                "label": "Reroll Dice",
                "custom_id": json.dumps({"bfn":"dicereroll","rolls":1,"userid":usid})
            }]
        }]
    }
    sleep(1)
    requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=dicerolled)
    return
