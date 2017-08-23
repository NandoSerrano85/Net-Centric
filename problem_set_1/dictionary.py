#code to help me with definition blocks from problem set 1
import json, re
from random import randint

def confirm():
    cont = raw_input("would you like to continue: ")
    if re.search('y',cont):
        return False
    elif re.search('n', cont):
        return True
    else:
        print "Please enter 'yes' or 'no' || y or n"
        confirm()

def user_input(key, value):
    accuracy = 0
    answer = raw_input("What is the definition for ''{}'': ".format(key))
    value = value.split(' ')
    print value
    answer = answer.split(' ')
    print answer
    for n in range(0, len(value)-1):
        if n < len(answer):
            if re.search(value[n], answer[n]) :
                accuracy = accuracy + 1
            else:
                pass
    print accuracy
    accuracy = (abs(accuracy - (len(value)-1)) / (len(value)-1)) * 100
    print accuracy

def main():
    word_list = list()
    doc = open('dict.json', 'r')
    dictionary = json.loads(doc.read())
    for key, value in dictionary.iteritems():
        word_list.append(key)
    end = False
    while end == False:
        n = randint(0,len(word_list)-1)
        value = dictionary[word_list[n]]
        user_input(word_list[n], value)
        end =  confirm()
    search = None

main()
