# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>
QCC:
0. Similar to java.
1. The word "route" makes me believe that is referring to a directory and the lack of a directory name afterwards leads me to say that it runs it from the current folder it is in. 
2. Terminal
3. It prints __main__ in the terminal and also an IP Address. 
4. It will appear anywhere because I can see it.
5. In Java when you use methods for class
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



