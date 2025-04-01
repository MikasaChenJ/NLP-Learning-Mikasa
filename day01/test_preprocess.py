from preprocess_utils import clean_text, tokenize, remove_stopwords

text = "Natural Language Processing is powerful, isn't it?"

cleaned = clean_text(text)
tokens = tokenize(cleaned)
filtered = remove_stopwords(tokens)

print("原始文本：", text)
print("清洗后：", cleaned)
print("分词结果：", tokens)
print("去停用词后：", filtered)
