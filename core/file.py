class FileStream:
    filename = "";
    
    def __init__(self, filename = "") -> None:
        self.filename = filename;
    
    def write(self, data):
        with open(self.filename or "wordlist.txt", 'w') as file:
            file.write(data);