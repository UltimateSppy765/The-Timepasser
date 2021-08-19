from imports.utils.common.anipicc import pic

def select(animal:str,oguser:str,usid:str,aid:str,token:str,iid:str):
    if usid!=oguser:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> You can't use that select menu on someone else's message, please try on your own one."
            }
        }
    return {
        "type": 7,
        "data": pic(anim=False,animal=animal,usid=usid)
    }
