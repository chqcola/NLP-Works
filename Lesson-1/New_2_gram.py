import pandas as pd
filename = 'movie_comments.csv' #https://github.com/Computing-Intelligence/datasource/raw/master/movie_comments.csv
content = pd.read_csv(filename,encoding='utf-8',low_memory=False)
comment = content['comment'].tolist() #筛选
import re
def set(string):
    return re.findall('\w+',string) #清洗
comment_clean = [''.join(set(str(a)))for a in comment]
import codecs
with codecs.open('article.txt','w','utf-8') as f:
    for a in comment_clean:
        f.write(a + '\n')
import jieba
def cut(string):return list(jieba.cut(string))
SET=[]
for i,line in enumerate(open(('article.txt'),encoding='utf-8')):
    if i>100000:break
    SET += cut(line) #切词
from collections import Counter
words_count = Counter(SET)
def prob_1(word):
    return words_count[word]/len(SET)
SET_2_GRAM = [''.join(SET[i:i+2]) for i in range(len(SET[:-2]))]
words_count_2 = Counter(SET_2_GRAM)
def prob_2(word1,word2):
    if word1+word2 in words_count_2:
        return words_count_2[word1+word2] / len(SET_2_GRAM)
    else:
        return 1 / len(SET_2_GRAM)
def get_probablity(sentence):
    words = cut(sentence)
    sentence_pro = 1
    for i, word in enumerate(words[:-1]):
        next_ = words[i+1]
        probability = prob_2(word,next_)
        sentence_pro *= probability
    return sentence_pro
if __name__ == '__main__':
    print(get_probablity('我很喜欢你的故事'))
    print(get_probablity('我很喜欢你的谎言'))