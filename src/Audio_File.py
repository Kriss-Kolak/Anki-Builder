import os
from src.utils import hash_string_list
from config.config import AUDIO_FILE_EXTENSION

class Audio_File:

    def __init__(self, content: str, hash_id: str, file_path: str):
        self.content: str = content
        self.hash_id: str = hash_id
        self.file_path: str = file_path
        self.is_created: bool = self._check_is_created()


    def _check_is_created(self) -> bool:
        return os.path.exists(self.file_path)
                
    def __str__(self):
        return f"""
                <------------------------------> \n
                Audio_File \n
                Content: {self.content} \n
                Hash_id: {self.hash_id} \n
                File_path: {self.file_path} \n
                Is_created: {self.is_created} \n
                <------------------------------> \n
                """
    

def get_Audio_Files_list(content_list: list[str], deck_audio_folder: str) -> list[Audio_File]:
    
    if len(content_list) == 0:
        raise Exception("Content list is empty")
    
    Audio_Files_list: list[Audio_File] = []

    hash_list = hash_string_list(content_list)

    

    for content, hash_id in zip(content_list, hash_list):
        file_path = os.path.join(deck_audio_folder, hash_id + AUDIO_FILE_EXTENSION)
        obj = Audio_File(content, hash_id, file_path)
        Audio_Files_list.append(obj)

    return Audio_Files_list

def get_Audio_Files_paths(Audio_Files: list[Audio_File]) -> list[str]:
    audio_files_paths: list[str] = []
    for audio_file in Audio_Files:
        audio_files_paths.append(audio_file.file_path)
    return audio_files_paths