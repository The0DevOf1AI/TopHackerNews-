# TopHackerNews Scraper

This is a simple Python script that scrapes and ranks popular posts from [Hacker News](https://news.ycombinator.com/) using `requests` and `BeautifulSoup`.

It fetches the top 2 pages, filters posts with more than 99 points, and sorts them by vote count in descending order.

---

## 📌 Features

- Fetches data from multiple pages
- Parses and filters posts with high votes
- Ranks stories by score
- Uses BeautifulSoup for HTML parsing

---

## 🛠 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install requirements:

```bash
pip install requests beautifulsoup4
