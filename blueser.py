import serial

def main():
    sp = serial.Serial()
    sp.port = 'COM4'
    sp.baudrate = 9600
    sp.timeout = 5

    sp.open()
    sp.readline() #to give the hardware handshake time to happen
    sp.write(chr(1))
    value = sp.readline()
    print value
    sp.write(chr(0))
    sp.close()

if __name__ == "__main__":

    main()