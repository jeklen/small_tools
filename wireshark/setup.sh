#! /bin/bash

# when facing "There are no interfaces on which a capture can be done"
# or facing "you don't have permission to capture on that device"

sudo dpkg-reconfigure wireshark-common
sudo chmod +x /usr/bin/dumpcap
