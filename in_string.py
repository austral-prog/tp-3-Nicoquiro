def check_vowels():
    name = input("Ingresa un nombre: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    name_lower = name.lower()
    
    for vowel in vowels:
        print(f"Contiene {vowel}: {vowel in name_lower}")
    
