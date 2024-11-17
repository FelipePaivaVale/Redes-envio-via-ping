import gnupg

gpg = gnupg.GPG() 

def decrypt_file(input_file, passphrase):
    with open(input_file, 'rb') as f:
        decrypted_data = gpg.decrypt_file(f, passphrase=passphrase)

    if decrypted_data.ok:
        print("descriptografado")
        return decrypted_data.data.decode('utf-8') 
    else:
        print("falha:", decrypted_data.status)
        return None

resultado = decrypt_file("arquivo_capturado.gpg", "senha123")

if resultado:
    with open("arquivo_descriptografado.txt", "w") as output_file:
        output_file.write(resultado)


