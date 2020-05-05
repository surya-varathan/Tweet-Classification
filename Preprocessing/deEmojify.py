file1 = open("Tweets.csv","r")

data = file1.read()

out = data.encode('ascii','ignore').decode('ascii')

print(out)

file2 = open("Tweets1.csv","w")

file2.write(out)

file1.close()
file2.close()

