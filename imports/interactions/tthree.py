import traceback,json
from imports.buttons import *
from imports.selects import *
from imports.utils import fail
from imports.utils.errors.errhandle import handle

buttons=["dicereroll","quote","banipic"]
selects=["quote","aboutme","anipic"]

def tthree(r):
    try:
        c=json.loads(r.json["data"]["custom_id"])
    except:
        return fail.cfail()
    try:
        if r.json["data"]["component_type"]==2:
            return buttonitr(r=r,c=c)
        elif r.json["data"]["component_type"]==3:
            return selectitr(r=r,c=c)
    except:
        return handle(r=r,t=traceback.format_exc())

def buttonitr(r,c):
    bname=c["bfn"]
    itruser=r.json["member"]["user"]
    if not bname in buttons:
        return fail.cfail()
    if bname=="dicereroll":
        return dicereroll.btn(binfo=c,usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
    elif bname=="quote":
        return bquote.btn(binfo=c,usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
    elif bname=="banipic":
        return banipic.btn(binfo=c,usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])

def selectitr(r,c):
    sname=c["sfn"]
    itruser=r.json["member"]["user"]
    svalues=r.json["data"]["values"]
    if not sname in selects:
        return fail.cfail()
    if sname=="quote":
        return squote.select(query=svalues[0],sinfo=c,usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
    elif sname=="aboutme":
        return saboutme.select(query=svalues[0],usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
    elif sname=="anipic":
        return sanipic.select(animal=svalues[0],oguser=c["userid"],usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
    elif sname=="errlogaction":
        return serror.select(msg=r.json["message"],action=values[0],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"],uid=itruser["id"])
