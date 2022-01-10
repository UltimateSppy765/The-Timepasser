from imports.utils.quotes.qlogic import findtitles
from random import sample

def atc(input):
    input=input.strip()
    titles=findtitles(input)
    if titles==[]:
        return {"type":8,"data":{"choices":[]}}
    rtlist=[]
    for i in titles:
        if len(rtlist)<26:
            if i.lower()==input.lower():
                rtlist.append(i)
                titles.remove(i)
            elif i.lower() in input.lower() or input.lower() in i.lower():
                rtlist.append(i)
                titles.remove(i)
    if len(rtlist)==25:
        list=rtlist
    else:
        num=len(titles) if 25-len(rtlist)>len(titles) else 25-len(rtlist)
        list=rtlist+sample(set(titles),num)
    nlist=[]
    for i in list:
        nlist.append({"name":i if input in i else f'{input} from {i}',"value":i if input in i else json.dumps({'s':input,'a':i})})
    return {
        "type": 8,
        "data": {
            "choices": nlist
        }
    }
