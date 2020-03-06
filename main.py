import os
import fnmatch
import sys

comando_ffmpeg = 'ffmpeg'
codecVideo = '-c:v libx264'
crf = '-crf 23'
preset = '-preset fast'
codecAudio = '-c:a aac'
bitrateAudio = '-b:a 320k'
newExtension = '.mp4'

fromPath = '/Users/wguilherme/Downloads/records'

for root, folders, files in os.walk(fromPath):
    for file in files:
        if file.endswith(('.mov', '.mp4')):
            fullPath = os.path.join(root, file)
            fileName, fileExtension = os.path.splitext(file)
            newFileName = fileName + '_converted' + newExtension
            exportFile = os.path.join(root, newFileName)
            command = f'{comando_ffmpeg} -i "{fullPath}" ' \
                f'{codecVideo} {crf} {preset} {codecAudio} {bitrateAudio} "{exportFile}"'
            os.system(command)
