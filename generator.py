from core.tokenizer import Tokenizer;
from core.generator import PasswordGenerator;

# Initialize the tokenizer and extract tokens from the characthers.txt file
tokenizer = Tokenizer();
tokens = tokenizer.init();
    
# Generate the possible combinations
generator = PasswordGenerator(tokens);
generated = generator.generate();



