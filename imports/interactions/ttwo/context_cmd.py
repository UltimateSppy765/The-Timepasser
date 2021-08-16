import traceback
from imports.utils import fail

usctxcmds=["Avatar"]
msgctxcmds=[]

def contextc(r):
    if r.json["data"]["type"]==2:
        return uscontext(r)
    elif r.json["data"]["type"]==3:
        return msgcontext(r)
    else:
        return {"type":4,"data":{"flags":64,"content":"<:tickNo:315009174163685377> Context Command Type could not be identified.\n_Perhaps a new type in the API that I didn't hear of just yet..._"}}}

def msgcontext(r):
    cname=r.json["data"]["name"]
    if not cname in msgctxcmds:
        return fail.existnt(cname)

def uscontext(r):
    cname=r.json["data"]["name"]
    if not cname in usctxcmds:
        return fail.existnt(cname)
