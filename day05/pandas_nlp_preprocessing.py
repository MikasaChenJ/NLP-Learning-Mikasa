import pandas as pd
from day01.preprocess_utils import clean_text, tokenize


# 指定分隔符为制表符 \t
df = pd.read_csv("data/new_train.txt", sep='\t', header=None, names=['text', 'label'])

print(df.head())
print(df.info())

label_map = {'neg': 0, 'pos': 1}
df['label'] = df['label'].map(label_map)

df['clean_text'] = df['text'].apply(clean_text)

df[['label', 'clean_text']].to_csv('data/cleaned_train.csv', index=False)
