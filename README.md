# 🛒 Amazon Product Scraper

A Python-based web scraper that extracts product information from Amazon's search results page using **Selenium**, **BeautifulSoup**, and **OpenPyXL**, and saves it to a well-formatted Excel file with hyperlinks.

---

## 📌 Features

- Searches for **laptops** on Amazon
- Extracts:
  - Product Name
  - Price
  - Rating (with star representation)
  - Number of Reviews
  - Availability Status
  - Product Link
- Saves results in `amazon_products_with_links.xlsx`
  - Clickable product links
  - Neatly formatted columns

---

## 🔧 Requirements

Install the required packages using:

```bash
pip install -r requirements.txt

