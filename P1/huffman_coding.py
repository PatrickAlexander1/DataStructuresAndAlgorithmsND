import sys
from heapq import heapify, heappush, heappop
from collections import defaultdict


class Node:
    
    def __init__(self, frequency, value = None):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
        self.bit = None
        
    def __gt__(self, other_node):
        return self.frequency > other_node.frequency
        
def merge_nodes(node1, node2):
    
    combined_frequency = node1.frequency + node2.frequency
    parent = Node(combined_frequency)
    if node1.frequency < node2.frequency:
        parent.left = node1
        parent.right = node2
        node1.bit = 0
        node2.bit = 1
    else:
        parent.left = node2
        parent.right = node1
        node2.bit = 1
        node1.bit = 0
        
    return parent

def get_frequencies(data):
    
    assert type(data) == str

    frequencies = defaultdict(int)
    for val in data:
        frequencies[val] += 1
        
    if len(frequencies.keys()) == 1:
        #https://cboard.cprogramming.com/cplusplus-programming/56414-huffman-code-single-character-file.html
        # Idea for dummy node
        frequencies['filler'] = 1
    return frequencies


def huffman_encoding(data):
    
    assert(len(data) > 0)
    def create_tree(data):
            
        frequencies = get_frequencies(data)
        min_heap = [Node(frequencies[key], key) for key in frequencies]
        heapify(min_heap)
        while len(min_heap) > 1:
            node1 = heappop(min_heap)
            node2 = heappop(min_heap)
            new_node = merge_nodes(node1, node2)
            heappush(min_heap, new_node)
            
        tree =  heappop(min_heap)
        
        return tree
    
    def get_codes(tree, route='', routes = {}):
        
        
        if tree.value:
            routes[tree.value] = route
        else:
            temp1 = route + '0'
            temp2 = route + '1'
            get_codes(tree.left, temp1)
            get_codes(tree.right, temp2)
            
        return routes
    

    def encode_string(codes, data):
        
        encoded_string = ''
        for char in data:
            encoded_string += codes[char]
            
        return encoded_string
    
    tree = create_tree(data)
    codes = get_codes(tree)

    encoded_string = encode_string(codes, data)
    return encoded_string, tree


def huffman_decoding(data,tree):
    
    huffman_tree = [tree]
    current_tree = huffman_tree[0]
    output = ''
    
    while True:

        if data == '':
            output += current_tree.value
            break
        if current_tree.value != None:
            output += current_tree.value
            current_tree = huffman_tree[0]
        elif data[0] == '0':
            current_tree = current_tree.left
            data = data[1:]
        elif data[0] == '1':
            current_tree = current_tree.right
            data = data[1:]
            
    return output

if __name__ == "__main__":

    
    # Test Case 1
    a_great_sentence = "The bird is the word"
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    #Test case 2
    a_great_sentence = "aaaa"
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print(decoded_data)
    
    # Test case 3, assertion error 
#    a_great_sentence = ""
#    
#    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#    print ("The content of the data is: {}\n".format(a_great_sentence))
#    
#    encoded_data, tree = huffman_encoding(a_great_sentence)
#    
#    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#    print ("The content of the encoded data is: {}\n".format(encoded_data))
#    
#    decoded_data = huffman_decoding(encoded_data, tree)
#    
#    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#    print ("The content of the encoded data is: {}\n".format(decoded_data))
#    print(decoded_data)