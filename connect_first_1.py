import subprocess
import time
import os
import logging
import paho.mqtt.client as mqtt

# Set your MQTT broker details
broker_address = "localhost"
broker_port = 1883
topic_for_mqttOut_1 = "output_messages_3/first_connect"

def publish_message(topic, message):
    client = mqtt.Client()
    client.connect(broker_address, broker_port, 60)
    client.publish(topic, message)
    client.disconnect()


# Set up logging
logging.basicConfig(filename='/home/demo/Desktop/workspace/connect_first.log', level=logging.DEBUG)
logging.info('connect_first.py Script Started')
#import paho.mqtt.client as mqtt

# Set your MQTT broker details
#broker_address = "localhost"
#broker_port = 1883
#topic_for_mqttIn = "script/disconnect"

# Set the DISPLAY environment variable
os.environ['DISPLAY'] = ':0'

# Set the home directory
home_directory = "/home/demo/Desktop/workspace/"

# Move out of sysrepo folder and enter netopeer2 folder
os.chdir(home_directory)
netopeer2_folder = os.path.join(home_directory, "netopeer2")

# Open an xterm window and execute netopeer2-cli
xterm_command = f"DISPLAY=:0 xterm -e sudo netopeer2-cli"
process = subprocess.Popen(xterm_command, shell=True)

# Wait for the process to finish (you may need to adjust the sleep duration)
time.sleep(2)  # Adjust as needed

# Send the 'help' command
subprocess.run(['xdotool', 'type', 'help'])
subprocess.run(['xdotool', 'key', 'Return'])
time.sleep(1)
subprocess.run(['xdotool', 'type', 'connect-first --tls --host 10.10.10.11 --cert /home/demo/Desktop/workspace/demo_files/certs/cli.crt --key /home/demo/Desktop/workspace/demo_files/certs/cli_key.key --trusted /home/demo/Desktop/workspace/demo_files/certs/ca_IDevID.pem'])
subprocess.run(['xdotool','key','Return'])
time.sleep(3)
# You can send more commands here if needed
# For example:
subprocess.run(['xdotool', 'type', 'status'])
subprocess.run(['xdotool', 'key', 'Return'])

publish_message(topic_for_mqttOut_1, "Initial Connection is established")
# Wait for the process to finish (you may need to adjust the sleep duration)
time.sleep(2)  # Adjust as needed

#def on_message(client, userdata, msg):
#    if msg.payload.decode() == "Disconnect Button is pressed":
#       logging.info("Disconnect Button is pressed")
#       print ("Disconnect button is pressed")
       #commands = [
       #           "disconnect",
       #           "exit"
       # ]
       #print("Before disconnect commands")
       #for command in commands:
            #print(f"Sending command: {command}")
#       subprocess.run(['xdotool', 'type', 'disconnect'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#       subprocess.run(['xdotool', 'key', 'Return'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#            #print ("Error is:", stderr)
#       time.sleep(1)
#       print("After disconnect commands")

       # Loop through each command and send it using xdotool
       #for command in commands:
       #    subprocess.run(['xdotool', 'type', command])
       #    subprocess.run(['xdotool', 'key', 'Return'])
       #    time.sleep(1) 

#       close_terminal_command = "Ctrl+Shift+Q"
#       subprocess.run(['xdotool', 'key', close_terminal_command])

# Close the xterm window
subprocess.run(['xdotool', 'key', 'Ctrl+Shift+Q'])



#client = mqtt.Client()
#client.on_message = on_message

#client.connect(broker_address, broker_port, 60)
#client.subscribe(topic_for_mqttIn)

#client.loop_forever()
