class FileStream:
    filename = "";
    
    def __init__(self, filename = "") -> None:
        self.filename = filename;
    
    def getContent(self):
        with open("generated/" + self.filename or "generated/wordlist.txt", 'r') as file:
            return file.read();
        
    def write(self, data):
        with open("generated/" + self.filename or "generated/wordlist.txt", 'w') as file:
            file.write(str(data));
    
    def writeLine(self, data):
        with open("generated/" + self.filename or "generated/wordlist.txt", 'a') as file:
            file.write(str(data) + "\n");