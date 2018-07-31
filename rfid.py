import serial
#import paho.mqtt.client as mqtt
ser = serial.Serial("COM4",115200,timeout= 0.5) 
print (ser.name)
#ser.write("hello")
# client_id = ""
# client = mqtt.Client(client_id=client_id)
# client.connect("127.0.0.1")
#for i in range(999):

while True:
    value = ser.readline()

    # print(value)
    # value = value.split('\n')
    # print(value)
    value = value.replace(' ','')
    value = value.replace('\n','')
    # value = value.splitlines()
    if (len(value)==9):
        print(len(value))
        print(value)
        print('------')
        #client.publish("plusone", value)
    #client.publish("asd", "123")
# print value 
