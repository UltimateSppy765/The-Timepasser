import os
from flask import Flask,request,jsonify,abort
from discord_interactions import verify_key_decorator,InteractionType,InteractionResponseType
from imports.interactions import ttwo,tthree

app = Flask(__name__)

@app.route('/',methods=['POST'])
@verify_key_decorator(os.environ['CLIENT_ID'])
def code():
    if request.json["type"]==1:
        return jsonify({
            "type": 1
        })
    elif request.json["type"]==2:
        return jsonify(ttwo.slashc(r=request))
    elif request.json["type"]==3:
        return jsonify(tthree.tthree(r=request))

port=os.getenv('PORT')
if port:
    app.run(host='0.0.0.0',port=port)
else:
    print("Unable to find PORT environment variable.")
