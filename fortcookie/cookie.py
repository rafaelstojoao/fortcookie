import pandas as pd
class FortuneCookie:

    def __init__(self):

        import pandas as pd

        url = 'https://raw.githubusercontent.com/rafaelstojoao/fortcookie/master/dataset/mymind.txt'
        df = pd.read_csv(url, error_bad_lines=False)
        print(df)


        # self.url = 'https://raw.githubusercontent.com/rafaelstojoao/fortcookie/master/dataset/mymind.txt'
        # self.localUrl = '../dataset/mymind.dat'
        # self.lines = [i for i in open(self.url).readlines()]

        self.myfortune = ""

    def creck(self):
        import random
        key = random.randint(0,len(self.lines))
        print(self.lines[key])
        return

if __name__ == '__main__':
    cookie = FortuneCookie()
    cookie.creck()


# creck()
