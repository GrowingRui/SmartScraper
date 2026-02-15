# SmartScraper: Distributed Dynamic Scraper with Chrome Extension Integration

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Framework-Scrapy-green.svg)](https://scrapy.org/)
[![Selenium](https://img.shields.io/badge/Automation-Selenium-red.svg)](https://www.selenium.dev/)
[![Flask](https://img.shields.io/badge/API-Flask-black.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-important.svg)](https://opensource.org/licenses/MIT)

**SmartScraper** is a high-performance distributed web scraping system that bridges manual browsing with automated data extraction.

By combining a **Chrome Extension trigger**, a **Flask API gateway**, and a **Scrapy + Selenium engine**, it delivers a seamless:

> 🔎 **"What You See Is What You Scrape"** experience.

---

## ✨ Key Features

- 🎯 **One-Click Scraping**  
  Trigger scraping directly from your active browser tab using a custom Chrome Extension.

- ⚡ **Dynamic JavaScript Rendering**  
  Fully supports AJAX, infinite scroll, and JS-heavy websites via Selenium automation.

- 🔄 **Auto Pagination Detection**  
  Automatically detects and clicks "Next Page" buttons recursively.

- 🛠️ **Zero Manual Driver Setup**  
  Uses `webdriver-manager` to auto-download and match the correct ChromeDriver version.

- 📊 **Structured JSON Output**  
  Generates clean, formatted `result.json` ready for analytics or ML pipelines.

- 🧩 **Modular Architecture**  
  Clear separation between frontend trigger, middleware API, and scraping engine.

---

## 🏗️ System Architecture

The system operates across three independent layers:

### 1️⃣ Chrome Extension (Frontend Trigger)
- Captures the active tab URL
- Sends a POST request to the local Flask API
- Provides a simple UI for one-click scraping

### 2️⃣ Flask API (Middleware Gateway)
- Receives scraping tasks
- Launches Scrapy spiders as subprocesses
- Acts as the bridge between browser and crawler

### 3️⃣ Scrapy + Selenium Engine (Core Scraper)
- Controls real browser via Selenium
- Extracts dynamic content
- Handles pagination logic
- Saves structured output to JSON

---

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SmartScraper.git
cd SmartScraper
```

### 2. Install Dependencies

Make sure you are using **Python 3.8+**

```bash
pip install -r requirements.txt
```

### 3. Start the Backend API

From the project root:

```bash
python app.py
```

If successful, you should see:

```
Running on http://127.0.0.1:5000
```

### 4. Load the Chrome Extension

1. Open Chrome
2. Navigate to:

```
chrome://extensions/
```

3. Enable **Developer Mode**
4. Click **Load unpacked**
5. Select the `chrome_extension` folder inside this project

The **Smart Scraper** icon will appear in your toolbar.

### 5. Run Your First Scrape

1. Open a target listing page (e.g., products, movies, listings)
2. Click the **Smart Scraper** extension icon
3. Click **Start Scraping**
4. Wait until console shows:

```
Spider closed
```

5. Check your output:

```
scrapy_app/result.json
```

---

## 📂 Project Structure

```
SmartScraper/
│
├── app.py                     # Flask API Gateway
├── requirements.txt           # Python dependencies
├── README.md
│
├── chrome_extension/          # Chrome Extension (Manifest V3)
│   ├── manifest.json
│   ├── popup.html
│   └── popup.js
│
└── scrapy_app/                # Scrapy project
    ├── scrapy.cfg
    ├── settings.py
    ├── result.json
    └── spiders/
        └── universal_spider.py
```

---

## 🛠️ Customization Guide

To scrape a different website, modify selectors inside:

```
scrapy_app/spiders/universal_spider.py
```

### Update Item Container Selector

```python
items = self.driver.find_elements("css selector", ".your-item-container")
```

### Update Data Fields

```python
for item in items:
    yield {
        "title": item.find_element("css selector", ".title-class").text,
        "price": item.find_element("css selector", ".price-class").text,
        "rating": item.find_element("css selector", ".rating-class").text,
    }
```

### Update Pagination Logic

```python
next_btn = self.driver.find_element("css selector", "a.next-page-link")
```

---

## ⚙️ Configuration Options

You may configure:

- User-Agent rotation → `settings.py`
- Headless mode → Selenium options
- Download delay → Scrapy settings
- Concurrent requests → Scrapy settings

---

## 🧪 Example Use Cases

- E-commerce product scraping
- Movie database extraction
- Academic listing collection
- Market research automation
- Data pipeline feeding

---

## ⚠️ Legal & Ethical Disclaimer

This project is intended for educational and research purposes only.

Before scraping any website:

- Check its `robots.txt`
- Review its Terms of Service
- Respect rate limits
- Avoid overwhelming servers

The developer assumes no responsibility for misuse.

---

## 📌 Requirements

- Python 3.8+
- Google Chrome installed
- Internet connection

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as a distributed scraping architecture demonstration project.
