import hashlib
import os
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List, Union

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.elements import and_
from sqlalchemy.sql.schema import Index, ForeignKeyConstraint, ForeignKey
from sqlalchemy.sql.sqltypes import Time

from errors.errors import AuthError
from util import constants

Base = declarative_base()


class Config(Base):
    __tablename__ = 'config'

    name = Column(String, primary_key=True)
    value = Column(Integer)

    def __repr__(self):
        return "<Config(id='{0!s}', value='{1!s}')>".format(self.name, self.value)


class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = (Index('account_unique_idx', 'email', 'type', unique=True),)

    fake_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    local_root = Column(String, nullable=False)
    selective_enabled = Column(Boolean, nullable=False)
    selective_partial_new = Column(Boolean, nullable=False)
    folder_mime_type = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    usage = Column(Integer, nullable=False)
    usage_in_drive = Column(Integer, nullable=False)
    max_upload_size = Column(Integer, nullable=False)
    max_import_size = Column(Integer)
    last_changes_seen_flag = Column(String, nullable=False)
    connection_handler = None
    import_types_map = dict()
    export_types_map = dict()

    __mapper_args__ = {
        'polymorphic_identity': 'account',
        'polymorphic_on': type
    }

    def connect(self) -> None:
        pass

    def set_current_last_changes(self) -> None:
        pass

    def download(self, remote_id: str, path: str) -> None:
        pass

    def upload(self, parent_id: str, path: str) -> None:
        pass

    def move(self, remote_id: str, new_parent_id: str) -> None:
        pass

    def delete(self, remote_id: str) -> None:
        pass

    def remote_root(self) -> str:
        pass

    def check_local_changes(self) -> List[dict]:
        pass

    def check_remote_changes(self) -> List[dict]:
        pass

    def list_all_remote_files(self) -> List[dict]:
        pass

    def list_all_local_files(self) -> List[dict]:
        pass

    def initial_sync(self) -> None:
        pass

    def __repr__(self):
        return u"<Account_{0!s}(id='{1!s}', email='{2!s}')>".format(self.type, self.id, self.email)

    @staticmethod
    def authenticate(account):
        pass

    @staticmethod
    def checksum_function(path: Union[Path, str]) -> str:
        pass

    @staticmethod
    def parse_user(obj, connection_handler):
        pass


class AccountFile(Base):
    __tablename__ = 'accountfiles'
    __table_args__ = (
        Index('account_file_id_idx', 'account_id', 'file_account_id', 'file_local_path', unique=True),
        ForeignKeyConstraint(
            ['account_id', 'file_account_parent_id'],
            ['accountfiles.account_id', 'accountfiles.file_account_id']
        )
    )

    account_id = Column(Integer, ForeignKey(Account.fake_id), primary_key=True)
    file_account_id = Column(String, primary_key=True)
    file_account_parent_id = Column(String)
    file_local_path = Column(String, nullable=False)
    file_remote_hash = Column(String)
    file_remote_mime = Column(String, nullable=False)
    file_remote_modified_time = Column(Time, nullable=False)
    file_remote_size = Column(Integer)
    file_remote_version = Column(Integer, nullable=False)
    ignore = Column(Boolean, nullable=False)

    account = relationship(Account, backref='files')
    children = relationship('AccountFile', remote_side=[account_id, file_account_id],
                            backref=backref('parent', remote_side=[account_id, file_account_parent_id]),
                            primaryjoin=and_(
                                account_id == Account.fake_id,
                                account_id == foreign(account_id),
                                file_account_parent_id == foreign(file_account_id)
                            ))

    def __repr__(self):
        return "<AccountFile(path='{0:s}')>".format(self.file_local_path)


class GDrive(Account):
    __tablename__ = 'gdrive'
    __mapper_args__ = {
        'polymorphic_identity': 'GDrive',
    }

    fake_id = Column(String, ForeignKey(Account.fake_id), primary_key=True)

    def connect(self):
        GDrive.authenticate(self)

    def set_current_last_changes(self):
        self.last_changes_seen_flag = self.connection_handler.changes().getStartPageToken().get('startPageToken')

    def list_all_remote_files(self) -> List[dict]:
        result = []
        page_token = None
        files_resource = self.connection_handler.files()
        while True:
            files = files_resource.list(
                pageSize=100,
                orderBy='folder,modifiedTime desc,name',
                q="trashed!=true",
                fields='files(capabilities(canCopy,canEdit,canShare),fullFileExtension,id,lastModifyingUser(' +
                       'displayName,emailAddress,me),md5Checksum,mimeType,modifiedTime,name,ownedByMe,owners(' +
                       'displayName,emailAddress,me),parents,shared,sharedWithMeTime,sharingUser(displayName,' +
                       'emailAddress,me),size,version),nextPageToken',
                pageToken=page_token
            ).execute()
            result.extend(files.get('files'))
            page_token = files.get('nextPageToken')
            if not page_token:
                break
        return result

    @staticmethod
    def checksum_function(path: Union[str, Path]) -> str:
        md5 = hashlib.md5()
        chunk_size = 128 * md5.block_size
        with open(str(path), 'rb') as f:
            for chunk in iter(lambda: f.read(chunk_size), b''):
                md5.update(chunk)
        return md5.hexdigest()

    @staticmethod
    def parse_user(obj: Account, connection_handler) -> Account:
        about_user_response = connection_handler.about().get(
            fields='exportFormats,importFormats,maxImportSizes,maxUploadSize,storageQuota,user'
        ).execute()

        user = about_user_response.get('user')

        if not obj:
            email = user.get('emailAddress')
            obj = GDrive(email=email, local_root=str(constants.OMNISYNC_DEF_SYNC_DIR / 'Google Drive' / email),
                         folder_mime_type='application/vnd.google-apps.folder')

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

    @staticmethod
    def authenticate(account: Account = None):

        scopes = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.appdata',
                  'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.metadata',
                  'https://www.googleapis.com/auth/drive.metadata.readonly',
                  'https://www.googleapis.com/auth/drive.photos.readonly',
                  'https://www.googleapis.com/auth/drive.readonly']
        client_secret_file = 'gdrive_id.json'
        application_name = 'OmniSync'
        credential_dir = constants.OMNISYNC_BASE_CRED_DIR / 'gdrive'

        Path.mkdir(credential_dir, parents=True, exist_ok=True)
        if account:
            credential_path = credential_dir / (account.email + '.json')
        else:
            credential_path = Path(NamedTemporaryFile(delete=False).name)

        store = Storage(str(credential_path))
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(client_secret_file, scopes)
            flow.user_agent = application_name
            credentials = tools.run_flow(flow, store)

        if not credentials:
            raise AuthError("could not obtain authorization.")

        service = discovery.build('drive', 'v3', http=credentials.authorize(httplib2.Http()))

        about = service.about().get(fields='user(emailAddress)').execute()

        user = about.get('user')
        email = user.get('emailAddress')

        if account and account.email != email:
            raise AuthError("user mistmatch.")

        if not account:
            shutil.copyfile(str(credential_path), str(credential_dir / (email + '.json')))
            os.remove(str(credential_path))

        account = GDrive.parse_user(account, service)

        return account


class OneDrive(Account):
    __tablename__ = 'onedrive'
    __mapper_args__ = {
        'polymorphic_identity': 'OneDrive',
    }

    fake_id = Column(String, ForeignKey(Account.fake_id), primary_key=True)

    def connect(self):
        OneDrive.authenticate(self)
