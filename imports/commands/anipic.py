import requests

def cmd(anim:bool,animal:str):
    if animal=="Fox":
        if anim==False:
            foxy=requests.get("https://randomfox.ca/floof").json()
            url=foxy["image"]
            cont=":fox: Here's a fox pic for you."
            ftext="Powered by RandomFox"
            ficon="https://cdn.discordapp.com/attachments/789798190353743874/798118721091928074/logo.png"
            greet="Ring-ding-ding-ding-dingeringeding!"
        else:
            return {
                "type": 4,
                "data": {
                    "flags": 64,
                    "content": "<:tickNo:315009174163685377> Sorry to say but I cannot send animated fox pics yet.\n> **A message from the bot developers:**\n> We could not find any free API which provided animated GIFs of real foxes. (*and not cartoon/meme ones*) In case if you do find any such API and would like to see this feature in the bot, please contact us, the help would be appreciated! (Info on bot devs in `/aboutme devs`)",
                    "embeds": [
                        {
                            "title": ":fox: To make up for it, here's a cute fox GIF I like:",
                            "color": 3092791,
                            "image": {
                                "url": "https://cdn.discordapp.com/attachments/789798190353743874/835248004478402630/fox-happy.gif"
                            },
                            "footer": {
                                "text": "GIF from Tenor",
                                "icon_url": "https://cdn.discordapp.com/attachments/789798190353743874/798133763896377404/9XiZf6X9.png"
                            }
                        }
                    ]
                }
            }
    elif animal=="Cat":
        imgtype="png,jpg" if anim==False else "gif"
        caty=requests.get(f"https://api.thecatapi.com/v1/images/search?size=small&mime_types={imgtype}",headers={"x-api-key":os.environ['CAT_API']}).json()
        url=caty[0]['url']
        cont=":cat: Here's a cat pic for you." if anim==False else ":cat: Here's an animated cat pic for you."
        greet="Meow..."
        ftext="Powered by The Cat API"
        ficon="https://cdn.discordapp.com/attachments/789798190353743874/794474344410906654/thecatapi_256xW.png"
    elif animal=="Dog":
        imgtype="png,jpg" if anim==False else "gif"
        dogy=requests.get(f"https://api.thedogapi.com/v1/images/search?size=small&mime_types={imgtype}",headers={"x-api-key":os.environ['DOG_API']}).json()
        url=dogy[0]['url']
        cont=":dog: Here's a dog pic for you." if anim==False else ":dog: Here's an animated dog pic for you."
        greet="Woof!"
        ftext="Powered by The Dog API"
        ficon="https://cdn.discordapp.com/attachments/789798190353743874/794491188643102730/Z.png"
    return {
        "type": 4,
        "data": {
            "content": cont,
            "embeds": [
                {
                    "title": greet,
                    "color": 3092791,
                    "image": {
                        "url": url
                    },
                    "footer": {
                        "text": ftext,
                        "icon_url": ficon
                    }
                }
            ]
         }
    }
