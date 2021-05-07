from imports import misc,fun, stuff
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
                return misc.aboutme(token=r.json["token"],iid=r.json["id"],aid=r.json["application_id"],subc=r.json["data"]["options"][0]["name"],uid=r.json["member"]["user"]["id"])
            elif cmdname=="dice":
                return fun.dice(aid=r.json["application_id"],token=r.json["token"],iid=r.json["id"])
            elif cmdname=="simon":
                return fun.simon(r.json["data"]["options"][0]["value"])
            elif cmdname=="echo":
                return fun.echo(text=r.json["data"]["options"][0]["value"],uname=r.json["member"]["user"]["username"],id=r.json["member"]["user"]["id"],disc=r.json["member"]["user"]["discriminator"],av=r.json["member"]["user"]["avatar"])
            elif cmdname=="guessnum":
                return fun.guessnum(guess=r.json["data"]["options"][0]["value"],aid=r.json["application_id"],iid=r.json["id"],token=r.json["token"])
            elif cmdname=="avatar":
                try:
                    use=r.json["data"]["options"][0]["value"]
                except KeyError:
                    use=None
                return fun.avatar(us=use,uname=r.json["member"]["user"]["username"],id=r.json["member"]["user"]["id"],disc=r.json["member"]["user"]["discriminator"],av=r.json["member"]["user"]["avatar"])
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
