# Day 3：中文情感分类器（TF-IDF + LR）& 数据结构练习

本日任务目标是：完成一个基于 TF-IDF 特征 + 逻辑回归分类器的中文情感分类模型，并配套实现文本预处理、模型保存、预测、数据结构练习等工程化组件。

---

## 📌 今日内容总览

- ✅ 使用 `jieba` 对中文文本进行分词
- ✅ 构建 `TfidfVectorizer` 提取文本特征（支持 ngram）
- ✅ 使用 `LogisticRegression` 模型进行训练
- ✅ 保存模型至 `.pkl` 文件，供后续测试调用
- ✅ 编写 `test_classifier.py` 支持用户输入实时预测
- ✅ 纯 Python 实现词频统计器（dict + sorted + lambda）
- ✅ 掌握 Python 中 `for` 遍历、`lambda` 匿名函数、切片、all() 等基础技能

---

## 📁 项目结构说明

day03/
├── data/
│   └── new_train.txt         # 训练数据（每行：句子	标签）
├── model/
│   └── text_classifier.pkl   # 保存的 TF-IDF + LR 模型
├── train_classifier.py       # 训练脚本，生成模型
├── test_classifier.py        # 测试脚本，输入句子预测情感
├── utils.py                  # 词频统计器 & lambda 测试函数
└── README.md

---

## 🧪 示例句子预测

🔎 输入：这电影太棒了，我太喜欢了！
📌 预测结果：pos
------------------------------
🔎 输入：剧情太拖沓，看得我头疼
📌 预测结果：neg

---

## 🧠 今日掌握技能总结

- 🔤 中文分词：`jieba.lcut(text)`
- 🧠 TF-IDF 特征提取：`TfidfVectorizer(stop_words, ngram_range)`
- 📈 训练模型：`LogisticRegression()`
- 💾 模型保存：`joblib.dump(model, 'xxx.pkl')`
- 📊 模型预测：`model.predict(...)`
- 🧮 词频统计练习：`dict`、`sorted`、`lambda`
- ✅ Python 逻辑函数：`all()`、`any()`
- 🔁 灵活遍历：支持字符串、列表、集合、字典的遍历方式

---

## 🎯 Mikasa 今日成就解锁

- ✅ 从 0 构建了 TF-IDF + 逻辑回归的中文情感模型
- ✅ 学会模型保存 / 加载与交互式预测
- ✅ 理解了词频排序、lambda 排序逻辑
- ✅ 初步具备工程型项目结构与组织能力
- ✅ 已提交 day03 项目至 GitHub 准备发布



