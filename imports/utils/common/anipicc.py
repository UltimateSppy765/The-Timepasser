import os,requests,json

catopt={"label":"Cat","description":"Shows you a cat picture.","value":"Cat","emoji":{"name":"cat","id":"847614941548249108"}}
dogopt={"label":"Dog","description":"Shows you a dog picture.","value":"Dog","emoji":{"name":"dog","id":"847621035981537280"}}
foxopt={"label":"Fox","description":"Shows you a fox picture.","value":"Fox","emoji":{"name":"fox","id":"847621244899426365"}}

def pic(anim:bool,animal:str,usid:str):
    if animal=="Fox":
        if anim==True:
            return {
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
                ],
                "components": [{
                    "type": 1,
                    "components": [{
                        "type": 2,
                        "style": 5,
                        "label": "Search Fox GIFs on Giphy!",
                        "url": "https://giphy.com/search/Cute-Fox"
                    }]
                }]
            }
        else:
            return {
                "content": ":fox: Here's a fox pic for you.",
                "embeds": [
                    {
                        "title": "Ring-ding-ding-ding-dingeringeding!",
                        "color": 3092791,
                        "image": {
                            "url": requests.get("https://randomfox.ca/floof").json()["image"]
                        },
                        "footer": {
                            "text": "Powered by RandomFox",
                            "icon_url": "https://cdn.discordapp.com/attachments/789798190353743874/798118721091928074/logo.png"
                        }
                    }
                ],
                "components": [{
                    "type": 1,
                    "components": [{
                        "type": 2,
                        "style": 1,
                        "label": "Another one!",
                        "emoji": {
                            "name": "fox",
                            "id": "847621244899426365"
                        },
                        "custom_id": json.dumps({"bfn":"banipic","userid":usid,"anim":anim,"animal":animal})
                    }]
                  },
                  {
                    "type": 1,
                    "components": [{
                        "type": 3,
                        "placeholder": "View a different animal picture",
                        "custom_id": json.dumps({"sfn":"anipic","userid":usid}),
                        "options": [catopt,dogopt]
                    }]
                }]
            }
    if animal=="Cat":
        imgtype="png,jpg" if anim==False else "gif"
        url=requests.get(f"https://api.thecatapi.com/v1/images/search?size=small&mime_types={imgtype}",headers={"x-api-key":os.environ['CAT_API']}).json()[0]['url']
        cont=":cat: Here's a cat pic for you." if anim==False else ":cat: Here's an animated cat pic for you."
        greet="Meow..."
        bemname="cat"
        bemid="847614941548249108"
        selectopt=[dogopt,foxopt]
        ftext="Powered by The Cat API"
        ficon="https://cdn.discordapp.com/attachments/789798190353743874/794474344410906654/thecatapi_256xW.png"
    elif animal=="Dog":
        imgtype="png,jpg" if anim==False else "gif"
        url=requests.get(f"https://api.thedogapi.com/v1/images/search?size=small&mime_types={imgtype}",headers={"x-api-key":os.environ['DOG_API']}).json()[0]['url']
        cont=":cat: Here's a dog pic for you." if anim==False else ":dog: Here's an animated dog pic for you."
        greet="Woof..."
        bemname="dog"
        bemid="847621035981537280"
        selectopt=[catopt,foxopt]
        ftext="Powered by The Dog API"
        ficon="https://cdn.discordapp.com/attachments/789798190353743874/794491188643102730/Z.png"
    return {
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
        ],
        "components": [{
            "type": 1,
            "components": [{
                 "type": 2,
                 "style": 2,
                 "label": "Another one!",
                 "emoji": {
                     "name": bemname,
                     "id": bemid
                 },
                 "custom_id": json.dumps({"bfn":"banipic","userid":usid,"anim":anim,"animal":animal})
              },
              {
                 "type": 2,
                 "style": 1,
                 "label": "An Animated one!" if anim==False else "A Static one!",
                 "custom_id": json.dumps({"bfn":"banipic","userid":usid,"anim":False if anim==True else True,"animal":animal}),
                 "emoji": {
                     "id": "847621447954071562" if anim==False else "847623094436233266",
                     "name": "animated" if anim==False else "static"
                 }
            }]
          },
          {
            "type": 1,
            "components": [{
                "type": 3,
                "placeholder": "View a different animal picture",
                "custom_id": json.dumps({"sfn":"anipic","userid":usid}),
                "options": selectopt
            }]
        }]
    }
