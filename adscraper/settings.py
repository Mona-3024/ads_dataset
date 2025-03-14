# Scrapy settings for adscraper project
BOT_NAME = "adscraper"

SPIDER_MODULES = ["adscraper.spiders"]
NEWSPIDER_MODULE = "adscraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "adscraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# DOWNLOAD_DELAY = 3
# See also autothrottle settings and docs

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#     "adscraper.middlewares.AdscraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#     "adscraper.middlewares.AdscraperDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# EXTENSIONS = {
#     "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# ITEM_PIPELINES = {
#     "adscraper.pipelines.AdscraperPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
FEED_FORMAT = "json"
FEED_URI = "ads.json"
ITEM_PIPELINES = {
    'adscraper.pipelines.AdsJsonPipeline': 1,
}

# Enable Playwright middleware
# Set up the Playwright download handler
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# Enable the Playwright middleware
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Set the timeout for requests
DOWNLOAD_TIMEOUT = 60  # Set to 60 seconds or higher

# Specify the browser type for Playwright (Chromium, Firefox, Webkit)
PLAYWRIGHT_BROWSER_TYPE = 'chromium'  # You can change this to 'firefox' or 'webkit'

# Set up Playwright launch options
# settings.py
PLAYWRIGHT_BROWSER_CLOSE_ON_QUIT = False
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "timeout": 60000  # Increase timeout to 60 seconds
}

# Retry configuration
RETRY_ENABLED = True
RETRY_TIMES = 3  # Number of retry attempts
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]  # HTTP error codes to retry

# Enable concurrent requests for Playwright (optional)
CONCURRENT_REQUESTS = 8
