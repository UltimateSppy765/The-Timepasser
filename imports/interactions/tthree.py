import traceback,json
from imports.buttons import *
from imports.utils import fail

def tthree(r):
    try:
        b=json.loads(r.json["data"]["custom_id"])
        bname=b["bfn"]
        if bname=="dicereroll":
            return dicereroll.btn(binfo=b,usid=r.json["member"]["user"]["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
    return
