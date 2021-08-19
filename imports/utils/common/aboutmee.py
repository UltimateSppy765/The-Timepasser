def meinfo(query):
    if query=="story":
        return {
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
            "components": [{
                "type": 1,
                "components": [{
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
                }]
              }
            ]
        }
    elif query=="devs":
        return
    elif query=="links":
        return
