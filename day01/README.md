# 📘 Day 01 2025.4.1 - 文本预处理模块 & 词频统计器

## ✅ 今日完成任务

- [x] 编写文本预处理模块（`preprocess_utils.py`）
  - clean_text(): 小写化 + 去标点
  - tokenize(): 使用 nltk 分词
  - remove_stopwords(): 去英文停用词
- [x] 编写测试脚本（`test_preprocess.py`）并成功运行
- [x] 编写词频统计器（`word_count.py`）
- [x] 完成学习总结 README 文档
- [x] 成功提交 GitHub 🎉

---

## 🧠 模块说明

### `preprocess_utils.py`
> 封装了英文文本预处理常用函数，可在未来项目中直接复用：

```python
clean_text(text) -> str
tokenize(text) -> list[str]
remove_stopwords(tokens) -> list[str]
