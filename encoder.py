from random import choice, randint
from spellchecker import SpellChecker
spell = SpellChecker()


def encode(txt):
	chars = {}
	bad_syms = (' ', ',', '.', ':', ';', '?', '!', "'", '"')

	for i in txt:
		if i not in chars.keys() and i not in bad_syms:
			chars[i] = 1
		elif i not in bad_syms:
			chars[i] += 1
		else:
			if i != "'" or i != '"':
				txt = txt.replace(i, ' ')

	txt = txt.split(' ')
	mx = max(chars.values())
	add_txt = ''

	while bool(chars):
		r_char = choice(tuple(chars.keys()))
		if chars[r_char] < mx:
			add_txt += r_char
			chars[r_char] += 1
		else:
			chars.pop(r_char)

	splt = randint(1, 6)
	while splt < len(add_txt):
		if spell.correction(add_txt[0:splt]) == add_txt[0:splt]:
			continue
		txt.insert(randint(1, len(txt)), add_txt[0:splt])
		add_txt = add_txt.replace(add_txt[0:splt], '')
		splt = randint(1, 6)

	txt.insert(randint(1, len(txt)), add_txt[0:splt])
	return ' '.join(txt)


if __name__ == '__main__':
	txt_to_encode = input("Input text: ").lower()
	encoded = encode(txt_to_encode)
	print(encoded)
	input('Press Enter to continue...')
