import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.amazon.com/dp/B0B2LRRH1K",
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())