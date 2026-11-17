import os

try:
    import mysql.connector
except:
    print("Please install mysql.connector on your client!")
    exit()

# Start Connection
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="advaymysql123",
  database="audio_files"
)

cursor = conn.cursor()

# Find Latest Versison
cursor.execute("SELECT filename,created_at from files where id = 1")
for x in cursor:
    version,versiontime = int(x[0]),x[1]

# Find installed version
v = int(open("app_version.txt", "r").read())
print("Your Current Version:",v)

# If Newer Version Present
if version > v:
    print("Found a newer version:",version,versiontime,".\nDeleting older version audio files.")
    all = [file for file in os.listdir("audiotts") if os.path.isfile(os.path.join("audiotts", file))]
    for x in all:
        os.remove("audiotts/"+x)
    print("Downloading new files now.")
    cursor.execute("SELECT audio_data,filename FROM files where id > 1")
    i = 0
    for x in cursor:
        i += 1
        with open("audiotts/"+x[1], 'wb') as file:
            file.write(x[0])
    else:
        print("Saved",i,"audio files")

    # Update installed version
    f = open("app_version.txt", "w")
    f.write(str(version))
    f.close()
    print("Update Successful!")
else:
    print("You're up to date!\nYou have the latest version of audio files")
    print("No Update Required")

# Close connnection
cursor.close()
conn.close()
