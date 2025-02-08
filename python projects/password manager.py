def encryption(word):
    encrypted_word = ""
    string = "abcdefghijklmnopqrstuvwxyz"
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"
    number_encryption = "0123456789"

    for alpha in word:
        if alpha.isupper():  
            index = (string.find(alpha.lower()) + 3) % 26
            encrypted_word += string[index].lower()
        elif alpha.islower():
            index = (string.find(alpha) + 3) % 26
            encrypted_word += string[index].upper()
        elif alpha.isdigit():  
            index = (number_encryption.find(alpha) + 3) % 10
            encrypted_word += number_encryption[index]
        elif alpha in special_chars:
            index = (special_chars.find(alpha) + 3) % len(special_chars)
            encrypted_word += special_chars[index]
        else:
            encrypted_word += alpha

    return encrypted_word            


def decryption(encrypted_word):
    decrypted_word = ""
    string = "abcdefghijklmnopqrstuvwxyz"
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"
    number_decryption = "0123456789"

    for alpha in encrypted_word:
        if alpha.isupper():  
            index = (string.find(alpha.lower()) - 3) % 26
            decrypted_word += string[index].lower()
        elif alpha.islower():
            index = (string.find(alpha) - 3) % 26
            decrypted_word += string[index].upper()
        elif alpha.isdigit():  
            index = (number_decryption.find(alpha) - 3) % 10
            decrypted_word += number_decryption[index]
        elif alpha in special_chars:
            index = (special_chars.find(alpha) - 3) % len(special_chars)
            decrypted_word += special_chars[index]
        else:
            decrypted_word += alpha

    return decrypted_word

            
        
    return decrypted_word

def add(input,domain,dic):
    encrypted_input=encryption(input)
    dic[domain]=encrypted_input
    return dic

def main():
    password = input("Enter the password to access the list of passwords: ")
    dic = {}

    if password == "this":
        while True:
            operation = input("Do you want to add/view password and q for quit: ").strip().lower()

            if operation == "add":
                user_input = input("Enter the password: ")
                user_domain = input("For which website or domain is this password for: ")
                add_password = add(user_input, user_domain, dic)
                print("Password added with encryption:", dic)

            elif operation == "view":
                if dic:
                    for keys in dic:
                        print(f"Encrypted password for {keys}: {dic[keys]}")  # Debugging print
                        decrypted_password = decryption(dic[keys])
                        print(f"Password for {keys} is {decrypted_password}")
                else:
                    print("No passwords stored yet.")

            elif operation == "q":
                print("You have decided to quit the program")
                break

            else:
                print("Invalid option, please enter 'add', 'view', or 'q'.")

    else:
        print("This is not a correct password. Try again.")

    print("Have a nice day!")        

main()