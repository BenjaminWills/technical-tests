from pickle import DICT
import random
import string

dictionary = open('dictionary.txt','r')
dictionary_data = dictionary.read()

DICTIONARY_LIST = dictionary_data.replace('\n','.').split('.')
ALPHABET = [*string.ascii_uppercase]

def get_chars_of_word(word:str):
    return [*word]

def get_letter_score(letter:str):
    score_dict = {
        'E':1,'A':1,'I':1,'O':1,'N':1,'R':1,'T':1,'L':1,'S':1,'U':1,
        'D':2,'G':2,
        'B':3,'C':3,'M':3,'P':3,
        'F':4,'H':4,'V':4,'W':4,'Y':4,
        'K':5,
        'J':8,'X':8,
        'Q':10,'Z':10}
    return score_dict[letter]

def get_word_score(word:str):
    characters = get_chars_of_word(word)
    word_score = 0
    for char in characters:
        word_score += get_letter_score(char.upper())
    return word_score

def get_bag():
    bag = {
        'E':12,
        'A':9,'I':9,
        'O':8,
        'N':6,'R':6,'T':6,
        'L':4,'S':4,'U':4,'D':4,
        'G':3,
        'B':2,'C':2,'M':2,'P':2,'F':2,'H':2,'V':2,'W':2,'Y':2,
        'K':1,'J':1,'X':1,'Q':1,'Z':1
    }
    return bag

def is_in_bag(bag:dict,letter:str):
    return bag[letter] != 0

def get_letter(bag:dict):
    random_index = random.randint(0,25)
    random_letter = ALPHABET[random_index]
    while not is_in_bag(bag,random_letter):
        random_index = random.randint(0,25)
        random_letter = ALPHABET[random_index]
    return random_letter
    

def get_tiles(num:int = 7):
    hand = []
    bag = get_bag()
    for i in range(num):
        random_letter = get_letter(bag)
        hand.append(random_letter)
        bag[random_letter] -= 1
    return hand

def is_anagram(tiles:list,dict_word:str):
    word_1_list = list(tiles)
    word_1_list.sort()
    word_2_list = list(dict_word.upper())
    word_2_list.sort()
    return word_1_list == word_2_list

def find_valid_word(tiles:list):
    for i in range(len(tiles)):
        for j in range(i,len(tiles)):
            sub_tile = tiles[i:j]
            print(sub_tile)
            for word in DICTIONARY_LIST:
                if is_anagram(sub_tile,word):
                    return word
    return None

def find_valid_words(tiles:list):
    possible_words = []
    dict_list = DICTIONARY_LIST
    for i in range(len(tiles)):
        for j in range(i,len(tiles)):
            sub_tile = tiles[i:j]
            for word in dict_list:
                if is_anagram(sub_tile,word):
                    possible_words.append(word)
                    dict_list.remove(word)
        return possible_words

def find_longest_word(words:list):
    if len(words) == 0:
        return None
    return max(words)

tiles = get_tiles()
print(find_valid_word(tiles))