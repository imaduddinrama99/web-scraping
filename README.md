# Web Scraping Data Pekerjaan 

Project ini merupakan program Python untuk melakukan web scraping data pekerjaan dari website Real Python (Fake Jobs), kemudian menyimpannya ke dalam format JSON dan CSV. Selain itu, project ini dilengkapi dengan fitur CRUD (Create, Read, Update, Delete) untuk mengelola data.

---

## Sumber Data

Data diambil dari:
* https://realpython.github.io/fake-jobs/

---

## Teknologi yang Digunakan

* Python
* requests
* BeautifulSoup (bs4)
* pandas

---

## Cara Menjalankan

### 1. Install dependency

```
pip install requests beautifulsoup4 pandas
```

### 2. Jalankan scraping

```
python scraper.py
```

### 3. Jalankan CRUD

```
python crud.py
```

---

## Output

Program akan menghasilkan:

* data.json (format JSON)
* data.csv (format CSV)

Contoh data:

```
  {
  "id": 1,
  "title": "Senior Python Developer",
  "company": "Payne, Roberts and Davis",
  "location": "Stewartbury, AA",
  "date": "2021-04-08"
  },
```

---

## Fitur CRUD

* Menambahkan data pekerjaan
* Menampilkan data dalam bentuk tabel
* Mengubah data berdasarkan ID
* Menghapus data

---

## Catatan

* Data digunakan hanya untuk keperluan pembelajaran
* Website yang digunakan merupakan situs latihan scraping

---

## Author

*Nama: Muchammad Imaduddin Ramadhani

*MataKuliah: PENGEMBANGAN APLIKASI BERBASIS WEB
