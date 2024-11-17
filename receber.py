from scapy.all import *
import gnupg

gpg = gnupg.GPG()

def process_icmp_packet(packet):
    if packet.haslayer(ICMP) and packet.haslayer(Raw):
        payload = packet[Raw].load
        print("Received a chunk of data")

        with open('arquivo_capturado.gpg', "wb") as temp_file:
            temp_file.write(payload)
   
print("Listening for ICMP packets...")
sniff(filter="icmp", prn=process_icmp_packet)
