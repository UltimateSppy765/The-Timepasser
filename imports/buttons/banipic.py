import requests,os
from imports.utils.common import anipicc

baseurl=os.environ["BASE_URL"]

def btn(aid:str,iid:str,token:str,usid:str,binfo):
    if usid!=binfo["userid"]:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> You can't use that button on someone else's message, please try on your own one."
            }
        }
    requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":anipicc.pic(anim=binfo["anim"],animal=binfo["animal"],usid=binfo["userid"])})
    return
