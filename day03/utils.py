import jieba


def top_k_words(text:str ,k:int=5):
    words=jieba.lcut(text)

    freq_dict={}
    for word in words:
        if word.strip():
            if word in freq_dict:
                freq_dict[word]+= 1
            else:
                freq_dict[word]=1
 # 3. 排序词频
    sorted_words = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # 4. 返回前 k 个
    return sorted_words[:k]



if __name__ == "__main__":
    text = "我真的真的很喜欢这部电影，剧情太棒了，真的推荐！"
    result = top_k_words(text, k=3)
    print("出现频率最高的词：", result)