import os
import requests
import lxml
import bs4
from random import choice,randint
from flask import Flask, request, jsonify,abort
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType


CLIENT_PUBLIC_KEY = '731d23ca5906b7f156c4f606ad29ae1d6efaf82661889227e9226f8694d5fbce'

app = Flask(__name__)

@app.route('/', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def test():
    
    if request.json["type"] == 1:        
        return jsonify({
            "type": 1
        })
    
    else:
        cmd_name = request.json["data"]["name"] #to make it easy to check for name
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
            dice = [1,2,3,4,5,6,"**The dice got stuck against the wall. Try Again!**","**The dice got lost. Try Again!**"]
            roll = choice(dice)
            content = f"The dice rolled {roll}." if type(roll) == int else roll
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
                result = ":confetti_ball:You guessed it right!:confetti_ball:" if num == guess else f'Aah! You have guessed it wrong\nThe number was {num}'

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
        elif cmd_name == "ranani":
            res = requests.get('https://api.thecatapi.com/v1/images/search?size=small&mime_types=png,jpg')
            soup = bs4.BeautifulSoup(res.text,"lxml")
            soup = soup.p.text
            imglist = eval(soup)
            imgurl = imglist[0]['url']
            return jsonify(
                {
                    "type": 4,
                    "data": {
                        "tts": False,
                        "content":"meow",
                        "embeds" : [
                        {"image":{
                            "url":imgurl}
                        }],
                        "allowed_mentions": []
                    }
                }
            )

port = os.getenv('PORT')
if port:
    app.run(host='0.0.0.0',port=port)
else:
    print("Not able to get the PORT env variable.")
