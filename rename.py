import pathlib

i=0
for path in pathlib.Path("traits/Tattoo").iterdir():
    i = i + 1
    if path.is_file():
        old_name = path.stem
        old_extension = path.suffix
        directory = path.parent
        new_name = "tattoo"+str(i)+"#18"+ old_extension
        path.rename(pathlib.Path(directory, new_name))
