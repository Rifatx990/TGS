import zipfile
import os
import subprocess
import sys

zip_path = "TGscheduler-main.zip"
extract_dir = "TGscheduler-main"

# Extract the zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print(f"Extracted {zip_path} to {extract_dir}")

# Recursively find main.py
main_path = None
for root, dirs, files in os.walk(extract_dir):
    if "main.py" in files:
        main_path = os.path.join(root, "main.py")
        break

if main_path:
    print(f"Running {main_path}...")
    subprocess.run([sys.executable, main_path])
else:
    print("main.py not found in the extracted folder.")
