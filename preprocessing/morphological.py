from janome.tokenizer import Tokenizer
import pickle
import collections

t = Tokenizer()

with open('../books/wagahai_list.pickle', 'rb') as f:
    wagahai_list = pickle.load(f)


# 形態素分ける
words = []
for sentence in wagahai_list:
    # print(t.tokenize(sentence, wakati=True))
    words += t.tokenize(sentence, wakati=True)

c = collections.Counter(words)
print(c)
