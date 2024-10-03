import datetime
f = open("results.txt", "w")
f.write("Results at: ", datetime.datetime.now())
f.close()