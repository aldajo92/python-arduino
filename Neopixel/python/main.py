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


    def send_value(led, r, g, b):
        string_led = 'led-' + str(led) + '-' + str(r) + '-' + str(g) + '-' + str(b) + '\n'
        serial_port.write(string_led)
        time.sleep(0.02)


    def run():
        time.sleep(2)

        for i in range(0, 255, step):
            for j in range(0, leds):
                send_value(j, i, 254 - i, 254 - i)
            time.sleep(delay)

        for i in range(0, 255, step):
            for j in range(0, leds):
                send_value(j, 254 - i, 0, i)
            time.sleep(delay)

        for i in range(0, 255, step):
            for j in range(0, leds):
                send_value(j, 0, 255, 254 - i)
            time.sleep(delay)

        for i in range(0, 255, step):
            for j in range(0, leds):
                send_value(j, 255, 254 - i, i)
            time.sleep(delay)

        for i in range(0, leds):
            send_value(leds - 1 - i, 0, 0, 0)
            time.sleep(0.1)


    try:
        run()
    except KeyboardInterrupt:
        time.sleep(0.1)
        for i in range(0, leds):
            send_value(leds - 1 - i, 0, 0, 0)
        print "Closed program"
