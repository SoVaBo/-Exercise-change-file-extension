from pathlib import Path


root = Path('files')
fpaths = root.glob("**/*") 
newsuf = ".csv"
for path in fpaths:
  if path.is_file():
    newfpath = path.with_suffix(newsuf)
    path.rename(newfpath)