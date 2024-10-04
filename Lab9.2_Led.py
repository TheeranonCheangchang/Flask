from flask import Flask, render_template
 
app = Flask(__name__) 

@app.route('/<led>/<name>')
def index(led,name): 
   
   return render_template('lab9_led.html', led=led, name=name)
    
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')