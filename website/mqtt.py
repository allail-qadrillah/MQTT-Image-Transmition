import paho.mqtt.client as mqtt
import threading
import datetime
import base64

class MqttClient():
  def __init__(self):
      self.connected = False
  
  def connectTo(self, broker: str, topic: str, port=1883, timeout=60):
      # Create an MQTT client object
      client = mqtt.Client()

      # Set the callback functions
      client.on_connect = self.on_connect
      client.on_message = self.on_message

      try:
      # Connect to the broker
        client.connect(broker, port, timeout)
        self.connected = True
      except:
        print("Error connecting to Broker")
        self.connected = False
        pass

      # Subscribe to a topic
      client.subscribe(topic)
      # Start the MQTT client loop in a new thread
      t = threading.Thread(target=client.loop_forever)
      t.start()
      # client.loop_forever()

# Define callback functions
  def on_connect(self, client, userdata, flags, rc):
      print(f"Connected with result code "+str(rc))
      print(f"Client   : {client}")
      print(f"User Data: {userdata}")
      print(f"Flags    : {flags}")

  def on_message(self, client, userdata, msg):
      print("From Topik "+msg.topic+": "+str(msg.payload))
      # ubah base64 dari topik menjadi gambar
      self.Base64ToImg(encoded_string=msg.payload,
                        img_path=f"website/static/img/history/{self.get_filename()}")

  def Base64ToImg(self, encoded_string: str, img_path="image.jpg"):
    # Decode gambar dari format base64
    decoded_image = base64.b64decode(encoded_string)
    with open(img_path, "wb") as image_file:
        image_file.write(decoded_image)
  
  def get_filename(self):
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"


# client = MqttClient()
# print(client.connected)
# client.connectTo(broker="broker.emqx.io", topic="python/mqtt")
# print(client.connected)

