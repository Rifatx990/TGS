import zipfile
import os
import subprocess
import sys

# Path to your zip file
zip_path = "TGscheduler-main.zip"

# Directory to extract
extract_dir = "TGscheduler-main"

# Step 1: Extract the zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print(f"Extracted {zip_path} to {extract_dir}")

# Step 2: Run main.py
main_path = os.path.join(extract_dir, "main.py")

if os.path.exists(main_path):
    print(f"Running {main_path}...")
    # Use the same Python interpreter
    subprocess.run([sys.executable, main_path])
else:
    print("main.py not found in the extracted folder.")
