from random import choice

tings=["Drank too much juice...","Lazed around too much...","**Started studying**...","Looked at myself in the mirror...","Walked into the 'I give up Pit'...","**Someone asked me whether I was smart...**"]

def existnt(cname:str):
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": f"> <:tickNo:315009174163685377> Sorry to say but the command you tried to use (which is `/{cname}`) is currently unavailable (and probably under development or modification :tools:).\n> Please try again later."
        }
    }

def ctxexistnt(cname:str):
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": f"> <:tickNo:315009174163685377> Sorry to say but the context command you tried to use (which is `{cname}`) is currently unavailable (and probably under development or modification :tools:).\n> Please try again later."
        }
    }

def cfail():
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": f"> <:tickNo:315009174163685377> Sorry to say but the message component you tried to use is currently unavailable (and probably under development or modification :tools:).\n> Please try again later."
        }
    }

def dmerr():
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": "> <:tickNo:315009174163685377> Sorry, my commands do not work in DMs, please use them in a guild."
        }
    }
