import jieba
import joblib
from sklearn.metrics import accuracy_score

model=joblib.load('model/text_classifier.pkl')

texts=[]
labels=[]

with open("data/val.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if '\t' in line:
            parts = line.split('\t')
            texts.append(parts[0])
            labels.append(parts[1])
seg_texts = [' '.join(jieba.lcut(text)) for text in texts]
preds = model.predict(seg_texts)
acc = accuracy_score(labels, preds)
print(acc)
print("\n❌ 错误样本示例：")
wrong = 0
for text, label, pred in zip(texts, labels, preds):
    if label != pred:
        print(f"原始：{text}\n标签：{label}，预测：{pred}")
        print("-" * 30)
        wrong += 1
    if wrong >= 5:
        break
print(f"预测结果样本（前10）：{preds[:10]}")
print(f"真实标签样本（前10）：{labels[:10]}")


