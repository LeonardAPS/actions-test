import paramiko
import pandas as pd
import os
from connector import SFTP  # Import your existing SFTP class here

class SFTPFileManager:
    def __init__(self):
        self.sftp = SFTP()  # Instantiate your existing SFTP class
        self.sftp_conn = self.sftp.connect()

    def get_latest_folder(self):
        folders = self.sftp_conn.listdir()
        latest_folder = max(folders)
        return latest_folder

    def get_file_information(self, folder_name):
        folder_path = os.path.join(self.sftp_conn.getcwd(), folder_name)
        files = self.sftp_conn.listdir(folder_path)
        df = pd.DataFrame(columns=['File Name', 'Call ID', 'File Size'])
        for file in files:
            file_path = os.path.join(folder_path, file)
            file_size = self.sftp_conn.stat(file_path).st_size
            call_id = file.split('_')[1]
            df = df.append({'File Name': file, 'Call ID': call_id, 'File Size': file_size}, ignore_index=True)
        return df

    def get_latest_folder_file_information(self):
        latest_folder = self.get_latest_folder()
        df = self.get_file_information(latest_folder)
        return df

    def close_connection(self):
        self.sftp_conn.close()

