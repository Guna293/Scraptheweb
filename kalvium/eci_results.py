
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def extract_parliamentary_constituencies(soup):
    main_content = soup.find('main', class_='inner-content')
    if not main_content:
        return None
    pc_section = main_content.find('div', class_='pc-wrap')
    if not pc_section:
        return None
    return pc_section.find('h1').text.strip()

def extract_assembly_constituencies(soup):
    main_content = soup.find('main', class_='inner-content')
    if not main_content:
        return []

    counts = []
    state_sections = main_content.find_all('div', class_='state-item')
    for section in state_sections:
        state_name = ' '.join(section.find('h2').text.split())
        constituency_count = section.find('h1').text.strip()
        counts.append((state_name, constituency_count))

    buttons = main_content.find_all('a', class_='btn-big')
    for button in buttons:
        state_name = button.text.strip()
        counts.append((state_name, None))
    
    return counts

def print_results(parliamentary_constituencies, assembly_constituencies):
    if parliamentary_constituencies:
        print(f"Parliamentary Constituencies: {parliamentary_constituencies}")

    print("\nAssembly Constituencies:")
    for state, count in assembly_constituencies:
        print(f"{state}: {count if count else 'No count provided'}")

def scrap():
    url = "https://results.eci.gov.in/"
    soup = fetch_page_content(url)

    parliamentary_constituencies = extract_parliamentary_constituencies(soup)
    assembly_constituencies = extract_assembly_constituencies(soup)

    print_results(parliamentary_constituencies, assembly_constituencies)

if _name_ == "_main_":
    scrap()
