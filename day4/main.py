import itertools

def clean_data(data):
    # passphrases are strings of characters separated by spaces
    return list(map(lambda x:x.split(" "), data))

def is_unique(passphrase):
    # passphrase contains duplicate words if casting to set changes (reduces) length
    return len(passphrase) == len(set(passphrase))

def is_anagram(word1, word2):
    # word is an anagram if sorting it makes it the same
    return sorted(word1) == sorted(word2)

def contains_anagram(passphrase):
    # if any two words in the passphrase are an anagram, passphrase is invalid
    for words in itertools.combinations(passphrase, r=2):
        if is_anagram(*words):
            return True
    return False

def part1(data):
    return len([passphrase for passphrase in data if is_unique(passphrase)])

def part2(data):
    return len([passphrase for passphrase in data if is_unique(passphrase) and not contains_anagram(passphrase)])

        

            