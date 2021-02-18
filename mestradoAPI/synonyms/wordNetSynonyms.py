# import spacy

# import nltk
# nltk.download('wordnet')
# nltk.download('omw')
from builtins import str

from nltk.corpus import wordnet

def retornaSimilaridade(palavra1, palavra2):
    word1 = wordnet.synsets(palavra1, lang='por')
    word2 = wordnet.synsets(palavra2, lang='por')
    print(str(word1) + "==" + str(len(word1)))
    print(str(word2) + "==" + str(len(word2)))

    print(len(word1) > 0)
    print(len(word2) > 0)

    if len(word1) > 0 and len(word2) > 0:
        syns1 = word1[0]
        syns2 = word2[0]
        print(str(syns1.name()) + ' - ' + str(syns2.name()) + ' = ', syns1.wup_similarity(syns2))
        return syns1.wup_similarity(syns2)
    return 0


# palavra = 'gato'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# syns = wordnet.synsets("comeu", lang='por')
# print('comeu', syns)
#
# palavra = 'rato'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# palavra = 'felino'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# syns = wordnet.synsets("come", lang='por')
# print('come', syns)
#
# palavra = 'roedor'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
#
# syn1 = 'cat.n.01'
# syn2 = 'mouse.n.01'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
# syn1 = 'cat.n.01'
# syn2 = 'felidae.n.01'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
# syn1 = 'mouse.n.01'
# syn2 = 'felidae.n.01'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
# syn1 = 'felidae.n.01'
# syn2 = 'rodent.n.01'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
# syn1 = 'mouse.n.01'
# syn2 = 'rodent.n.01'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
# palavra = 'cachorro'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# palavra = 'cão'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# syn1 = 'bitch.n.04'
# syn2 = 'canine.n.02'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
# palavra = 'problema'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# palavra = 'obstáculo'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# syn1 = 'difficulty.n.02'
# syn2 = 'frustration.n.02'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
#
#
# palavra = 'feliz'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# palavra = 'risonho'
# syns = wordnet.synsets(palavra, lang='por')
# print(palavra, syns)
# print(palavra + ' lemmas', syns[0].lemmas()[0])
# name = syns[0].name()
# print(palavra + ' lemmas name', name)
# print(palavra + ' lemmas palavras', wordnet.synset(name).lemma_names('por'))
#
# syn1 = 'beaming.s.01'
# syn2 = 'beaming.s.01'
# w1 = wordnet.synset(syn1)
# w2 = wordnet.synset(syn2)
# print(syn1 + ' - ' + syn2 + ' = ', w1.wup_similarity(w2))
#
#
#
# palavra = 'comeu'
# print(wordnet.synsets(palavra))

# a = wordnet.lemmas('carro', lang='por')
# print(wordnet.synsets('carro', lang='por', pos=wordnet.NOUN))
# print(a)
# print(wordnet.synset('car.n.01').lemma_names('por'))
# car = wordnet.synset('car.n.01').lemma_names('por')
# dog_lemma = wordnet.lemmas('cão', lang='por')
# print(dog_lemma)
# print(wordnet.synset('bitch.n.04').lemma_names('por'))
#
# nlp = spacy.load("pt_core_news_sm")
# tokens = nlp("carro automóvel bicicleta moto")
#
# for token in tokens:
#     for token2 in tokens:
#         print(token.text, token2.text, token.similarity(token2))