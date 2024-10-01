from requests import get

URL = "https://www.huffpost.com/entry/100-quotes-from-100-extraordinary-women_b_6483622"

response = get(URL)

with open("quotes.html", "w", encoding="utf-8") as fp:
    fp.write(response.text)