#!/usr/bin/python3
import serial
# Rareblog http://blog.rareschool.com/2021/01/controlling-raspberry-pi-pico-using.html

class Talker:
    TERMINATOR = '\r'.encode('UTF8')

    def __init__(self, timeout=2):
        self.serial = serial.Serial('/dev/ttyACM0', 115200, timeout=timeout)

    def send(self, text: str):
        line = '%s\r\f' % text
        self.serial.write(line.encode('utf-8'))
        reply = self.receive()
        reply = reply.replace('>>> ','') # lines after first will be prefixed by a propmt
        if reply != text: # the line should be echoed, so the result should match
            raise ValueError( 'expected "{}" got "{}"'.format(text,reply) )

    def receive(self) -> str:
        line = self.serial.read_until(self.TERMINATOR)
        return line.decode('UTF8').strip()

    def close(self):
        self.serial.close()

t = Talker()

t.send("print_state()")

#t.send('2+2')
print(t.receive())

