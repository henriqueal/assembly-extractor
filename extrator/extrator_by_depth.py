import nltk
def showDict(list_dict):
	print("etrou aqui");
	tuple = ""
	tokens = ["add", "mul", "ld", "st", "misc"]
	#print(list_dict)
	for i in range(4):
		#print(list_dict[i][i].keys())
		for token in tokens:
			if token not in list_dict[i][i].keys():
				tuple += "0,"
			else:
				tuple += str(list_dict[i][i][token]) + ","

	return tuple


def extract(filename):

	# lista de tokens
	token_list = ["add", "mul", "st", "ld"];
	token = "misc";

	# open file
	f = open (filename, "r");
	
	# Read all lines
	lines = f.readlines();
	
	flagBeginCode = False;
	listDict = range(10);
	
	for i in range(10):
		dict = {i:{}};
		listDict[i] = dict;
	headers_tokens = 0;
	depth = 0;

	dict = {0:{}};
	
	for line in lines:

		if(".indent" in line):
			break;
		
		#condicao de parada do arquivo
		if(line.startswith('\n')):
			continue;
			#break;
		
		#Vou ler as linhas ate achar o comeco do codigo
		if(flagBeginCode == False):		
			if(line.startswith('DSP')):
				flagBeginCode = True;
		#depois que comecar eu vou fazer o processamento
		else:

			#if("end" in line):
				#break;
				
			# preciso encontrar um header
			if not line.startswith('\t'):
				
				line = line.replace("! ", "");
				line = line.replace("#", "0_");
				headers_tokens = nltk.word_tokenize(line);
				
				if headers_tokens[len(headers_tokens)-1].startswith("Depth="):
					depthSplitList = headers_tokens[len(headers_tokens)-1].split("=");
					depth = int(depthSplitList[1]);	
					
				else:
					depth = 0;
				
				dict = listDict[depth];
				
			else:
				body_tokens = nltk.word_tokenize(line);
				
				if("add" in body_tokens[0]):
					token = "add";
				elif("mul" in body_tokens[0]):
					token = "mul";
				elif("st" in body_tokens[0]):
					token = "st";
				elif("ld" in body_tokens[0]):
					token = "ld";
				else:
					token = "misc";
					
					
				if token in dict[depth].keys():
					dict[depth][token] = dict[depth][token] + 1;
				else: 		
					dict[depth][token] = 1;
					
		f.close()
	return listDict;
