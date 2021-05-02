from googleapiclient import discovery
import os,json

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
    if tox>0.9 or prof>0.5:
        return True
    else:
        return False