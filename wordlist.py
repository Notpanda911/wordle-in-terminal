

#file to make list of words from words.txt
with open('words.txt', 'r') as f:
    wordlist = [line.strip() for line in f]
