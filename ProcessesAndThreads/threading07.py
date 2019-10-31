from threading import Thread
from time import ctime,sleep
from atexit import register
from re import compile
from urllib.request import urlopen as uopen

REGEX = compile("#([\d,]+) in Books ")
AMZN = "http://amazon.com/dp/"
ISBNs = {
    "0132269937":"Core Python Programming",
    "0132356139":"Python Web Development with Django",
    "0137143419":"Python Fundamentals"
}

def getRanking(isbn):
    page = uopen("{}{}".format(AMZN,isbn))
    data = page.read().decode('utf-8')
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print("- {} ,ranked: {}".format(ISBNs[isbn],getRanking(isbn)))

def main():
    print("start,",ctime())
    for isbn in ISBNs:
        #print(isbn)
        _showRanking(isbn)
        #Thread(target=_showRanking,args=(isbn,)).start()

@register
def _atexit():
    print("all DONE at: ",ctime())

if __name__ == "__main__":
    main()