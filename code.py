import os
import requests
import wikiquote
from random import choice,randint
from flask import Flask, request, jsonify,abort
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType


CLIENT_PUBLIC_KEY = '731d23ca5906b7f156c4f606ad29ae1d6efaf82661889227e9226f8694d5fbce'

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
            if request.json["guild_id"] == '789147777069744179' and request.json["channel_id"] == '789147777069744182':
                usd = request.json["member"]["user"]["id"]
                return jsonify(
                    {
                        "type": 3,
                        "data": {
                            "tts": False,
                            "content": f"Sorry <@{usd}>, I've been instructed not to do anything in <#789147777069744182>.",
                            "embeds" : [],
                            "allowed_mentions": []
                        }
                    }
                )
            else:
                cmd_name = request.json["data"]["name"] #to make it easy to check for name
                if cmd_name == 'simon':
                    return jsonify(
                        {
                            "type": 3,
                            "data": {
                                "tts": False,
                                "content":f'Simon says {request.json["data"]["options"][0]["value"]}',
                                "embeds" : [],
                                "allowed_mentions": []
                            }
                        }
                    )
                elif cmd_name == "dice":
                    dice = [1,2,3,4,5,6,"**The dice got stuck against the wall. Try Again!**","**The dice got lost. Try Again!**"]
                    roll = choice(dice)
                    content = f"The dice rolled {roll}." if type(roll) == int else roll
                    return jsonify(
                        {
                            "type": 3,
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
                            "type": 3,
                            "data": {
                                "tts": False,
                                "content":result,
                                "embeds" : [],
                                "allowed_mentions": []
                            }
                        }
                    )
                elif cmd_name == "echo":
                    usname = request.json["member"]["user"]["username"]
                    usid = request.json["member"]["user"]["id"]
                    usav = request.json["member"]["user"]["avatar"]
                    intext = request.json["data"]["options"][0]["value"]

                    if usav.startswith('a_'):
                        imgurl = f"https://cdn.discordapp.com/avatars/{usid}/{usav}.gif"
                    else:
                        imgurl = f"https://cdn.discordapp.com/avatars/{usid}/{usav}"
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
                                        "icon_url": imgurl
                                    }
                                }
                            ],
                            "allowed_mentions": []
                        }
                    })
                elif cmd_name == "anipic":
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
                                "type": 4,
                                "data":{
                                    "tts": False,
                                    "content": greet,
                                    "embeds": [
                                        {
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
                                                "url": "https://tenor.com/view/fox-cute-adorable-sleepy-gif-15311158"
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
                else:
                    return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "tts": False,
                                "content":f'Command Under :tools:Development:tools:',
                                "embeds" : [],
                                "allowed_mentions": []
                            }
                        }
                    )
    except Exception as e:
        return jsonify(
                        {
                            "type": 4,
                            "data": {
                                "tts": False,
                                "content":f'Sorry, A Error Has Occured\n```py\n{type(e).__name__} : {e}\n```',
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
