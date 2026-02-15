BOT_NAME = 'scrapy_app'
SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

# 伪装
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
ROBOTSTXT_OBEY = False

# 允许 403 错误通过进入 Selenium
HTTPERROR_ALLOWED_CODES = [403]

# --- 导出美化设置 ---
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_INDENT = 4  # 每一层缩进4个空格，这样结果就不是一整行了

LOG_LEVEL = 'INFO'
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'