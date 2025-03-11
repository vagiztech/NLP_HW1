import pandas as pd
import glob
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

all_files = glob.glob("CSVHouseMD/*.csv")
df_list = [pd.read_csv(f, encoding='utf-8', encoding_errors='replace') for f in all_files]
df = pd.concat(df_list, ignore_index=True)

house_lines = df[df['name'] == 'House'].copy()

nltk.download('punkt', force=True)
nltk.download('wordnet', force=True)
nltk.download('stopwords', force=True)
nltk.download('punkt_tab', force=True)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

house_lines['Dialogue_processed'] = house_lines['line'].apply(preprocess_text)

word_counts = Counter(' '.join(house_lines['Dialogue_processed']).split())

def remove_rare_words(text):
    return ' '.join([word for word in text.split() if word_counts[word] > 2])

house_lines['Dialogue_processed'] = house_lines['Dialogue_processed'].apply(remove_rare_words)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
tfidf_matrix = vectorizer.fit_transform(house_lines['Dialogue_processed'])

def find_best_reply(query_en: str) -> str:
    processed_query = preprocess_text(query_en)
    query_vec = vectorizer.transform([processed_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_index = similarities.argmax()
    best_reply_en = house_lines['line'].iloc[best_index]
    return best_reply_en