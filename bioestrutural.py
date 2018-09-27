#/bin/envs python3
#-*- encoding: utf-8 -*-

#	if(re.findall(r"^>[a-zA-Z0-9]{6}$",line)):	

try:
	import numpy as np
except ImportError:
	raise ImportError("pip3 install numpy")

try:
	import pandas as pd 
except ImportError:
	raise ImportError("pip3 install pandas")

import os, argparse, math , re
from decimal import Decimal

# Criar uma lista com as letras do dicionario e armazenar o valor 
global keys
#keys = ['A', 'T', 'C', 'G']
keys = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z', '-'] 



def one_seq_pssm(seq):

	# Armazenar sequências em listas 
	list_seq = seq.split('\n')
	list_seq2 = []
	for ii in list_seq:
		list_seq2.append(list(ii))
	
	# removendo espaço
	del(list_seq2[-1])
	
	# Transformando a lista em array numpy e fazendo a transporta do array.
	array_seq2 = np.array(list_seq2)
	array_seq2 = array_seq2.transpose()
	
	print(array_seq2)
	
	aminoacid = dict.fromkeys(keys,0)

	pfm = pd.DataFrame(data=[],index=keys,columns=[])

	for i in range(len(array_seq2)):
		#print(aminoacid)
		aminoacid = dict.fromkeys(keys, 0)
		for j in range(len(array_seq2[i])):
		 	aminoacid[array_seq2[i,j]] = aminoacid[array_seq2[i, j]] + 1

		pfm[i] = [round(math.log(((x/10)/0.05),2), 2) if (x != 0 or x == '-')  else '-inf' for x in list(aminoacid.values())]

	
	return pfm

def Xseqs_pssm(seq):

	#labels = []
	#sub_list = []
	# Armazenar sequências em listas 
	list_seq = {}
	str_aux = ''
	with open(seq,'r') as file:
		for line in file:
			if(line[0] == '>'):
				line = line.strip('\n')
				list_seq[line] = ''
				str_aux = line
			else:
				list_seq[str_aux] += line
		
	len_seq = []
	list_seq2 = []
	for i in list_seq.keys():
		list_seq[i] = list_seq[i].replace('\n','')[:-1]
		len_seq.append(len(list_seq[i]))
	

	pfm = pd.DataFrame(0,index=keys,columns=[x for x in range(max(len_seq))])

	for index,seq in enumerate(list_seq.values()):
		#print(index,seq,sep='\n')
		for index_letter,letter in enumerate(seq):
			pfm.fillna(value=0,inplace=True) 
			pfm.loc[letter,index_letter] += 1
							
	pssm = pfm.applymap(lambda x: round(math.log((x/len(len_seq))/0.05,2),2) if x != 0 else '-inf')
	

	return pssm
	
def main():

	parser = argparse.ArgumentParser(description="BioInformatica Estrutural PSSMs - version(0.0.1)")
	parser.add_argument("-f","--file", 	dest="file", nargs="?", required=True, help="Arquivo que contem a sequencia")
	args = parser.parse_args()

	fh = open(args.file,'r')
	file = fh.read()


	if(file[0] == '>'):
		resultado = Xseqs_pssm(args.file)
	else:
		resultado = one_seq_pssm(file)
		
	print(resultado)
	
	
if __name__ == "__main__":
	main()
