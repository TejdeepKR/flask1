from flask import Flask,redirect,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/calculate',methods=['GET'])
def math_operation():
    opeartion= request.json["operation"]
    num1 = request.json["num1"]
    num2 = request.json["num2"]


    if opeartion == 'add':
        res = num1+num2
    elif opeartion == 'sub':
        res = num1 - num2
    elif opeartion == 'div':
        res= num1/num2
    else:
        res = num1 * num2

    return res




if __name__=='__main__':
    app.run(debug=True)