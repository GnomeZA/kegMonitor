import RPi.GPIO as GPIO

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)


#Sets the the 3 relay channels to high or low
def setRelay(channel, state):
    #true will set the chosen channel to low
    if state:
        if channel == 1:
            GPIO.output(18,GPIO.LOW)
        elif channel == 2:
            GPIO.output(27,GPIO.LOW)
        elif channel == 3:
            GPIO.output(22,GPIO.LOW)
    #false will set the chosen channel to high        
    else:
        if channel == 1:
            GPIO.output(18,GPIO.HIGH)
        elif channel == 2:
            GPIO.output(27,GPIO.HIGH)
        elif channel == 3:
            GPIO.output(22,GPIO.HIGH)
            



