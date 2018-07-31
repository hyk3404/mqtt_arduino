import serial
import paho.mqtt.client as mqtt
ser = serial.Serial("COM4") 
print ser.name
ser.write("hello")
i = ser.read()
value = ser.readline()


client_id = ""
client = mqtt.Client(client_id=client_id)
client.connect("127.0.0.1")
#topic = "plusone"
#payload = "hello mqtt"
client.publish("plusone", value)
client.publish("asd", "123")
print value
print i
ser.close()            


# If broker asks client ID.
