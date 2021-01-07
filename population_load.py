import bs4
import requests


def load():
    res = requests.get(f"http://doheth.co.uk/info/countries-of-the-world.php")
    soup = bs4.BeautifulSoup(res.content, "lxml")
    result = soup.select(".name")
    country_lits = []
    cur = soup.select(".data")
    li = []
    for i in cur:
        l = i.text.split("\n")
    p = (l[29:-1:1])
    i = 0
    j = 4
    k = 5
    db = []
    while i < len(p):
        try:
            data = {"name": p[i], "population": p[k], "currency": p[j]}
            i = i + 14
            j = j + 14
            k = k + 14

            db.append(data)
        except:
            pass
    return db


