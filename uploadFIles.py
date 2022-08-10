import os
from re import L 
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:

                localpath = os.path.join(root, filename)
            
                relative_path = os.path.realpath(localpath, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BHwHgP8COB839w1_T5i2l-HP4-FRexJg3EC7HI9SOMV7hTveJRUfH5m5PCAxG2C8ebcKT4nPY3_mrzhDLyRUhRnpzw3rsd-EZkZAUIzVupQkSV61yeliCOlQWlolFa8iNo-rylk'
    transferData = TransferData(access_token)

    file_from = str("Enter the folder path to transfer : -")
    file_to = str("File has been moved")

main()

    