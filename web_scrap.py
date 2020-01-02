# pip install scikit-image
# pip install requests
# pip install beautifulsoup4


from skimage import io
import requests
from bs4 import BeautifulSoup

input1 = input("Enter The Product Name: \n ")
min_range = input("Enter The Minimun Amount of Product in Numbers: \n")
max_range = input("Enter The Maximum Amount of Product in Numbers: \n")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

product = requests.get('https://www.amazon.in/s?k={0}&rh=p_36%3A{1}00-{2}00&s=review-rank'.format(input1,min_range,max_range), headers=headers)
soup = BeautifulSoup(product.content, features="html")

#a = soup.find_all("div",class_='a-section aok-relative s-image-fixed-height')

print('\n')
print('The Products Best For You according to your Budget are :\n')

detail= soup.find_all('img',class_='s-image')
alt = []
for everyitem in detail:
    alt.append(everyitem['alt'])

src = []
for everyitem in detail:
    src.append(everyitem['src'])


detail2 = soup.find_all('span',class_='a-price-whole')

price = []
for everyitem in detail2:
    price.append(everyitem.get_text())
i=1
for result in range(0,18):
     
    print(+i,'. Name of The Product : ' +alt[result])
    print('    Price : '+price[result], 'RS.')
    print('    Image of Product : ')
    j = src[result]
    io.imshow(io.imread(j))
    io.show()
    
    print('\n')
    i=i+1
    

