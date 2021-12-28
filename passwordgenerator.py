import string
import random

class PasswordGenerator:
    default_sample = string.ascii_letters + string.digits + string.punctuation
    def __init__(self, number, size):
        self.number = number
        self.size = size
    
    def createPasswords(self):
        password = ""
        for l in range(self.size):
            password += random.choice(PasswordGenerator.default_sample)
        return password

    def iteratePasswords(self):
        passwordList = []
        for password in range(self.number):
            passwordList.append(self.createPasswords())
        return passwordList
