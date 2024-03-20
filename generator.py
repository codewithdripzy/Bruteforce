from core.tokenizer import Tokenizer;
from core.generator import PasswordGenerator;
from core.file import FileStream;

# This method is called every time a password is generated
def logData(psw, indexes, data):
    print(psw);
    
# Initialize the tokenizer and extract tokens from the characthers.txt file
tokenizer = Tokenizer("data/test_characthers.txt");
tokens = tokenizer.init();
    
# Generate the possible combinations
generator = PasswordGenerator(tokens, min_length=8, max_length=8);
generated = generator.generate(logData);

# do something with the generated passwords
file = FileStream("wordlist.txt");
file.write(generated);

