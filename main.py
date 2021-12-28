from passwordgenerator import PasswordGenerator
from qrgenerator import QRGenerator

def main():
    number = int(input("Passwords to generate: "))
    size = int(input("Password lenght: "))
    gen = PasswordGenerator(number,size)
    passwords = gen.iteratePasswords()
    print(passwords)

    items = QRGenerator(passwords)
    print(items.createQR())
    
    

if __name__ == "__main__":
    main()