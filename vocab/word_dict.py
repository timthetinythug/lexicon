#

def vocab(words):
    vocabulary = {}
    for i in words:
        for k in i[1:]:
            x = k.split(",")
            if x[0] in vocabulary:
                if int(x[1]) == 0: # incorrect attempt
                    vocabulary[x[0]] += 1
            else:
                if int(x[1]) == 0: # incorrect attempt
                    vocabulary[x[0]] = 1
                else:
                    vocabulary[x[0]] = 0

    return vocabulary


