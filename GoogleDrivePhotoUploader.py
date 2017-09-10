

#------------------------------------------------------------------------------
#
#   Requirements: rclone  -  https://rclone.org/
#               : rclone is already configured with a remote called 
#               : GoogleDrive
#                
#------------------------------------------------------------------------------



import os, subprocess

# PHOTO_DIR = '/srv/samba/Pictures/010_PhotoAlbums'

PHOTO_DIR = '/srv/samba/Documents_Charl/Other/Temp/TestFolder'


def upload_photos():

    for root, dirs, files in os.walk(PHOTO_DIR):
        for fname in files:
            album_name = (os.path.basename(os.path.normpath(root)))
            print ("proccsing " + album_name + ": " + fname)
            subprocess.run (["rclone", "copy", root, "GoogleDrive:" + \
                "Google Photos/" + album_name])


if __name__=='__main__':
    
    upload_photos()
