
from party_wise_results import extract_party_results
from candidate_wise_results import extract_winners_details

url_main = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
url_base = "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-"

party_results = extract_party_results(url_main)
if party_results:
    while True:
        selected_index = input("Enter the index to display its link number (or 'exit' to exit): ")
        if selected_index.lower() == 'exit':
            break
        try:
            selected_index = int(selected_index)
            if 1 <= selected_index <= len(party_results):
                link_id = party_results[selected_index - 1][4]
                url_detail = f"{url_base}{link_id}.htm"
                extract_winners_details(url_detail)
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index number.")