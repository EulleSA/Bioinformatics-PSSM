#/bin/envs python
#-*- encoding: utf-8 -*-
import numpy as np 
import pandas as pd 
import os, argparse

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
#	print(array_seq2)

	aminoacid = dict.fromkeys(keys,0)

	for index,letter in enumerate(array_seq2):
		print(letter[4])
#		print(index)
		aminoacid[letter[4]] = aminoacid[letter[4]] + 1

	print(aminoacid)

if __name__ == "__main__":
	main()
