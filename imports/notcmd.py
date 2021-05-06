from googleapiclient import discovery
from random import choice,randint
import os,json,wikiquote,wikiquotes

API_KEY=os.environ['P_API_KEY']
service=discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

def usav(id:str,discid:str,av):
    if av is None:
        return f"https://cdn.discordapp.com/embed/avatars/{int(discid)%5}.png"
    elif av.startswith("a_"):
        return f"https://cdn.discordapp.com/avatars/{id}/{av}.gif"
    else:
        return f"https://cdn.discordapp.com/avatars/{id}/{av}.webp"

def analyse(cont:str):
    ar1= {
        "comment": {"text": f"{cont}"},
        "requestedAttributes": {"SEVERE_TOXICITY": {}}
    }
    ar2= {
        "comment": {"text": f"{cont}"},
        "requestedAttributes": {"PROFANITY": {}}
    }
    try:
        res1=service.comments().analyze(body=ar1).execute()
    except:
        tox=0.5
    else:
        k=json.loads(json.dumps(res1))
        tox=k["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]
    try:
        res2=service.comments().analyze(body=ar2).execute()
    except:
        prof=0.5
    else:
        v=json.loads(json.dumps(res2))
        prof=v["attributeScores"]["PROFANITY"]["summaryScore"]["value"]
    if tox>0.9 or prof>0.95:
        if tox>0.9 and prof>0.95:
            reason=f"Detected {round(tox*100,3)}% Toxicity and {prof*100}% Profanity"
        elif tox>0.9:
            reason=f"Detected {round(tox*100,3)}% Toxicity"
        else:
            reason=f"Detected {round(prof*100,3)}% Profanity"
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": f"> <:tickNo:315009174163685377> Sorry, your command usage was blocked as harmful text was detected in your input.\n> If you think it is a mistake, please contact the bot developers. (You can see them through `/aboutme devs`)\n> Reason: {reason}\n> :confused: Your input: (*just in case you forgot what you wrote...*)\n```\n{cont}\n```"
            }    
        }
    else:
        return None

def qsearch(query:str):
    ftext="Quotes from Wikiquote"
    ficon="https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
    thum="https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
    try:
        try:
            a=wikiquote.search(query)
        except:
            a=wikiquotes.search(query)
    except:
        json={
            "embeds": [
                {
                    "title": f"No result found for query: **'{query}'**",
                    "description": "Sorry, your query didn't work, please try with a different one.",
                    "color": 3092791,
                    "thumbnail": {
                        "url": thum
                    },
                    "footer": {
                        "text": ftext,
                        "icon_url": ficon
                    }
                }
            ]
        }
    else:
        for i in a:
            if query.lower() in i.lower():
                autor=i
                qt=choice(wikiquote.quotes(autor)) if (2==(num:=randint(1,2))) else wikiquotes.random_quote(autor,"english")
                break
            else:
                b=choice(a)
                c=wikiquote.quotes(b)
                for j in c:
                    if query.lower() in j.lower():
                        autor=b
                        qt=j
                        break
                try:
                    meow=f"{qt}\n- {autor}"
                except:
                    d=wikiquotes.get_quotes(b,"english")
                    for k in d:
                        if query.lower() in k.lower():
                            autor=b
                            qt=k
        try:
            json={
                "embeds": [
                    {
                        "title": f"Search result for query: **'{query}'**",
                        "description": f"{qt}\n- {autor}",
                        "color": 3092791,
                        "thumbnail": {
                            "url": thum
                        },
                        "footer": {
                            "text": ftext,
                            "icon_url": ficon
                        }
                    }
                ]
            }
        except:
            json={
                "embeds": [
                    {
                        "title": f"No result for query: **'{query}'**",
                        "description": "Sorry, couldn't find a quote for the given query, please try again.",
                        "color": 3092791,
                        "thumbnail": {
                            "url": thum
                        },
                        "footer": {
                            "text": ftext,
                            "icon_url": ficon
                        }
                    }
                ]
            }   
    return json
