from imports.utils import perspective,avpic

def cmd(text:str,uname:str,id:str,disc:str,av):
    um=perspective.analyse(cont=text)
    if um is not None:
        return um
    else:
        return {
            "type": 4,
            "data": {
                "embeds":[
                    {
                        "color": "3092791",
                        "description": text,
                        "author":{
                            "name": f"{uname}'s Echo!",
                            "icon_url": avpic.usav(id=id,discid=disc,av=av)
                        }
                    }
                ]
            }
        }
