import os,requests
from imports.utils.common.aboutmee import meinfo

baseurl=os.environ['BASE_URL']

def select(query:str,usid:str,aid:str,token:str,iid:str):
    if query=="devs":
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":6})
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=meinfo(query=query,uid=usid))
    else:
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data": meinfo(query=query,uid=usid)})
    return
