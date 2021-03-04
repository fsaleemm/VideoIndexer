import sys, getopt, requests

def GetAccessToken(api_url, location, account_id, api_key):
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    
    access_token_url = "{0}/auth/{1}/Accounts/{2}/AccessToken?allowEdit=true".format(api_url, location, account_id)
    
    access_token_result = requests.get(access_token_url, headers=headers)
    account_access_token = access_token_result.json()

    return account_access_token

def UploadFileLocal(video_path, api_url, location, account_id, account_access_token, video_name = None, video_description = None):
    form_data = {'file': open(video_path, 'rb')}
    
    return UploadMedia(video_path, api_url, location, account_id, account_access_token, form_data, video_name, video_description)
    
def UploadMedia(video_path, api_url, location, account_id, account_access_token, form_data, video_name = None, video_description = None):
    base_url = "{0}/{1}/Accounts/{2}".format(api_url, location, account_id)
    
    video_upload_url = "{0}/Videos?accessToken={1}&name={2}&description={3}&privacy=private&partition=default".format(base_url, account_access_token, video_name, video_description)
    
    upload_result = requests.post(video_upload_url, files=form_data)
    video_id = upload_result.json().get("id")
    return video_id

def GetUploadStatus(video_id, api_url, location, account_id, account_access_token):
    base_url = "{0}/{1}/Accounts/{2}".format(api_url, location, account_id)
    video_index_url = "{0}/Videos/{1}/Index?accessToken={2}&language=English".format(base_url, video_id, account_access_token)

    index_result = requests.get(video_index_url)
    return index_result

def SearchQuery(api_url, location, account_id, account_access_token, query):
    search_query_string = "query={0}".format(query)
    base_url = "{0}/{1}/Accounts/{2}".format(api_url, location, account_id)
    search_url = "{0}/Videos/Search?accessToken={1}&{2}".format(base_url, account_access_token, search_query_string)

    search_result = requests.get(search_url)
    return search_result

