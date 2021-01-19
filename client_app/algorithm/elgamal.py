from random import randint


class ElGamal():
    def __init__(self, P, G):
        self.P, self.G = P, G
        self.private_key = self.Generate_Private_Key()
        self.public_key = self.Generate_Public_Key()

    def Generate_Private_Key(self):
        # private_key = 3
        private_key = randint(
                        10000,
                        99999
        )

        while private_key >= self.P:
            private_key = randint(
                            10000,
                            99999
            )
        # private_key = 23920456797266019016593959482821930395790669073584
        return private_key

    def Generate_Public_Key(self):
        return int(pow(self.G, self.private_key, self.P))

    # def Generate_Private_Key(self, client_public_key):
    #     self.private_key = int(pow(client_public_key,
    #                                self.private_key, self.P))

    def Encrypt_Message(self, message, recv_public_key):
        encrypted_message = int(message) * pow(recv_public_key, self.private_key)
        encrypted_message = int(pow(encrypted_message, 1, self.P))
        return self.public_key, encrypted_message

        # decimal_message = [ord(char) for char in message]
        # encrypted_message = [str(ascii_code * self.private_key)
        #                      for ascii_code in decimal_message]
        #
        # encrypted_message = "_".join(encrypted_message)
        # return encrypted_message

    def Decrypt_Message(self, recv_public_key, encrypted_message):
        decrypted_message = pow(recv_public_key, self.P - self.private_key - 1)\
                                * encrypted_message
        decrypted_message = int(pow(decrypted_message, 1, self.P))
        return decrypted_message

        # encrypted_message = encrypted_message.split("_")
        # decrypted_message = [int(ecrypted_char) // self.private_key
        #                      for ecrypted_char in encrypted_message]
        # decrypted_message = [chr(ascii_code)
        #                      for ascii_code in decrypted_message]
        # decrypted_message = "".join(decrypted_message)
        # return decrypted_message
