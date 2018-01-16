from gensim.models import KeyedVectors
import pandas as pd
import tensorflow as tf

# from gensim.scripts.glove2word2vec import glove2word2vec
# glove_input_file = 'glove.6B.100d.txt'
# word2vec_output_file = 'glove.6B.100d.txt.word2vec'
# glove2word2vec(glove_input_file, word2vec_output_file)

df = pd.read_json('train_v1.1.json',lines=True)
dfnew=df[['answers','passages']].copy()
data_no=dfnew['passages'].count()
k=0
k=[]
data_list=[]
with open('ids.txt') as f:
	for line in f:
		j=line.split()
		k.append(int(j[0]))
		k.append(int(j[1]))
		data_list.append(k)
		k=[]

idloc = data_list
filename = 'glove.6B.100d.txt.word2vec'
model = KeyedVectors.load_word2vec_format(filename, binary=False)


concat1 = []
big_concat=[]
while(k < data_no):
    analysis = dfnew['passages'][k]
    no_of_passnow = len(dfnew['passages'][k])
    n_nop = 0
    pos_2 = 0
    while(n_nop < no_of_passnow):
        if (analysis[n_nop]['is_selected'] == 0):
            n_nop = n_nop + 1
        else:
            para = analysis[n_nop]['passage_text']
            npara = para.split()
            lpara = len(para.split())
            while (pos_2 < lpara):
                fsp = 0.0
                fep = 0.0
                if idloc[k][0] == pos_2:
                    fsp = 1.0
                if idloc[k][1] == pos_2:
                    fep = 1.0
                wordi = npara[pos_2]

                concat1.append(tf.concat([model[[wordi]], fsp, fep],2))
                concat1[pos_2]
                pos_2 = lpara
            big_concat.append(concat1)
            break
    k=k+1

