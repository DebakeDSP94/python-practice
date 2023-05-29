import requests

# Get the response from the API endpoint.

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
response.raise_for_status()
# 200

playFile = open('RomeoAndJuliet.txt', 'wb')
# Create a new file in write binary mode.
# The wb argument for the open() function
# opens the file in write binary mode.
# This will let you edit the file, but it
# keeps the existing file unchanged.

# Loop over the response object’s iter_content() method.
# Call write() on each iteration to write the content to the file.
for chunk in response.iter_content(100000):
    playFile.write(chunk)

playFile.close()
# Close the file to ensure that the last chunk
# is written to the file.
