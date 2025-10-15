"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Tomáš Kulhánek
email: kulhanek.hk@seznam.cz

"""

import sys
import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def server_response(url: str) -> BeautifulSoup:
    """Sends a GET request to the specified URL and returns a BeautifulSoup object."""
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def get_town_links(region_url):
    """Gets links to individual municipalities from a given territorial unit."""
    soup = server_response(region_url)
    town_links = []

    tables = soup.select("table")  
    for table in tables:
        for row in table.select('tr'):
            code = row.select_one('td:first-child a')
            name = row.select_one('td:nth-child(2)')
            if code and name:
                full_link = urljoin(region_url, code['href'])  
                town_links.append((code.text.strip(), name.text.strip(), full_link))

    if not town_links:
        print("Error: No territorial unit found! Check the entered URL.")
        sys.exit(1)

    print(f"Loaded {len(town_links)} municipalities.")  
    return town_links

def scrape_town_data(town_url):
    """Gets election data for a specific municipality."""
    soup = server_response(town_url)

    def get_value(headers_id):
        """Helper function for extracting value from cell based on headers attribute."""
        cell = soup.find("td", {"headers": headers_id})
        return cell.text.strip().replace("\xa0", "") if cell else "0"

    voters = get_value("sa2")  
    envelopes = get_value("sa3")  
    valid_votes = get_value("sa6")  

    parties = [p.text.strip() for p in soup.select("td.overflow_name")]

    votes_raw = soup.select("td.cislo[headers*=sa2][headers*=sb3]")  
    votes = [int(v.text.strip().replace("\xa0", "").replace(" ", "").replace(",", "")) for v in votes_raw]

    if len(parties) != len(votes):
        print(f"Error: Number of political parties ({len(parties)}) and the number of votes ({len(votes)}) doesn't match!")
        sys.exit(1)

    party_votes = dict(zip(parties, votes))
    return voters, envelopes, valid_votes, party_votes

def save_to_csv(filename, data, parties):
    """Saves data to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        headers = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy'] + parties
        writer.writerow(headers)

        for row in data:
            writer.writerow(row)

    print(f"Results saved to {filename}")

def main():
    if len(sys.argv) != 3:
        print("Use: python main.py <territorial_unit_url> <output_file.csv>")
        sys.exit(1)

    region_url = sys.argv[1]
    output_file = sys.argv[2]

    try:
        towns = get_town_links(region_url)
        all_data = []
        all_parties = set()
        town_data = {}

        for code, name, link in towns:
            voters, envelopes, valid_votes, party_votes = scrape_town_data(link)
            all_parties.update(party_votes.keys())
            town_data[code] = [code, name, voters, envelopes, valid_votes, party_votes]

        sorted_parties = list(next(iter(town_data.values()))[5].keys())  
        for code, (code, name, voters, envelopes, valid_votes, party_votes) in town_data.items():
            row = [code, name, voters, envelopes, valid_votes] + [party_votes.get(party, '0') for party in sorted_parties]
            all_data.append(row)

        save_to_csv(output_file, all_data, sorted_parties)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()