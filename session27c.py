import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt

url1 = "https://www.imdb.com/india/top-rated-indian-movies/"
# url = "https://www.espncricinfo.com/table/series/8048/season/2019/ipl" | Please Explore
response = requests.get(url1)
#print(response.text)


soup = BeautifulSoup(response.text, "html.parser")

movieNameTags = soup.find_all("td", class_="titleColumn")
movieRatingTags = soup.find_all("td", class_="ratingColumn imdbRating")

movieTitles = []
movieYears = []
movieRatings = []

for tag in movieNameTags:
    # print(tag)
    # print(tag.text)
    # print(tag.text.strip())

    title = tag.text.strip()
    year = int(title[-5:-1])

    movieTitles.append(title)
    movieYears.append(year)


print()

for tag in movieRatingTags:
    # print(tag)
    # print(tag.text)
    # print(tag.text.strip())
    rating = float(tag.text.strip())
    movieRatings.append(rating)


print()

#print(len(movieNameTags), len(movieRatingTags))

url2 = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
response2 = requests.get(url2)
soup = BeautifulSoup(response2.text, "html.parser")
movieNameTags2 = soup.find_all("h3", class_="lister-item-header")
movieRatingTags2 = soup.find_all("div", class_ = "inline-block ratings-imdb-rating")



movieTitles2 = []
movieYears2 = []
movieRatings2 = []


for tag in movieNameTags2:
    # print(tag)
    # print(tag.text)
     #print(tag.text.strip())

    title = tag.text.strip()
    year = int(title[-5:-1])

    movieTitles2.append(title)
    movieYears2.append(year)

for tag in movieRatingTags2:
    # print(tag)
    # print(tag.text)
     #print(tag.text.strip())

    rating = float(tag.text.strip())
    movieRatings2.append(rating)


#print((movieRatingTags2[0]))

print(len(movieRatingTags2), len(movieYears2))

if len(movieYears) and len(movieRatings) == 50 :
    breakpoint()
else:

  plt.scatter(movieYears, movieRatings, label = "india", color = "pink")
plt.scatter(movieYears2, movieRatings2, label = "america" , color = "black")
plt.legend()
plt.show()