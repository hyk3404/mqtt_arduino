
import paho.mqtt.client as mqtt
# If broker asks client ID.
client_id = ""
client = mqtt.Client(client_id=client_id)
client.connect("127.0.0.1")
topic = "plusone"
payload = "hello mqtt"

client.publish(topic, payload)
client.publish('123', 'asdasdasd')
#for i in xrange(10):
    #client.publish(topic, "%s - %d" % (payload, i))
    #time.sleep(0.01)