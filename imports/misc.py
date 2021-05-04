from random import choice
import os,requests,json

baseurl=os.environ['BASE_URL']
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

def dmerr():
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": "> <:tickNo:315009174163685377> Sorry, my commands do not work in DMs, please use them in a guild."
        }
    }

def eval(uid:str,token:str,iid:str,sc:str,aid:str,jsn):
    if uid not in ["730361955226746923","698200925311074485","770542184310243342"]:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "> <:tickNo:315009174163685377> You cannot use this command because you are not whitelisted."
            }
        }
    try:
        jsa=json.loads(jsn)
    except:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> The input given was not a valid JSON, please enter a valid JSON."
            }
        }
    else:
        if sc=="followup":
            jsp={
                "type": 4,
                "data": {
                    "content": "<a:typing:597589448607399949>  Processing Request..."
                }
            }
            requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsp)
            res=requests.post(f"{baseurl}webhooks/{aid}/{token}",headers={"Content-Type": "application/json"},json=jsa)
            if res.status_code==200:
                requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json={"content": f"<:tickYes:315009125694177281> Successfully evaluated JSON.```\nReturned Status Code: {res.status_code}\n```"})
                return 
            else:
                jsnerr={
                    "content": f"<:tickNo:315009174163685377> Your evaluation failed, detailed information given below:```\nReturned Status Code: {res.status_code}\n{res.json()}\n```"
                }
                requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsnerr)
                return 
        elif sc=="original":
            res=requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsa)
            if res.status_code==200:
                return
            else:
                return {
                    "type":  4,
                    "data": {
                        "content": f"<:tickNo:315009174163685377> Your evaluation failed, detailed information given below:```\nReturned Status Code: {res.status_code}\n{res.json()}\n```"
                    }
                }

def aboutme(token:str,iid:str,aid:str,subc:str,uid:str):
    if subc=="story":
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": f"Hey <@!{uid}>, you want to know **more **about me?\n*About me?* (Really?...)\nI am so honored to be given this opportunity.\nFine, it's storytime! :magic_wand:",
                "embeds": [
                    {
                        "color": 3092791,
                        "fields": [
                            {
                                "name": ":notebook_with_decorative_cover: The Story:",
                                "value": "Once upon a time, there used to be 2 people, who had a passion for coding. One was *lazy* while the other was diligent. Nevertheless, both of them managed to make great stuff! The *lazy* one wanted to build a community of people whom he could spend free time with. Eventually, they made a server where they brought some people. They tried to make it active and needed many sources for that. One source was making their own server bot. And as the name of the server was **':beginner:│The Timepass Squad'** (which they took 2 days to decide), they made me: **'The Timepasser'**! In process of my making, they even took help from a friend for testing things. (*who ended up being termed as **A Lab Rat** :test_tube: :rat: by the diligent one!*) My job is to provide you with recreational things to do so that you can spend your time joyfully.\nPlease support our community server :people_holding_hands: so that we can become a huge group of friends and do stuff together!"
                            },
                            {
                                "name": "Our Community Server:",
                                "value": "Please support us by joining our community server and making it a lively place!\nJoin Server: [Click Here!](https://discord.gg/JXGe9MfXPF)"
                            }
                        ]
                    }
                ]
            }
        }
    else:
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":5,"data":{"flags":64}})
        m= requests.get(f"{baseurl}users/698200925311074485",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"})
        s=requests.get(f"{baseurl}users/770542184310243342",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"})
        p=requests.get(f"{baseurl}users/730361955226746923",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"})
        a=requests.get(f"{baseurl}users/479195061792407562",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"})
        meow=m.json()
        sppy=s.json()
        plexi=p.json()
        aura=a.json()
        njs={
            "content": f"> Hey <@!{uid}>!\n> <:developer2:792583451063615518> Want the list of the bot developers? \n> Here you go:",
            "embeds": [
                {
                    "color": 3092791,
                    "fields": [
                        {
                            "name": ":pencil2: Bot Creators:",
                            "value": f"{meow['username']}#{meow['discriminator']} - <@!698200925311074485> (<a:cute_cat:795581665962622976> Cat Fan)\n{sppy['username']}#{sppy['discriminator']} - <@!770542184310243342> (:detective: They're a *Sppy*  beware)"
                        },
                        {
                            "name": ":man_technologist: Collaborators:",
                            "value": f"{plexi['username']}#{plexi['discriminator']} - <@!730361955226746923>"
                        },
                        {
                            "name": ":test_tube: Not to forget, our great bot tester! (*aka the lab rat mentioned in the Story*)",
                            "value": f"{aura['username']}#{aura['discriminator']} - <@!479195061792407562>"
                        },
                        {
                            "name": "Want to contact someone listed above?",
                            "value": "You might need to join our community server to contact them. (as their DMs might be disabled)\n[Join our Server!](https://discord.gg/JXGe9MfXPF)"
                        }
                    ]
                }
            ]
        }
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=njs)
        return
