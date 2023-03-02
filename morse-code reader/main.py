MORSE_DATA= { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


# decrypt function takes plain and readable text and conver to
def encrypt():
    """ encrypt taks in plain text and converts it into morse code"""
    text=input('enter text to convert to morse: ').upper()
    letters=[word for word in text]
    morse=''
    for letter in letters:
        if letter in MORSE_DATA:
            morse+= f'{MORSE_DATA[letter]}|'
        else:
            morse+=f'{letter}|'
    return print(morse)
    

#  decryting the morse code into plain text
def decrypt():
    morse_code=input('enter morse code: ').split('|')[:-1]
    text=''
    for code in morse_code:
        if code in MORSE_DATA.values():
            text += list(MORSE_DATA.keys())[list(MORSE_DATA.values()).index(code)]
        else:
            text += code
    return print(text.title())
print('========================================================MORSE CODE ENCRYPTO AND DECRYPTOR==========================================================')
   

comunication = True
while comunication:
    choice=input('encrypt/decrypt: ').lower()
    if choice=='encrypt':
        encrypt()
        choice2=input('\ndo you which to encrypt more? Y/N: ').lower()
        if choice2=='y':
            encrypt()
        else:
            comunication = False
    elif choice=='decrypt':
        decrypt()
        choice2=input('\ndo you which to decrypt more? Y/N: ').lower()
        if choice2=='y':
            decrypt()
        else:
            comunication = False
    else: 
        print('invalide option')
print('\n\n\nlicenced by NKDTECH')
