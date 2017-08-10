import glob, os, shutil

def move_to_backup_dir():
    source_dir = r'C:\Users\sumankalyan\PycharmProjects\MUSIC_DOWNLOADER' #Path where your files are at the moment
    dst = r'C:\Users\sumankalyan\PycharmProjects\MUSIC_DOWNLOADER\BACKUP' #Path you want to move your files to
    files = glob.iglob(os.path.join(source_dir, "*.mp3"))
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dst)
