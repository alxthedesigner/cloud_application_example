from flask import Flask
from flask import request

application = Flask(__name__)   #App Instance created

@application.route("/")         #When URL ends in '/', execute method
   def home():
      return WORDHTML

  WORDHTML = """
     <html><body>
         <h2>Word and Number Game</h2>
         <form action="/game">
             Enter a word: <input type='text' name='wrd'><br>
             Enter a number <input type='text' name='num'><br>
             <input type='submit' value='Continue'>
         </form>
     </body></html>"""

  
  
@application.route("/game")
  word = request.args.get('wrd', '')
  number = request.args.get('num', '')
  
  def infoDescription():
      doubled = number*2
      #print "The doubled value of", num, "is", doubled

      wordL = len(word)
      wordmsg1 = "Your word has", wordL, "letters"

      backwrd = word[::-1]
      if word == backwrd:
          wordmsg2 = "Your word is a palindrome! Your word spelled backwards is", backwrd
      else:
          wordmsg2 = "Your word spelled backwards is", backwrd

      return DESCRIPTIONHTML.format(doubled, wordmsg1, wordmsg2)
  
  DESCRIPTIONHTML = """
     <html><body>
         <h2>Your number doubled is, {0}!</h2>
         {1}, {2}
     </body></html>
     """

if __name__ == "__main__":
    application.run()             # run flask App Instance
