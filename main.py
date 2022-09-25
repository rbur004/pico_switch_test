# Turn on LED in button on
from machine import Pin
import utime
import json

class LightState:
    def __init__(self, pin_in, pin_out):
        
        self.switch_pin = Pin(pin_in, Pin.IN, Pin.PULL_UP)
        self.light_pin = Pin(pin_out, Pin.OUT)
        self.last_push_ms = utime.ticks_ms()
        self.last_push = utime.time()
        self.switch_pin.irq(trigger=Pin.IRQ_FALLING, handler=lambda ih: handle_int(self.switch_pin,pin_in))
        
# Catch the Pin interrupt
def handle_int(pin,gpio):
    global switch
    pin.irq(trigger=Pin.IRQ_FALLING, handler=None) # Disable interrupts while in handler
    time_s = utime.time()
    ticks_ms = utime.ticks_ms()
    diff_s = time_s - switch[gpio].last_push
    diff_ms = utime.ticks_diff(ticks_ms, switch[gpio].last_push_ms)
    # It has been at least 250ms since last push
    if pin.value() == 0 and ( diff_s > 2 or diff_ms > 250 ):
        switch[gpio].last_push = time_s
        switch[gpio].last_push_ms = ticks_ms
        switch[gpio].light_pin.toggle()
    pin.irq(trigger=Pin.IRQ_FALLING, handler=lambda ih: handle_int(pin,gpio)) # Enable interrupts again
  
def print_state():
    global switch
    r = {}
    for k,v in switch.items():
        r[k] = v.light_pin.value()
    print( json.dumps(r) )


def toggle_switch(s):
    switch[s].light_pin.toggle()
      
switch = {}
switch[0] = LightState(0,12)   # Grounding pin 0 will toggle pin 25
switch[1] = LightState(1,13) # Grounding pin 26 will toggle pin 25
switch[2] = LightState(2,14)   # Grounding pin 0 will toggle pin 25
switch[3] = LightState(3,15) # Grounding pin 26 will toggle pin 25
switch[4] = LightState(4,25) # Grounding pin 26 will toggle pin 25

