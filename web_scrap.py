import requests
from bs4 import BeautifulSoup

input1 = input("Enter The Product Name: \n ")
min_range = input("Enter The Minimun Amount of Product in Numbers: \n")
max_range = input("Enter The Maximum Amount of Product in Numbers: \n")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

product = requests.get('https://www.amazon.in/s?k={0}&rh=p_36%3A{1}00-{2}00&s=review-rank'.format(input1,min_range,max_range), headers=headers)
soup = BeautifulSoup(product.content, features="html")

# soup.find_all("div",class_='a-section aok-relative s-image-fixed-height')

print('\n')

for i in soup.find_all('img',class_='s-image'):
    print('Name Of Product : '+i['alt'])
    print('Image of Product : '+i['src'])
    print('\n')
