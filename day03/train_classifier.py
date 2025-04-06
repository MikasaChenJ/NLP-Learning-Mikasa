import jieba
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

texts=[]
labels=[]
stop_words=["我", "的", "了", "是", "也", "很", "太", "这", "那", "就", "都"]

with open('data/new_train.txt','r',encoding='utf-8') as f:
    for line in f:
        line=line.strip()
        parts=line.split('\t')
        if(len(parts)==2):
            # 1️⃣ 先用 jieba 分词
            seg = " ".join(jieba.lcut(parts[0]))  # 用空格拼接
            texts.append(seg)
            labels.append((parts[1]))
print('文本样本：',texts)
print('样本标签：',labels)

model = Pipeline([
    ('tfidf', TfidfVectorizer(
        stop_words=stop_words,
        ngram_range=(1, 4)
    )),
    ('clf', LogisticRegression())
])

model.fit(texts, labels)

# 保存模型
if joblib.dump(model, "model/text_classifier.pkl"):
    print("✅ 模型训练并保存成功！")

