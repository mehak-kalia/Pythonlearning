import requests
import threading    # built in module from python

"""
class FetchHealthNews:
    def fetch(self):
        print("Fetch News Started")
        url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=31c21508fad64116acd229c10ac11e84"
        response = requests.get(url)
        print(response.text)
        print("Fetch News Finished")
"""

#Inheritance: FetchHelthNews is now the Child of Thread
class FetchHealthNews(threading.Thread):

    # Overriding the Function from the Parent class
    # For a Child Thread, we must write long running operations in run function
    def run(self):
        print("Fetch News Started")
        url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=31c21508fad64116acd229c10ac11e84"
        response = requests.get(url)
        print(response.text)
        print("Fetch News Finished")


# whatever we write in main is executed in a sequence
def main():
    print("App Started")

    fRef = FetchHealthNews()
    # fRef.fetch()                # This may become a long running operation due to Internet Connectivity

    fRef.start()                  # This shall execute run function internally and will make it execute parallel to the main

    # Doing Some Operation
    for i in range(1, 11):
        print("i is:", i)

    print("App Finished")


if __name__ == '__main__':
    main()
