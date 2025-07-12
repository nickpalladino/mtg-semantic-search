import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://mtg.fandom.com/wiki/List_of_Magic_slang"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

slang_terms_list = []
content_div = soup.find('div', class_='mw-parser-output')

if content_div:
    for h4 in content_div.find_all('h4'):
        term_span = h4.find('span', class_='mw-headline')
        if not term_span:
            continue
        term = term_span.get_text(strip=True)

        definition_parts = []
        for sibling in h4.find_next_siblings():
            if sibling.name in ['h3', 'h4']:
                break
            if sibling.name in ['p', 'ul']:
                definition_parts.append(sibling.get_text(separator=' ', strip=True))
        
        if term and definition_parts:
            full_definition = " ".join(definition_parts)
            # Remove citations like [1], [2], etc.
            full_definition = re.sub(r'\s*\[[^\]]*\]', '', full_definition)
            # Remove extra spaces before punctuation
            full_definition = re.sub(r'\s+([,.!?;:])', r'\1', full_definition)
            # Normalize all whitespace to single spaces
            full_definition = re.sub(r'\s+', ' ', full_definition).strip()
            
            # Append to the list as an object with desired key order
            slang_terms_list.append({'term': term, 'description': full_definition})

with open("mtg_slang_fandom.json", "w") as f:
    json.dump(slang_terms_list, f, indent=4)

print(f"Scraping complete. Found {len(slang_terms_list)} terms. Slang terms saved to mtg_slang.json")