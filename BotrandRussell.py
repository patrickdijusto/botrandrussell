#!/usr/bin/python
import twitter
import time
import csv
from settings import *
import datetime
import random as rx

global now
global api

##now = datetime.datetime.now()
##message = str(now)
##print (message)
##
####def establishTwitter():
##
##print('establish the twitter object')
### see "Authentication" section below for tokens and keys
##api = twitter.Api(consumer_key=CONSUMER_KEY,
##        consumer_secret=CONSUMER_SECRET,
##        access_token_key=OAUTH_TOKEN,
##        access_token_secret=OAUTH_SECRET,
##        )
##
##print('twitter object established')
##
##        ##api.PostUpdate(message)
##
##	##return api


def getQuote():

        
        csv_file = csv.reader(open('politicalideals.csv', 'rb'))

        for row in csv_file:
                if rx.random()>.95:
                        print (csv_file.line_num)
                        break

        writeLog(str(row), 1, "a")						
        return row

def readTrumpianTweet():
	print ("nothing")
	
	
def getPast():
	## open file
	## 	Read # of trump's previous tweet
	## Close file?

	flx = open('pastNumber.csv',"r")
	
	row = flx.read()

	flx.close()

	writeLog("Writing past number: ", int(row), "w")
	               
	return int(row)

def getCurrent(pastNumber):
	
	##Contact twitter
	## Read Trump's most recent tweet
	## Extract Tweet ID Number

        St = api.GetUserTimeline(0,"realDonaldTrump",pastNumber,0,1)

        print("And now we print the Status of the last trump Tweet")

        writeLog("Gotten current: ", 1, "a")

        print(St)
        print (St[0].id)
        return St[0].id

def postReply(text,currentNumber):

        URX = "http://www.twitter.com/realDonaldTrump/status/"+str(currentNumber)

        print (URX)
        
	## Construct URL : Http://www.twitter.com/realDonaldTrump/status/<<NUMBER>>

        response = str(text)+" -- Bertrand Russell \n"+str(URX)

        print (response)

        ##
        status = api.PostUpdate(response)
        ##

        writeLog(response, 1, "a")

        print(status)
        

def writePast(ccc):
        flx = open('pastNumber.csv', "w")
        flx.write(str(ccc))
        flx.close()
        writeLog("writing past: ", int(ccc), "a")

		
def writeLog(TweetText, currentNumber, mode):

        print("Writing a log...")
        now = datetime.datetime.now()
        message = "\n"+str(now)
        
        fly = open("writeLog.txt", mode)
        fly.write(message)
        fly.write(TweetText)
        fly.write(str(currentNumber))
        fly.close()




##def establishTwitter():

print('establish the twitter object')
# see "Authentication" section below for tokens and keys
api = twitter.Api(consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=OAUTH_TOKEN,
        access_token_secret=OAUTH_SECRET,
        )

print('twitter object established')

        ##api.PostUpdate(message)

	##return api



pastNumber = getPast()

print ("Past number is:")

print (pastNumber)

currentNumber = getCurrent(pastNumber)

writePast(currentNumber)

TweetText = getQuote()

print (TweetText)


if (currentNumber > pastNumber):
        postReply(TweetText[0], currentNumber)


	
writeLog(TweetText[0], currentNumber, "a")

