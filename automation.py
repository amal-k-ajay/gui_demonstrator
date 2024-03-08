















import subprocess
import paho.mqtt.client as mqtt
import logging

# Set up logging
logging.basicConfig(filename='/home/demo/Desktop/workspace/second_first1.log', level=logging.DEBUG)
logging.info('Automation.py Script Started')

# Set your MQTT broker details
broker_address = "localhost"
broker_port = 1883
topic_for_mqttIn = "script/second_connect"
topic_for_mqttIn_1 = "script/operator_connect"
#topic_for_mqttOut = "script/output"
topic_for_mqttOut_1 = "output_messages_1/second_connect"
topic_for_mqttOut_2 = "output_messages_2/second_connect"
topic_for_mqttOut_3 = "output_messages_3/second_connect"

def publish_message(topic, message):
    client = mqtt.Client()
    client.connect(broker_address, broker_port, 60)
    client.publish(topic, message)
    client.disconnect()

def run_openssl_scripts(script_paths):
    for script_path in script_paths:
        process = subprocess.Popen(f'bash {script_path}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate()
        logging.info("Output messages from Open SSL script: %s", error)
#        print ("Output of sh file: ", error)
        publish_message(topic_for_mqttOut_1, error)

def run_python_scripts(python_scripts):
    for script_path in python_scripts:
        process = subprocess.Popen(f'sudo python3 {script_path}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate()
        publish_message(topic_for_mqttOut_2, output)
        logging.info("Output messages from Python script: %s", output)
        logging.error("Error message from Python script: %s", error)
        #print ("Output of the python script: ", output)
        #print ("Error in the python script: ", error)
        #message = output.decode()
        #print ("Messages of the python script: ", message)

def on_message(client, userdata, msg):
    if msg.payload.decode() == "Second Connect Button is pressed":
#if __name__ == '__main__':
       script_paths = [
        '/home/demo/Desktop/workspace/demo_files/second_connect/LDevID_server_operator.sh',
        '/home/demo/Desktop/workspace/demo_files/second_connect/LDevID_client_operator.sh'
       ]
       #subprocess.Popen('openssl x509 -in "/home/demo/Desktop/workspace/demo_files/certs/ca_LDevID.crt" -out "/home/demo/Desktop/workspace/demo_files/certs/ca_LDevID.pem" -outform PEM') 
       run_openssl_scripts(script_paths)
       python_scripts = ['/home/demo/Desktop/workspace/demo_files/second_connect/gen_keystore_file.py', '/home/demo/Desktop/workspace/demo_files/second_connect/gen_truststore_file.py', '/home/demo/Desktop/workspace/demo_files/second_connect/gen_tls_listen_file.py', '/home/demo/Desktop/workspace/second_connect/second_connect_1.py']
       run_python_scripts(python_scripts)
    elif msg.payload.decode() == "Operator Connect Button is pressed":
       print ("Operator Button is pressed")
       python_scripts = ['/home/demo/Desktop/workspace/second_connect/operator_connect.py']
       run_python_scripts(python_scripts)

client = mqtt.Client()
client.on_message = on_message

client.connect(broker_address, broker_port, 60)
client.subscribe(topic_for_mqttIn)
client.subscribe(topic_for_mqttIn_1)

client.loop_forever()
