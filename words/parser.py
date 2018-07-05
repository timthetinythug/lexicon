def parsed(doc):
    with open(doc) as f:
        data = f.readlines()
        words = list(map(lambda k: k.split(), data))
        # ------------------------------------------

        temp = []
        while words != []:
            k = words.pop(0)
            for i in k:
                if i not in temp:
                    temp.append(i)

        # ------------------------------------------
        return temp

