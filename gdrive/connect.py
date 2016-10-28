from __future__ import print_function
import httplib2
import os

from pathlib import Path
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from accounts.account import Account

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.appdata',
          'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.metadata',
          'https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.photos.readonly', 'https://www.googleapis.com/auth/drive.readonly']
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
    credential_dir = home_dir / '.credentials'  # / '.omnisync' / 'gdrive'
    # if account:
    #    credential_dir = credential_dir / account.name
    Path.mkdir(credential_dir, exist_ok=True)
    credential_path = credential_dir / 'temp.json'

    store = Storage(str(credential_path))
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + str(credential_path))
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
        pageSize=100, orderBy='folder,modifiedTime desc,name', q="trashed!=true",
        fields='files(capabilities(canCopy,canEdit,canShare),fullFileExtension,id,' +
               'lastModifyingUser(displayName,emailAddress,me),md5Checksum,mimeType,modifiedTime,name,ownedByMe,' +
               'owners(displayName,emailAddress,me),parents,shared,sharedWithMeTime,' +
               'sharingUser(displayName,emailAddress,me),size,version),nextPageToken', ).execute()

    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(item)


if __name__ == '__main__':
    main()
