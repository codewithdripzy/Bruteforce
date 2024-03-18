import os;

class Tokenizer:
    characthers = '';
    tokens = [];
    
    def __init__(self) -> None:
        path = os.path.abspath("./data/characthers.txt");
        
        with open(path) as chars:
            self.characthers = chars.read();
            
    def init(self):
        for token in self.characthers:
            self.tokens.append(token);
            
        return self.tokens;