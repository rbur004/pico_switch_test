# pico_switch_test

* Load main.py onto pico with Thonny
* close Thonny, as it causes problems with our using the serial port to talk to the pico via USB
* power cycle the pico, so it runs main.py
## From a standard Pi
Using Rareblogs example 'Talker' class. http://blog.rareschool.com/2021/01/controlling-raspberry-pi-pico-using.html
* print_state.py
  will print a json line, showing the light states.
* Toggle a lights state using the switch name defined in main.py (I used 0..4)
```
./toggle.py <switch_name>
```
 
