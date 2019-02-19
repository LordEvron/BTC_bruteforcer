# BitCoin Tester


## How it work
This code firstly fetch the richest bitcoins wallets from bitinfocharts.com and stores it in a list.It also dumps it in a file called "richWalletDump.txt"
Normally it fetch from page 2 to page 70. this is around 7000 addresses. You can configure it in the Main.py the amount of pages to be fetched.
Then it start to generate random private keys and from there the relative wallet. Then it checks if the wallet generated is in the rich wallet list.
If yes, it print both the private key and the wallet on the screen and also stores it in a file.

# Requirements
Python 2.7. You need to install the following packages:
+ "Requests" to perform HTTP requests
+ "ECDSA" for the elliptic curve functions required to generate wallets.
+ "BeautifulSoup" to parse xml files.

## Efficiency
It only uses the CPU and is written in python, so not efficient at all. in order to improve efficiency you would need to
write it in C++ use multi-thread, or even better use GPU acceleration.
So this code would process 10 private keys every seconds or so.
Note that the way i am generating random key with the trick of time.time(), allows at most 100 keys generated per seconds because it return the time in sssss.ms format. so if you get time.time faster than 100 times per second it will return the same timestamp

## NOTES
This code is just for education purpose. I am not responsible to miss-use of it.
Quite some time ago, i wanted to understand more the bitcoin wallet cryptography, so i developed this code in one
to better understand the under laying technology behind it. Also i am parsing the page from the webpage.. It is not guaranteed to work if they change the source code.

I partially reused a couple of function from another github page (for the pub key generation). Unfortunately I
lost track of the original source.

Anyway, this is just a quick test. Many similar and more efficient way  already exists such as using Hashcat (GPU powered) or using The Large Bitcoin Collider project.

## FAQ
+ How many Walled did you cracked? None
+ How likely is to find a collision? Veeeeery unluckily... Really, Is just hopeless....just run some numbers
+ I found a collision what should i do?  Is up to you... I suggest that you delete the found keys
+ Are you serious? No
+ I found a collision and I want to invite you to my yacht. Can I do that? Yes
+ I did not found a collision and I still want to invite you to my yacht. Can I do that? Yes

