import os
import requests
import wikiquote
import wikiquotes
from random import choice,randint
from flask import Flask, request, jsonify,abort
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType


CLIENT_PUBLIC_KEY = os.environ['CLIENT_ID']

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
                            "tts": False,
                            "content": f"Sorry <@{usid}>, I've been instructed not to do anything in <#789147777069744182>.",
                            "embeds" : [],
                            "allowed_mentions": []
                        }
                    }
                )
            else:
                cmd_name = request.json["data"]["name"] #to make it easy to check for name
                usname = request.json["member"]["user"]["username"]
                usav = request.json["member"]["user"]["avatar"]
                if usav.startswith('a_'):
                    avurl = f"https://cdn.discordapp.com/avatars/{usid}/{usav}.gif"
                else:
                    avurl = f"https://cdn.discordapp.com/avatars/{usid}/{usav}"
                if cmd_name == 'simon':
                    return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "tts": False,
                                "content":f'Simon says {request.json["data"]["options"][0]["value"]}',
                                "embeds" : [],
                                "allowed_mentions": []
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
                                "tts": False,
                                "content":content,
                                "embeds" : [],
                                "allowed_mentions": []
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
                                "tts": False,
                                "content":result,
                                "embeds" : [],
                                "allowed_mentions": []
                            }
                        }
                    )
                elif cmd_name == "echo":
                    intext = request.json["data"]["options"][0]["value"]
                    return jsonify({
                        "type": 3,
                        "data": {
                            "tts": False,
                            "content": "",
                            "embeds": [
                                {
                                    "description": intext,
                                    "author": {
                                        "name": f"{usname}'s Echo!",
                                        "icon_url": avurl
                                    }
                                }
                            ],
                            "allowed_mentions": []
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
                                    "tts": False,
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
                                    ],
                                    "allowed_mentions": []
                                }
                            })
                        else:
                            return jsonify({
                                "type": 4,
                                "data":{
                                    "tts": False,
                                    "content": "",
                                    "embeds": [
                                        {
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
                                    ],
                                    "allowed_mentions": []
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
                                "tts": False,
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
                                }],
                                "allowed_mentions": []
                            }
                        }
                    )
                    
                elif cmd_name == "testquote":
                    autext = f"Requested by {usname}"
                    if request.json["data"]["options"][0]["value"] == "qotd":
                        z = wikiquote.quote_of_the_day()
                        (qt, autor) = z
                        fttext = "Quotes from Wikiquote"
                        titl = "Quote of the Day:"
                        fticon = "https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
                    elif request.json["data"]["options"][0]["value"] == "random":
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

                            "tts": False,
                            "content": "",
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
                            ],
                            "allowed_mentions": []
                        }
                    })
                elif cmd_name == "avatar":
                    try:
                        options = request.json["data"]["options"]
                    except KeyError:
                        url = avurl
                        uname = usname
                    else:
                        uid = request.json["data"]["options"][0]["value"]
                        res = requests.get(f"https://discord.com/api/v8/users/{uid}",headers={"Authorization":"Bot NzkxMTUzODA2MDU4NDU1MDc1.X-LBZg.uhgfgX6U5tbRr0r0asEw0V52TGs"})
                        user = res.json()
                        uav = user["avatar"]
                        uname = user["username"]
                        if user["avatar"].startswith('a_'):
                            url = f"https://cdn.discordapp.com/avatars/{uid}/{uav}.gif"
                        else:
                            url = f"https://cdn.discordapp.com/avatars/{uid}/{uav}"
                    return jsonify({
                        "type": 3,
                        "data": {

                            "tts": False,
                            "content": "",
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
                            ],
                            "allowed_mentions": []
                        }
                    })
                else:
                    return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "tts": False,
                                "content":f'Sorry to say but the command you tried to use is currently unavailable (and probably under development :tools:).\nPlease try again later.',
                                "embeds" : [],
                                "allowed_mentions": []
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
                                "tts": False,
                                "content":f"Sorry, an error has occured. :negative_squared_cross_mark: Either your input has caused this error or it is from my side. Please report :clipboard: this to the bot developers along with the error code:\nError Code: {choi} *Joking*\n```py\n{type(e).__name__} : {e}\n```",
                                "embeds" : [],
                                "allowed_mentions": []
                            }
                        }
                    )
port = os.getenv('PORT')
if port:
    app.run(host='0.0.0.0',port=port)
else:
    print("Not able to get the PORT env variable.")
