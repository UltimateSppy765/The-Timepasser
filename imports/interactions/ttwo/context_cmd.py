import traceback
from imports.utils import fail
from imports.contextcmds.usercmds import *

usctxcmds=["Avatar"]
msgctxcmds=[]

def contextc(r):
    try:
        if r.json["data"]["type"]==2:
            return uscontext(r)
        elif r.json["data"]["type"]==3:
            return msgcontext(r)
        else:
            return {"type":4,"data":{"flags":64,"content":"<:tickNo:315009174163685377> Context Command Type could not be identified.\n_Perhaps a new type in the API that I didn't hear of just yet..._"}}
    except:
        return fail.err(traceback.format_exc())

def msgcontext(r):
    cname=r.json["data"]["name"]
    if not cname in msgctxcmds:
        return fail.ctxexistnt(cname)

def uscontext(r):
    cname=r.json["data"]["name"]
    targetusid=r.json["data"]["target_id"]
    ruser=r.json["data"]["resolved"]["users"][targetusid]
    if not cname in usctxcmds:
        return fail.ctxexistnt(cname)
    if cname=="Avatar":
        return avatar.uscmd(usid=targetusid,av=ruser["avatar"],uname=ruser["username"],disc=ruser["discriminator"])
