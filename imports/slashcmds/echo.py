from imports.utils import perspective,avpic

def cmd(text:str,uname:str,id:str,disc:str,av):
    if len(text)>500:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": f"<:tickNo:315009174163685377> Your echoed text is too long (`{len(text)}` characters to be precise), try making it under 500 characters to keep things good."
            }
        }
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
