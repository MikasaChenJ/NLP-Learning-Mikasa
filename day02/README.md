# 中文情感分类器 · Sentiment Classifier (TF-IDF + LR)

本项目是一个简易的中文情感分类模型，使用 jieba 进行中文分词，结合 TF-IDF 特征提取与逻辑回归模型（Logistic Regression）实现文本的情感分类（正面 / 负面）。

---

## 📁 项目结构

```
day02/
├── data/                        # 可扩展的中文语料库
├── model/
│   └── text_classifier.pkl      # 训练好的模型
├── tfidf_example.py             # TF-IDF 原理演示（中英支持）
├── train_classifier.py          # 模型训练脚本
├── test_classifier.py           # 模型测试脚本
└── README.md                    # 项目说明文档
```

---

## 🚀 快速开始

### 1️⃣ 安装依赖

```bash
pip install jieba scikit-learn joblib
```

### 2️⃣ 训练模型

```bash
python train_classifier.py
```

训练完成后，模型将保存为：

```
day02/model/text_classifier.pkl
```

### 3️⃣ 测试模型

```bash
python test_classifier.py
```

输出示例：

```
🔎 输入：我太喜欢这部电影了！
📌 预测结果：neg ❌（应为 pos）

🔎 输入：剧情太拖沓，看得我头疼
📌 预测结果：pos ❌（应为 neg）
```

---

## 💡 当前模型情况

| 项目                | 值                            |
|---------------------|-------------------------------|
| 模型类型            | TF-IDF + Logistic Regression  |
| 分词方法            | jieba 中文分词                |
| 训练样本数量        | 4 条（2 正面 + 2 负面）        |
| 当前准确率          | 约 50%（样本偏少，待改进）      |

---

## 🔧 待改进方向

- [ ] 增加训练样本数量，提高泛化能力
- [ ] 加入停用词过滤、ngram 组合特征
- [ ] 引入 Transformers / BERT 进行深度学习优化
- [ ] 封装 API 或制作 Web Demo 展示效果

---

## 📌 作者说明

此项目为 [Mikasa](https://github.com/MiaksaChenJ) NLP 算法工程师成长计划中的阶段性练习，项目持续迭代中。

欢迎 Star 🌟 & Fork 💻 一起学习进步！
