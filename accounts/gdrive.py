import hashlib
from pathlib import Path
from typing import List, Union

from accounts import gdrive_connect
from accounts.account import Account


class GDrive(Account):
    def __init__(self, ident: str, email: str, local_root: Path):
        super().__init__(email, local_root)
        self.max_import_sizes = dict()
        self.import_types_map = dict()
        self.export_types_map = dict()
        self.folder_mime_type = 'application/vnd.google-apps.folder'

    def connect(self):
        gdrive_connect.authenticate(self)

    def set_current_last_changes(self):
        self.last_changes_seen_flag = self.connection_handler.changes().getStartPageToken().get('startPageToken')

    def list_all_remote_files(self) -> List[dict]:
        result = []
        page_token = None
        files_resource = self.connection_handler.files()
        while True:
            files = files_resource.list(pageSize=100, orderBy='folder,modifiedTime desc,name',
                                        q="trashed!=true",
                                        fields='files(capabilities(canCopy,canEdit,canShare),fullFileExtension,id,' +
                                               'lastModifyingUser(displayName,emailAddress,me),md5Checksum,mimeType,' +
                                               'modifiedTime,name,ownedByMe,owners(displayName,emailAddress,me),' +
                                               'parents,shared,sharedWithMeTime,sharingUser(displayName,emailAddress,' +
                                               'me),size,version),nextPageToken', pageToken=page_token).execute()
            result.extend(files.get('files'))
            page_token = files.get('nextPageToken')
            if not page_token:
                break
        return result

    def checksum_function(self, path: Union[str, Path]) -> str:
        md5 = hashlib.md5()
        chunk_size = 128 * md5.block_size
        with open(str(path), 'rb') as f:
            for chunk in iter(lambda: f.read(chunk_size), b''):
                md5.update(chunk)
        return md5.hexdigest()

    @staticmethod
    def parse_user(obj, connection_handler) -> Account:
        about_user_response = connection_handler.about().get(
            fields='exportFormats,importFormats,' +
                   'maxImportSizes,maxUploadSize,storageQuota,user').execute()

        user = about_user_response.get('user')

        if not obj:
            email = user.get('emailAddress')
            obj = GDrive(email, Path.home() / 'OmniSync' / 'Google Drive' / email)

        obj.connection_handler = connection_handler

        obj.name = user.get('displayName')
        obj.import_types_map = about_user_response.get('importFormats')
        obj.export_types_map = about_user_response.get('exportFormats')
        obj.max_upload_size = about_user_response.get('maxUploadSize')
        obj.max_import_sizes = about_user_response.get('maxImportSizes')

        quota = about_user_response.get('storageQuota')
        obj.usage = quota.get('usage')
        obj.usage_in_drive = quota.get('usageInDrive')
        obj.capacity = quota.get('limit')

        return obj
