# Python is case sensitive for variable and function names.
# imports
from os import system

import tweepy
import time, sys
import datetime
#import webbrowser
#import requests

from sys import exit
from subprocess import Popen

# Get the message from Twitter.
def get_twitter_message( feed):
    CONSUMER_KEY = 'T2ie3oslfQfkP9ctklT8xeoyw'
    CONSUMER_SECRET = 'pnJ1RmqCVhYXXG3tltOyd1hgUgSrJrUr3T6aHQgEf19HE6C55M'
    ACCESS_TOKEN = '846744996665425920-RhTsk1jwU9JxDreJXBf8DjHNkL99WSe'
    ACCESS_TOKEN_SECRET = 'Ps1tnqw6nUKs4UJO816uvJNU2FxcDe7A27Rw1DgqNxaRb'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweets = api.search( q=feed)
    return tweets

# Create the image file
#def create_image( msg="No Message", textFileName="TelephonePiMessage.txt", imageFileName = "TelephonePiImage.png"):
#    print ('Image is creating...')
#    cmd = 'printf "' + message + '" > myfile.txt'
#    system( cmd)
#    #print "echo cmd: " + cmd
#    #convertCommand = "convert -size 1675x990 xc:transparent -font Arial -pointsize 48 -channel RGBA -gaussian 0x6 -fill black -draw \"text 20,320 '" + message + "'\" " + imageFileName
#    convertCommand = "convert -size 1675x990 xc:transparent -font Arial -pointsize 48 -channel RGBA -gaussian 0x6 -fill black -draw \"text 20,320 '$(cat myfile.txt)'\" " + imageFileName
#    x = system( convertCommand)
#    if x <> 0:
#        print ("Image creation failed. Here is the command: " + convertCommand)
#    else:
#        print ("Image created.")

# Display the image file.
#def display_image( imageFileName = "TelephonePiImage.png"):
#    print ("Displaying image " + imageFileName)
#    command = 'gpicview ' + imageFileName
#    p = Popen( ['gpicview', imageFileName])

# Capture image
#def capture_image():
#    print ("Displaying web page to capture image")
#                # webbrowser.open('http://75.88.44.164:8080/0/action/snapshot')    #
#    result = requests.get('http://75.88.44.164:8080/0/action/snapshot')    #
#    #print result
#    return

# Change understanding of the message
def understanding( message):
    pass

#=======================

f = open( 'lasttweet.txt','r+')
startTime = f.read()
if startTime == '':
    startTime = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

textfile = 'PiFile.txt'
imagefile = 'PiImage.png'
feedname = '#rgt_output'
print ('Starting to monitor for tweets from ' + feedname + ' after ' + startTime)
print ('Press Ctrl-c to stop.')
print ('Waiting',)

while True:
    messages = get_twitter_message( feedname)
    message =''
    for s in messages:
        if ( str(s.created_at) > startTime):
            sn = s.user.screen_name
            message = s.text.replace( "#rgt_output", "") # remove #rgt_output from the message
            message = message.replace( "'", "\\'") # escape the apostrophe
            message = message.replace( '"', '\\"') # escape the double-qoute
            nlp = message.find( ' ', 60)
            if ( nlp > 0):
                message = message[:nlp] + ' \\n ' + message[nlp+1:]
            # print "separated message: " + message
            print ("\nA new message was received which was created at " + str(s.created_at) + ":\n\"" + message + '"')
            #understanding( message)
#            create_image( message, textfile, imagefile)
#            display_image( imagefile)
            time.sleep(1.5)
#            capture_image()

            #system( 'rmIfFile.txt')

            startTime = str(s.created_at)
            f.seek(0) # set write position to beginning of file
            x = f.write( startTime)
            f.close() # need to close the file to force the data to be saved
            f = open( 'lasttweet.txt','r+')
            print ("\nWaiting for next message",)
        # end of if (str( s.created...
    # end of for loop
    print ('.',)
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        print ("\nEnding process")
        sys.exit(0)
