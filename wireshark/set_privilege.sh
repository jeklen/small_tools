#! /bin/bash
su
aptitude install libcap2-bin
addgroup --system wireshark
usermod -a -G wireshark zhang
newgrp wireshark
chgrp wireshark /usr/bin/dumpcap
chmod 750 /usr/bin/dumpcap
setcap cap_net_raw, cap_net_admin=eip /usr/bin/dumpcap
