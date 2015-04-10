import string , math

dictionary = list(string.ascii_lowercase)

def de_en_coder(key,token,state=True):
	"""
		(str,str,bool) -> (str)
		True -> encode
		False -> decode
	"""
	result = list()
	key , token_lower = key.lower() , token.lower()
	key_limit = len(key) - 1
	key_ptr = 0 
	for i,t in enumerate(token_lower) :
		if t not in dictionary :
			result.append(t)
			continue
		t_index = dictionary.index(t)
		k_index = dictionary.index(key[key_ptr])
		r_index = ( (state) and (t_index+k_index) or (t_index-k_index) ) %26
		if token[i].isupper():
			result.append(dictionary[r_index].upper())
		else:
			result.append(dictionary[r_index])
		key_ptr += (key_ptr==key_limit) and -key_ptr or 1
	return "".join(result)

if __name__ == "__main__" :
	word = "Hello World! My name is Berlin."
	key  = "claire"
	word_encoded = de_en_coder(key,word,True)
	word_decoded = de_en_coder(key,word_encoded,False)
	print word_encoded
	print word_decoded
