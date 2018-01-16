# -*- coding: utf-8 -*-

from rougescore import *
import pandas as pd
import numpy as np
df = pd.read_json('train_v1.1.json',lines=True)
dfnew=df[['answers','passages']].copy()
data_no=dfnew['passages'].count()
k=0
basescore= []
idloc = []
for k in range(data_no):
	basescore.append(0)
	idloc.append([0,0])
	
k=0
word_len=0
print data_no
while(k<data_no):
	no_of_passnow =len(dfnew['passages'][k])
	print df['answers'][k]
	print no_of_passnow
	human_gen= df['answers'][k]
	analysis = dfnew['passages'][k]
	n_nop=0
	while(n_nop<no_of_passnow):
		if(analysis[n_nop]['is_selected']==0):
			n_nop=n_nop+1
		else:
			
			para = analysis[n_nop]['passage_text']
			print para
			npara = para.split()
			lpara = len(para.split())
			
			while (word_len<lpara):	
				word_len=word_len+1	
				start_pos=0					
				while(start_pos<lpara):
					nk=""
					pos=start_pos
					pos_dummy=start_pos
					words=word_len					
					while(words>0 and pos<lpara):
						nk = nk+ npara[pos] +" "
						words=words-1 
						pos=pos+1
					score = rouge_l(nk, human_gen, 0 )
					if(score >basescore[k] ):
	
						basescore[k] = score
						idloc[k] = [pos_dummy,pos_dummy+word_len-1]
						
					start_pos=start_pos+1
			n_nop=n_nop+1
	print basescore[k]
	print idloc[k]
	iala=1
	jala=idloc[k][0]
	print jala
	while(iala<idloc[k][1]):
		print npara[jala],
		iala=iala+1
		jala=jala+1				
		
	n_nop=0
	start_pos=0
	word_len=0			
	k=k+1
	
with open('ids.txt','w') as f:
		for item in idloc:
	  		print>>f, item[0],item[1]























