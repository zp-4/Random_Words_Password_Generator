import argparse
import random
import string
import urllib.request
from bs4 import BeautifulSoup

def get_words_from_website(url):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), "html.parser")
    words = []
    for text in soup.stripped_strings:
        words += text.split()
    return words

def generate_password(words, num_words, separators):
    selected_words = random.sample(words, num_words)
    password = ""
    for i in range(num_words):
        password += selected_words[i]
        if i < num_words - 1:
            password += random.choice(separators)
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--website", type=str, default="https://www.yamli.com/", help="website to extract words from")
    parser.add_argument("-n", "--num_words", type=int, default=random.randint(4, 10), help="number of words to use in password")
    parser.add_argument("-s", "--separators", type=str, default="", help="separators to use between words")
    args = parser.parse_args()

    website = args.website
    num_words = args.num_words
    separators = args.separators

    if not website:
        website = "https://www.yamli.com/"

    words = get_words_from_website(website)

    if not separators:
        separators = random.sample([',', ';', ':', ' '], k=2)

    password = generate_password(words, num_words, separators)

    print(password)
