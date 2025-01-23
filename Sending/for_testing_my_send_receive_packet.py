from md_fw_declare import *
from md_fw_menu import *

# INVALID UDP PORT
PKT_Default_Receive = Ether(src="58:11:22:81:3A:40", dst="D8:3A:DD:A4:BF:0F") / dot1q / IPv6(
    src=VALID_SRC_IPv6,
    dst=VALID_DST_IPv6
) / UDP(sport=VALID_SPORT, dport=12345) / payload_default

# PKT_Default_Receive = Ether(src="58:11:22:81:3A:40", dst="D8:3A:DD:A4:BF:0F") / dot1q / IPv6(
#     src=VALID_SRC_IPv6,
#     dst=VALID_DST_IPv6
# ) / ICMPv6EchoRequest() / payload_default

def print_infor():
    try:
        global PKT_Default_Receive
        print("\n----------Packet Information-------------")
        PKT_Default_Receive.show()
    except Exception as ex:
        print(f"Error: {ex}")

# 16.1.15.2 Undefined UDP port message handling
def send_packet():
    global PKT_Default_Receive
    try:
        print("\n----------Sending Packet-------------")
        PKT_Default_Receive.show()
        sendp(PKT_Default_Receive, iface=IFACE) # type: ignore
    except Exception as ex:
        print(f"Error: {ex}\nPlease check if Ethernet is connected.")

def main():
    cloop = True
    while cloop:
        try:
            choice = print_menu()
            if int(choice) == 1:
                print_infor()
            elif int(choice) == 2:
                send_packet()
            elif int(choice) == 0:
                cloop = False
        except KeyboardInterrupt:
            print('\nThanks! See you later!\n\n')
            cloop = False
        except Exception as ex:
            print(f"Unexpected error: {ex}")

if __name__ == '__main__':
    main()
