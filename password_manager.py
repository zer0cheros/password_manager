from cryptography.fernet import Fernet
breakLoop = True

while breakLoop:
    master = input("input master password, type quit() to quit program: ")
    if(master == 'quit()'):
        break
    def load_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

    key = load_key()
    fer = Fernet(key)
    def loadSecret():
        with open("secret.txt", 'rb')as s:
            secret = s.read()
            return secret
    secret2 = loadSecret()
    secret = fer.decrypt(secret2).decode('utf-8')


    def view():
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "| Password:",
                    fer.decrypt(passw.encode()).decode())


    def add():
        name = input('Account Name: ')
        pwd = input("Password: ")

        with open('passwords.txt', 'a') as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


    while True:
        if master == secret:
            mode = input(
                "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
            if mode == "q":
                break

            if mode == "view":
                view()
            elif mode == "add":
                add()
            else:
                print("Invalid mode.")
                continue
        else:
            print('Invalid master password, try again')
            break