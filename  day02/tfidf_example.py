import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

# 示例中文句子（你可以改成任何你想练的）
docs = [
    "我喜欢自然语言处理",
    "自然语言处理是人工智能的重要方向",
    "我非常喜欢学习人工智能"
]

# 用 jieba 对每句话进行分词，并空格连接（TF-IDF 按空格划词）
seg_docs = [' '.join(jieba.lcut(doc)) for doc in docs]


# 初始化向量器并拟合
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(seg_docs)

# 打印词表
print("词表：", vectorizer.get_feature_names_out())

# 打印稠密向量矩阵
print("TF-IDF矩阵：")
print(X.toarray())
