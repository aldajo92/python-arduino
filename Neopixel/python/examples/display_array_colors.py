"""
Run this whit the following arguments in command line:
    -path to port / port name
    -baud rate (115200)
"""

import time
import serial
import sys

value1 = None
value2 = None
serial_port = None

leds = 15
step = 10
delay = 0

if __name__ == "__main__":

    try:
        value1 = sys.argv[1]
        value2 = int(sys.argv[2])
        serial_port = serial.Serial(value1, value2)
    except IndexError:
        print 'Error on input values'
        exit(0)
    except ValueError:
        print "please insert a valid Baud Rate"
        exit(0)
    except serial.SerialException:
        print "Resource busy or not exist"
        exit(0)


    def send_value(value, offset):
        string_led = 'led-' + str(offset) + '-' + str(value) + '\n'
        serial_port.write(string_led)


    def send_update():
        string_led = 'update-0-0\n'
        serial_port.write(string_led)


    def send_off():
        string_led = 'off-0-0\n'
        serial_port.write(string_led)


    def num_array(val):
        returned = ""
        for i in range(0, 20):
            returned += val
        return returned


    def run():
        time_delay = 0.2
        time.sleep(2)
        while True:
            send_value(num_array("2"), 0)
            send_value(num_array("2"), 20)
            send_value(num_array("2"), 40)
            send_value(num_array("2"), 60)
            send_value(num_array("2"), 80)
            send_value(num_array("2"), 100)
            send_value(num_array("2"), 120)
            send_update()
            time.sleep(time_delay)
            send_off()
            time.sleep(time_delay)

    try:
        run()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print "Closed program"
