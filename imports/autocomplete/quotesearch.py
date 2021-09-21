from imports.utils.quotes.qlogic import findtitles
from random import sample

def atc(input):
    input=input.strip()
    titles=findtitles(input)
    if titles==[]:
        return
    if len(titles)>20:
        list=sample(set(titles),20)
    else:
        list=titles
    rtlist=[]
    for i in list:
        rtlist.append({"name":i,"value":i})
    return {
        "type": 8,
        "data": {
            "choices": rtlist
        }
    }
