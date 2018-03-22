text="apple"

def encode_text(text):
	text.lower()
	first_letter = text[0]
	num_fl = text.count(first_letter)
	encoded_text = ""
	for char in text:
		if char.isalpha():
			num_char = ord(char) + num_fl 
			if num_char > ord('z'):
				num_char = num_char-26
			encoded_char = chr(num_char)
		encoded_text += encoded_char
	return encoded_text

print(encode_text(text))
