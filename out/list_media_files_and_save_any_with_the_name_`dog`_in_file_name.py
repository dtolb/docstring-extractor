# Example: list media files and save any with the name `dog` in file name 
media_list = api.get_media_files()
for media in media_list:
    if 'dog' in media['mediaName'].lower():
        stream, content_type = api.download_media_file(media['mediaName'])
        with io.open(media['mediaName'], 'wb') as file:
            file.write(stream.read())
