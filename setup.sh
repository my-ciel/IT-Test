#!/bin/bash

# Python Install 
echo "Updating package list and installing Python3..."
sudo apt update -y
sudo apt install python3 python3-pip -y

# Moving Lab files 
echo "Moving unit_test and integration_test folders to /home/ubuntu..."
mv IT-Test/unit_test /home/ubuntu/
mv IT-Test/integration_test /home/ubuntu/
mv IT-Test/test /home/ubuntu/
mv IT-Test/00-installer-config.yaml /home/ubuntu/.

echo "Setup complete!"
echo "Checking Python version..."
python3 --version


