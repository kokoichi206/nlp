import re
import pickle


with open("../books/wagahaiwa_nekodearu.txt", mode="r", encoding="utf-8") as f:
    wagahai_original = f.read()
print(wagahai_original)

wagahai = re.sub("《[^》]+》", "", wagahai_original)
wagahai = re.sub("［[^］]+］", "", wagahai)
wagahai = re.sub("[｜　「」\n]", "", wagahai)

separator = "。"
wagahai_list = wagahai.split(separator)
wagahai_list.pop()
wagahai_list = [x+separator for x in wagahai_list]

with open('../books/wagahai_list.pickle', mode='wb') as f:
    pickle.dump(wagahai_list, f)

