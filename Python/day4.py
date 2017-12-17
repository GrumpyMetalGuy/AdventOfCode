def loadPassphrases():
    phrases = []

    with open('../inputs/day4.txt', 'r') as phraseFile:
        line = phraseFile.readline()

        while line:
            phrases.append(line[:-1].split(' '))
            line = phraseFile.readline()

    return phrases


def validPhraseCount(phrases):
    filteredPhrases = [set(phrase) for phrase in phrases if len(phrase) == len(set(phrase))]

    return len(filteredPhrases)


def validNonAnagramPhraseCount(phrases):
    sortedPhrases = [[''.join(sorted(word)) for word in phrase] for phrase in phrases]
    filteredPhrases = [phrase for phrase in sortedPhrases if len(set(phrase)) == len(phrase)]

    return len(filteredPhrases)


def main():
    passphraseInputs = loadPassphrases()

    print(validPhraseCount(passphraseInputs))
    print(validNonAnagramPhraseCount(passphraseInputs))


if __name__ == '__main__':
    main()
