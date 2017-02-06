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


    def send_value(value):
        string_led = 'led-' + str(value) + '\n'
        print string_led
        serial_port.write(string_led)
        time.sleep(0.02)

    def num_array(val):
        returned = ""
        for i in range(0, 100):
            returned += val
        return returned


    def run():
        time_delay = 0.02
        time.sleep(2)
        # send_value("12341234")
        # time.sleep(time_delay)
        # send_value("00000000")
        # time.sleep(time_delay)
        # send_value("12341234")
        # time.sleep(time_delay)
        # send_value("00000000")
        # time.sleep(time_delay)
        # send_value("12341234")
        # time.sleep(time_delay)
        # send_value("00000000")
        # time.sleep(time_delay)
        # send_value("12341234")
        # time.sleep(time_delay)
        # send_value("00000000")
        # time.sleep(time_delay)
        # send_value("12341234")
        # time.sleep(time_delay)
        # send_value("00000000")
        # time.sleep(time_delay)

        while True:
            send_value(num_array("0"))
            time.sleep(time_delay)
            send_value(num_array("1"))
            time.sleep(time_delay)


    try:
        run()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print "Closed program"
