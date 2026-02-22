from pathlib import Path
from PIL import Image
import shutil

folder="/Users/hanhhip/Downloads"
album_folder="/Users/hanhhip/Downloads/resizeAlbum"
mv_folder="/Users/hanhhip/Downloads/resizeMV"
mv1_folder="/Users/hanhhip/Downloads/resizeMV1"
dry_run=True #True=print only, False=actually moved

p = Path(folder)
album = Path(album_folder)
mv = Path(mv_folder)
mv1 = Path(mv1_folder)

album.mkdir(exist_ok=True)
mv.mkdir(exist_ok=True)
mv1.mkdir(exist_ok=True)

files=[f for f in p.iterdir() if f.suffix.lower() in [".png",".jpg",".jpeg"]]
print(f"Found {len(files)} images\n")

for img_path in files:
    with Image.open(img_path) as img:
        w, h = img.size

    if abs(w - h) == 0:
        target = album
    elif (w, h) == (1280,720):
        target = mv
    elif (w, h) == (640,480):
        target = mv1
    else:
        print(f"Skipping: {img_path.name} ({w}x{h})")
        continue

    if dry_run:
        print(f"(Dry) Move: {img_path.name} -> {target.name}")
    else:
        shutil.move(img_path, target/img_path.name)
        print(f"Moved: {img_path.name} -> {target.name}")

print("Done.")