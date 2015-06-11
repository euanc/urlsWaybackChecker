# This program will take two inputs at the command line:
# 1. a source csv file that is produced by the twitter archive download and normally called "tweets.csv"
# 2. a destination directory
# and will look up each url you tweeted that was included in the tweets.csv file
# and check to see if it is included in the wayback machine. 
# it will then produce another csv file with two columns one with a url and one with a lookup result
# it only checks unique urls so doesn't duplicate where you've tweeted the same url twice
#
#I used Johan van der Knijff's iawayback program from https://github.com/bitsgalore/iawayback for the "checkURL" part of this program
#
# invoke it at the command line as follows:
# python urlsWaybackChecker.py tweets.csv /home/user/ 
#
# Author: Euan Cochrane


import sys
import urllib2
import json
import sys
import csv


dest_dir = str(sys.argv[2])

sourceFile = open(str(sys.argv[1]), 'rb')
urlsList = []



def checkURL(url):

    # API url (see: http://archive.org/help/wayback_api.php)
    urlAPI="http://archive.org/wayback/available?url="

    # URL we want to search for
    urlSearch = url

    req = urllib2.Request(urlAPI + urlSearch)
    response = urllib2.urlopen(req)
    the_page = response.read()

    # Decode json object
    data = json.loads(the_page)
    snapshots = data['archived_snapshots']
    if len(snapshots) == 0:
        # No snapshots available, so not available in Wayback
        available = False
        urlWayback = ""
        status = ""
        timestamp = ""

    else:
        # Snapshot(s) available
        # For now API only returns 1 snaphot, which is the most recent one.
        # May change in future API versions.
        closest = snapshots['closest']
        available = closest['available']
        urlWayback = closest['url']
        status = closest['status']
        timestamp = closest['timestamp']
    
    return(available, urlWayback, status, timestamp)

for row in csv.DictReader(sourceFile):
  #print row['expanded_urls']
  if not row['expanded_urls'].strip():
    pass
  else:
    if row['expanded_urls'].find(',') != -1:
      for result in row['expanded_urls'].split(','):
        urlsList.append(result)
    else:
	  urlsList.append(row['expanded_urls'])

csvfile = open(dest_dir + 'urlChecker.csv', 'w+')

fieldnames = ['url', 'result']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
writer.writeheader()

for url in set(urlsList):
  #print str(url)
  writer.writerow({'url': url, 'result': str(checkURL(url)[0])})

csvfile.close()