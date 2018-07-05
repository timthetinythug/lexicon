# parser(txt, marker) produces a list of lists parsed by marker
# parser: [string], string --> [[string], [string], ...]

def parser(txt, marker):
    temp = []
    # --------------------------------------------- The following parses the vocabulary by date
    #                                           >>> [['date', 'word', 'word', ...], ['date', 'word', 'word',...], ...]
    marker_index = []  # marks all the sym in formatted data
    counter = 0
    for i in txt:
        if i == marker:
            marker_index.append(counter)
        counter += 1

    counter = 0
    for i in marker_index:  # splits words by marker indexing
        temp.append(txt[counter:i])
        counter = i + 1
        # --------------------------------------------- End of parsing
    return temp


