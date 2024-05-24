# Turkish Word Extractor

**Description:**

TurkishWordExtractor is a Python program designed to scrape and extract Turkish words from Wiktionary. The program systematically accesses the Wiktionary word lists for each letter and collects words of specified lengths, from 3 to 9 letters. It then saves these words into separate text files based on their length. This tool is useful for linguists, language enthusiasts, and developers creating word games or language learning applications.

## Features

- Scrapes Turkish words from Wiktionary for each letter of the alphabet.
- Filters words by length, specifically extracting words with 3, 4, 5, 6, 7, 8, and 9 letters.
- Saves the extracted words into separate text files based on their length.
- Utilizes BeautifulSoup and requests libraries for web scraping.
- Ensures only lowercase words are included in the lists.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/affanatmaca/turkish-word-extractor.git
   
2. Navigate to the project directory:
   ```bash
   cd turkish-word-extractor

3. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4

## If you want extracted files

1. Extracted file links:
   Clean words (without swears) : https://github.com/affanatmaca/turkish-clean-words
   
   Turkish words : https://github.com/affanatmaca/turkish-words
