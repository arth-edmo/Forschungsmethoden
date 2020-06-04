import csv
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

# Read CSV file

stack = []

with open("match_list.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            stack.append(row[4])
            line_count += 1

# Download website

    filenumber = 1
while stack:
    outputstring = ""
    url = stack.pop()
    response = urllib.request.urlopen(url)
    webContent = response.read()
# Parse website
    soup = BeautifulSoup(webContent, "html.parser")
    paragraphs = soup.find_all("p", class_="paragraph")
    for each in paragraphs:
        outputstring += (str(each.get_text()))
    f = open(str(filenumber) + ".txt", "w+")
    try: f.write(outputstring)
    except UnicodeEncodeError:
        print("Encoding error")
    f.close()
    filenumber += 1
