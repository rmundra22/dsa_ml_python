class TrieNode:
    
    def __init__(self):
        # {!, ", #, $, %, &, ', (, ), *, +, ,, -, ., /, 0, 1, ... 9, :, ;, <, =, >, ?, @, A(17), B ..., Z(42), [, \, ], ^, _, `, a(49), b, ... z(74)}
        # 15 + 10 + 7 + 26 + 6 + 26 = 90, ord(letter) - ord('!) ==> all letters
        # ASCII {A:65, Z:90, a:97, z:122}
        self.children = [None]*90 #26: {a-z}, 58:{A-Z-()-a-z}, 90:{all characters}
        self.isEndOfWord = False
        self.word_counter = 0

       
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def _char_to_index(self, letter):
        return ord(letter) - ord('!')
    
    def insert(self, word):
        crawl_pt = self.root
        
        for letter in word:
            idx = self._char_to_index(letter)
            if not crawl_pt.children[idx]:
                crawl_pt.children[idx] = TrieNode()
            crawl_pt = crawl_pt.children[idx]
        
        crawl_pt.isEndOfWord = True
        crawl_pt.word_counter += 1
        print('({}) inserted!'.format(word))
            
    def search(self, word):
        crawl_pt = self.root
        
        for letter in word:
            idx = self._char_to_index(letter)
            if not crawl_pt.children[idx]:
                print('\n"{}" is not present in dictionary!'.format(word))
                return
            crawl_pt = crawl_pt.children[idx]
        
        if crawl_pt.isEndOfWord:
            print('\n"{}" is present in dictionary!'.format(word))
            print('"{}" is present {} time(s)'.format(word, crawl_pt.word_counter))
        else:
            print('\n"{}" is not present in dictionary!'.format(word))
        return
            
            
def main():
    dictionary = ['pprt', 'paris', '1paris', 'Bat', 'paris', 'party', 'ball']
    trie = Trie()
    
    for word in dictionary:
        trie.insert(word)
    
    trie.search('party')
    trie.search('paris')
    trie.search('1paris')
    trie.search('Bat')
    trie.search('rate')
    
    
if __name__ == "__main__":
    main()
        