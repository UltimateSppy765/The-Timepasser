from imports import misc
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
            else:
                return misc.existnt(cname=cmdname)
        except:
            return misc.err(error=traceback.format_exc())