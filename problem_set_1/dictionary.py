#code to help me with definition blocks from problem set 1
import json, re
from random import randint

def main():
    doc = open('dict.json', 'r')
    dictionary = json.loads(doc.read())
    end = False
    while end == False:
        # n = randint(0,len(dictionary)-1)
        print "inside loop\n"
        key, value = dictionary['host']
        print key + "\n" + value
        # word = input("what is the definition: ")
        end = True
    search = None

main()
