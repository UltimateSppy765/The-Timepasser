from random import choice

tings=["Drank too much juice...","Lazed around too much...","**Started studying**...","Looked at myself in the mirror...","Walked into the 'I give up Pit'...","**Someone asked me whether I was smart...**"]

def err(error:str):
    return {
        "type": 4,
        "data": {
            "content": f"> <:tickNo:315009174163685377> Sorry, an error has occured. Either your input has caused this error or it is from my side.\n> **__Error Code:__** {choice(tings)}",
            "embeds": [
                {
                    "description": f":clipboard: **Please report this error to the bot developers:**\n```py\n{error}\n```",
                    "color": 3092791,
                    "footer": {
                        "text": "For finding the bot developers, run '/aboutme devs'.",
                        "icon_url": "https://cdn.discordapp.com/avatars/791153806058455075/4fc80d3c7cf9bf40fba1d461e1ad5c54.webp"
                    }
                }
            ]
        }
    }

def existnt(cname:str):
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": f"> <:tickNo:315009174163685377> Sorry to say but the command you tried to use (which is `/{cname}`) is currently unavailable (and probably under development or modification :tools:).\n> Please try again later."
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
