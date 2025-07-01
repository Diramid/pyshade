def decryption(encrypted_data: str, char_map: dict[str, int]) -> str | None :

    decrypted_data: str = ""

    try:
        number_splited: list[str] = encrypted_data.split("/")
        for num in number_splited:
            for key, value in char_map.items():
                if num == str(value):
                    decrypted_data += key 
                    break
                

    except Exception as err:
        raise Exception(f"pyshade: there is a problem: {err}")
    
    return decrypted_data