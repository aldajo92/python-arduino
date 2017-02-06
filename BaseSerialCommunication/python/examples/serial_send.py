"""
Run this whit the following arguments in command line:
    -path to port / port name
    -baud rate (115200)
    -data to send
"""

import time
import serial
import sys

value1 = None
value2 = None
value3 = None
serial_port = None

leds = 15
step = 10
delay = 0

if __name__ == "__main__":

    try:
        value1 = sys.argv[1]
        value2 = int(sys.argv[2])
        value3 = sys.argv[3]
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


    def send_data(data):
        serial_port.write(data)
        print data


    def send_data_ln(data):
        send_data(str(data) + '\n')


    try:
        time.sleep(2)
        send_data_ln(value3)
        print "data sent: " + value3
    except KeyboardInterrupt:
        time.sleep(0.1)
        print "Closed program"
