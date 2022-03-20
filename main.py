from requests import get
from random import choice

class Word:

    def __init__(self):
        self.word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        self.symbols = ['#', '/', '!', '@', '*', '&', '£', '$', '%', '^', '~']
        self.symbol = choice(self.symbols)
        _ = (input("memorable word: "))
        self.num = (str(input("memorable number: ")))
        self.var = _.replace(_[0], _[0].upper())
        

    def get_word(self):

        # we want to take the words from website, then use them as strings
        response = get(self.word_site)
        byte_words = response.content.splitlines() # splits into a list
        byte = choice(byte_words)
        self.word = byte.decode('utf-8') # byte --> string

    def get_pw(self):
        print(f"password:  {self.var}{self.symbol}{self.num}{self.word}")

foo = Word()

# f"password:  {var}{symbol}{var_num}{str_word}"

if __name__ == '__main__':
    foo.get_word()
    foo.get_pw()