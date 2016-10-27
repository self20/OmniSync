from __future__ import print_function
import httplib2
import os

from pathlib import Path
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from accounts.account import Account

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'OmniSync'


def get_credentials(account: Account = None):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = Path.home()
    credential_dir = home_dir / '.omnisync' / 'gdrive'
    if account:
        credential_dir = credential_dir / account.name
    Path.mkdir(credential_dir, exist_ok=True)
    credential_path = os.path.join(credential_dir, account.name if account else 'temp.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))
