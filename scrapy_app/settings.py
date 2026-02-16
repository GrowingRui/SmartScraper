BOT_NAME = 'scrapy_app'
SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

# --- 核心稳定性设置 ---
# 1. 必须设为 1，因为 Selenium 实例在当前架构下不支持并发翻页
CONCURRENT_REQUESTS = 1

# 2. 设置下载延迟，模仿人类翻页速度，防止被封
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

# 3. 禁用 Cookie 追踪
COOKIES_ENABLED = False

# 4. 伪装浏览器指纹
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOWED_CODES = [403]

# --- 导出美化 ---
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_INDENT = 4

LOG_LEVEL = 'INFO'
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'