import encoder
import decoder

if __name__ == "__main__":
    txt = input("Введите текст: ").lower()
    checksum = 0
    for i in txt:
        checksum += ord(i)

    encoded = encoder.encode(txt)
    decoded = decoder.decode(encoded)
    ssum = 0
    for i in decoded:
        ssum += ord(i)
    while ssum != checksum:
        ssum = 0
        encoded = encoder.encode(txt)
        decoded = decoder.decode(txt)
        for i in decoded:
            ssum += ord(i)

    print(encoded)
    input('Нажмите на любую клавишу для продолжения...')
