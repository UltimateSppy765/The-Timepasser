import os,requests
from imports.utils.common.aboutmee import meinfo

baseurl=os.environ['BASE_URL']

def cmd(token:str,iid:str,aid:str,subc:str,uid:str):
    if subc=="devs":
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":5,"data":{"flags":64}})
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=meinfo(query=subc,uid=uid))
    else:
        requests.post(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=meinfo(query=subc,uid=uid))
    return
