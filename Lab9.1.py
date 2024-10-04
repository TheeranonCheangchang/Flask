from flask import Flask 
  
app = Flask(__name__) 


@app.route('/<opt>/<a>/<b>') 
def maths(opt,a,b): 
    a = float(a)
    b = float(b)
    if opt == '+':
        ans = a + b
    elif opt == '-':
        ans = a - b
    elif opt == '*':
        ans = a * b
    elif opt == 'div':
        ans = a / b if b != 0 else 'Error: Division by zero'
    else:
        return 'Error: Invalid operation'
    return f'<h3>{a} {opt} {b} = {ans}</h3>'

@app.route('/')
def index():
    return 'Lab 9_4'
    
  
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')