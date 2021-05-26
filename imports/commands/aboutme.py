import os,requests

baseurl=os.environ['BASE_URL']

def cmd(token:str,iid:str,aid:str,subc:str,uid:str):
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
                            }
                        ]
                    }
                ],
                "components": [
                    {
                        "type": 1,
                        "components": [
                            {
                                "type": 2,
                                "style": 5,
                                "url": "https://discord.gg/JXGe9MfXPF",
                                "label": "Community Server Link!"
                            },
                            {
                                "type": 2,
                                "style": 5,
                                "url": "https://discord.com/api/oauth2/authorize?client_id=791153806058455075&scope=applications.commands",
                                "label": "Bot Invite Link"
                            }
                        ]
                    }
                ]
            }
        }
    else:
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":5,"data":{"flags":64}})
        meow= requests.get(f"{baseurl}users/698200925311074485",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"}).json()
        sppy=requests.get(f"{baseurl}users/770542184310243342",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"}).json()
        plexi=requests.get(f"{baseurl}users/730361955226746923",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"}).json()
        aura=requests.get(f"{baseurl}users/479195061792407562",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"}).json()
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
                            "value": "You might need to join our community server to contact them. (as their DMs might be disabled)\nYou can join the server using the button below!"
                        }
                    ]
                }
            ],
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "style": 5,
                            "url": "https://discord.gg/JXGe9MfXPF",
                            "label": "Our Community Server!"
                        }
                    ]
                }
            ]
        }
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=njs)
        return
