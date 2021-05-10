from imports.commands import simon,echo,avatar,guessnum,dice,aboutme
from imports import misc,stuff
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
                return misc.eval(uid=r.json["member"]["user"]["id"],token=r.json["token"],iid=r.json["id"],sc=r.json["data"]["options"][0]["name"],aid=r.json["application_id"],jsn=r.json["data"]["options"][0]["options"][0]["value"])
            elif cmdname=="aboutme":
                return aboutme.cmd(token=r.json["token"],iid=r.json["id"],aid=r.json["application_id"],subc=r.json["data"]["options"][0]["name"],uid=r.json["member"]["user"]["id"])
            elif cmdname=="dice":
                return dice.cmd(aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif cmdname=="simon":
                return simon.cmd(r.json["data"]["options"][0]["value"])
            elif cmdname=="echo":
                return echo.cmd(text=r.json["data"]["options"][0]["value"],uname=r.json["member"]["user"]["username"],id=r.json["member"]["user"]["id"],disc=r.json["member"]["user"]["discriminator"],av=r.json["member"]["user"]["avatar"])
            elif cmdname=="guessnum":
                return guessnum.cmd(guess=r.json["data"]["options"][0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"])
            elif cmdname=="avatar":
                try:
                    use=r.json["data"]["options"][0]["value"]
                except KeyError:
                    use=None
                return avatar.cmd(us=use,uname=r.json["member"]["user"]["username"],id=r.json["member"]["user"]["id"],disc=r.json["member"]["user"]["discriminator"],av=r.json["member"]["user"]["avatar"])
            elif cmdname=="quote":
                return stuff.quote(subc=r.json["data"]["options"][0]["name"],query=r.json["data"]["options"][0]["options"][0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"])
            elif cmdname=="anipic":
                try:
                    ani=r.json["data"]["options"][1]["value"]
                except:
                    ani=False
                return stuff.anipic(animal=r.json["data"]["options"][0]["value"],anim=ani)
            else:
                return misc.existnt(cmdname)
        except:
            return misc.err(traceback.format_exc())
