import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.selector import Selector
import time


class UniversalSpider(scrapy.Spider):
    name = "universal_spider"

    def __init__(self, url=None, *args, **kwargs):
        super(UniversalSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else []

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def parse(self, response, **kwargs):
        self.logger.info(f"正在爬取: {response.url}")
        self.driver.get(response.url)

        # 预留充足加载时间，并执行滚动以触发懒加载
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        html = self.driver.page_source
        sel = Selector(text=html)

        # 1. 容器识别（覆盖 Top250, 豆列, 搜索页等）
        items = sel.css('.item, .doulist-item, .subject-item')
        self.logger.info(f"本页识别到 {len(items)} 个条目")

        for item in items:
            # --- 标题提取：多路径贪婪匹配 ---
            # 抓取所有可能的标题标签文本
            title_parts = item.css(
                '.hd a span::text, .title a::text, .title::text, .post a::text, .pl2 a::text').getall()

            # --- 数据清洗：消除 nbsp (\xa0) 和干扰词 ---
            # .split() 会自动处理 \xa0, \t, \n 等所有空白符
            raw_title = " ".join("".join(title_parts).split())
            clean_title = raw_title.replace("播放全片", "").replace("/", "").strip()

            # --- 评分与链接 ---
            rating = item.css('.rating_num::text, .rating_nums::text, .rating::text').get()
            link = item.css('a::attr(href)').get()

            if clean_title and len(clean_title) > 1:
                yield {
                    "title": clean_title,
                    "rating": rating.strip() if rating else "N/A",
                    "link": link
                }

        # --- 翻页逻辑：基于文本的 XPath 探测（最稳健） ---
        try:
            next_page = self.driver.find_element("xpath", "//a[contains(text(), '后页') or contains(text(), '下一页')]")
            next_url = next_page.get_attribute("href")
            if next_url and next_url != "#":
                self.logger.info(f"发现下一页: {next_url}")
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
        except Exception:
            self.logger.info("已到达最后一页")

    def closed(self, reason):
        if hasattr(self, 'driver'):
            self.driver.quit()