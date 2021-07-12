from gensim.models import word2vec
import pickle


with open('../books/wagahai_words.pickle', mode='rb') as f:
    wagahai_words = pickle.load(f)

model = word2vec.Word2Vec(wagahai_words,
                vector_size=100,
                min_count=5,
                window=5,
                epochs=20,
                sg=0)

# 猫と人間を足した結果
model.wv.most_similar(positive=["猫", "人間"])
# 人間＋猫ー夢
model.wv.most_similar(positive=["猫", "人間"], negative=["夢"])
