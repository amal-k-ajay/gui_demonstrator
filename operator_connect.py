import subprocess
import os
import time
import logging

# Set up logging
#logging.basicConfig(filename='/home/demo/Desktop/workspace/second_connect3.log', level=logging.DEBUG)
#logging.info('second_connect1.py Script Started')

# Set the DISPLAY environment variable
os.environ['DISPLAY'] = ':0'

os.environ['XAUTHORITY'] = '/home/demo/.Xauthority'

#os.environ['HOME'] = '/home/demo'

def get_window_id(command):
    result = subprocess.check_output(['xdotool', 'search', '--onlyvisible', '--class', 'xterm'])
    return result.decode('utf-8').strip()

xterm_command = f"xterm -e sudo netopeer2-cli"
process = subprocess.Popen(xterm_command, shell=True)
time.sleep(3)

second_connect = "connect --tls --host 10.10.10.11 --cert /home/demo/Desktop/workspace/demo_files/second_connect/operator_client.crt --key /home/demo/Desktop/workspace/demo_files/second_connect/operator_client.key --trusted /home/demo/Desktop/workspace/demo_files/certs/ca_LDevID.pem"
subprocess.run(['xdotool', 'type', second_connect])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(3)

additional_command_3 = "status"
subprocess.run(['xdotool', 'type', additional_command_3])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(5)
