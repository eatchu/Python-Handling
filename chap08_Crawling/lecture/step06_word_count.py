
import pickle

# 1. pickle file load
file = open('./chap08_Crawling/data/new_crawling.pickle', mode='rb')
news_crawling = pickle.load(file) # list로 반환
print(type(news_crawling)) # list
print(news_crawling)


# 2. word 전처리

def clean_text(texts) :
    from re import sub
    # 1. 소문자 변경
    texts_re = [text.lower() for text in texts]

    # 2. 슷자 제거
    texts_re2 = [sub('\\d', '', text) for text in texts_re]

    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = [sub(punc_str, '', text) for text in texts_re2]

    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = [sub(spec_str, '', text) for text in texts_re3]

    # 5. 공백 제거
    texts_re5 = [sub('\s', ' ', text) for text in texts_re4]
    return texts_re5

clean_news = clean_text(news_crawling)
print(clean_news)


# 3. word count
word_count = {}
for texts in clean_news :
    for word in texts.split() :
        word_count[word] = word_count.get(word,0) + 1
print(word_count)

word_count2 = word_count.copy() # 객체 복제

# 4. 2음절 이상의 단어만 추출 (의미없는 단어 제거 목적)
for word in word_count.keys() :
    if len(word) < 2 :
        del word_count2[word]
print(word_count2)
print(len(word_count)) # 241
print(len(word_count2)) # 229

# 5. top10, tep5
'''
pip install collections-extended
'''

from collections import Counter

count = Counter(word_count2)
top5 = count.most_common(5)
print(top5) # [('none', 19), ('코로나', 4), ('[바로잡습니다]', 4), ('지급', 3), ('수출', 3)]

# 무의미한 단어 삭제
del count['none']
del count['[바로잡습니다]']
top10 = count.most_common(10)
print(top10) # [('코로나', 4), ('지급', 3), ('수출', 3), ('고용', 3), ('소득', 3),
             # ('기여도는', 3), ('만원', 3), ('이사장', 3), ('트럼프', 3), ('재난지원금', 2)]


# data frame 생성
import pandas as pd
top10_df = pd.DataFrame(top10, columns=['word','count'])
print(top10_df)

# 차트 생성
'''
pip install matplotlib
'''
# 차트 한글 지원 코드
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 패키지 호출
import matplotlib.pyplot as plt

# 선 그래프
plt.plot(top10_df['word'], top10_df['count']) # plt.plot(x축,y축)
plt.title('top10 word count')
plt.show()

# 막대 그래프
plt.bar(top10_df['word'], top10_df['count']) # plt.plot(x축,y축)
plt.title('top10 word count')
plt.show()





