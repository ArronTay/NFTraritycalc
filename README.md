# NFT Raritycalc

## packages required
- pandas
- request
- datetime
- selenium

## how to use
Two programs
- retrieveRarity
- retrieve current sales

### Retrieve rarity
The 'retrieve rarity' scrapes rarity tools for the list of a collections rarities and stores in an excel file. The names of the collections and urls should be easy to change to use the program for NFTs of your choice!
This program uses selenium webdriver for chrome, if you want to run this then please update the chrome program path and 
the webdriver path accordingly. This part of the program is still reasonably buggy due to Rarity.tools not allowing so many requests from one machine.
if using this program for Dark Horizon the rarity index excel file already exists, however for other collections you
will have to use this to create one. When rarity tools throw an error just restart the program it will continue from
where it got up to before the crash.

### Retrieve current sales
The 'retrieve current sales' uses the Open Sea api to obtain the prices of all the NFTs currently on sale and then gets the rarity of each one from the excel document obtained before.
This program uses the requests package and should work on all operating systems. Just ensure the rarity index excel file
it tries to read into memory has the correct name!

If you like this program and make some healthy profits, donations are welcome eth address: 0x8E3e4D4D7bD974362158779b651F1c6A8ceff4d0
