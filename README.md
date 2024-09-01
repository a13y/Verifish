# Verifish

Verifish is a program designed to take well known or commonly used websites for phishing scams and generate fake domains using leetspeak. These fake domains are often used by phishers as their malicious website which are then blocked by Verifish as it uses the systems hosts or /etc/hosts file to block phishing.


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

# Attribute

Wordlists were taken from the following:

* wordlist.txt: https://github.com/bensooter/URLchecker
* domain.csv: https://www.domcop.com/openpagerank/what-is-openpagerank
