# RWPG (Random Words Password Generator)

RWPG is a Python script that extracts words from a website and uses them to generate a random password. The script takes three optional command-line arguments:

    -w or --website: the URL of the website to extract words from (default: https://www.yamli.com/)
    -n or --num_words: the number of words to use in the generated password (default: between 4 and 10)
    -s or --separators: the separator(s) to use between the words in the generated password (default: two randomly chosen separators from ",", ";", ":" and " ")

# Requirements

This script requires Python 3 and the following packages:

    argparse
    beautifulsoup4

To install the required packages, run the following command in the terminal:

    pip install -r requirements.txt

This will install the required packages listed in the requirements.txt file.
# Usage

To use the RWPG script, run the following command:

    python rwpg.py [-w WEBSITE] [-n NUM_WORDS] [-s SEPARATORS]

For example, to generate a password using 6 randomly selected words from `https://www.yahoo.fr/` with the separators "," and ";" run the following command:

    python rwpg.py -w https://www.yahoo.fr/ -n 6 -s ,;

The generated password will be printed to the console.
# License

This script is licensed under the MIT License. Feel free to use, modify and distribute it as you wish.
