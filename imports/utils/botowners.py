import os,requests

baseurl=os.environ['BASE_URL']
bottoken=os.environ['BOT_TOKEN']

def ownerids():
    appowners=requests.get(f"{baseurl}oauth2/applications/@me",headers={"Authorization":f"Bot {bottoken}"}).json()
    list=[]
    for i in appowners["team"]["members"]:
        list.append(i["user"]["id"])
    return list
