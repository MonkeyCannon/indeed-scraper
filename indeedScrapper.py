#This code is based on and inspired by https://scrapfly.io/blog/how-to-scrape-indeedcom/
#1. Open a terminal and write pip install httpx
#Then in the terminal write pip install scrapfly-sdk
import httpx
from scrapfly import ScrapflyClient, ScrapeConfig
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
}
#Variables that holds the url for indeed in Norway and in usa
linkNorway = "https://no.indeed.com/jobs?"
linkUSA = "https://www.indeed.com/jobs?"

#Ask user what country they want jobinfo from
print("Hello and welcome to the indeed webscraper")
print("What country do you want to get data from?")
country = input(" Norway(N) or USA (U): ")

#Set the first part of the URL string to the country the user want
if country == "N" or "n":
    startURL= linkNorway
    country= "Norway"
    print("Norway. Okay!")
if country == "U" or "u":
    startURL= linkUSA
    country = "USA"
    print("The US of friggin A!")

#Ask user for where and what they want to search for and collects it in two strings
print("-----------------------------------------------------------")
print("Great! So where in " + country + " do you want jobs from? (If you want from the whole country. Leave it Empty)")
whatPlace = input("Where: ")

print("-----------------------------------------------------------")
print("Nice. So What do you want to work with?")
whatJob = input("What: ")

print("So " + whatJob + " in " + whatPlace)
print("-----------------------------------------------------------")

if whatPlace == "":
    #fullURL = httpx.get(startURL + "q=" + whatJob, headers=HEADERS)
    #print(fullURL)
    client = ScrapflyClient(key="YOUR_API_KEY")
    result = client.scrape(ScrapeConfig(url=startURL + "q=" + whatJob, asp=True,))
    print(result)