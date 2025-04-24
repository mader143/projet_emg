import zipfile

# List of files to include
files_to_zip = ["equipe_01_main.py", "q1_potentiel.py", "q2_champE.py", "q3_trajectoire.py", "fonctions_communes.py", "devoir_numerique.pdf"]

# Output zip file name
zip_filename = "devoir_num.zip"

# Create the zip file
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in files_to_zip:
        zipf.write(file)

print(f"Created {zip_filename} with: {', '.join(files_to_zip)}")
