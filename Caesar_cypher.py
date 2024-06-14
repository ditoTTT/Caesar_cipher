from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# text = 'mjqqt'
# shift = 5
new_text = []
end_of_cypher = False
while  end_of_cypher == False:
    if direction == 'encode':
        def encrypt(letter):
            for x in letter:
                if (alphabet.index(x) + shift) > len(alphabet):
                    var = (shift - (len(alphabet) - alphabet.index(x)))
                    new_text.append(alphabet[var])
                else:
                    var = alphabet.index(x) + shift
                    new_text.append(alphabet[var])
            shifted_text = ''.join(new_text)
            print(f"The encoded text is {shifted_text}")
        encrypt(text)
        question = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
        if question == 'no':
            end_of_cypher = True
            print('Goodbye')
        elif question == 'yes':
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            new_text = []
        else:
            print('Write a correct input!')
    else:
        def decrypt(letter):
            for x in letter:
                var = alphabet.index(x) - shift
                new_text.append(alphabet[var])
            shifted_text = ''.join(new_text)
            print(f"The decoded text is {shifted_text}")
        decrypt(text)
        question = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
        if question == 'no':
            end_of_cypher = True
            print('Goodbye')
        elif question == 'yes':
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            new_text = []
        else:
            print('Write a correct input!')