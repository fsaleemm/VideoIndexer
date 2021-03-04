import requests
import os, sys, getopt, traceback, time
import Helper

VIDEO_INDEXER_ACCOUNT = None
VIDEO_INDEXER_API_KEY = None
VIDEO_INDEXER_LOCATION = None
API_URL = "https://api.videoindexer.ai"
MEDIA_FILE_PATH = None

def main(argv):
    ParseArgs(argv)

    if VIDEO_INDEXER_ACCOUNT and VIDEO_INDEXER_API_KEY and VIDEO_INDEXER_LOCATION and MEDIA_FILE_PATH :
        account_access_token = Helper.GetAccessToken(API_URL, VIDEO_INDEXER_LOCATION, VIDEO_INDEXER_ACCOUNT, VIDEO_INDEXER_API_KEY)
        
        video_id = Helper.UploadFileLocal(MEDIA_FILE_PATH, API_URL, VIDEO_INDEXER_LOCATION, VIDEO_INDEXER_ACCOUNT, account_access_token)

        # Check Status every minutes until processed
        while True:
            index_result = Helper.GetUploadStatus(video_id, API_URL, VIDEO_INDEXER_LOCATION, VIDEO_INDEXER_ACCOUNT, account_access_token)
            processing_state = index_result.json().get("state")

            if processing_state != "Uploaded" and processing_state != "Processing":
                print("Full JSON:")
                print(index_result.json())
                break
            else:
                print("Video has not finished processing. Wait a minute then try again.")
                print("Waiting for 60 seconds before retry ...")
                time.sleep(60)

    else:
        Usage()
        sys.exit


def Usage(msg=None):
    print ("UploadFile.py -a <account id> -k <api Key> -l <indexer location> -f <file path to upload>")
    if msg:
        print (msg)

def ParseArgs(argv):
    global VIDEO_INDEXER_ACCOUNT, VIDEO_INDEXER_API_KEY, VIDEO_INDEXER_LOCATION, MEDIA_FILE_PATH
    try:
        opts, args = getopt.getopt(argv, "ha:k:l:f:", ["accountId=", "apiKey=", "indexerLocation=", "mediaFilePath="])

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
            elif opt in ("-f", "--mediaFilePath"):
                MEDIA_FILE_PATH = arg

    except:
        Usage("Error: {0}".format(traceback.print_exc()) )
        sys.exit(2)

main(sys.argv[1:])