#Caesar Cipher Program
#using one function 
#Finsihed Code
def caesar(start_text , shift_amount , cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *=1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter) 
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x',
            'y', 'z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_coninue = True

while should_coninue:
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt :\n ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number :\n "))
    shift = shift % 26

    caesar(start_text=text , shift_amount=shift , cipher_direction=direction)

end = input("Type 'yes' if you want to go again otherwise type 'no'. \n ")
if end =='no':
    should_coninue = False
    print("Goodbye")