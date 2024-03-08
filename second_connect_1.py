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

#    while True:
#        try:
#            # Get the ID of the active window
#            result = subprocess.check_output(['xdotool', 'getactivewindow'])
#            window_id = result.decode('utf-8').strip()
            
            # Check if the window still exists
#            subprocess.check_output(['xdotool', 'getwindowname', window_id])
            
#            return window_id
#        except subprocess.CalledProcessError:
#            print("Error: Xdotool error or invalid window. Retrying...")
#            time.sleep(1)  # Wait for a moment before retrying

    # Wait for an xterm window to appear
#    subprocess.run(['xdotool', 'search', '--class', 'xterm'])
    
    # Get the window ID of the last opened xterm window
#    result = subprocess.check_output(['xdotool', 'search', '--onlyvisible', '--class', 'xterm'])
#    return result.decode('utf-8').strip()

# Set the home directory
home_directory = "/home/demo/Desktop/workspace/"

# Define the command for netopeer2-cli
netopeer2_cli_command = "sudo netopeer2-cli"

os.chdir(home_directory)
netopeer2_folder = os.path.join(home_directory, "netopeer2")

# Open an xterm window and execute netopeer2-cli
#subprocess.run(['xterm', '-e', 'bash', '-c', 'cd {}; {}; exec bash'.format(netopeer2_folder, netopeer2_cli_command)])
# Open an xterm window and execute netopeer2-cli
logging.info("Opening the xterm terminal")
#xterm_commaqnd = f"Display:0 xterm -e sudo netopeer2-cli"
# Command to open xterm and run netopeer2-cli
#xterm_command = f"su - demo -c 'DISPLAY=:0 xterm -e netopeer2-cli'"
#xterm_command = f"xterm -e 'su - demo -c \"DISPLAY=:0 netopeer2-cli\"'"
#xterm_command = f"su - demo -c 'DISPLAY=:0 xterm -e /bin/bash -i -c \"sleep 2 && netopeer2-cli\"'"
xterm_command = f"xterm -e sudo netopeer2-cli"
process = subprocess.Popen(xterm_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# Wait for the process to complete
#stdout, stderr = process.communicate()

# Log the output
#logging.info(f"stdout: {stdout}")

# Log any errors
#if process.returncode != 0:
#   logging.error(f"stderr: {stderr}")
#   logging.error(f"Command exited with non-zero return code: {process.returncode}")
#else:
#   logging.info("Command executed successfully")

#cli_window_id = get_window_id()

# Add a delay to allow netopeer2-cli to start before sending commands
#import time
time.sleep(2)

# Send additional command to netopeer2-cli
#additional_command = "help"
subprocess.run(['xdotool', 'type', 'help'])
subprocess.run(['xdotool', 'key', 'Return'])
time.sleep(1)

additional_command_1 = "connect-first --tls --host 10.10.10.11 --cert /home/demo/Desktop/workspace/demo_files/certs/cli.crt --key /home/demo/Desktop/workspace/demo_files/certs/cli_key.key --trusted /home/demo/Desktop/workspace/demo_files/certs/ca_IDevID.pem"
subprocess.run(['xdotool', 'type', additional_command_1])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(1)

additional_command_2 = "status"
subprocess.run(['xdotool', 'type', additional_command_2])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(1)

edit_config_commands = [
    "edit-config --target candidate --config=/home/demo/Desktop/workspace/demo_files/second_connect/keystore.xml", "commit",
    "edit-config --target candidate --config=/home/demo/Desktop/workspace/demo_files/second_connect/truststore.xml", "commit",
    "edit-config --target candidate --config=/home/demo/Desktop/workspace/demo_files/second_connect/tls_listen.xml", "commit",
]

# Loop through each command and send it using xdotool
for command in edit_config_commands:
    subprocess.run(['xdotool', 'type', command])
    subprocess.run(['xdotool', 'key', 'Return'])
    time.sleep(2) 

for _ in range(1):  # Close two terminals
    window_id = get_window_id("xterm")  # Get the window ID using xdotool
    subprocess.run(['xdotool', 'windowclose', window_id])  # Close the terminal using xdotool
    time.sleep(5)  # Brief delay to ensure full closure

# Close client window
#subprocess.run(['xdotool', 'windowactivate', cli_window_id])
#subprocess.run(['xdotool', 'key', 'ctrl+C'])  # Ctrl+C to close the xterm window

# Restart client
#subprocess.run(['xterm', '-e', 'bash', '-c', 'cd {}; {}; exec bash'.format(netopeer2_folder, netopeer2_cli_command)])
xterm_command = f"xterm -e sudo netopeer2-cli"
process = subprocess.Popen(xterm_command, shell=True)
time.sleep(3)

second_connect = "connect --tls --host 10.10.10.11 --cert /home/demo/Desktop/workspace/demo_files/second_connect/operator_client.crt --key /home/demo/Desktop/workspace/demo_files/second_connect/operator_client.key --trusted /home/demo/Desktop/workspace/demo_files/certs/ca_LDevID.pem"
subprocess.run(['xdotool', 'type', second_connect])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(5)

additional_command_3 = "status"
subprocess.run(['xdotool', 'type', additional_command_3])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(5)

#for _ in range(1):  # Close two terminals
#    window_id = get_window_id("xterm")  # Get the window ID using xdotool
#    subprocess.run(['xdotool', 'windowclose', window_id])  # Close the terminal using xdotool
#    time.sleep(1)  # Brief delay to ensure full closure
