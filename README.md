# MCP23017

Simple script for getting this expansion board up and running

https://www.amazon.com/CQRobot-Ocean-Compatible-Motherboard-Simultaneously/dp/B08DFNR2JW/ref=cm_cr_arp_d_product_top?ie=UTF8

1. Copy the above files to a directory
2. Update the address in the python file. For this board 0x27 is the default.
3. Connect the expansion board to your raspberry pi. Just need 3.3v or 5v and GND and then the SDA & SLC pins
4. Connect an LED to PA4 and PB0
5. Now run the script "python3 test.py"
6. They will both flash 
