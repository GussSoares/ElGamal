from random import randint


class ElGamal():
    def __init__(self, P, G):
        self.P, self.G = P, G
        self.private_num = self.Generate_Private_Number()
        self.public_key = self.Generate_Public_Key()

    def Generate_Private_Number(self):
        private_num = randint(
                            10000000000000000000000000000000000000000000000000,
                            99999999999999999999999999999999999999999999999999
        )
        # private_key = 23920456797266019016593959482821930395790669073584
        return private_num

    def Generate_Public_Key(self):
        return int(pow(self.G, self.private_num, self.P))

    def Generate_Private_Key(self, client_public_key):
        self.private_key = int(pow(client_public_key,
                                   self.private_num, self.P))

    def Encrypt_Message(self, message):
        decimal_message = [ord(char) for char in message]
        encrypted_message = [str(ascii_code * self.private_key)
                             for ascii_code in decimal_message]

        encrypted_message = "_".join(encrypted_message)
        return encrypted_message

    def Decrypt_Message(self, encrypted_message):
        encrypted_message = encrypted_message.split("_")
        decrypted_message = [int(ecrypted_char) // self.private_key
                             for ecrypted_char in encrypted_message]
        decrypted_message = [chr(ascii_code)
                             for ascii_code in decrypted_message]
        decrypted_message = "".join(decrypted_message)
        return decrypted_message


# def Generate_Parameters_PG():
#     P = 66952748238564900903939127649986228632532313405399
#     G = 50198608759272757702393646073477911607815113132586
#     return P, G
#
#
# if __name__ == '__main__':
#
#     P, G = Generate_Parameters_PG()
#
#     client_1 = ElGamal(P, G)
#     client_2 = ElGamal(P, G)
#
#     message = "Codigo do GuS"
#
#     client_1.Generate_Private_Key(client_2.public_key)
#     client_2.Generate_Private_Key(client_1.public_key)
#
#     encrypted_message = client_1.Encrypt_Message(message)
#     decrypted_message = client_2.Decrypt_Message(encrypted_message)
#     print(decrypted_message)
