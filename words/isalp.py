#notalp takes in a word and outputs proper alphabetical format without any syntax or punctuation

def notalp(s):
    if s.isalpha() == True:
        return s
    else:
        for i in range(len(s)):
            if s[i].isalpha() == False:
                if i == len(s) - 1:
                    return notalp(s[:i])
                elif i == len(s) - 2:
                    if s[-1] == 'd':
                        return notalp(s[:i])
                    elif s[-1] == 't':
                        if s == "can't":
                            return "cannot"
                        elif s[i - 1] == 'n':
                            return notalp(s[:i - 1])
                    elif s[-1] == 's':
                        return notalp(s[:i])
                    elif s[i:] == 've':
                        return notalp(s[:i])
            elif s[0] == '"' or s[0] == '(':
                return notalp(s[1:])

#art grabs small words

def art(s):
    if len(s) <= 2:
        return False
    else:
        return True