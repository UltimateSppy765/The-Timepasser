from imports import misc,fun
import traceback
def slashc(r):
    try:
        r.json["member"]
    except:
        return misc.dmerr()
    else:
        try:
            cmdname=r.json["data"]["name"]
            if cmdname=="eval":
                misc.eval(token=r.json["token"],iid=r.json["id"],sc=r.json["data"]["options"][0]["name"],aid=r.json["application_id"],jsn=r.json["data"]["options"][0]["options"][0]["value"])
                return
            elif cmdname=="aboutme":
                return misc.aboutme(subc=r.json["data"]["options"][0]["name"],uid=r.json["member"]["user"]["id"])
            elif cmdname=="dice":
                return fun.dice(aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif cmdname=="echo":
                return fun.echo(r.json["data"]["options"][0]["value"])
            else:
                return misc.existnt(cmdname)
        except:
            return misc.err(traceback.format_exc())
