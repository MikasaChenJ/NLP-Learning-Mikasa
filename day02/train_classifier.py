import jieba
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 简单的中文句子和标签
texts = [
    "这部电影很好看，我很喜欢！",     # 正面
    "剧情精彩，演员演技很棒",         # 正面
    "这部电影太差劲了",             # 负面
    "我不喜欢这部电影，很失望",       # 负面
]

labels = ['pos', 'pos', 'neg', 'neg']  # 对应情感标签

# 中文分词预处理
seg_texts = [' '.join(jieba.lcut(text)) for text in texts]

# 用 Pipeline 构造向量器 + 分类器一体化模型
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# 模型训练
model.fit(seg_texts, labels)

# 保存模型到 model/ 目录
joblib.dump(model, 'model/text_classifier.pkl')

print("✅ 模型训练完成并已保存")
