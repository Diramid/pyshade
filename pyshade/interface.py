from pyshade.encryption import Encryption
from pyshade.decryption import Decryption
from pyshade.map import CharMap
import json

class Pyshade: 

    @staticmethod
    def encrypt(data: str):
    
        try:
            encrypted_data: str | None = Encryption.encrypt_data(data, CharMap.char_map)

            return {
                "data": encrypted_data,
                "key": CharMap.char_map
            }           
        
        except Exception as err:
            print(err)
            return
        
    @staticmethod
    def encrypt_jsonkey(data: str):

        try:
            encrypted_data: str | None = Encryption.encrypt_data(data, CharMap.char_map)

            return {
                "data": encrypted_data,
                "key":json.dumps(CharMap.char_map)
            }            
        
        except Exception as err:
            print(err)
            return
        
    @staticmethod
    def decrypt(data: str, secret_key: dict[str, int]) -> str | None:

        try:

            decrypted_data: str | None = Decryption.decryption(data, secret_key)

            return decrypted_data
        
        except Exception as err:
            print(err)
            return
        
    @staticmethod
    def decrypt_jsonkey(data: str, secret_key: str) -> str | None:

        try:

            decrypted_data: str | None = Decryption.decryption(data, json.loads(secret_key))

            return decrypted_data
        
        except Exception as err:
            print(err)
            return