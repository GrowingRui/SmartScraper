import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class UniversalSpider(scrapy.Spider):
    name = "universal_spider"

    def __init__(self, url=None, *args, **kwargs):
        super(UniversalSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else []

        # Selenium 配置
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def parse(self, response, **kwargs):
        self.logger.info(f"正在抓取页面: {response.url}")
        self.driver.get(response.url)
        time.sleep(4)  # 给 Ajax 留点加载时间

        # 1. 抓取当前页面的电影条目
        items = self.driver.find_elements("css selector", ".doulist-item")
        for item in items:
            try:
                # 提取电影详情
                title_node = item.find_element("css selector", ".title a")
                yield {
                    "title": title_node.text,
                    "rating": item.find_element("css selector", ".rating_nums").text,
                    "link": title_node.get_attribute("href"),
                    "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
                }
            except Exception:
                continue  # 跳过非电影条目（如广告）

        # 2. 自动翻页逻辑
        try:
            # 尝试寻找豆瓣的“后页”按钮
            next_btn = self.driver.find_element("css selector", "span.next a")
            if next_btn:
                next_url = next_btn.get_attribute("href")
                self.logger.info(f"发现下一页链接: {next_url}")
                # 递归调用自身
                yield scrapy.Request(next_url, callback=self.parse)
        except:
            self.logger.info("已到达最后一页或未发现翻页按钮。")

    def closed(self, reason):
        if hasattr(self, 'driver'):
            self.driver.quit()