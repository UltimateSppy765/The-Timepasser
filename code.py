import os
from imports.utils.fail import dmerr
from flask import Flask,request,jsonify,abort
from discord_interactions import verify_key_decorator
from imports.interactions import tthree,tfour
from imports.interactions.ttwo import slash_cmd,context_cmd

app=Flask(__name__)

#"it" refers to the interaction received unless specified.

@app.route('/',methods=['POST']) #Don't mess with this, this is used to make the app listen to `POST` requests on the route specified in the function.
@verify_key_decorator(os.environ['CLIENT_ID']) #Don't mess with this, it is used to verify the incoming interactions.
def code():
    try:  #Tries to get the guild ID.
        request.json["guild_id"]
    except:  #If interaction was used in a DM (basically guild ID doesn't exist in a DM), returns an error.
        return dmerr()
    if request.json["type"]==2: #Checks if it is an APPLICATION_COMMAND.
        if request.json["data"]["type"]==1: #Checks and runs if it is a CHAT_INPUT command.
            return jsonify(slash_cmd.slashc(r=request))
        else: #Runs this if it is a USER/MESSAGE command.
            return jsonify(context_cmd.contextc(r=request))
    elif request.json["type"]==3: #Checks and runs if it is a MESSAGE_COMPONENT.
        return jsonify(tthree.tthree(r=request))
    elif request.json["type"]==4:
        return jsonify(tfour.tfour(r=request)) #Checks and runs if it is an Autocomplete Interaction.

port=os.getenv('PORT') #Gets the OS PORT that is open (stored in environment variables).
if port: #Checks and runs the app if a PORT exists in the environment variables.
    app.run(host='0.0.0.0',port=port)
else:
    print("Unable to find PORT environment variable.")
