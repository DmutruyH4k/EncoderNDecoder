from spellchecker import SpellChecker


def decode(txt):
    spell = SpellChecker()
    txt = txt.split(' ')
    bad_words = spell.unknown(txt)

    for i in bad_words:
        txt.pop(txt.index(i))

    for i in txt:
        if len(i) == 1 and i != 'a' and i != 'i':
            txt.pop(txt.index(i))

    return ' '.join(txt)


if __name__ == '__main__':
    text = input('Введите зашифрованный текст: ').lower
    text = decode(text)
    print('Расшифрованный текст: ', text)
