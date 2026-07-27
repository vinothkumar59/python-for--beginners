"""
Topic : OS & Pathlib

Author : Vinoth Kumar
"""

import os
from pathlib import Path

print("=" * 50)
print("CURRENT DIRECTORY")
print("=" * 50)

print(os.getcwd())

print("=" * 50)
print("LIST DIRECTORY")
print("=" * 50)

for item in os.listdir():
    print(item)

print("=" * 50)
print("CREATE DIRECTORY")
print("=" * 50)

os.makedirs("demo_folder", exist_ok=True)

print("Folder Created")

print("=" * 50)
print("PATHLIB EXISTS")
print("=" * 50)

path = Path("demo_folder")

print(path.exists())

print("=" * 50)
print("IS DIRECTORY")
print("=" * 50)

print(path.is_dir())

print("=" * 50)
print("CREATE FILE")
print("=" * 50)

file = Path("demo.txt")

file.write_text("Welcome to Python")

print(file.exists())

print("=" * 50)
print("READ FILE")
print("=" * 50)

print(file.read_text())

print("=" * 50)
print("FILE SIZE")
print("=" * 50)

print(file.stat().st_size)

print("=" * 50)
print("RENAME FILE")
print("=" * 50)

new_file = Path("python.txt")

if file.exists():
    file.rename(new_file)

print(new_file.exists())

print("=" * 50)
print("DELETE FILE")
print("=" * 50)

if new_file.exists():
    new_file.unlink()

print("File Deleted")

print("=" * 50)
print("DELETE DIRECTORY")
print("=" * 50)

folder = Path("demo_folder")

if folder.exists():
    folder.rmdir()

print("Directory Deleted")

print("=" * 50)
print("OS & PATHLIB COMPLETED")
print("=" * 50)