# Movind two SG90 Servos conected with Raspberry Pi Pico by SSK (TechCree)

# Load Libaries 
from machine import Pin, PWM
import _thread
import time
from machine import ADC
import utime


#Definition of Servo Positions
#0 Grad
MIN = 300000 

# 90 Grad
MID = 1200000

#more Grad definitions
MID190 = 400000
MID180 = 500000   
MID170 = 600000
MID160 = 700000   
MID150 = 800000   
MID140 = 900000   
MID130 = 1000000  
MID120 = 1100000  
MID110 = 1200000  
MID100 = 1300000  
MID90 = 1400000   
MID80 = 1500000   
MID70 = 1600000   
MID60 = 1700000   
MID50 = 1800000   
MID40 = 1900000
MID30 = 2000000   
MID20 = 2100000   
MID10 = 2200000   

#180 Grad
MAXA = 2200000

#maximum
MAX = 2600000


# function to handle first core(1)
def first_core_function():
    pwm = PWM(Pin(15))
    pwm.freq(50)
    
    pwm.duty_ns(MID180)
    utime.sleep(1)
    pwm.duty_ns(MID10)
    time.sleep(1)
    pwm.duty_ns(MID50)
    print("Servo 1")
    

# function to handle second core(2)
def second_core_function():
    while True:
        pwm = PWM(Pin(14))
        pwm.freq(50)
        
        pwm.duty_ns(MID10)
        time.sleep(1)
        pwm.duty_ns(MID100)
        time.sleep(1)
        pwm.duty_ns(MID180)
        print("Servo 2") 
                

# start new thread 
_thread.start_new_thread(second_core_function, ())

# main loop on core 1
while True:
    # execute the first core function
    first_core_function()
