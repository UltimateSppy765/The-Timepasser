import os,requests,json

baseurl=os.environ['BASE_URL']

def cmd(uid:str,token:str,iid:str,sc:str,aid:str,jsn):
    if uid not in ["730361955226746923","698200925311074485","770542184310243342"]:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "> <:tickNo:315009174163685377> You cannot use this command because you are not whitelisted."
            }
        }
    try:
        jsa=json.loads(jsn)
    except:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": f"> <:tickNo:315009174163685377> The input given was not a valid JSON, please enter a valid JSON.\nYour Input:```json\n{jsn}\n```"
            }
        }
    else:
        if sc=="followup":
            jsp={
                "type": 4,
                "data": {
                    "content": "<a:typing:597589448607399949>  Processing Request..."
                }
            }
            requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsp)
            res=requests.post(f"{baseurl}webhooks/{aid}/{token}",headers={"Content-Type": "application/json"},json=jsa)
            if res.status_code==200:
                requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json={"content": f"<:tickYes:315009125694177281> Successfully evaluated JSON.```\nReturned Status Code: {res.status_code}\n```"})
                return 
            else:
                jsnerr={
                    "content": f"<:tickNo:315009174163685377> Your evaluation failed, detailed information given below:```\nReturned Status Code: {res.status_code}\n{res.json()}\n```"
                }
                requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsnerr)
                return 
        elif sc=="original":
            res=requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsa)
            if res.status_code==200:
                return
            else:
                return {
                    "type":  4,
                    "data": {
                        "content": f"<:tickNo:315009174163685377> Your evaluation failed, detailed information given below:```\nReturned Status Code: {res.status_code}\n{res.json()}\n```"
                    }
                }
