import os
import pathlib
import shutil

dir_path = "path"

file_list = []
executables = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        file_list.append(path)

for file in os.listdir(dir_path):
    file_extension = pathlib.Path(file).suffix
    if (file_extension) == ".exe" or file_extension==".EXE":
        path = f"path/{file}"
        dest_path = f"path/Executables/{file}"
        shutil.move(path, dest_path)
    elif (file_extension) == ".pdf":
        path = f"path/{file}"
        dest_path = f"path/PDFs/"
        shutil.move(path, dest_path)
    elif (
        (file_extension) == ".mp3"
        or file_extension == ".mp4"
        or file_extension == ".mkv"
    ):
        path = f"path/{file}"
        dest_path = f"path/Media/"
        shutil.move(path, dest_path)
    elif (
        (file_extension) == ".ppt"
        or file_extension == ".pptx"
        or file_extension == ".pptm"
    ):
        path = f"path/{file}"
        dest_path = f"path/PPTs/"
        shutil.move(path, dest_path)
    elif (
        (file_extension) == ".png"
        or file_extension == ".jpg"
        or file_extension == ".jpeg"
        or file_extension == ".JPG"
        or file_extension == ".PNG"
        or file_extension == ".JPEG"
    ):
        path = f"path/{file}"
        dest_path = f"path/images/"
        shutil.move(path, dest_path)
    elif file_extension==".xlsx" or file_extension==".xls" or file_extension==".csv":
        path=f"path/{file}"
        dest_path = f"path/Spreadsheets/"
        shutil.move(path,dest_path)
    elif file_extension==".txt" or file_extension==".doc" or file_extension==".docx":
        path=f"path/{file}"
        dest_path = f"path/Text_Documents/"
        shutil.move(path,dest_path)
    elif file_extension==".rar" or file_extension==".zip" or file_extension==".tar" or file_extension==".gz":
        path=f"path/{file}"
        dest_path = f"path/Compressed/"
        shutil.move(path,dest_path)
    else:
        if os.path.isdir(dir_path)!=True:
            path=f"path/{file}"
            dest_path = f"path/Miscellaneous/"
            shutil.move(path,dest_path)
