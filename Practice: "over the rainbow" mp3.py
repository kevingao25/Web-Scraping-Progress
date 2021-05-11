import requests

res = requests.get("https://static.pandateacher.com/Over%20The%20Rainbow.mp3")
mp3 = res.content

# Return response in binary
music = open("rainbow.mp3", 'wb')

# Store mp3 into music file
music.write(mp3)

# Close the file
music.close()