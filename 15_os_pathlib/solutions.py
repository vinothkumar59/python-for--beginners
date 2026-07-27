import os
from pathlib import Path

print(os.getcwd())

print(os.listdir())

folder = Path("test")

folder.mkdir(exist_ok=True)

print(folder.exists())

file = Path("sample.txt")

file.write_text("Hello")

print(file.read_text())

print(file.stat().st_size)

print(file.is_file())

print(folder.is_dir())

print(file.resolve())

file.unlink()

folder.rmdir()