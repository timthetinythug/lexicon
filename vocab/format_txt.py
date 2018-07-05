# format_txt(lines) takes in individual line from a text file and removes the following:
#   "\n" at the end of individual lines
#   "empty lines
# format_txt: "string" --> "string"

def format_txt(line):
    if type(line) == None:
        return None
    else:
        return line[:-1]

def format(txt):
    data = format_txt(list(map(lambda k: k.strip().lower(), txt)))
    return list(filter(lambda k: k != '', data))


