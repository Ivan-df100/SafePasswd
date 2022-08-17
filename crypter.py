class Crypter:
    def __init__(self, key: str) -> None:
        self.kpos = -1
        self.key = key
        self.keyPretty = [ord(k) for k in key]
        self.lenkey = len(self.keyPretty) - 2

    def crypt(self, text: str):
        textNormalized = [ord(k) for k in text]
        result = ""
        for char in textNormalized:
            n = self.next()
            result += chr(char ^ n)
        self.kpos = -1
        return result


    def next(self):
        if self.kpos == self.lenkey:
            self.kpos = 0
        else:
            self.kpos += 1
        return self.keyPretty[self.kpos]