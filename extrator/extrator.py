import nltk

def main():
	# open file
	f = open ("function.optim.s", "r");
	
	# Read all lines
	lines = f.readlines();
	
	flagBeginCode = False;
	listDict = [];
	dict = {};
	headers_tokens = 0;
	depth = 0;
	
	for line in lines:
	
		#condicao de parada do arquivo
		if(line.startswith('\n')):
			break;
		
		#Vou ler as linhas ate achar o comeco do codigo
		if(flagBeginCode == False):		
			if(line.startswith('DSP')):
				flagBeginCode = True;
		#depois que comecar eu vou fazer o processamento
		else:
			# preciso encontrar um header
			if not line.startswith('\t'):
				# tokeniza a linha
				line = line.replace("! ", "");
				line = line.replace("#", "0_");
				
				headers_tokens = nltk.word_tokenize(line);
				
				print(headers_tokens);
				#print(headers_tokens[len(headers_tokens) - 1]);
				# verifica se o dicionario nao esta vazio
				if bool(dict):
					listDict.append(dict);
				dict = {headers_tokens[0]:{}};
				
				if headers_tokens[len(headers_tokens)-1].startswith("Depth="):
					depthSplitList = headers_tokens[len(headers_tokens)-1].split("=");
					depth = depthSplitList[1];
				dict[headers_tokens[0]]['depth'] = depth; 
			
			else:
				body_tokens = nltk.word_tokenize(line);

				if body_tokens[0] in dict[headers_tokens[0]].keys():
					dict[headers_tokens[0]][body_tokens[0]] = dict[headers_tokens[0]][body_tokens[0]] + 1;
				else: 		
					dict[headers_tokens[0]][body_tokens[0]] = 1;
	listDict.append(dict);
	print listDict;
if __name__ == "__main__":
	main()