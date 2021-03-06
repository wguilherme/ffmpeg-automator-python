import os
import fnmatch
import sys

codecVideo = '-c:v libx264 '
crf = '-crf 25 '
preset = '-preset veryfast '
codecAudio = '-c:a aac -ac 2 '
bitrateAudio = '-b:a 128k '
newExtension = '.mp4'

config = codecVideo + crf + preset + codecAudio + bitrateAudio

fromPath = '/Users/wguilherme/Downloads/records'

for root, folders, files in os.walk(fromPath):
    for file in files:
        if file.endswith(('.mov')):
            fullPath = os.path.join(root, file)
            fileName, fileExtension = os.path.splitext(file)
            newFileName = fileName + '_converted' + newExtension
            exportFile = os.path.join(root, newFileName)
            command = f'ffmpeg -i "{fullPath}" {config} "{exportFile}"'
            print(command)
            os.system(command)
