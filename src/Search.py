import requests
import os, sys, getopt, traceback, time
import Helper

VIDEO_INDEXER_ACCOUNT = None
VIDEO_INDEXER_API_KEY = None
VIDEO_INDEXER_LOCATION = None
API_URL = "https://api.videoindexer.ai"
QUERY = None

def main(argv):
    ParseArgs(argv)

    if VIDEO_INDEXER_ACCOUNT and VIDEO_INDEXER_API_KEY and VIDEO_INDEXER_LOCATION and QUERY:
        account_access_token = Helper.GetAccessToken(API_URL, VIDEO_INDEXER_LOCATION, VIDEO_INDEXER_ACCOUNT, VIDEO_INDEXER_API_KEY)
        
        search_result = Helper.SearchQuery(API_URL, VIDEO_INDEXER_LOCATION, VIDEO_INDEXER_ACCOUNT, account_access_token, QUERY)

        print("Search Results:")
        print(search_result.json())
        
    else:
        Usage()
        sys.exit


def Usage(msg=None):
    print ("Search.py -q <account id> -k <api Key> -l <indexer location> -q <query>")
    if msg:
        print (msg)

def ParseArgs(argv):
    global VIDEO_INDEXER_ACCOUNT, VIDEO_INDEXER_API_KEY, VIDEO_INDEXER_LOCATION, QUERY
    try:
        opts, args = getopt.getopt(argv, "ha:k:l:q:", ["accountId=", "apiKey=", "indexerLocation=", "query="])

        for opt, arg in opts:
            if opt == '-h':
                #Usage()
                sys.exit
            elif opt in ("-a", "--accountId"):
                VIDEO_INDEXER_ACCOUNT = arg
            elif opt in ("-k",  "--apiKey"):
                VIDEO_INDEXER_API_KEY = arg
            elif opt in ("-l", "--indexerLocation"):
                VIDEO_INDEXER_LOCATION = arg
            elif opt in ("-q", "--query"):
                QUERY = arg

    except:
        Usage("Error: {0}".format(traceback.print_exc()) )
        sys.exit(2)

main(sys.argv[1:])