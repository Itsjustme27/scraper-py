import csv
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

filename = "fake_jobs.csv"

job_boxes = soup.find_all('div', class_='card')
jobs = []
for box in job_boxes:
    job = {
        'title': box.h2.text.strip(),
        'company': box.h3.text.strip(),
        'location': box.find('p', class_='location').text.strip(),
        'link': box.find('a', string='Apply')['href']
    }
    jobs.append(job)

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'company', 'location', 'link'])
    writer.writeheader()
    for job in jobs:
        writer.writerow(job)


#for j in jobs[:5]: # print only 5 for brevity
#    print(j)



# print(soup.prettify())
