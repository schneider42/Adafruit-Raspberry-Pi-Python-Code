#!/usr/bin/env python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
# ----------------------------------------------------------------------
# Test code

lcd = Adafruit_CharLCDPlate()
lcd.begin(16, 2)
lcd.clear()
lcd.message("Adafruit RGB LCD\nPlate w/Keypad!")
sleep(1)

col = (('Red' , lcd.RED) , ('Yellow', lcd.YELLOW), ('Green' , lcd.GREEN),
        ('Teal', lcd.TEAL), ('Blue'  , lcd.BLUE)  , ('Violet', lcd.VIOLET),
        ('Off' , lcd.OFF) , ('On'    , lcd.ON))

print "Cycle thru backlight colors"
for c in col:
    print c[0]
    lcd.clear()
    lcd.message(c[0])
    lcd.backlight(c[1])
    sleep(0.5)

btn = ((lcd.SELECT, 'Select', lcd.ON),
        (lcd.LEFT  , 'Left'  , lcd.RED),
        (lcd.UP    , 'Up'    , lcd.BLUE),
        (lcd.DOWN  , 'Down'  , lcd.GREEN),
        (lcd.RIGHT , 'Right' , lcd.VIOLET))

print "Try buttons on plate"
lcd.clear()
lcd.message("Try buttons")
prev = -1
while True:
    for b in btn:
        if lcd.buttonPressed(b[0]):
            if b is not prev:
                print b[1]
                lcd.clear()
                lcd.message(b[1])
                lcd.backlight(b[2])
                prev = b
            break
