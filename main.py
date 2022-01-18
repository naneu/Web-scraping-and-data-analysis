import csv
import requests
from bs4 import BeautifulSoup

page = 1

while page <= 34:
    base_url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{}".format(page)
    response = requests.get(base_url)
    website_html = response.text

    soup = BeautifulSoup(website_html, "html.parser")
    with open('payscale_data_2.csv', 'a') as f:
        writer = csv.writer(f)

        for tr in soup.find_all('tr')[1:]:
            span = tr.find_all('span', class_='data-table__value')
            data = [i.text.replace('\n', '') for i in span]
            writer.writerow(data)

    page += 1
