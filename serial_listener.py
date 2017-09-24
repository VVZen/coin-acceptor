import serial
import sys
import glob

def list_serial_ports():
    '''
    List serial port names
    '''

    # check current OS
    if sys.platform.startswith("win"):
        ports = ["COM{}".format(i + 1) for i in range(256)]
    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        ports = glob.glob("/dev/tty[A-Za-z]*")
    elif sys.platform.startswith("darwin"):
        ports = glob.glob("/dev/tty.*")
    else:
        raise EnvironmentError("Unsopported platform")
    
    # add available ports
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    print "Serial ports available:\n\t{}".format("\n\t".join(result))

# read messages from serial
def read_from_serial(serialName, baudRate):
    coin_acceptor = serial.Serial(serialName, baudRate)
    sys.stdout.write("-"*60)
    sys.stdout.write("\n")
    sys.stdout.write("Started reading on serial\n")
    sys.stdout.write("-"*60)
    sys.stdout.write("\n")
    while True:
        sys.stdout.write(coin_acceptor.readline())
        sys.stdout.flush()

# entry point
def main():
    list_serial_ports()
    read_from_serial("/dev/tty.usbmodemFA131", 9600)

if __name__ == "__main__":
    main()