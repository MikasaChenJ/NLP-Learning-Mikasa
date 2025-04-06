
# 1. 加载模型
import jieba
import joblib

model = joblib.load('model/text_classifier.pkl')

# 2. 准备要预测的中文句子
test_sentences = [
    "这电影真难看，我不喜欢",
    "剧情太拖沓，看得我头疼",
    "演员演得很好，剧情也不错",
    "我真的不推荐这部电影，又慢又无聊"
]

# 3. 分词 + 拼接（注意：必须和训练时一致）
seg_sentences = [' '.join(jieba.lcut(sent)) for sent in test_sentences]

# 4. 模型预测
predictions = model.predict(seg_sentences)

# 5. 输出结果
for sent, label in zip(test_sentences, predictions):
    print(f"🔎 输入：{sent}")
    print(f"📌 预测结果：{label}")
    print('-' * 30)