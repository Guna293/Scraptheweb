
from utils import fetch_soup
from tabulate import tabulate

def extract_winners_details(url):
    soup = fetch_soup(url)
    if soup is None:
        return None

    try:
        winning_candidate = soup.find('h2').text.strip()
        table = soup.find('table', class_='table')
        rows = table.find_all('tr')

        extracted_data = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 5:
                s_no = columns[0].text.strip()
                constituency = columns[1].text.strip()
                candidate_name = columns[2].text.strip()
                total_votes = columns[3].text.strip()
                margin = columns[4].text.strip()

                extracted_data.append([s_no, constituency, candidate_name, total_votes, margin])

        headers = ["S.No", "Parliament Constituency", "Winning Candidate", "Total Votes", "Margin"]
        print(f"Winning Candidate: {winning_candidate}")
        print(tabulate(extracted_data, headers=headers, tablefmt="pretty"))

    except Exception as e:
        print(f"Error while extracting winner details: {str(e)}")
        return None