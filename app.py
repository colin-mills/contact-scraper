#Scrape for emails and phones

from contactscraper.controller import Controller

instance = Controller(starting_urls=['https://alteritytherapeutics.com'], 
                       scrape_numbers=False,
                       scrape_emails=True,
                       region="US",
                       max_results=5)

instance.scrape()






#Print Results

import json

with open('output.json', 'r') as raw_output:
    data = raw_output.read()
    output = json.loads(data)

print(json.dumps(output, indent=2))
