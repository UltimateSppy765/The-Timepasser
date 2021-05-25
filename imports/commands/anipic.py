import os,requests
from imports.utils.common import anipicc

def cmd(anim:bool,animal:str,usid:str):
    return anipicc.pic(anim=anim,animal=animal,usid=usid)
