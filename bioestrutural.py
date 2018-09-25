#/bin/envs python3
#-*- encoding: utf-8 -*-

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

def PSSMsCalculate(seq):

	labels = []
	sub_list = []
	# Armazenar sequências em listas 
	list_seq = {}
	str_aux = ''
	with open(seq,'r') as file:
		for line in file:
			if(line[0] == '>'):
				list_seq[line] = ''
				str_aux = line
			else:
				list_seq[str_aux] += line
		#	if(re.findall(r"^>[a-zA-Z0-9]{6}$",line)):	
		#		labels.append(line.strip('\n'))
		#	else:
		#		list_seq.append(line.strip('\n'))
	print(labels)
	print(list_seq)

	for i in list_seq.keys():
		list_seq[i] = list_seq[i].split('\n')[:-1]
		#for ii in list_seq[i]:
			 
		#array_seq2 = np.array(list_seq[i])
		#array_seq2 = array_seq2.transpose()
	
	print(list_seq)
'''
	list_seq = seq.split('\n')
	list_seq2 = []
	
	
	#for match in re.finditer(r"^>[a-zA-Z0-9]{6}",list_seq):
	#	labels.append(match)
	print(list_seq)
	
	for match in list_seq:
		if (re.findall(r"^>[a-zA-Z0-9]{6}",match)):
			labels.append(match)
	print(labels)

	for ii in list_seq:
		list_seq2.append(list(ii))
	
	# removendo espaço
	del(list_seq2[-1])
	
	# Transformando a lista em array numpy e fazendo a transporta do array.
	array_seq2 = np.array(list_seq2)
	array_seq2 = array_seq2.transpose()
	
	#print(array_seq2)
	
	aminoacid = dict.fromkeys(keys,0)

	pfm = pd.DataFrame(data=[],index=keys,columns=[])
	#print(newDF)
	#M = []

	for i in range(len(array_seq2)):
		#print(aminoacid)
		aminoacid = dict.fromkeys(keys, 0)
	
		for j in range(len(array_seq2[i])):
		 	aminoacid[array_seq2[i,j]] = aminoacid[array_seq2[i, j]] + 1

		pfm[i] = [round(math.log(((x/10)/0.05),2), 2) if x != 0 else 'NaN' for x in list(aminoacid.values())]


	return pfm
'''
def main():

	parser = argparse.ArgumentParser(description="BioInformatica Estrutural PSSMs - version(0.0.1)")
	parser.add_argument("-f","--file", 	dest="file", nargs="?", required=True, help="Arquivo que contem a sequencia")
	args = parser.parse_args()

	#fh = open(args.file,'r')
	#line = fh.read()

	resultado = PSSMsCalculate(args.file)
	print(resultado)
	
	
if __name__ == "__main__":
	main()