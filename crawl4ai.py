# -*- coding: utf-8 -*-

!pip install "crawl4ai @ git+https://github.com/unclecode/crawl4ai.git"

from crawl4ai import WebCrawler

crawler = WebCrawler()

crawler.warmup()

result = crawler.run(
    url = "https://zbiz.io/"
)

# Print the extracted content
print(result.markdown)
