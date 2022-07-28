from sphero_sprk import Sphero
from time import sleep
from datetime import datetime
from utils import map

'''
raw motor modes:
0x00: off (open circuit)
0x01: forward
0x02: reverse
0x03: brake (motor shorted)
0x04: ignore (motor speed and mode unchanged)
orb.set_raw_motor_values(0x01,255,0x01,255)
'''

orb = Sphero("EE:26:97:91:E8:45") # if you're trying to run this on your own sphero, remember to replace the bluetooth address to avoid a giant fucking headache
orb.connect()
orb.set_rgb_led(25,78,25)
orb.set_stabilization(True)

#orb.roll(0,0)
#for i in range(359):
    #orb.roll(0,i)
    #print(i)
    #sleep(0.005)

while True:
    orb.roll(0,255)
    ####orb.set_raw_motor_values(0x01,255,0x01,255)
    minute = datetime.now().minute
    heading = round(map(minute, 0, 59, 0, 359))

    print(f"minute is {minute}, translates to motor heading {heading}")
    orb.roll(255,heading)
    sleep(1)

