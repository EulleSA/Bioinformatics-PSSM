#/bin/envs python
#-*- encoding: utf-8 -*-
import numpy as np 
import pandas as pd 
import os, argparse
import math
# Criar uma lista com as letras do dicionario e armazenar o valor 
global keys
keys = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z'] 

def PSSMsCalculate():
	print("função para calcular a matrix pssm")

def main():

	parser = argparse.ArgumentParser(description="BioInformatica Estrutural PSSMs - version(0.0.1)")
	parser.add_argument("-f","--file", 	dest="file", nargs="?", required=True, help="Arquivo que contem a sequencia")
	args = parser.parse_args()

	fh = open(args.file,'r')
	line = fh.read()

	# Armazenar sequências em listas 
	list_seq = line.split('\n')
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
	#print(newDF)
	#M = []

	for i in range(len(array_seq2)):
		#print(aminoacid)
		aminoacid = dict.fromkeys(keys, 0)
		for j in range(len(array_seq2[i])):
		 	aminoacid[array_seq2[i,j]] = aminoacid[array_seq2[i, j]] + 1

		pfm[i] = [x/10 for x in list(aminoacid.values())]
		
		#pfm[i] = [math.log((x/10)/0.05,2) for x in list(aminoacid.values()) if x != 0]

		

	print(pfm)
		
	

	# Dicionario dentro de dataFrame ?
		
		#print(newDF)
		#M.append(df1)
		#print(aminoacid)
		#newDF = pd.concat(aminoacid)

	#print(M)
	#newDF = pd.concat(M)
	#print(aminoacid)
	
if __name__ == "__main__":
	main()