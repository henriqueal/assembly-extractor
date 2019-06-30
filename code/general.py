import os
import extrator_by_depth as ext

def showDict(list_dict):
        #print("etrou aqui");
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


def func1 (path):
	

	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		print r
		for file in f:
			#if '.xml' in file:
			print file
			list_dict = ext.extract(os.path.join(r, file))
			print list_dict
			files.append(os.path.join(r, file))
			 

	for f in files:
		print(f)
		
def func2():
	mylist = []
	#mylist.append(['add0', 'mul0', 'ld0', 'st0', 'misc0', 'add1', 'mul1', 'ld1', 'st1', 'misc1', 'add2', 'mul2', 'ld2', 'st2', 'misc2', 'add3', 'mul3', 'ld3', 'st3', 'misc3']);
	path_root = '/home/henrique/Documentos/'
	file = 'DSP_w_vec_c/'
	path_assembly = path_root + 'assembly/' + file
	path_latency = path_root + 'latency/' + file
	con = 0
	for i in range(1000):
		exists = os.path.isfile(path_assembly + str(i+1) + ".0.galo");
		if exists:
			f = open(path_latency+str(i+1))
			latency=f.read()
			##if latency == "" or latency=='-4':
				##continue
			list_dict = ext.extract(path_assembly+str(i+1)+".0.galo")
			f.close();
			mylist.append(str(i+1)+","+showDict(list_dict)+latency)
		else:
			con += 1	
	print con

	
	fw = open(path_root + "assembly-extractor/out/" + file + "output.txt", "a")
	for i in mylist:
		fw.write(i)
		fw.write("\n")
	fw.close()

func2()
