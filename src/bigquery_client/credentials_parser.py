import os
from google.oauth2 import service_account

from ..constants import DEFAULT_DATASET

class Credentials:
    """
    Class to parse Google Cloud credentials from a JSON file.
    """

    def __init__(self, credentials_file):
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_file)
        self._project_id = self.credentials.project_id
        self._dataset_id = os.getenv("DATASET_ID", DEFAULT_DATASET)

    @property
    def project_id(self):
        return self._project_id
    
    @property
    def dataset_id(self):
        return self._dataset_id
    
