import string , math

dictionary = list(string.ascii_lowercase)

def decoder(key , decode):
	result = list()
	key_limit = len(key) - 1
	key_ptr = 0
	for d in decode :
		d_index = dictionary.index(d)
		k_index = dictionary.index(key[key_ptr])
		result.append(dictionary[ (d_index-k_index)%26 ])
		key_ptr += (key_ptr==key_limit) and -key_ptr or 1
	return "".join(result)


def encoder(key , encode):
	result = list()
	key_limit = len(key) - 1
	key_ptr = 0 
	for e in encode :
		if e not in dictionary :
			result.append(e)
			continue
		e_index = dictionary.index(e)
		k_index = dictionary.index(key[key_ptr])
		result.append(dictionary[ (e_index+k_index)%26 ])
		key_ptr += (key_ptr==key_limit) and -key_ptr or 1
	return "".join(result)

if __name__ == "__main__" :
	word = "berlin"
	key  = "claire"
	word_decoded = decoder(key,word)
	word_encoded = encoder(key,word_decoded)
	print word_decoded
	print word_encoded
