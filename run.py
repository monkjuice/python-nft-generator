from pathlib import Path
import csv
from PIL import Image
import random
from os.path import exists

assetsFolder = "\\assets"

BASES = ['BLINDERS']

traitsPool = {}
traitWeightsPool = {}

traits = ['BG', 'HEAD', 'SHOES', 'PANTS', 'UPPER', 'FACE', 'EYES', 'ACC_left', 'ACC_right', 'MOUTH', 'EYES', 'ACC_cara', 'BASE']
traitsOrder = ['HEAD-B', 'SHOES-B', 'PANTS-B', 'UPPER-B', 'gral\BASE', 'PANTS-F','SHOES-F', 'PANTS-F2', 
'UPPER-F', 'ACC_left', 'ACC_right', 'gral\MOUTH', 'gral\EYES', 'ACC_cara', 'HEAD-F']


def genTraitsPool():
    currentTrait = ''

    with open("traitsDist.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()

            if stripped_line == 'ï»¿':
                continue

            if stripped_line in traits:
                currentTrait = stripped_line
                traitsPool[stripped_line] = []
                traitWeightsPool[stripped_line] = []

            if currentTrait != '' and stripped_line != '' and stripped_line not in traits:

                weight = int(stripped_line[stripped_line.index('(') + 1:stripped_line.index(')')])

                trait = stripped_line[0:stripped_line.index('(') - 1]

                traitsPool[currentTrait].append(trait)
                traitWeightsPool[currentTrait].append(weight)

            
def buildImages():
    for i in range(10):
        currentCharacterTraits = { i : [] for i in traits }

        imgPath = ('assets\\hoppaz\\' + random.choices(traitsPool['BG'], traitWeightsPool['BG'], k=1)[0] + "-BG.png")

        result = Image.open(imgPath).convert("RGBA").resize((2048,2048))

        for t in traits[1:len(traits)]:
            trait = random.choices(traitsPool[t], traitWeightsPool[t], k=1)[0]
            
            currentCharacterTraits[t] = trait

        for t in traitsOrder:
            traitImgPath = ''
            traitImg = None
            if '-' in t:
                traitPathValue = currentCharacterTraits[t[0:t.index('-')]]
                traitPathKey = t[0:t.index('-')]

                layerPos = t[t.index('-') + 1: len(t)]

                traitImgPath = 'assets\\hoppaz\\' + traitPathValue + '-' + traitPathKey + '_' + layerPos + ".png"
                print(traitImgPath)
                if not exists(traitImgPath):
                    continue
            elif '\\' in t:
                traitPathValue = currentCharacterTraits[t[t.index('\\') + 1: len(t)]]
                traitPathKey = t[t.index('\\') + 1: len(t)]

                traitImgPath = 'assets\\gral\\' + traitPathValue + '-' + traitPathKey + ".png"
                print(traitImgPath)
                if not exists(traitImgPath):
                    continue
            else:
                traitPathValue = currentCharacterTraits[t]
                traitPathKey = t

                traitImgPath = 'assets\\hoppaz\\' + traitPathValue + '-' + traitPathKey + ".png"
                print(traitImgPath)
                if not exists(traitImgPath):
                    continue
            
            traitImg = Image.open(traitImgPath).convert("RGBA").resize((2048,2048))

            print(result.mode)
            print(traitImg.mode)

            result = Image.alpha_composite(result, traitImg)
        result.save('C:\\results\\' + str(i) + '.png')


# def findFile():


genTraitsPool()
buildImages()