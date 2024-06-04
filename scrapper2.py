import requests
from bs4 import BeautifulSoup

def search(query, num_results, start):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'}
    url = f"https://www.google.com/search?q={query}&num={num_results}&start={start}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve the page")
        return None

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for item in soup.find_all('a', href=True):
        link = item['href']
        if ('http' in link or 'https' in link) and not "google.com" in link:
            links.append(link)
    return links

def main():
    query = "site:.tr"
    num_results_per_page = 100
    total_results = 1000  # Çekmek istediğiniz toplam sonuç sayısı

    with open("google_tr_domains.txt", "w") as file:
        file.write("")  # Dosyayı baştan oluşturmak için boş yazma işlemi

    for start in range(0, total_results, num_results_per_page):
        html = search(query, num_results_per_page, start)
        if html:
            results = parse(html)
            with open("google_tr_domains.txt", "a", encoding="UTF-8") as file:
                for result in results:
                    file.write(f"{result}\n")
            print(f"Completed batch starting at {start}")
        else:
            print("Failed")

if __name__ == "__main__":
    main()
