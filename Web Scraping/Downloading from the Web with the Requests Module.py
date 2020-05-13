import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt') #downloads the file at this link
print(res.status_code) #returns status code e.g. 401, 404, 200
# 200 --> everything okay
# 401 --> unauthorized error
# 404 --> page not found

print(len(res.text)) #res.text holds a string of the entire play
# line returns length

res.raise_for_status() #raise an exception if there was an error with running the file, do nothing if everything fine

playFile = open("RomeoAndJuliet.txt", "wb") #needs it to be in write-binary mode to maintain the unicode style of the text
for chunk in res.iter_content(100000): #iter_content returns chunks of the content (100000) --> number of bytes per iteraction
    playFile.write(chunk)

playFile.close()
