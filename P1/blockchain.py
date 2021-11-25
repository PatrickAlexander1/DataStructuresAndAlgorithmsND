import hashlib
from time import gmtime, strftime

class Block:

    def __init__(self, data, previous_hash = None, timestamp = strftime("%a, %d %b %Y %H:%M:%S", gmtime())):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.previous_hash)
        self.prev = None

    def calc_hash(self, previous_hash):
        sha = hashlib.sha256()
        hash_str = str(previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    

class Blockchain:

    def __init__(self):
        self.blockchain = None

    def add_block(self, data):
        
        if self.blockchain is None:
            new_block = Block(data)
            self.blockchain = new_block
        else:
            last_block = self.blockchain
            last_block_hash = last_block.hash
            new_block = Block(data, last_block_hash)
            new_block.prev = last_block
            self.blockchain = new_block
    


    def get_history(self):
        out = ''
        current_block = self.blockchain
        if current_block == None:
            print('Empty Blockchain')
        while current_block:
            out += 'Data: {}, Hash: {}, Timestamp: {} \n'.format(current_block.data, current_block.hash, current_block.timestamp)
            current_block = current_block.prev
        print(out)

        

# Test case 1
blockchain = Blockchain()
blockchain.add_block('sender: y, recipient: x, amount: 10')
blockchain.add_block('sender: x, recipient: y, amount: 20')
blockchain.add_block('sender: y, recipient: x, amount: 20')
blockchain.get_history()




#Test case 2
blockchain = Blockchain()
blockchain.get_history()


#Test case 3 all blocks have the same timestamp
blockchain = Blockchain()
blockchain.add_block('sender: y, recipient: x, amount: 10')
print(blockchain.blockchain.timestamp)
blockchain.add_block('sender: x, recipient: y, amount: 20')
print(blockchain.blockchain.timestamp)
blockchain.add_block('sender: y, recipient: x, amount: 20')
print(blockchain.blockchain.timestamp)


# Test adding 1000 blocks
blockchain = Blockchain()
for i in range(1000):
    blockchain.add_block(i)
    



    

