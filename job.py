import datetime
f = open("results.txt", "w")
f.write(f"Results at: {datetime.datetime.now()}")
f.close()