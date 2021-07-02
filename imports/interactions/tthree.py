import traceback,json
from imports.buttons import *
from imports.utils import fail

def tthree(r):
    try:
        try:
            c=json.loads(r.json["data"]["custom_id"])
        except:
            return fail.cfail()
        if r.json["data"]["component_type"]==2:
            bname=c["bfn"]
            if bname=="dicereroll":
                return dicereroll.btn(binfo=c,usid=r.json["member"]["user"]["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif bname=="quote":
                return bquote.btn(binfo=c,usid=r.json["member"]["user"]["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif bname=="banipic":
                return banipic.btn(binfo=c,usid=r.json["member"]["user"]["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            else:
                return fail.cfail()
        elif r.json["data"]["component_type"]==3:
            return fail.cfail()
    except:
        return fail.err(traceback.format_exc())
