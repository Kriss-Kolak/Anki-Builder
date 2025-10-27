import os

class Audio_File:

    def __init__(self, content, hash_id, file_path):
        self.content = content
        self.hash_id = hash_id
        self.file_path = file_path
        self.is_created = self._check_is_created()
    
    def _check_is_created(self) -> bool:
        if os.path.exists(self.file_path):
            return True
        return False