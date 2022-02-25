from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from PIL import Image
from PIL.ExifTags import TAGS

def list_media():
    """
    Returns a list of all names of media.
    """
    _, filenames = FileSystemStorage().listdir("")
    return list(filenames)
def media_delete(name):
    """
    Returns True if the media deleted else return False
    """
    if name in list_media():
        fss = FileSystemStorage()
        fss.delete(name)
        return True
    return False

def media_save(name, image):
    """
    Returns media url after saving
    """
    fss = FileSystemStorage()
    file = fss.save(name, image)
    file_url = fss.url(file)
    return file_url

def media_info(pathName):
    image = Image.open(pathName)
    width, height = image.size
    exifdata = image.getexif()
    imageDate = {}
    imageDate['width'] = width
    imageDate['height'] = height
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
        imageDate[tag] = data
    return imageDate
