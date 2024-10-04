import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

# Pin configuration
SW1 = 27
SW2 = 17

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.OUT)  # Change to OUTPUT to control LEDs
GPIO.setup(SW2, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('ex_led2.html')

@app.route('/<led>', methods=['POST'])
def led(led):
    if led == 'led1':
        ledstate = request.form['led1State']
        if ledstate == "ON":
            GPIO.output(SW1, GPIO.HIGH)
        elif ledstate == "OFF":
            GPIO.output(SW1, GPIO.LOW)

        return render_template('ex_led2.html', ledstate=ledstate)

    elif led == 'led2':
        ledstate = request.form['led2State']
        if ledstate == "ON":
            GPIO.output(SW2, GPIO.HIGH)
        elif ledstate == "OFF":
            GPIO.output(SW2, GPIO.LOW)

        return render_template('ex_led2.html', ledstate=ledstate)

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0')
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # Cleanup GPIO settings on exit
