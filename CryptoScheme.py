import hashlib as hl
import os.path
import os


print("Enter cypher key")
key = Normalize_key(input())
def Normalize_key(key):
	pre_pass = hl.md5(bytes(key))
	normalized_key =pre_pass.hexdigest()
	return normalized_key




def Main(img,key):
	crypted_blocks = []
	current_block = "" 
	current_block_id = 0
	with open(img,"rb") as f:
		data = f.read()
		data = Normalize_image(data)


		ammount_blocks = data % 16

		while current_block_id != ammount_blocks - 1:
			for i in range(0,16):
				current_block += hex(data[i])
			current_block = Normalize_block(current_block)
			crypted_blocks.append(xor(current_block,key))
			current_block_id += 1
	Build(crypted_blocks,os.path.basename() + str(".cjpg"))








def Normalize_image(data):
	exist = len(data) % 16
	if exist != 0:
		arr1 = bytearray(16 - exist)
		data = data + arr1
	return data
def Normalize_block(str_):
	arr = list(str_)
	for i in range (0,len(str_)):
		if i % 4 == 0:
			arr[i] = r"/"
	res = "".join(arr)
	return res
def pre_xor(str_):
	return int(str_,base=16)

def xor(a,b):
	pre_xor(a)
	pre_xor(b)
	return a ^ b
def Build(container,name):
	data = "".join(container)
	with open (name,"wb") as f:
		f.write(data)
		return 0

def BunchCrypt(key,path):
	os.makedir("hidden")
	os.system('attrib' + path + "\\hidden" + '+H')
	files = os.walk(path)
	for i in files:
		if not os.isdir(i):
			os.system("move" + i + " " + os.path.dirname(i) + "\\hidden" + os.path.basename(i))
			Main(i,key)

def Restore(path):
	os.chdir(path + "\\hidden")
	for i in os.walk(os.cwd()):
		os.system("move" + i + " " "..\\" + os.path.basename(i))