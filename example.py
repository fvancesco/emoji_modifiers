'''
Emojis are represented in the vocab as:
- emo:00000001, ..., emo:00001339 (see mapping.tsv)
while the modifiers as:
- mod:00000000, mod:00000001, mod:00000002, ..., mod:00000006
where the first 5 are skin tone modifiers from lighest to darkest, 
and the last two (5,6) are male and female

When we set senses=0 in sw2v we learn for emoji "emo0x:mod0x"
1) "emo0x" 
2) "mod0x"

When we set senses=1 in sw2v we learn for emoji "emo0x:mod0x"
1) "emo0x" 
2) "emo0x:mod0x"
'''

from gensim.models.keyedvectors import KeyedVectors
import re

def conv_sw2v_to_emo(s, base=True):
	new_s = s
	if s.startswith("mod:000"):
		new_s = modifiers_keys[int(s[-1])]
	elif s.startswith("emo:000"):
		if base:
			new_s = sw2v_base_to_emo[s]
		else:
			new_s = sw2v_to_emo[s]
	return new_s

def print_nn(nn, base=True):
	to_print = []
	for w,_ in nn:
		to_print.append(conv_sw2v_to_emo(w, base=base))
	print(" ".join(to_print))
		
def print_emo_nn(target, nn, topn=10, base=True):
	to_print = []
	printed = 0
	for w,_ in nn:
		if w.startswith("emo:000"):
			to_print.append(conv_sw2v_to_emo(w, base=base))
			printed+=1
		if printed > topn:
			break
	print(target,": ", " ".join(to_print))

modifiers_keys = ['🏻','🏼','🏽','🏾','🏿', '♂️', '♀️']

model_path_s0 = "word_emoji_embedding_s0.bin"
model_path_s1 = "word_emoji_embedding_s1.bin"
m0 = KeyedVectors.load_word2vec_format(model_path_s0, binary=True)
m1 = KeyedVectors.load_word2vec_format(model_path_s1, binary=True)

path_to_mapping = "mapping.tsv"
sw2v_to_emo, sw2v_base_to_emo = {}, {}
emo_to_sw2v, emo_to_sw2v_base = {}, {}
for l in open(path_to_mapping).read().split("\n"):  
    t = l.split("\t")
    sw2v_to_emo[t[3]] = t[1]
    emo_to_sw2v[t[1]] = t[3]
    emo_base = re.sub('['+ "".join(modifiers_keys) +']', '', t[1])
    sw2v_base_to_emo[t[4]] = emo_base
    emo_to_sw2v_base[emo_base] = t[4]

topn = 100

# -------- s0 --------
print("\n --- s0 examples --- \n")

#example of base emoji
nn = m0.most_similar(positive=emo_to_sw2v["👍"], topn=topn)
print_emo_nn("👍", nn)

#lightest modifier
nn = m0.most_similar(positive="mod:00000000", topn=topn)
print_emo_nn('🏻', nn)

#darkest modifier
nn = m0.most_similar(positive="mod:00000004", topn=topn)
print_emo_nn('🏿', nn)

#male modifier
nn = m0.most_similar(positive="mod:00000005", topn=topn)
print_emo_nn('♂️', nn)

#female modifier
nn = m0.most_similar(positive="mod:00000006", topn=topn)
print_emo_nn('♀️', nn)

# -------- s1 --------
print("\n --- s1 examples --- \n")

nn = m1.most_similar(positive=emo_to_sw2v["👍"], topn=topn)
print_emo_nn("👍", nn, base=False)

nn = m1.most_similar(positive=emo_to_sw2v["👍🏿"], topn=topn)
print_emo_nn("👍🏿", nn, base=False)

nn = m1.most_similar(positive=emo_to_sw2v["👍🏻"], topn=topn)
print_emo_nn("👍🏻", nn, base=False)

