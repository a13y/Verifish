#==============================
# Verifish
#
# Verifish is a Python program that takes a list of genuine domain names and
# generates fake domain names usually used by scammers for phishing. These
# fake domain names are then added to the /etc/hosts lists to point to 
# non-existent ip addresses and prevent phishing sites from being accessed,
# hence blocking them and keeping one's device safe from phishing.
#
#
# default list taken from: URLchecker https://github.com/bensooter/URLchecker/tree/master
# csv list taken from: Open PageRank https://www.domcop.com/openpagerank/what-is-openpagerank
#==============================


# import modules
import csv
import time
from itertools import product

# start time of the program
start_time = time.time()

# variables
# built-in wordlist
wordlist = [
'twitter.com',
'youtube.com',
'wired.com',
'google.com',
'amazon.com',
'amazon.com.sg',
'hbo.com',
'hboasia.sg',
'netflix.com',
'steam.com',
'lazada.sg',
'shopee.sg',
'singtel.sg',
'microsoft.com',
'apple.com',
'archiveofourown.org',
'docs.google.com',
'tiktok.com',
'instagram.com',
'facebook.com',
'mastodon.social',
'acer.com',
'samsung.com',
'itch.io',
'outlook.com',
'discord.com',
'slack.com',
'github.com',
'linkedin.com',
'reddit.com',
'wikipedia.org',
'yahoo.com',
'amazon.com',
't.co',
'pinterest.com',
'tumblr.com',
'netflix.com',
'ebay.com',
'quora.com',
'bilibili.com',
'baidu.com',
'yandex.ru',
'live.com',
'office.com',
'mail.ru',
'vk.com',
'twitch.tv',
'stackexchange.com',
'aliexpress.com',
'paypal.com',
'booking.com',
'craigslist.org',
'huffpost.com',
'cnn.com',
'theguardian.com',
'wordpress.org',
'weather.com',
'sports.yahoo.com',
'bbc.com',
'imdb.com',
'zoom.us',
'github.com',
'msn.com',
'yahoo.co.jp',
'dailymotion.com',
'reuters.com',
'cnbc.com',
'yahoo.co.uk',
'forbes.com',
'livejournal.com',
'bestbuy.com',
'chaturbate.com',
'mayoclinic.org',
'espn.com',
'microsoftonline.com',
'sourceforge.net',
'wix.com',
'wikihow.com',
'coursera.org',
'dribbble.com',
'salesforce.com',
'hbo.com',
'webmd.com',
'imgur.com',
'canva.com',
'domain.com',
'theverge.com',
'stackoverflow.com',
'zillow.com',
'aol.com',
'whatsapp.com',
'chase.com',
'airbnb.com',
'substack.com',
'collegeboard.org',
'news.yahoo.com',
't.co',
'hdfc.com',
'dell.com',
'squarespace.com',
'newyorktimes.com',
'intuit.com',
'healthline.com',
'investopedia.com',
'jstor.org',
'bloomberg.com',
'postmates.com',
'target.com',
'expedia.com',
'health.com',
'openai.com',
'pinterest.com',
'tumblr.com',
'netflix.com',
'ebay.com',
'quora.com',
'bilibili.com',
'baidu.com',
'yandex.ru',
'live.com',
'office.com',
'mail.ru',
'vk.com',
'twitch.tv',
'stackexchange.com',
'aliexpress.com',
'paypal.com',
'booking.com',
'craigslist.org',
'huffpost.com',
'cnn.com',
'theguardian.com',
'wordpress.org',
'weather.com',
'sports.yahoo.com',
'bbc.com',
'imdb.com',
'zoom.us',
'github.com',
'msn.com',
'yahoo.co.jp',
'dailymotion.com',
'reuters.com',
'cnbc.com',
'yahoo.co.uk',
'forbes.com',
'livejournal.com',
'bestbuy.com',
'chaturbate.com',
'mayoclinic.org',
'espn.com',
'microsoftonline.com',
'sourceforge.net',
'wix.com',
'wikihow.com',
'coursera.org',
'dribbble.com',
'salesforce.com',
'hbo.com',
'webmd.com',
'imgur.com',
'canva.com',
'domain.com',
'theverge.com',
'stackoverflow.com',
'zillow.com',
'aol.com',
'whatsapp.com',
'chase.com',
'airbnb.com',
'substack.com',
'collegeboard.org',
'news.yahoo.com',
'hdfc.com',
'dell.com',
'squarespace.com',
'newyorktimes.com',
'intuit.com',
'healthline.com',
'investopedia.com',
'jstor.org',
'bloomberg.com',
'postmates.com',
'target.com',
'expedia.com',
'health.com',
'shopify.com',
'snapchat.com',
'flickr.com',
't.co',
'alibaba.com',
'target.com',
'bestbuy.com',
't.co',
'dailymotion.com',
'chaturbate.com',
'mayoclinic.org',
'espn.com',
'microsoftonline.com',
'sourceforge.net',
'wix.com',
'wikihow.com',
'coursera.org',
'dribbble.com',
'salesforce.com',
'hbo.com',
'webmd.com',
'imgur.com',
'canva.com',
'domain.com',
'theverge.com',
'stackoverflow.com',
'zillow.com',
'aol.com',
'whatsapp.com',
'chase.com',
'airbnb.com',
'substack.com',
'collegeboard.org',
'news.yahoo.com',
'hdfc.com',
'dell.com',
'squarespace.com',
'newyorktimes.com',
'intuit.com',
'healthline.com',
'investopedia.com',
'jstor.org',
'bloomberg.com',
'postmates.com',
'target.com',
'expedia.com',
'health.com',
'shopify.com',
'snapchat.com',
'flickr.com',
't.co',
'alibaba.com',
'target.com',
'bestbuy.com',
't.co',
'dailymotion.com',
'chaturbate.com',
'mayoclinic.org',
'espn.com',
'microsoftonline.com',
'sourceforge.net',
'wix.com',
'wikihow.com',
'coursera.org',
'dribbble.com',
'salesforce.com',
'hbo.com',
'webmd.com',
'imgur.com',
'canva.com',
'domain.com',
'theverge.com',
'stackoverflow.com',
'zillow.com',
'aol.com',
'whatsapp.com',
'chase.com',
'airbnb.com',
'substack.com',
'collegeboard.org',
'news.yahoo.com',
'hdfc.com',
'dell.com',
'squarespace.com',
'newyorktimes.com',
'intuit.com',
'healthline.com',
'investopedia.com',
'jstor.org',
'bloomberg.com',
'postmates.com',
'target.com',
'expedia.com',
'health.com',
'shopify.com',
'snapchat.com',
'flickr.com',
'posb.com',
'dbs.com'
]


# leetspeak dictionary
leet_dict = {
        'A': '4', 'a': '4',
        'B': '8', 'b': '8',
        'E': '3', 'e': '3',
        'G': '9', 'g': '9',
        'I': '1', 'i': '1',
        'O': '0', 'o': '0',
        'S': '5', 's': '5',
        'T': '7', 't': '7'
}

# other variables
csv_list = []
file_list = []
first_column_list = []
hosts_content = ''



# leetspeak variations
# list  options
def generate_leet_variations(word):
    options = []
    for char in word:
        if char in leet_dict:
            # Add both the leet version and the original character
            options.append([char, leet_dict[char]])
        else:
            # Add only the original character
            options.append([char])
    
    # Generate all combinations of these options
    variations = [''.join(combination) for combination in product(*options)]
    return variation


# convert wordlist to leetspeak
def convert_to_leetspeak(wordlist):
    all_variations = []
    for word in wordlist:
        options = []
        for char in word:
            if char in leet_dict:
                options.append([char, leet_dict[char]])
            else:
                options.append([char])

        #generate all combinations of these options

        all_variations.extend([''.join(combination) for combination in product(*options)])
    return all_variations


# removes a small list from a big list
def remove_words_from_list(big_list, small_list):

    # Compute the difference between the sets
    result_set = set(big_list) - set(small_list)
    
    return list(result_set)

def replace_text_between_markers(file_path, new_content, start_marker='----start----', end_marker='-----end-----'):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    start_index = None
    end_index = None
    
    # Find indices of start and end markers
    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        if end_marker in line:
            end_index = i
            break
    
    if start_index is None:
        raise ValueError(f"Start marker '{start_marker}' not found in the file.")
    if end_index is None:
        raise ValueError(f"End marker '{end_marker}' not found in the file.")
    
    # If the end marker is before the start marker, raise an error
    if end_index <= start_index:
        raise ValueError("End marker must come after the start marker.")
    
    # Replace content between markers
    # Write updated content back to the file
    print('writing to file...')
    open(file_path, 'w').write(''.join(lines[:start_index + 1]) + ''.join(new_content) + ''.join(lines[end_index + 1:]))



# add the .sg to the urls if not present
def add_sg(url_list):
    new_list = []
    for url in url_list:
        if url.endswith('.com'):
            new_list.append(url)
            new_list.append(url + '.sg')
        else:
            new_list.append(url)
    return new_list

# add www. part to the urls if not present
def add_www(url_list):
    new_list = []
    for url in url_list:
        if not url.startswith('www.'):
            new_list.append('www.' + url)
        else:
            new_list.append(url)
    return new_list

# take loading variables and function time
load_var_func_time = time.time()

print('Loading wordlists...')
# Open and read the file
with open('wordlist.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    
    # Strip leading/trailing whitespace from each line and add to the list
    file_list = [line.strip() for line in lines]


with open('domain.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Iterate over each row in the CSV
    for row in csv_reader:
        # Append the second column value to the list
        if row:  # Check if the row is not empty
            first_column_list.append(row[1])




# put all lists together
wordlist += file_list + first_column_list

# create www. and .sg versions of all websites and put them with the list
wordlist += add_www(wordlist) + add_sg(wordlist)


# remove duplicates
wordlist = list(set(wordlist))

# take loading wordlist time
load_wordlist_time = time.time()


print('generating fake domains...')

# convert the list to leepseak
website_list = convert_to_leetspeak(wordlist)

# remove the legitimate websites from the final fake domain list
final_list = remove_words_from_list(website_list, wordlist)

# remove duplicates
final_list = list(set(final_list))

# add the 0.0.0.0 ip address to each domain name to point it to nowhere
for i in range(len(final_list)):
    final_list[i] = '\n0.0.0.0 ' + final_list[i]

# get the time taken to generate fake domain names
generate_fake_domains = time.time()


# start writing into hosts file
try:
    replace_text_between_markers('/etc/hosts', final_list)

except ValueError:
    open('/etc/hosts', 'w').write(open('/etc/hosts', 'r').read() + '\n\n\n----start----\n\n' +  ''.join(final_list) + '\n\n\n-----end-----\n\n')
    print('writing to file...')


# get the time to write the data to the /etc/hosts file
end_time = time.time()

# calculate stats
total_time = end_time - start_time
total_seconds = total_time % 60
total_minutes = total_time // 60
total_hours =  total_minutes // 60

var_func_time = load_var_func_time - start_time
wordlist_time = load_wordlist_time - load_var_func_time
fake_domains_time = generate_fake_domains - load_wordlist_time
write_file_time = end_time - generate_fake_domains


# display stats and first 10 domains
print('\n\n--------------------first ten fake domains generated--------------------\n')
for i in range(len(final_list)):
    print(final_list[i], end='')
    if i > 9:
        break
# URL generation stats
print('\n\n\n--------------------URL generation stats--------------------\n\n')
print(f'URLs generated:       {len(final_list)}')
print(f'Original wordlist:    {len(wordlist)}')
print(f'Generation ratio:     {len(final_list)/len(wordlist):.2f}')
print(f'Space taken up:       {len(''.join(final_list))/1000000:.2f} MB')

# time stats
print('\n\n--------------------Time taken stats--------------------\n\n')
print(f'Total time taken:     {total_hours} h {total_minutes} m {total_seconds:.2f} s')
print(f'initial loading:      {var_func_time:.2f} s')
print(f'wordlist generation:  {wordlist_time:.2f} s')
print(f'fake url generation:  {fake_domains_time:.2f} s')
print(f'time writing to file: {write_file_time:.2f} s')



