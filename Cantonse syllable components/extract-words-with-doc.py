import os
os.chdir("G:\\我的雲端硬碟\\Uncertainty estimation with probabilities")

import pycantonese as pc
import re
import numpy as np
import pandas as pd
if __name__ == '__main__':
    corpus = pc.hkcancor()
    allwords = corpus.tagged_words(by_files = True);


# Remove punctuation
for file in allwords.keys():
    i = 0
    for word in allwords[file]:
        if (not (word[2].isalnum())):
            allwords[file].pop(i)
        else:
            i = i + 1
        
# Remove foreign words
for file in allwords.keys():
    i = 0
    for word in allwords[file]:
        if (not (re.match('X.+', word[1]) == None) and not (word[0] == '鴨寮街')):
            allwords[file].pop(i)
        i = i + 1
# 揸fit, call機x3, 操fitx2 were also excluded
        
parsed_words = [] 
unparsed_words = []
parsed_word_files = []

for file in allwords.keys():
    i = 0;
    filename = re.sub("[A-Z]:\\\\.*\\\\hkcancor\\\\","",file)
    for word in allwords[file]:
        try:
            print("Word parsed: ", word)
            parsed_words.append(pc.parse_jyutping(word[2]));
            parsed_word_files.append(filename);
        except ValueError:
            unparsed_words.append(word)
            print("Error: The word ", word[2], " cannot be parsed.")
        except IndexError:
            unparsed_words.append(word)
            print("Error: The word ", word[2], " cannot be parsed.")

parsed_syls = []
parsed_syls_files = []

i = 0;
for word in parsed_words:
    for syl in word:
        parsed_syls.append(syl);
        parsed_syls_files.append(parsed_word_files[i]);
    i = i + 1;
    
sylDF = pd.DataFrame(parsed_syls)
sylDF = pd.concat([sylDF, pd.DataFrame(parsed_syls_files)], axis=1)
sylDF.columns = ["o","n","c","t","file"]
sylDF.to_csv("all_syls_withfile.csv",index=False, encoding='utf-8')

parsed_words_table = []
parsed_words_files = []
i = 0;
for word in parsed_words:
    new_row = [None] * 16;
    segtones_array = [x for xs in word for x in xs];
    new_row[0:len(segtones_array)] = segtones_array;
    print(segtones_array)
    parsed_words_table.append(new_row);
    parsed_words_files.append(parsed_word_files[i]);
    i = i + 1;
    
wordsDF = pd.DataFrame(parsed_words_table)
wordsDF = pd.concat([wordsDF, pd.DataFrame(parsed_word_files)], axis=1)
wordsDF.to_csv("all_words_withfile.csv",index=False, encoding='utf-8')
