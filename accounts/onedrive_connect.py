from __future__ import print_function

from pathlib import Path

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from accounts.onedrive import OneDrive
from errors.errors import AuthError

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.appdata',
          'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.metadata',
          'https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.photos.readonly', 'https://www.googleapis.com/auth/drive.readonly']
CLIENT_SECRET_FILE = 'gdrive_id.json'
APPLICATION_NAME = 'OmniSync'
CREDENTIAL_DIR = Path.home() / '.omnisync' / 'auth' / 'onedrive'


def authenticate(account: OneDrive = None) -> OneDrive:
    Path.mkdir(CREDENTIAL_DIR, parents=True, exist_ok=True)
    if account:
        credential_path = CREDENTIAL_DIR / (account.email + '.json')
    else:
        credential_path = CREDENTIAL_DIR / 'temp.json'

    store = Storage(str(credential_path))
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)

    if not credentials:
        raise AuthError("could not obtain authorization.")

    service = discovery.build('drive', 'v3', http=credentials.authorize(httplib2.Http()))

    about = service.about().get(
        fields='user(id,emailAddress)').execute()

    user = about.get('user')

    if not account:
        credential_path.rename(CREDENTIAL_DIR / (user.get('emailAddress') + '.json'))

    account = OneDrive.parse_user(account, service)

    return account


if __name__ == '__main__':
    authenticate()
