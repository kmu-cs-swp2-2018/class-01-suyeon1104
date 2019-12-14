class DB:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()


        for line in lines:
            word = line.rstrip()
            self.words.append(word)
