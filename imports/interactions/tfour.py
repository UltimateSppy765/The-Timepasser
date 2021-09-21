def tfour(r):
    cmdname=r.json["data"]["name"]
    if cmdname=="quote":
        return quotesearch.atc()
