import numpy as np
from isalp import notalp, art

potter_series = ["harry_1.txt", "harry_2.txt", "harry_3.txt", "harry_4.txt", "harry_5.txt", "harry_6.txt", "harry_7.txt"]

dic_ow = {}

def format(txt):
    with open(txt) as f:
        sum_length = 0
        data = f.readlines()
        new_data = list(filter(lambda k: not len(k)<=3, data))
        newer_data = list(map(lambda k: k.strip(), new_data))
        newest_data = list(map(lambda k: k.split(), newer_data))
        print(newest_data)
        M = []
        while newest_data != []:
            x = newest_data.pop(0)
            for i in x:
                M.append(i.lower())
        N = list(map(lambda k: notalp(k), M))
        O = list(filter(lambda k: not type(k) == type(None), N))
        P = list(filter(lambda k: art(k), O))
        for i in P:
            if i in dic_ow:
                dic_ow[i] += 1
            else:
                dic_ow[i] = 1
                sum_length += len(i)
        num_words = len(dic_ow)
        average = sum_length/num_words

format("da_vinci_code.txt")
