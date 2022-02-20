def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def isValidSiteswap(s):
    d = set()
    n = len(s)
    for i in range(n):
        d.add((ord(s[i])+i)%n)
    if len(d) == len(s):
        return True
    return False

if __name__ == '__main__':
    english_words = load_words()

    ss_words = []
    for w in english_words:
        if isValidSiteswap(w):
            # print(w)
            ss_words.append(w+"\n")
    ss_words.sort()

    with open("siteswap_words.txt", "w") as file1:
        file1.writelines(ss_words)