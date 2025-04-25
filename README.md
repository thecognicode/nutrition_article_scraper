# Nutrition Article Scraper

This is a Python script that scans news articles from popular websites, looking for information related to nutrition terms. It then visualizes the frequency of these terms using a bar chart.

## What it does
- Scrapes articles from two major news websites: BBC and The Guardian.
- Searches for a predefined list of nutrition-related terms.
- Extracts relevant sentences containing those terms.
- Visualizes the frequency of nutrition terms found in the articles.

## How It Works
1. The script visits the given URLs (BBC and The Guardian).
2. It collects article links from the main pages.
3. Then, it fetches the content of each article and looks for key terms related to nutrition, such as `protein`, `vitamin`, `fat`, etc.
4. If any of these terms are found in the article, the script extracts the sentence containing the term.
5. Finally, the script creates a bar chart showing how many times each term appears in the scraped articles.

## Tools used:
- Python 3.x
- Requests
- BeautifulSoup
- spaCy
- Matplotlib

## Installation
To run this project, you need to install the required libraries. You can do this by running:

pip install -r requirements.txt

requirements.txt should contain the following:
requests
beautifulsoup4
spacy
matplotlib

Additionally, you'll need to install the en_core_web_sm model for spaCy
To use the scraper, simply run your Python script

Output

The script will show a bar chart of the nutrition terms and save it as `nutrition_terms.png`.


