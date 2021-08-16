from imports.slashcmds import *
from imports.utils import fail
import traceback

availablecmds=["aboutme","anipic","avatar","dice","echo","eval","guessnum","quote","simon"]

def slashc(r):
    cmdname=r.json["data"]["name"]
    itruser=r.json["member"]["user"]
    options=r.json["data"]["options"]
    if not cmdname in availablecmds:
        return fail.existnt(cmdname)
    else:
        try:
            if cmdname=="eval":
                return eval.cmd(uid=itruser["id"],token=r.json["token"],iid=r.json["id"],sc=options[0]["name"],aid=r.json["application_id"],jsn=options[0]["options"][0]["value"])
            elif cmdname=="aboutme":
                return aboutme.cmd(token=r.json["token"],iid=r.json["id"],aid=r.json["application_id"],subc=options[0]["name"],uid=itruser["id"])
            elif cmdname=="dice":
                return dice.cmd(usid=itruser["id"],aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif cmdname=="simon":
                return simon.cmd(options[0]["value"])
            elif cmdname=="echo":
                return echo.cmd(text=options[0]["value"],uname=itruser["username"],id=itruser["id"],disc=itruser["discriminator"],av=itruser["avatar"])
            elif cmdname=="guessnum":
                return guessnum.cmd(guess=options[0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"])
            elif cmdname=="avatar":
                try:
                    use=options[0]["value"]
                except KeyError:
                    use=None
                return avatar.cmd(us=use,uname=itruser["username"],id=itruser["id"],disc=itruser["discriminator"],av=itruser["avatar"])
            elif cmdname=="quote":
                return quote.cmd(subc=options[0]["name"],query=options[0]["options"][0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"],usid=itruser["id"])
            elif cmdname=="anipic":
                try:
                    ani=options[1]["value"]
                except:
                    ani=False
                return anipic.cmd(usid=itruser["id"],animal=options[0]["value"],anim=ani)
        except:
            return fail.err(traceback.format_exc())
