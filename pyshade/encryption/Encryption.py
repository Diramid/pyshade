import random

def generate_unique_value(char_map: dict[str,int]) -> int:
    
    existing = set(char_map.values())
    while True:
        num = random.randint(1, 1000)
        if num not in existing:
            return num

def encrypt_data(data: str, char_map: dict[str, int]) -> str | None:

    encrypted_array: list[str] = []

    for char in char_map:
        unique_num: int = generate_unique_value(char_map)
        char_map[char] = unique_num

    for letter in data:
        try:
            if letter not in char_map:
                raise Exception(f"character {letter} is not supported")
            encrypted_num: int = char_map[letter]

            encrypted_array.append(str(encrypted_num))

        except Exception as err:
            raise Exception(f"pyshade: there is a problem: {err}")
        
    return "/".join(encrypted_array)