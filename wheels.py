import RPi.GPIO as io

io.setmode(io.BCM)
in_pin1 = 15
in_pin2 = 17
in_pin3 = 23
in_pin4 = 22

io.setup(in_pin1, io.OUT)
p1 = io.PWM(in_pin1, 50)
p1.start(0)
io.setup(in_pin2, io.OUT)
p2 = io.PWM(in_pin2, 50)
p2.start(0)
io.setup(in_pin3, io.OUT)
p3 = io.PWM(in_pin3, 50)
p3.start(0)
io.setup(in_pin4, io.OUT)
p4 = io.PWM(in_pin4, 50)
p4.start(0)

def forward():
    p1.start(100)
    p2.start(0)
    p3.start(100)
    p4.start(0)
    print("forward")

def reverse():
    p1.start(0)
    p2.start(100)
    p3.start(0)
    p4.start(100)
    print("reverse")

def right():
	p1.start(0)
	p2.start(50)
	p3.start(50)
	p4.start(0)
	print("right")

def left():
	p1.start(50)
	p2.start(0)
	p3.start(0)
	p4.start(50)
	print("left")

def stop():
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0) 
    print("stahp")

while True:
    cmd = raw_input("Enter w (forward) or s (reverse) or a (left) or d (right) or x (stop): ")
    if cmd == "":
        continue
    direction = cmd[0]
    if direction == "w":
        forward()
    elif direction == "s":
        reverse()
    elif direction == "a":
	left()
    elif direction == "d":
	right()
    elif direction == "x":
        stop()
    else:
        stop()

