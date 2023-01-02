from icrawler.builtin import GoogleImageCrawler
from config import path

google_crawler = GoogleImageCrawler(storage=
                                    {"root_dir": path
                                     })

def parse_img(name):
    google_crawler.crawl(keyword=name, max_num=1)

def main():
    name = input("Name img: ")
    parse_img(name)

if __name__ == "__main__":
    main()