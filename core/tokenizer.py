import os;

class Tokenizer:
    characthers = '';
    tokens = [];
    file = "";
    
    def __init__(self, file) -> None:
        self.file = file;
        path = os.path.abspath(self.file or "./data/characthers.txt");
        
        with open(path) as chars:
            self.characthers = chars.read();
            
    def init(self):
        for token in self.characthers:
            self.tokens.append(token);
            
        return self.tokens;