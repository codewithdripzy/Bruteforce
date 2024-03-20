class PasswordGenerator:
    length = 4;
    max_length = 18;
    tokens = None;
    iteration = 0;
    indexes = [0, 0, 0, 0];
    # indexes = [136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 136, 0];
    
    
    def __init__(self, tokens, cached_index = [], min_length = 4, max_length= 18) -> None:
        i = 0;
        indexes = [];
        
        self.tokens = tokens;
        self.max_length = max_length;
        
        if min_length > 0:
            while i < min_length:
                indexes.append(0);
                i += 1;
        
        self.indexes = indexes;
        if cached_index:
            self.indexes = cached_index;
    
    def generate(self, next = None, data = None):
        if(self.batchIsCompleted()):
            print("completed");
        else:
            self.generateBatch(next, data);
    
    def generateBatch(self, next = None, data = None):
        psw = self.createPassword();
        
        if next:
            next(psw, self.indexes, data);
        
        while not self.batchIsCompleted():
            self.incrementIndex();
            psw = self.createPassword();
            
            if next:
                next(psw, self.indexes, data);
        else:
            if not len(self.indexes) >= self.max_length:
                self.incrementIndex();
                self.resetIndexes();
                self.generateBatch(next, data);
            else:
                print("endl");
    
    def createPassword(self):
        i = 0;
        psw = '';
        
        while i < len(self.indexes):
            psw += self.tokens[self.indexes[i]];
            i += 1;
        return psw;
            
    def resetIndexes(self):
        i = 0;
        
        while i < len(self.indexes):
            self.indexes[i] = 0;
            i += 1;
        
    def incrementIndex(self):
        # 
        self.incrementRecursively(len(self.indexes));
    
    # This hanldes incrementation after generating all combination in one index
    def incrementRecursively(self, i):
        # get current index
        index = i - 1;
        
        # check if the batch process is still on
        if not self.batchIsCompleted():
            # make sure the number of index is not `0`
            if i >= 0:
                # check if the current index has reached the last token 
                if self.indexes[index] == (len(self.tokens) - 1):
                    # rest the current index and move to index before it
                    self.indexes[index] = 0;
                    self.incrementRecursively(index);
                else:
                    # continue incrementing the current index
                    self.indexes[index] += 1;
            else :
                # cj
                if not self.indexes[0] == (len(self.tokens) - 1):
                    self.indexes[index] += 1;
        else:
            # start another batch process if the previous one is completed
            self.indexes.append(0);
            self.incrementRecursively(len(self.indexes));
                
    # this method is used to control the iteration of the code
    def batchIsCompleted(self):
        # check if the values of the index are the same length as the number of tokens avalable
        for i in self.indexes:
            if(i != (len(self.tokens) - 1)):
                return False;
        return True;