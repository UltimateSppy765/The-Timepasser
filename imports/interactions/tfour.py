from interactions.autocomplete import *

def tfour(r):
    cmdname=r.json["data"]["name"]
    if cmdname=="quote":
        return quotesearch.atc(input=r.json["data"]["options"][0]["options"][0]["value"])
