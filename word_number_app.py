from flask import Flask
from flask import request

application = Flask(__name__)   #App Instance created

@application.route("/")         #When URL ends in '/', execute method
num1 = input("Enter random number:")

def doubleNumber(num):    #Create 'doubleNumber' method
  doubled = num*2
  print "The doubled value of", num, "is", doubled

@application.route("/word")
word1 = raw_input("Enter a word: ")
       
def wordLength(wrd):
    wordL = len(wrd)
    print "Your word has", wordL, "letters"

def spellBackwards(wrd):
    backwrd = wrd[::-1]
    if wrd == backwrd:
        print "Your word is a palindrome!"

    print "Your word spelled backwards is", backwrd

if __name__ == "__main__":
    application.run()             # run flask App Instance
