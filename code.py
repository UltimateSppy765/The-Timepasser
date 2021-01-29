import os
import requests
import wikiquote
import wikiquotes
from random import choice,randint
from threading import Thread
from flask import Flask, request, jsonify,abort
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType


CLIENT_PUBLIC_KEY = os.environ['CLIENT_ID']
baseUrl = "https://discord.com/api/v8/"
headers = {"Authorization":"Bot NzkxMTUzODA2MDU4NDU1MDc1.X-LBZg.uhgfgX6U5tbRr0r0asEw0V52TGs"}

app = Flask(__name__)

@app.route('/', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def code():
    try:
        if request.json["type"] == 1:        
            return jsonify({
                "type": 1
            })

        else:
            usid = request.json["member"]["user"]["id"]
            if request.json["guild_id"] == '789147777069744179' and request.json["channel_id"] == '789147777069744182':
                return jsonify(
                    {
                        "type": 3,
                        "data": {
                            "flags": 64,
                            "content": f"Sorry <@{usid}>, I've been instructed not to do anything in <#789147777069744182>."
                        }
                    }
                )
            else:
                cmd_name = request.json["data"]["name"] #to make it easy to check for name
                usname = request.json["member"]["user"]["username"]
                usav = request.json["member"]["user"]["avatar"]
                discid = request.json["member"]["user"]["discriminator"]
                if usav is None:
                    heh = int(discid)%5
                    avurl = f"https://cdn.discordapp.com/embed/avatars/{heh}.png"
                elif usav.startswith('a_'):
                    avurl = f"https://cdn.discordapp.com/avatars/{usid}/{usav}.gif"
                else:
                    avurl = f"https://cdn.discordapp.com/avatars/{usid}/{usav}.webp"
                if cmd_name == 'simon':
                    return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "content":f'Simon says {request.json["data"]["options"][0]["value"]}'
                            }
                        }
                    )
                elif cmd_name == "dice":
                    dice = [1,2,3,4,5,6,"**The dice got stuck against the wall. Try Again!** :exploding_head:","**The dice got lost. Try Again!** :thinking:"]
                    roll = choice(dice)
                    if type(roll) == int:
                        rolle = roll - 1
                    emlist = ["<:dice_1:755891608859443290>", "<:dice_2:755891608741740635>", "<:dice_3:755891608251138158>", "<:dice_4:755891607882039327>", "<:dice_5:755891608091885627>", "<:dice_6:755891607680843838>"]
                    content = f"The dice rolled {roll}. {emlist[rolle]}" if type(roll) == int else roll
                    return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "content":content
                            }
                        }
                    )
                elif cmd_name == "guessnum":
                    guess = request.json["data"]["options"][0]["value"]
                    if guess not in range(1,11):
                        result = "Guess a number between 1 to 10, silly!"
                    else:
                        num = randint(1,10)
                        result = ":confetti_ball:You guessed it right!:confetti_ball:" if num == guess else f'Aah! You have guessed it wrong. :thumbdown:\nThe number was {num}.'

                    return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "content":result
                            }
                        }
                    )
                elif cmd_name == "echo":
                    intext = request.json["data"]["options"][0]["value"]
                    return jsonify({
                        "type": 3,
                        "data": {
                            "embeds": [
                                {
                                    "description": intext,
                                    "author": {
                                        "name": f"{usname}'s Echo!",
                                        "icon_url": avurl
                                    }
                                }
                            ]
                        }
                    })
                elif cmd_name == "anipic":
                    autext = f"Requested by {usname}"
                    if request.json["data"]["options"][0]["value"] == 'Fox':
                        if len(request.json["data"]["options"]) == 1 or request.json["data"]["options"][1]["value"] == False:
                            api = "https://randomfox.ca/floof"
                            foxy = requests.get(api).json()
                            fox = foxy["image"]
                            greet = ":fox: Here's a fox pic for you."
                            fttext = "Powered by RandomFox"
                            fticon = "https://cdn.discordapp.com/attachments/789798190353743874/798118721091928074/logo.png"
                            titletxt= "Ring-ding-ding-ding-dingeringeding!"
                            return jsonify({
                                "type": 3,
                                "data":{
                                    "content": greet,
                                    "embeds": [
                                        {
                                            "author": {
                                                "name": autext,
                                                "icon_url": avurl
                                            },
                                            "title": titletxt,
                                            "image": {
                                                "url": fox
                                            },
                                            "footer": {
                                                "text": fttext,
                                                "icon_url": fticon
                                            }
                                        }
                                    ]
                                }
                            })
                        else:
                            return jsonify({
                                "type": 3,
                                "data":{
                                    "embeds": [
                                        {
                                            "author": {
                                                "name": autext,
                                                "icon_url": avurl
                                            },
                                            "title": "I'm so sorry",
                                            "description": "I cannot get you random animated pictures of foxes just yet, but please look at this one :fox: pic I know of:",
                                            "image": {
                                                "url": "https://cdn.discordapp.com/attachments/789798190353743874/798137454518730773/tenor.gif"
                                            },
                                            "footer": {
                                                "text": "Gif from Tenor",
                                                "icon_url": "https://cdn.discordapp.com/attachments/789798190353743874/798133763896377404/9XiZf6X9.png"
                                            }
                                        }
                                    ]
                                }
                            })
                    elif request.json["data"]["options"][0]["value"] == 'Cat':
                        if len(request.json["data"]["options"]) == 1 or request.json["data"]["options"][1]["value"] == False:
                            res = requests.get('https://api.thecatapi.com/v1/images/search?size=small&mime_types=jpg,png')
                        else:
                            res = requests.get('https://api.thecatapi.com/v1/images/search?size=small&mime_types=gif')
                        imgjson = res.json()
                        imgurl = imgjson[0]['url']
                        greet = ":cat: Here's a cat pic for you."
                        fttext = "Powered by The Cat API"
                        fticon = "https://cdn.discordapp.com/attachments/789798190353743874/794474344410906654/thecatapi_256xW.png"
                        titletxt = "Meow..."
                    elif request.json["data"]["options"][0]["value"] == 'Dog':
                        if len(request.json["data"]["options"]) == 1 or request.json["data"]["options"][1]["value"] == False:
                            res = requests.get('https://api.thedogapi.com/v1/images/search?size=small&mime_types=jpg,png')
                        else:
                            res = requests.get('https://api.thedogapi.com/v1/images/search?size=small&mime_types=gif')
                        imgjson = res.json()
                        imgurl = imgjson[0]['url']
                        greet = ":dog: Here's a dog pic for you."
                        fttext = "Powered by The Dog API"
                        fticon = "https://cdn.discordapp.com/attachments/789798190353743874/794491188643102730/Z.png"
                        titletxt= "Woof!"
                    return jsonify(
                        {
                            "type": 3,
                            "data": {
                                "content":greet,
                                "embeds" : [
                                {
                                    "author": {
                                        "name": autext,
                                        "icon_url": avurl
                                    },
                                    "title": titletxt,
                                    "footer":{
                                        "text": fttext,
                                        "icon_url": fticon
                                    },
                                    "image":{
                                    "url":imgurl
                                    }
                                }]
                            }
                        }
                    )
                    
                elif cmd_name == "testquote":
                    autext = f"Requested by {usname}"
                    if request.json["data"]["options"][0]["name"] == "get":
                        if request.json["data"]["options"][0]["options"][0]["value"] == "qotd":
                            z = wikiquote.quote_of_the_day()
                            (qt, autor) = z
                            fttext = "Quotes from Wikiquote"
                            titl = "Quote of the Day:"
                            fticon = "https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
                        elif request.json["data"]["options"][0]["options"][0]["value"] == "random":
                            api = " http://api.quotable.io/random"
                            random_quote = requests.get(api).json()
                            qt = random_quote["content"]
                            autor = random_quote["author"]
                            titl = "Random Quote:"
                            fttext = "Powered by Quotable"
                            fticon = "https://cdn.discordapp.com/attachments/789798190353743874/796731399671250954/G7Xop8IK4d3myXhyWYendh3hmR9cz0at9cwvyXD4DiMS3tgKznJnfTaFIIBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlPIfKPtH5.png"
                        return jsonify({
                            "type": 3,
                            "data": {
                                "embeds": [
                                    {
                                        "author": {
                                            "name": autext,
                                            "icon_url": avurl
                                        },
                                        "title": titl,
                                        "description": f"{qt}\n- {autor}",
                                        "thumbnail": {
                                            "url": "https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
                                        },
                                        "footer": {    
                                             "text": fttext,
                                             "icon_url": fticon
                                         }
                                    }
                                ]
                            }
                        })
                    elif request.json["data"]["options"][0]["name"] == "search":
                        
                        def searching(inpuq,token):
                            try:
                                a = wikiquotes.search(inpuq, "english")
                            except:
                                msg = "Sorry, no Author matched the query, please search a different one."
                            else:
                                for c in a:
                                    if inpuq in c:
                                        autor = c
                                        qt = wikiquotes.random_quote(autor, "english")
                                        break
                                else:
                                    g = wikiquotes.get_quotes(choice(a), "english")
                                    for f in h:
                                        if inpuq in f:
                                            autor = choice(a)
                                            qt = f
                                            break
                            try:
                                msg = f"Quote: {qt}\n- {autor}"
                            except:
                                msg = "Sorry, no Author or quote matched your query, please try again."
                            
                            fttext = "Quotes from Wikiquote"
                            fticon = "https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
                            json = {
                                    "embeds":[
                                        {
                                            "author": {
                                                "name": autext,
                                                "icon_url": avurl
                                        },
                                            "title": "Quote",
                                            "description": msg,
                                            "thumbnail": {
                                                "url": "https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
                                        },
                                             "footer": {    
                                                "text": fttext,
                                                "icon_url": fticon
                                             }
                                        }
                                    ]
                                }
                            res = requests.patch(f"{baseUrl}/webhooks/791153806058455075/{token}/messages/@original",headers=headers,json=json)
                            
                        inpuq = request.json["data"]["options"][0]["options"][0]["value"]
                        fttext = "Quotes from Wikiquote"
                        fticon = "https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
                        
                        token = request.json["token"]
                        thread = Thread(target=searching, args = (inpuq,token))
                        thread.start()
                        
                        return jsonify({    
                            "type": 3,
                            "data": {
                                "embeds": [
                                    
                                    {
                                        "title": f":mag: Searching for query '{inpuq}'..."
                                    }
                                ]
                            }
                        })
                elif cmd_name == "avatar":
                    try:
                        options = request.json["data"]["options"]
                    except KeyError:
                        url = f"{avurl}?size=256"
                        uname = usname
                    else:
                        uid = request.json["data"]["options"][0]["value"]
                        res = requests.get(f"{baseUrl}users/{uid}",headers=headers)
                        if not res.ok:
                             return jsonify(
                                {
                                    "type": 3,
                                    "data": {
                                        "flags": 64,
                                        "content": f"Sorry <@{usid}>, but that user does not exist in Discord :thumbsdown:. Try with someone else."
                                    }
                                }
                            )
                        user = res.json()
                        uav = user["avatar"]
                        uname = user["username"]
                        disc = user["discriminator"]
                        if user["avatar"] is None:
                            print(disc)
                            hah = int(disc)%5
                            url = f"https://cdn.discordapp.com/embed/avatars/{hah}.png"
                        elif user["avatar"].startswith('a_'):
                            url = f"https://cdn.discordapp.com/avatars/{uid}/{uav}.gif?size=256"
                        else:
                            url = f"https://cdn.discordapp.com/avatars/{uid}/{uav}.webp?size=256"
                    return jsonify({
                        "type": 3,
                        "data": {
                            "embeds": [
                                {
                                    "author": {
                                        "name": f"Requested by {usname}",
                                        "icon_url": avurl
                                    },
                                    "title": f"{uname}'s Avatar:",
                                    "image": {
                                        "url": url
                                    },
                                }
                            ]
                        }
                    })
                elif cmd_name == "aboutme":
                    return jsonify(
                        {
                            "type": 3,
                            "data": {
                                "flags": 64,
                                "content": f"Hey <@{usid}>, let me tell you my story :notebook_with_decorative_cover: of origin:\n> Once upon a time, there used to be 2 people, who had a *passion* for coding. One was *lazy* while the other was diligent. Nevertheless, both of them managed to make great stuff! The *lazy* one wanted to build a community of people whom he could spend free time with. Eventually, they made a server where they brought some people. They tried to make it active and needed many sources for that. One source was making their own server bot. And as the name of the server was **':beginner:│The Timepass Squad'** (which they took 2 days to decide), they made me: **'The Timepasser'**! In process of my making, they even took help from a friend for testing things. (*who ended up being termed as **A Lab Rat** :test_tube: :rat: by the diligent one!*) My job is to provide you with recreational things to do so that you can spend your time joyfully.\nPlease support our community server :people_holding_hands: so that we can become a huge group of friends and do stuff together!\nOur Server: https://discord.gg/XGz4Pr34aR"
                            }
                        }
                    )
                elif cmd_name == "createinvite":
                    cid = request.json["channel_id"]
                    res = requests.post(f"{baseUrl}/channels/{cid}/invites",headers=headers,json={})
                    inviteCode = res.json()["code"]
                    inviteLink = f"https://discord.gg/{inviteCode}"
                    return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "content": f"<@{usid}>, I have created your invite :postbox: link to this channel!\n**Invite Link:** {inviteLink}\n*This link expires in 24 hours :clock:.*"
                            }
                        }
                    )
                else:
                    return jsonify(
                        {
                            "type": 3,
                            "data": {
                                "flags": 64,
                                "content":f'Sorry to say but the command you tried to use (which is `/{cmd_name}`) is currently unavailable (and probably under development or modification :tools:).\nPlease try again later.'
                            }
                        }
                    )
    
    except Exception as e:
        tings = ["Drank too much juice...", "Lazed around too much...", "**Started studying**...", "Looked at myself in the mirror...", "Walked into the 'I give up Pit'...", "**Someone asked me whether I was smart...**"]
        choi = choice(tings)
        return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "content":f"Sorry, an error has occured. :negative_squared_cross_mark: Either your input has caused this error or it is from my side. Please report :clipboard: this to the bot developers along with the error code:\nError Code: {choi} *Joking*\n```py\n{type(e).__name__} : {e}\n```"
                            }
                        }
                    )
port = os.getenv('PORT')
if port:
    app.run(host='0.0.0.0',port=port)
else:
    print("Not able to get the PORT env variable.")
