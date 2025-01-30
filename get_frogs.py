# Matrix bot that will ideally post random images of frogs to a Matrix server.
import aiohttp
from math import floor
from random import random
from bs4 import BeautifulSoup

BASE_URL = "https://calphotos.berkeley.edu"
FROG_URL = (
    BASE_URL
    + "/cgi/img_query?where-lifeform=Animal--Amphibian+%2844335%29&rel-taxon=contains&where-taxon=&rel-namesoup=matchphrase&where-namesoup=frog&rel-location=matchphrase&where-location=&rel-county=eq&where-county=any&rel-state=eq&where-state=any&rel-country=eq&where-country=any&where-collectn=any&rel-photographer=contains&where-photographer=&rel-kwid=equals&where-kwid=&max_rows=24"
)
# Temp variable, scrape it girl
TOTAL_FROGS = 10845


async def get_frog():
    async with aiohttp.ClientSession() as session:
        # it's actually ceil don't @ me I want full pages of frogs
        total_pages = floor(TOTAL_FROGS / 24)
        page_start = floor(random() * (total_pages - 1)) * 24

        data = {
            "query_src": "",
            "tmpfile": "462539",
            "num-matches": TOTAL_FROGS,
            "max": "24",
            "prevwhere": "",
            "button_flag": "",
            "prevselect": "*",
            "table": "img",
            "special": "",
            "OK2SHOWPRIVATE": "",
            "display2": "",
            "display3": "",
            "display4": "",
            "display5": "",
            "display6": "",
            "display7": "",
            "display8": "",
            "display9": "",
            "display10": "",
            "display11": "",
            "display12": "",
            "display13": "",
            "title_tag": "",
            "next": "next+24",
            "row-to-start": "{row_start}".format(row_start=page_start),
        }

        async with session.post(
            FROG_URL,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=data,
        ) as response:
            html = await response.text()

        soup = BeautifulSoup(html, "html.parser")
        frogs = soup.find_all("img")

        frog_index = floor(random() * len(frogs))
        img_src = frogs[frog_index]["src"]
        file_extension = img_src.split(".")[-1]

        async with session.get(BASE_URL + img_src) as response:
            content = await response.read()

        filename = f"frog.{file_extension}"
        with open(filename, "wb") as f:
            f.write(content)

        return filename
