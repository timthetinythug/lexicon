class Word:
    def __init__(self, freq=None):
        self.freq = freq
        self.name = str(self)
        self.length = len(self.name)

