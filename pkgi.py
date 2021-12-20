import csv
import urllib.request

url = "http://nopaystation.com/tsv/PS3_GAMES.tsv"
print('Downloading PS3_GAMES.tsv...')
req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'})

with open('PS3_GAMES.tsv', 'wb') as file:
	file.write(urllib.request.urlopen(req).read())

newlist = []

with open('PS3_GAMES.tsv', newline='', encoding="utf8") as csvfile:
    listreader = csv.reader(csvfile, delimiter='	', quotechar='"')
    csvfile.readline() # Skip first line
    print("Rearranging list...")
    for row in listreader:
        newrow = []
        newrow.append(row[5]) # Content ID
        newrow.append('0')    # Flags (unused)
        newrow.append(row[2]) # Name
        newrow.append('')     # Description (unused)
        newrow.append('')     # RAP file in HEX (16 bytes)
        newrow.append(row[3]) # PKG Download Link
        newrow.append(row[8]) # Filesize
        newrow.append(row[9]) # Checksum
        newlist.append(newrow)

with open('pkgi.txt', 'w', newline='', encoding="utf8") as csvfile:
    listwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    print('Saving pkgi.txt...')
    for newrow in newlist:
        listwriter.writerow(newrow)
