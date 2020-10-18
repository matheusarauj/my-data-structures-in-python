# URI 1556 - Removendo Letras

def find(sequence, anwsers, words, wordsN, i):
    if i == wordsN:
        anwsers.add(sequence)
    else:
        sequenceAux = sequence + words[i]
        if sequenceAux not in anwsers:
            find(sequenceAux, anwsers, words, wordsN, i + 1)
        find(sequence, anwsers, words, wordsN, i + 1)

while True:
    try:
        words = list(input())
        anwsers, wordsN = set(), len(words)

        find('', anwsers, words, wordsN, 0)
        anwsers.remove('')

        for i in sorted(anwsers):
            print(i)
        print()

    except EOFError:
        break