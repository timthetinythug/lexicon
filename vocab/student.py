from format_txt import format
from parsed import parser
from word_dict import vocab


# Student will create an object for student with student name &
# and parse their vocabs for further implementation
# type(name) == string
# type(vocab_sheet) == string (file.txt)
# have the following file format:
#   Date
#   word, 0 or 1
#   word, 0 or 1
#           .
#           .
#           .
#   ***
#           .
#           .
#           .
#   ***
#   \n

class Student:

    def __init__(self, name, vocab_sheet):

        self.name = name
        self.vocab = {}
        self.excel = []

        with open(vocab_sheet) as f:
            data = f.readlines()
            formatted = format(data)
            self.excel = parser(formatted, '***')
            self.vocab = vocab(self.excel)

    def __eq__(self, other):
        if (self.name == other.name) and \
                (self.excel == other.excel):
            return True
        else:
            return False

    def __repr__(self):
        temp = "Student: "
        temp += self.name + '\n' + "Vocab: "
        for i in self.vocab:
            temp += i + '\n' + " "*len("vocab: ")
        return str(temp)


