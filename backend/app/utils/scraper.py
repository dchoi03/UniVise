import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


async def main():
    browser_conf = BrowserConfig(headless=True)  # or False to see the browser
    run_conf = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS, checks_robots_txt=True, stream=False
    )

    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun(
            url="https://www.sydney.edu.au/courses/courses/pc/master-of-professional-engineering-accelerated-biomedical-engineering.html",
            config=run_conf,
        )
        print(result.markdown)


if __name__ == "__main__":
    asyncio.run(main())
