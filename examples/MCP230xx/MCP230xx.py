#!/usr/bin/env python

from Adafruit_MCP230XX import Adafruit_MCP230XX

# ****************************************************
# Set num_gpios to 8 for MCP23008 or 16 for MCP23017!
# If you have a new Pi you may also need to add: bus=1
# ****************************************************
mcp = Adafruit_MCP230XX(address=0x20, num_gpios=16)

# Set pins 0, 1, 2 as outputs
mcp.config(0, mcp.OUTPUT)
mcp.config(1, mcp.OUTPUT)
mcp.config(2, mcp.OUTPUT)

# Set pin 3 to input with the pullup resistor enabled
mcp.pullup(3, True)

# Read pin 3 and display the results
print "%d: %x" % (3, mcp.input(3))

# Python speed test on output 0 toggling at max speed
while True:
    mcp.output(0, 1) # Pin 0 High
    mcp.output(0, 0) # Pin 0 Low
