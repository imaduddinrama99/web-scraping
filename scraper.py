import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    if not jobs:
        print("Data tidak ditemukan")
        exit()

    data = []
    id_counter = 1

    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        date = job.find("time").text.strip()

        data.append({
            "id": id_counter,
            "title": title,
            "company": company,
            "location": location,
            "date": date
        })

        id_counter += 1

    # JSON
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # CSV
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)

    print(f"Data berhasil disimpan! Total: {len(data)}")

else:
    print("Gagal mengambil data")