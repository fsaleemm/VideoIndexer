# Video Indexer

This repository contains sample python scripts for using the Video Indexer API to Upload media file and search for text.

There is introduction to the [FFmpeg tool](https://ffmpeg.org/) to inspect the video/audio files and convert to VideoIndexer supported codecs.

## Prerequisites

1) Create a Video Indexer Account using the steps [here](https://docs.microsoft.com/en-us/azure/media-services/video-indexer/connect-to-azure).

1) Make a note of your Account ID.

1) Make note of the Indexer Location. We used a trial version in the instructions below.

1) Subscribe to the Video Indexer API by following steps [here](https://docs.microsoft.com/en-us/azure/media-services/video-indexer/video-indexer-use-apis#subscribe-to-the-api).

1) Make a note of the Primary API Key.

1) Install [Visual Studio Code](https://code.visualstudio.com/).

1) Install the Python extension by following the instructions [here](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Executing Python scripts 

Clone the repository and follow the below instructions to execute the python scripts. Look through the python scripts to see example of calling the Video Indexer API.

### Upload Media File

Execute the [UploadFile.py](src/UploadFile.py).

~~~bash
 python src/UploadFile.py -a <account id> -k <api Key> -l <indexer location> -f <file path to upload> 
~~~

For example:

~~~bash
python src/UploadFile.py -a aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee -k abcdefg12345 -l trial -f data/beach_waves_narrated.mp4 
~~~

The script will upload the media file and then check for processing status every minute until processed and outputs the Full JSON response from the API will all the insights.

![](images/ss1.PNG)

If you log in to the [Video Indexer Portal](https://www.videoindexer.ai/), and go to Media Files. You should see the upload and indexing progress.

![](images/ss2.PNG)

### Search for Text

Execute the [Search.py](src/Search.py).

~~~bash
 python src/Search.py -a <account id> -k <api Key> -l <indexer location> -q <query> 
~~~

For example:

~~~bash
python src/Search.py -a aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee -k abcdefg12345 -l trial -q "coronado"
python src/Search.py -a aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee -k abcdefg12345 -l trial -q "coronado beach" 
~~~

Results are returned in JSON format. 

~~~bash
{'results': [{'accountId': 'aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee', 'id': '368b37c2b4', 'partition': 'default', 'externalId': None, 'metadata': None, 'name': 'None', 'description': 'None', 'created': '2021-03-03T22:25:39.151+00:00', 'lastModified': '2021-03-03T22:31:33.081+00:00', 'lastIndexed': '2021-03-03T22:25:44.172+00:00', 'privacyMode': 'Private', 'userName': 'Farhat Saleem', 'isOwned': True, 'isBase': True, 'hasSourceVideoFile': True, 'state': 'Processed', 'moderationState': 'OK', 'reviewState': 'None', 'processingProgress': '100%', 'durationInSeconds': 13, 'thumbnailVideoId': '368b37c2b4', 'thumbnailId': '49671fad-b4a7-4414-b0a5-d14cb628dc1f', 'searchMatches': [{'startTime': '00:00:00', 'type': 'Transcript', 'text': "Here's a few shots of the waves in Coronado Beach", 'exactText': 'Coronado'}, {'startTime': '00:00:00', 'type': 'NamedLocation', 'text': 'Coronado Beach', 'exactText': 'Coronado'}], 'indexingPreset': 'Default', 'streamingPreset': 'Default', 'sourceLanguage': 'en-US', 'sourceLanguages': ['en-US'], 'personModelId': '00000000-0000-0000-0000-000000000000'}], 'nextPage': {'pageSize': 25, 'skip': 0, 'done': True}}
~~~

## FFMPEG

1) Download the [FFmpeg tool](https://ffmpeg.org/download.html).

1) Extract the download tool to a directory of your choice.

### Inspecting Video/Audio Files

1) Run the tool from the installation directory and provide as input the video/audio file.

~~~code
ffmpeg.exe -i <path_to_video/audio_file>
~~~

For example:
~~~cmd
ffmpeg.exe -i ..\..\VideoIndexer\data\beach_waves_narrated.mp4
~~~

Output:

![](images/ss3.PNG)

### Converting Video/Audio Files

The FFMPEG tool [documentation](https://ffmpeg.org/ffmpeg.html) has details of converting files. Below are just a few examples that worked for some files that had problem with transcribing using the VideoIndexer during our testing.

You can force a specific codec to the input files if the codec is unkown:

~~~code
ffmpeg.exe -f <codec to enforce> -i <path to input file> <path to output file>
~~~

For example:
~~~code
ffmpeg.exe -f act -i ..\data\14967.wav ..\data\z.mp4
~~~

To force specific codec to the audio stream:

~~~code
ffmpeg.exe -acodec <codec to enforce> -i <path to input file> <path to output file>
~~~

For example:
~~~cmd
ffmpeg.exe -acodec g729 -i ..\data\14968.wav ..\data\a.mp4
~~~

To force specific codec and add filters (-af):

~~~cmd
ffmpeg.exe -acodec g729 -i ..\data\14967.wav -af "afftdn=nf=-25" ..\data\a.mp4
~~~