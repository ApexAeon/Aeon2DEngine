import pygame, sys
from pygame.locals import *
from common import DISPLAYSURF
from common import FONT
import json
import time
import math

def loadAssets(): # Attempts to load all assets listed in assets.json into the assets dictionary. Replaced missing textures with error texture.
    asset_list = json.loads(open('../game/metadata/asset_list.json').read())
    assets = []
    for pair in assetlist:
        try:
            assets[pair] = pygame.image.load(asset_list[pair])
        except:
            assets[pair] = pygame.Surface((25, 25))
    return assets
def getAsset(name, assets): # Get an already loaded asset, if asset not found, replace with error texture.
    if name in assets:
        return assets[name]
    else:
        return pygame.Surface((25, 25))
def getMask(name, masks):
    if name in masks:
        return masks[name]
    else:
        return pygame.mask.from_surface(pygame.Surface((25, 25)))
def loadAsset(filename): # Attempts to load a single image, if an error occurs, it loads the error texture instead.
    try:
        return pygame.image.load(filename)
    except:
        return pygame.Surface((25, 25))
def getLevel(name, level):
    if name in level:
        return level[name]
    else:
        return pygame.Surface((25, 25))
