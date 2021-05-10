from imports.utils import perspective

def simon(text:str):
    um=perspective.analyse(cont=text)
    if um is not None:
        return um
    else:
        return {
            "type": 4,
            "data": {
                "content": f"Simon says {text}"
            }
        }
