🛒 Amazon Product Scraper
A Python-based web scraper that extracts product information from Amazon's search results page using Selenium, BeautifulSoup, and OpenPyXL, and saves it to a well-formatted Excel file with hyperlinks.

📌 Features
Searches for laptops on Amazon

Extracts:

Product Name

Price

Rating (with star representation)

Number of Reviews

Availability Status

Product Link

Saves results in amazon_products_with_links.xlsx

Clickable product links

Neatly formatted columns

🔧 Requirements
Install the required packages using:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt
txt
Copy
Edit
beautifulsoup4
selenium
openpyxl
webdriver-manager
🚀 How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/amazon-product-scraper.git
cd amazon-product-scraper
Run the script

bash
Copy
Edit
python amazon_scraper.py
Output

Excel file saved as: amazon_products_with_links.xlsx


