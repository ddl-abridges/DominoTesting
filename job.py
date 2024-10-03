import datetime
f = open("/mnt/artifacts/results.txt", "w")
f.write(f"Results at: {datetime.datetime.now()}")
f.close()