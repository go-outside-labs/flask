def generate_md5_hash(string):
	import hashlib
	return hashlib.md5(string.encode('utf-8')).hexdigest()
	
string = "heeelllloo"
print(string)
print(generate_md5_hash(string))
