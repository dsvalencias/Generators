import qrcode
#import tempfile

class QRGenerator:
    #defaultPath = "D:/Repositories/Learning/PasswordGenerator/PasswordGenerator/gen"
    def __init__(self, data):
        self.data = data
        
    
    def createQR(self):
        img = qrcode.make(self.data)
        try:
            img.save("save.png")
        except:
            return FileNotFoundError
        return "OK"
