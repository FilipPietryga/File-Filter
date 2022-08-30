import shutil, os
import os.path

DOCUMENT = "document"
VIDEO = "video"
MUSIC = "music"
IMAGE = "image"
PROGRAM = "program"
PRESENTATION = "presentation"
WEBSITE = "website"
GIF = "gifs"
ARCHIVE = "archive"
SCRIPT = "scripts"
VIRTUAL = "virtual computers"
DATA = "data"
LIBRARIES = "libraries"
VECTOR = "vector"

DOCUMENT_FORMATS = ("txt", "html", "pdf", "odt", 
                    "xls", "xlsx", "doc", "docx", 
                    "html", "pdf", "odt", "md")

PRESENTATION_FORMATS = ("ppt", "pptx")

WEBSITE_FORMATS = ("html", "css", "js", "tsx", 
                  "scss", "sass", "jsx", "ts")

IMAGE_FORMATS =  ("bmp", "gif", "jpeg", "jpg", 
                  "png", "psd", "raw",  "tif", 
                  "tiff","tif", "eps", "indd")

GIF_FORMATS = ("gif")

VECTOR_FORMATS = ("svg", "ai")

MUSIC_FORMATS =  ("aiff", "alac", "dsd", "flac", 
                  "mp3", "ogg", "pcm", "wav", 
                  "3gp", "acc")

VIDEO_FORMATS =  ("aiff", "alac", "dsd", "flac",
                  "ogg", "pcm", "wav", "yuv"
                  "3gp", "amv", "asf", "avi",
                  "drc", "f4a", "f4b", "flv",
                  "gflv", "m4p", "mkv", "mng",
                  "mov", "mp2", "mp4", "mpg",
                  "mpe", "viv", "rnxf", "mpeg",
                  "vob", "viv", "webm", "wmv",
                  "f4p", "f4v", "gifv", "m4v",
                  "mxf", "ogv", "rm", "prproj")

PROGRAM_FORMATS =  ("exe", "bin", "com", "cpl", 
                    "ins", "job", "msc", "jse", 
                    "msi", "msp", "paf", "scr", 
                    "sct", "vb",  "u3p", "ws", 
                    "wsf", "wsh", "app", "dat")

SCRIPT_FORMATS = ("bat", "vbs", "wsf"
                  "asp", "cmd", "vbe", "vbscript")

ARCHIVE_FORMATS =  ("rar", "zip", "shar", "iso", "ibr",
                    "tar", "sbx", "br", "gz", "iz",
                    "iz4", "izo", "izma", "sz", "z",
                    "zst", "7z", "s7z", "apk",
                    "arc", "wsf", "cpt", "dmg",
                    "gca", "hki", "kgb", "jar",
                    "pit", "rk", "pim", "sfx",
                    "shk", "sit", "sqx", "tgz",
                    "tar.Z", "tar.bz2", "tbz2",
                    "tar.lz", "tlz", "tar.xz", "txz",
                    "tar.zst", "uca", "uha", "war",
                    "xar", "xp3", "yz1", "zipx",
                    "zz", "ecc", "par", "par2")

VIRTUAL_FORMATS =  ("vdi", "iso")

DATA_FORMATS = ("json", "xml", "data")

LIBRARIES_FORMATS = ("lib", "dll", "hpp", "h")

DOCUMENT_FOLDER_NAME = "dokumenty"
PRESENTATION_FOLDER_NAME = "dokumenty/prezentacje"
WEBSITE_FOLDER_NAME = "dokumenty/strony"
IMAGE_FOLDER_NAME = "obrazy"
GIF_FOLDER_NAME = "obrazy/gify"
VECTOR_FOLDER_NAME = "obrazy/wektory"
MUSIC_FOLDER_NAME = "muzyka"
VIDEO_FOLDER_NAME = "wideo"
PROGRAM_FOLDER_NAME = "programy"
SCTIPT_FOLDER_NAME = "programy/skrypty"
LIBRARIES_FOLDER_NAME = "programy/biblioteki"
ARCHIVE_FOLDER_NAME = "archiwum"
VIRTUAL_FOLDER_NAME = "komputery wirtualne"
DATA_FOLDER_NAME = "dane"

def moveFileIntoDir(destination):
  print("log: file has been moved to: " + destination)
  def closure(file): 
    shutil.move(file, destination)
  return closure

def switchDir(filetype):
  print("log: file has its destination switched")
  dictionary = {
    DOCUMENT: moveFileIntoDir(DOCUMENT_FOLDER_NAME),
    PRESENTATION: moveFileIntoDir(PRESENTATION_FOLDER_NAME),
    WEBSITE: moveFileIntoDir(WEBSITE_FOLDER_NAME),
    VIDEO: moveFileIntoDir(VIDEO_FOLDER_NAME),
    MUSIC: moveFileIntoDir(MUSIC_FOLDER_NAME),
    IMAGE: moveFileIntoDir(IMAGE_FOLDER_NAME),
    GIF: moveFileIntoDir(GIF_FOLDER_NAME),
    PROGRAM: moveFileIntoDir(PROGRAM_FOLDER_NAME),
    SCRIPT: moveFileIntoDir(SCTIPT_FOLDER_NAME),
    ARCHIVE: moveFileIntoDir(ARCHIVE_FOLDER_NAME),
    VIRTUAL: moveFileIntoDir(VIRTUAL_FOLDER_NAME),
    DATA: moveFileIntoDir(DATA_FOLDER_NAME),
    LIBRARIES: moveFileIntoDir(LIBRARIES_FOLDER_NAME),
    VECTOR: moveFileIntoDir(VECTOR_FOLDER_NAME)
  }
  return dictionary.get(filetype, lambda: "error: unsupported file type")

print("log: program started")

os.chdir(".")

def createDir(path):
  if os.path.isdir(path):
      print(path + " exists")
  else:
      print(path + " doesn't exists")
      os.mkdir(path)

createDir("dokumenty")
createDir("dokumenty/prezentacje")
createDir("dokumenty/strony")
createDir("obrazy")
createDir("obrazy/gify")
createDir("obrazy/wektory")
createDir("wideo")
createDir("muzyka")
createDir("programy")
createDir("programy/skrypty")
createDir("programy/biblioteki")
createDir("archiwum")
createDir("komputery wirtualne")
createDir("dane")

for filename in os.listdir('./'):
  print("log: file has been opened")
  extension = os.path.splitext(filename)[1][1:]
  dictionary = {
    DOCUMENT_FORMATS: 
      switchDir(DOCUMENT),
      
    PRESENTATION_FORMATS: 
      switchDir(PRESENTATION),
      
    WEBSITE_FORMATS: 
      switchDir(WEBSITE),
    
    IMAGE_FORMATS: 
      switchDir(IMAGE),
      
    GIF_FORMATS: 
      switchDir(GIF),
    
    MUSIC_FORMATS: 
      switchDir(MUSIC),
    
    VIDEO_FORMATS: 
      switchDir(VIDEO),
      
    PROGRAM_FORMATS: 
      switchDir(PROGRAM),
      
    SCRIPT_FORMATS: 
      switchDir(SCRIPT),
      
    ARCHIVE_FORMATS: 
      switchDir(ARCHIVE),
      
    VIRTUAL_FORMATS: 
      switchDir(VIRTUAL),
      
    DATA_FORMATS:
      switchDir(DATA),
      
    LIBRARIES_FORMATS:
      switchDir(LIBRARIES),
      
    VECTOR_FORMATS:
      switchDir(VECTOR)
  }
  
  dictionary = {key: value for keys, value in dictionary.items() for key in keys}

  dictionary.get(extension, lambda _: "error: unsupported extension")(filename)