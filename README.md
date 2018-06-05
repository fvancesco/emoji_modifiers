## How Gender and Skin Tone Modifiers Affect Emoji Semantics in Twitter 
#### Francesco Barbieri and Jose Camacho Collados

The following repository includes the pre-trained embeddings from the paper *How Gender and Skin Tone Modifiers Affect Emoji Semantics in Twitter*  (*SEM 2018).

### Use our embeddings

We release the two sets of 100-dimensional SW2V embeddings trained on Twitter:

1. Word, base emoji and modifier embeddings.
 The vocabulary includes words (e.g. house, car, ...), base emojis (without sex or skin tone modifiers, e.g. 👍), and Modifiers (e.g. male/female, or light/dark skin tone). Download embeddings here: COMING SOON [~300 MB]

2. Word and emoji (base and modified) embeddings.
The vocabulary includes words (e.g. house, car, ...) and emojis, both base (without sex or skin tone modifiers, e.g. 👍), and with modifiers (e.g.  👍🏻,👍🏽,👍🏿). Download embeddings here: COMING SOON [~300 MB]

Notes:
- All words are lowercased.
- For obtaining the original emoji and modifier encoding from the embeddings, you can use the following mapping (COMING SOON).

### Train New Embeddings

We used the original SW2V code for training the embeddings: http://lcl.uniroma1.it/sw2v/ . We used the SW2V code with the following parameters, run from the terminal as follows:

Word, base emoji and modifier embeddings (1): 
```bash
TH=1 #threads
INPUT="tweets.txt"
OUTPUT="word_emoji_embedding_s0.bin"
sw2v -train $INPUT -output $OUTPUT -cbow 1 -size 100 -window 6 -negative 0 -hs 1 -threads $TH -binary 1 -iter 5 -update 0 -senses 0 -synsets_input 1 -synsets_target 1
```

Word and emoji (base and modified) embeddings.
```bash
TH=1 #threads
INPUT="tweets.txt"
OUTPUT="word_emoji_embedding_s1.bin"
sw2v -train $INPUT -output $OUTPUT -cbow 1 -size 100 -window 6 -negative 0 -hs 1 -threads $TH -binary 1 -iter 5 -update 0 -senses 1 -synsets_input 1 -synsets_target 1
```

#### Coming soon:
- [ ] Links to embeddings (by the end of this week)
- [ ] Code for raw dataset filtering prior training
 
For more information please check the main reference paper: http://aclweb.org/anthology/S18-2011

If you use any of the resources from this page, please cite the reference paper:
```bash
@InProceedings{barbieri:sem2018,
  author = 	"Barbieri, Francesco
		and Camacho-Collados, Jose",
  title = 	"How Gender and Skin Tone Modifiers Affect Emoji Semantics in Twitter",
  booktitle = 	"Proceedings of the Seventh Joint Conference on Lexical and Computational Semantics",
  year = 	"2018",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"101--106",
  location = 	"New Orleans, Louisiana",
  url = 	"http://aclweb.org/anthology/S18-2011"
}

```
