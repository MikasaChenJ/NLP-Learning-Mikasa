import random
import jieba

# 简单的同义词库（你可以手动扩展）
synonyms = {
    "喜欢": ["热爱", "喜爱", "偏爱"],
    "讨厌": ["厌恶", "不喜欢"],
    "电影": ["影片", "片子"],
    "剧情": ["情节", "故事"],
    "演员": ["表演者", "主角"],
    "无聊": ["枯燥", "乏味"]
}

# 常见插入词
inserts = ["真的", "非常", "特别", "有点", "超级"]

# 单句增强逻辑
def augment_text(text: str) -> str:
    words = jieba.lcut(text)
    new_words = words.copy()

    # 1. 同义词替换
    for i, word in enumerate(new_words):
        if word in synonyms and random.random() < 0.3:  # 30%概率替换
            new_words[i] = random.choice(synonyms[word])

    # 2. 随机插入词
    if random.random() < 0.5:
        insert_word = random.choice(inserts)
        insert_pos = random.randint(0, len(new_words))
        new_words.insert(insert_pos, insert_word)

    # 3. 随机删除
    if len(new_words) > 3 and random.random() < 0.3:
        del_pos = random.randint(0, len(new_words) - 1)
        new_words.pop(del_pos)

    return ''.join(new_words)


# 主程序：读原始数据，写增强数据
input_file = "data/new_train.txt"
output_file = "data/new_train_aug.txt"

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:

    for line in fin:
        line = line.strip()
        if '\t' in line:
            text, label = line.split('\t')

            fout.write(f"{text}\t{label}\n")  # 原始
            for _ in range(2):  # 生成两条增强
                new_text = augment_text(text)
                fout.write(f"{new_text}\t{label}\n")

print("✅ 数据增强完成，已生成 new_train_aug.txt")
