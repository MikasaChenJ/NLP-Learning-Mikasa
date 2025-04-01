import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# 第一次用nltk需要下载两个词库（只需要一次）
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def clean_text(text: str) -> str:
    # 小写化 + 去标点
    return re.sub(r'[^\w\s]', '', text.lower())

def tokenize(text: str) -> list[str]:
    return word_tokenize(text)

def remove_stopwords(tokens: list[str]) -> list[str]:
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word.lower() not in stop_words]
