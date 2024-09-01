# Verifish
Verifish is a security app designed to protect you from phishing scams by verifying the legitimacy of digital content and links.

Phishing sites often use slight variations and leetspeak to mimic legitimate websites.

Verifish detects these tricks by filtering and rejecting suspicious links, providing real-time alerts to keep you safe online.

The name "Verifish" combines "Verify" and "Phishing," reflecting its mission to safeguard users from online threats.


# Installation

To install the program, clone the github repository. wordlist.txt and doman.csv can be replaced with your own list.
```
git clone https://github.com/a13y/Verifish
cd Verifish
```


# Usage

## Linux
To run the program on Linux, simply run the program in terminal with sudo priviledges to allow it to edit the /etc/hosts file.
```
sudo python main.py
```

## MacOS
To run the program on MacOS, simply run the program in terminal with sudo priviledges to allow it write access to the /etc/hosts file.
```
sudo python main.py
```

# Attributes

Wordlists were taken from the following:

* wordlist.txt: https://github.com/bensooter/URLchecker
* domain.csv: https://www.domcop.com/openpagerank/what-is-openpagerank
