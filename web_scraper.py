import requests
import bs4

url = input("Enter Your URL-> ")
response = requests.get(url)

# we don't need print unordered scrabed data 

# print(type(response))
# print(response.text)

filename = "temp.html"
bs = bs4.BeautifulSoup(response.text, "html.parser")

formatted_text = bs.prettify()

print(formatted_text)
with open(filename, "w+" ,encoding="utf-8")as f:
    f.write(formatted_text)