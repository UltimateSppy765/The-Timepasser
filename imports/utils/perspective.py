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
                "content": f"> <:tickNo:315009174163685377> Sorry, your command usage was blocked as harmful text was detected in your input.\n> If you think it is a mistake, please contact the bot developers. (You can see them through `/aboutme devs`)\n> **Reason:** {reason}\n> :confused: __Your input:__ (*just in case you forgot what you wrote...*)\n```\n{cont}\n```"
            }    
        }
    else:
        return None
