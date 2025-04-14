import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import spacy
import matplotlib.pyplot as plt
from collections import Counter


nlp = spacy.load("en_core_web_sm")


urls = [
    'https://www.bbc.com/news/technology',
    'https://www.theguardian.com/technology',
]


terms = [
    'protein', 'vitamin', 'fat', 'carbohydrate', 'fiber', 'nutrient', 'energy', 'mineral',
    'calcium', 'iron', 'zinc', 'magnesium', 'potassium', 'sodium', 'omega-3',
    'amino acid', 'antioxidant', 'dietary supplement', 'metabolism', 'micronutrient',
    'macronutrient', 'healthy diet', 'nutritional value', 'food intake', 'energy intake'
]



def get_article_links(base_url):
    try:
        soup = BeautifulSoup(requests.get(base_url).content, 'html.parser')
        return [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True)]
    except:
        return []

def extract_text(url):
    try:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        return ' '.join([p.get_text() for p in soup.find_all('p')])
    except:
        return ""

results = []


for site in urls:
    print(f"\n Сканируем: {site}")
    for link in get_article_links(site):
        text = extract_text(link)
        if any(term in text.lower() for term in terms):
            doc = nlp(text)
            for sent in doc.sents:
                if any(term in sent.text.lower() for term in terms):
                    results.append((link, sent.text.strip()))
                    break  


for link, sentence in results:
    print(f"\n {link}\n {sentence}")

all_text = ' '.join([sent for _, sent in results]).lower()
word_counts = Counter(word for word in all_text.split() if word in terms)


if word_counts:
    plt.figure(figsize=(10, 5))
    plt.bar(word_counts.keys(), word_counts.values(), color='skyblue')
    plt.title('Частота ключевых слов по питанию')
    plt.ylabel('Количество')
    plt.xlabel('Слова')
    plt.tight_layout()
    plt.savefig('nutrition_terms.png')
    plt.show()
else:
    print("\n Ничего не найдено для визуализации.")
