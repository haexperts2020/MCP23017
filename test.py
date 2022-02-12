# this script flashes an LED on pin 4 (PA4) and 8 (PB0) of a CQRobot Ocean: MCP23017 IO Expansion Board

from time import sleep          # Import sleep from time
import Adafruit_GPIO.MCP230xx as MCP230XX # Import Adafruit MCP23017 Library

mcp = MCP230XX.MCP23017(address=0x27) # Instantiate mcp object, this is the default address

mcp.setup(4, MCP230XX.GPIO.OUT) # setup pin 4
mcp.setup(8, MCP230XX.GPIO.OUT) # setup pin 8

for x in range(100):
        
        mcp.output(4, 1)    # Set pin to HIGH (ON) (1)
        mcp.output(8, 1)    # Set pin to HIGH (ON) (1)
        sleep(.5)
        mcp.output(4, 0)    # Set pin to LOW (OFF) (0)
        mcp.output(8, 0)    # Set pin to LOW (OFF) (0)
        sleep(.5)
