from imports.utils import perspective

def cmd(text:str):
    if len(text)>500:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": f"<:tickNo:315009174163685377> Simon can't say too long stuff. It can only speak upto 500 characters long _speeches_.\nYour speech is a whopping `{len(text)}` characters long."
            }
        }
    um=perspective.analyse(cont=text)
    if um is not None:
        return um
    else:
        return {
            "type": 4,
            "data": {
                "content": f"Simon says {text}"
            }
        }
