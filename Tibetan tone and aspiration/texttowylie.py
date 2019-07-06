# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:56:59 2019

@author: User
"""
import io
import os
os.chdir("G:/我的雲端硬碟/Uncertainty estimation with probabilities/Tibetan tone case")

from pyewts import pyewts;
import numpy as np;

converter = pyewts()

#https://stackoverflow.com/questions/21292552/equivalent-of-paste-r-to-python
import functools
def reduce_concat(x, sep=""):
    return functools.reduce(lambda x, y: str(x) + sep + str(y), x)

def paste(*lists, sep=" ", collapse=None):
    result = map(lambda x: reduce_concat(x, sep=sep), zip(*lists))
    if collapse is not None:
        return reduce_concat(result, sep=collapse)
    return list(result)

fileIDsToSearch = np.arange(27,689)
fileIDs = [];
files = [];
wylieTexts = [];
for fileID in fileIDsToSearch:
    try:
        with io.open("WebCrawl/uvrip" + str(fileID) + ".txt", 'r', encoding='utf8') as f:
            text = f.read()
            print("Successful");
        files.append(text);
        fileIDs.append(fileID);
        wylieTexts.append(converter.toWylie(text));
    except FileNotFoundError:
        print("No such file.");


with open("wylie_texts.txt", "w") as text_file:
    for text in wylieTexts:
        print(text, file=text_file)
