import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)

#pins assign

lm_ena = 33
lm_pos = 35
lm_neg = 37

rm_ena = 36
rm_pos = 38
rm_neg = 40

#output mode

gpio.setup(lm_ena,gpio.OUT)
gpio.setup(lm_pos,gpio.OUT)
gpio.setup(lm_neg,gpio.OUT)

gpio.setup(rm_ena,gpio.OUT)
gpio.setup(rm_pos,gpio.OUT)
gpio.setup(rm_neg,gpio.OUT)

def moverobot(direction):
    if(direction == "f"):
        print("forward")
        gpio.output(lm_ena,gpio.HIGH)
        gpio.output(lm_pos,gpio.HIGH)
        gpio.output(lm_neg,gpio.LOW)

        gpio.output(rm_ena,gpio.HIGH)
        gpio.output(rm_pos,gpio.HIGH)
        gpio.output(rm_pos,gpio.LOW)

    if(direction == "b"):
        print("backwards")
        gpio.output(lm_ena,gpio.HIGH)
        gpio.output(lm_pos,gpio.LOW)
        gpio.output(lm_neg,gpio.HIGH)

        gpio.output(rm_ena,gpio.HIGH)
        gpio.output(rm_pos,gpio.LOW)
        gpio.output(rm_pos,gpio.HIGH)

    if(direction == "r"):
        print("right")
        gpio.output(lm_ena,gpio.HIGH)
        gpio.output(lm_pos,gpio.HIGH)
        gpio.output(lm_neg,gpio.LOW)

        gpio.output(rm_ena,gpio.HIGH)
        gpio.output(rm_pos,gpio.LOW)
        gpio.output(rm_pos,gpio.HIGH)
    
    if(direction == "l"):
        print("left")
        gpio.output(lm_ena,gpio.HIGH)
        gpio.output(lm_pos,gpio.LOW)
        gpio.output(lm_neg,gpio.HIGH)

        gpio.output(rm_ena,gpio.HIGH)
        gpio.output(rm_pos,gpio.HIGH)
        gpio.output(rm_pos,gpio.LOW)

    if(direction == "s"):
        print("stop")
        gpio.output(lm_ena,gpio.HIGH)
        gpio.output(lm_pos,gpio.LOW)
        gpio.output(lm_neg,gpio.LOW)

        gpio.output(rm_ena,gpio.HIGH)
        gpio.output(rm_pos,gpio.LOW)
        gpio.output(rm_pos,gpio.LOW)

for i in range(0,5):
    moverobot("f")
    sleep(1)
    moverobot("b")
    sleep(1)
    moverobot("r")
    sleep(1)
    moverobot("l")
    sleep(1)
    moverobot("s")
    sleep(1)

gpio.cleanup
