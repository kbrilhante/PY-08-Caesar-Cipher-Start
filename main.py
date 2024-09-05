characters = list("abcdefghijlmnopqrstuvwxyz")


# encrypts the text
def encrypt(text, key):
    """ encrypts the text based on the key """
    pass


# decrypts text
def decrypt(enc_text, key):
    """ decrypts the text based on the key """
    pass


# menu
opt = 0
options = 4
while opt != options:
    while opt < 1 or opt > options:
        txtMenu = "Menu:\n"
        txtMenu += "1 - Encrypt message\n"
        txtMenu += "2 - Decrypt message\n3 - Change key\n4 - Quit\n> "
        opt = int(input(txtMenu))
        if opt < 1 or opt > options:
            print("Choose a valid option\n")

    # handle the menu here:

    if opt == 1:
        # encrypt
        pass
    elif opt == 2:
        # decrypt
        pass
    elif opt == 3:
        # change key
        pass

    if opt != 4:
        opt = 0
        print("\n\n")
