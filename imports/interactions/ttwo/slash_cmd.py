from imports.slashcmds import *
from imports.utils import fail
import traceback
from imports.utils.errors.errhandle import handle

availablecmds=["aboutme","anipic","avatar","dice","echo","eval","guessnum","quote","simon"]

def slashc(r):
    cmdname=r.json["data"]["name"]
    itruser=r.json["member"]["user"]
    if not cmdname in availablecmds:
        return fail.existnt(cmdname)
    else:
        try:
            if cmdname=="eval":
                options=r.json["data"]["options"]
                return eval.cmd(uid=itruser["id"],token=r.json["token"],iid=r.json["id"],sc=options[0]["name"],aid=r.json["application_id"],jsn=options[0]["options"][0]["value"])
            elif cmdname=="aboutme":
                return aboutme.cmd(token=r.json["token"],iid=r.json["id"],aid=r.json["application_id"],subc=r.json["data"]["options"][0]["name"],uid=itruser["id"])
            elif cmdname=="dice":
                return dice.cmd(usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif cmdname=="simon":
                return simon.cmd(r.json["data"]["options"][0]["value"])
            elif cmdname=="echo":
                return echo.cmd(text=r.json["data"]["options"][0]["value"],uname=itruser["username"],id=itruser["id"],disc=itruser["discriminator"],av=itruser["avatar"])
            elif cmdname=="guessnum":
                return guessnum.cmd(guess=r.json["data"]["options"][0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"])
            elif cmdname=="avatar":
                try:
                    use=r.json["data"]["options"][0]["value"]
                except KeyError:
                    use=None
                return avatar.cmd(us=use,uname=itruser["username"],id=itruser["id"],disc=itruser["discriminator"],av=itruser["avatar"])
            elif cmdname=="quote":
                options=r.json["data"]["options"]
                return quote.cmd(subc=options[0]["name"],query=options[0]["options"][0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"],usid=itruser["id"])
            elif cmdname=="anipic":
                options=r.json["data"]["options"]
                ani=False
                for i in options:
                    if i["name"]=="animal":
                        anioption=i["value"]
                    elif i["name"]=="animated":
                        ani=i["value"]
                return anipic.cmd(usid=itruser["id"],animal=anioption,anim=ani)
        except:
            return handle(r=r,t=traceback.format_exc())
