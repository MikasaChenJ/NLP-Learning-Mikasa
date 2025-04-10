# 📘 Day 5：NumPy + Pandas 数据处理实战 | Mikasa

本日目标：掌握 NumPy 和 Pandas 两大数据处理库，完成情感分类文本的读取、清洗与保存，构建干净数据源，为模型训练做好准备。

---

## ✅ 今日学习目标

### 🔢 NumPy 基础
- 掌握 ndarray 的创建与 reshape
- 理解 axis 的含义与广播机制
- 使用布尔索引与切片筛选数据
- 完成基础练习题（见 `numpy_exercise.py`）

### 🧾 Pandas 预处理
- 成功读取 `new_train.txt`（使用 `\t` 分隔）
- 使用 `map()` 将标签转换为数字（pos → 1, neg → 0）
- 应用自定义 `clean_text` 函数进行文本清洗
- 保存清洗结果为 `cleaned_train.csv`

---

## 🗂️ 项目结构概览

```
day05/
├── data/
│   ├── new_train.txt
│   └── cleaned_train.csv
├── numpy_exercise.py
├── pandas_intro.py
├── pandas_nlp_preprocessing.py
└── README.md
```

---

## 🚀 技术关键点记录

- `.map(dict)` 可以快速将字符串标签转换为数字
- `axis=0` 是对列操作，`axis=1` 是对行操作
- NumPy 广播机制可以处理不同维度数组相加
- Pandas `apply()` 可批量应用清洗函数
- 推荐使用 `.to_csv()` 保存中间结果便于调试

---

## 💭 今日感想


> 示例：今天搞懂了 axis 的本质和标签映射的作用，感觉数据“终于干净了”，很适合投喂给模型训练了！


