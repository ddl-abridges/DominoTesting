import datetime
import os
artifacts_path = "/mnt/artifacts/"
results_path = os.path.join(parent_dir, "results01")
os.mkdir(results_path)

f = open("/mnt/artifacts/results01/results.txt", "w")
f.write(f"Results at: {datetime.datetime.now()}")
f.close()