import traceback
from interactions.autocomplete import *
from imports.utils.errors.errhandle import handle

def tfour(r):
    cmdname=r.json["data"]["name"]
    try:
        if cmdname=="quote":
            return quotesearch.atc(input=r.json["data"]["options"][0]["options"][0]["value"])
    except:
        return handle(r=r,t=traceback.format_exc())
