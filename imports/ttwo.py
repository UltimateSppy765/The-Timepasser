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
            if r.json["member"]["user"]["id"] not in ["482526553616416782","479195061792407562","730361955226746923","698200925311074485","770542184310243342"]:
                return misc.existnt(cmdname)
            if cmdname=="eval":
                return misc.eval(uid=r.json["member"]["user"]["id"],token=r.json["token"],iid=r.json["id"],sc=r.json["data"]["options"][0]["name"],aid=r.json["application_id"],jsn=r.json["data"]["options"][0]["options"][0]["value"])
            elif cmdname=="aboutme":
                return misc.aboutme(subc=r.json["data"]["options"][0]["name"],uid=r.json["member"]["user"]["id"])
            elif cmdname=="dice":
                return fun.dice(aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif cmdname=="simon":
                return fun.simon(r.json["data"]["options"][0]["value"])
            elif cmdname=="echo":
                return fun.echo(text=r.json["data"]["options"][0]["value"],uname=r.json["member"]["user"]["username"],id=r.json["member"]["user"]["id"],disc=r.json["member"]["user"]["discriminator"],av=r.json["member"]["user"]["avatar"])
            elif cmdname=="guessnum":
                return fun.guessnum(guess=r.json["data"]["options"][0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"])
            else:
                return misc.existnt(cmdname)
        except:
            return misc.err(traceback.format_exc())
