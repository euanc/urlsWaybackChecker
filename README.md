# urlsWaybackChecker
A small program to check the urls you've tweeted from a twitter archive download and confirm if they are available in the wayback machine at www.archive.org
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
