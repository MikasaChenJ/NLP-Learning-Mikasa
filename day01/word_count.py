def count_words(text: str) -> dict:
    freq = {}  # 用来记录每个单词的频率
    words = text.lower().split()  # 转小写并按空格分词
    for word in words:
        word = word.strip(".,!?()[]'\"")  # 去掉两边的标点
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq

# 示例测试
if __name__ == "__main__":
    text = "I love NLP. I love Python. Python is powerful!"
    result = count_words(text)
    print("词频统计结果：")
    print(result)
