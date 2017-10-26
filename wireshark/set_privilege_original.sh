su
aptitude install libcap2-bin
groupadd wireshark
usermod -a -G wireshark your_username
newgrp wireshark
chgrp wireshark /usr/bin/dumpcap
chmod 750 /usr/bin/dumpcap
setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
