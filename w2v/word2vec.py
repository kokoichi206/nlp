from gensim.models import word2vec
import pickle


with open('../books/wagahai_words.pickle', mode='rb') as f:
    wagahai_words = pickle.load(f)

# size: 中間層のニューロン数
# min_count: この値以下の出現回数の単語を無視
# window: 対象単語を中心とした前後の単語数
# sg: skip-gramを使うかどうか、0:CBOW, 1:skip-gram
model = word2vec.Word2Vec(wagahai_words,
                vector_size=100,
                min_count=5,
                window=5,
                epochs=20,
                sg=0)

print(model.wv.vectors.shape)

# 類似度の高い単語
print(model.wv.most_similar("猫"))
# コサイン類似度での計算を行なっている
import numpy as np
a = model.wv.__getitem__("猫")
b = model.wv.__getitem__("人間")
cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cos_sim)
