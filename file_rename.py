import os

dir_name = './kasumin_voice/'

for i, filename in enumerate(os.listdir(dir_name), start=1):
    if filename.endswith(".MOV"):
        new_file = f"kasumin_{i}.mov"
        original = os.path.join(dir_name, filename)
        new_path = os.path.join(dir_name, new_file)
        os.rename(original, new_path)
        print(f"{i}: Renamed {filename} to {new_file}")