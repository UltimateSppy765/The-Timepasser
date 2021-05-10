def usav(id:str,discid:str,av):
    if av is None:
        return f"https://cdn.discordapp.com/embed/avatars/{int(discid)%5}.png"
    elif av.startswith("a_"):
        return f"https://cdn.discordapp.com/avatars/{id}/{av}.gif"
    else:
        return f"https://cdn.discordapp.com/avatars/{id}/{av}.webp"
