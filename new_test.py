import serial
import json
import serial.tools.list_ports

# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.dumps(x)
# fnew = open("output.txt", "wt")
# fnew.write(y)
# fnew.close()

print("list all available ports and read data:")
for port in serial.tools.list_ports.comports():
    print("hwid:", port.hwid)
    print("device:", port.device)
    print("name:", port.name)
    print("description:", port.description)
    print("pid:", port.pid)
    print("vid:", port.vid)
    print("serial_number:", port.serial_number)
    print("location:", port.location)
    print("manufacturer:", port.manufacturer)
    print("product:", port.product)
    print("interface:", port.interface)
    
    print("Start of working with port COM")
    try:
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = port.name # for example COM1
        ser.timeout = 3
        print(ser) # Serial<id=0xa81c10, open=False>(port='COM1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=3, xonxoff=0, rtscts=0)
        try:
            ser.open()
            print(ser.is_open) # True
            try:
                # x = ser.read()
                # print("x" + x)
                while True:
                    rawdata = (ser.readline().decode('ascii'))
                    print(rawdata)
                    prefix = "Output_{}.txt"
                    postfix = port.name
                    filename = prefix.format(postfix) # Example : Output_COM1.txt 
                    f = open(filename, "at") # Append text file.
                    f.write(rawdata)
                    f.close()
            except:
                print("Port ", ser.port ," can not be read")    
            ser.close()
            print(ser.is_open) # False
        except:
            print("Port ", ser.port ," can not be opened")
    except:
        print("there is a problem with ", ser.port ," port")
    print("End of working with port " , ser.port , "\n")