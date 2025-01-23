from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.inet6 import *
from random import randint
from netaddr import *
import binascii
import sys
import signal
from threading import Thread
from sqlalchemy import false

# Interface
IFACE = "Ethernet"  # Fill the ID of destination network card

# Number of threads used
PKT_COUNT = 5

# Scan Ports
FROM_PORT = 1
TO_PORT = 65536

# MAC Address
SRC_MAC = "58-11-22-81-3A-40"  # Fill your MAC Address here
DST_MAC = "D8:3A:DD:A4:BF:0F"  # Fill the destination MAC
INVALID_SRC_MAC = "fa:fb:fc:fd:fe:ff"  # Invalid MAC

# VLAN ID
VLAN_ID = 25

# IPv6s
INVALID_DST_IPv6 = "fd53:abcd:1234:3::xx"  # Invalid IPv6
INVALID_SRC_IPv6 = "fd53:abcd:1234:3::xx"  # Invalid IPv6
VALID_SRC_IPv6 = "fd53:abcd:1234:5::10"
VALID_DST_IPv6 = "fd53:abcd:1234:5::14"
VALID_DST_Multicast = "ff02::1"
INVALID_DST_Multicast = "ff02::2"

# Ports
VALID_SPORT = 13400
VALID_DPORT = 13400
INVALID_DPORT = 13456
INVALID_SPORT = 13456
RANGE = (1000, 65535)
pro_type = TCP

# Layers
dot1q = Dot1Q(vlan=VLAN_ID) # type: ignore

# Payload
payload_default = "fd53:abcd:1234:5::12"

# Packets
PKT_Default_Receive = (
    Ether() /
    dot1q /
    IPv6(
        src=VALID_SRC_IPv6,
        dst=VALID_DST_IPv6
    ) /
    pro_type(
        sport=VALID_SPORT,
        dport=VALID_DPORT
    ) /
    ICMPv6EchoRequest()/
    
    payload_default
)

PKT_Default_Send = (
    Ether(
        dst=SRC_MAC,
        src=DST_MAC
    ) /
    dot1q /
    IPv6(
        src=VALID_DST_IPv6,
        dst=VALID_SRC_IPv6
    ) /
    pro_type(
        sport=VALID_DPORT,
        dport=VALID_SPORT
    ) /
    payload_default
)
