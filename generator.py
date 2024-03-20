from core.tokenizer import Tokenizer;
from core.generator import PasswordGenerator;
from core.file import FileStream;

# This method is called every time a password is generated
file = FileStream("wordlist.txt");

def writeData(psw, indexes, data):
    file.writeLine(psw);
    
# Initialize the tokenizer and extract tokens from the characthers.txt file
tokenizer = Tokenizer("data/test_characthers.txt");
tokens = tokenizer.init();
    
# Generate the possible combinations
generator = PasswordGenerator(tokens, min_length=2, max_length=8);
generated = generator.generate(writeData);


