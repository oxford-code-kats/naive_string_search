def word_search(search_term, text):
	matches = 0
	for idx in range(len(text)):
		matches += check_match(idx, search_term, text)
	print(matches)
	return matches

def check_match(idx, search_term, text):
	offset = 0
	for char in search_term:
		if char == text[idx + offset]:
			offset += 1
			if offset == len(search_term):
				return 1
	return 0