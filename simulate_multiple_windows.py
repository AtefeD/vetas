import json
import os
import subprocess
from datetime import datetime, timedelta

start_date_0 = '2008-05-30T00:00:00'
n_days = 21

for i in range(n_days):
    start_date = datetime.fromisoformat(start_date_0) + timedelta(days=i)
    end_date = datetime.fromisoformat(start_date_0) + timedelta(days=i + 1)


    with open('./input/args.json', 'r') as fh:
        dict = json.load(fh)
        dict["start_date"] = start_date.isoformat()
        dict["end_date"] = end_date.isoformat()
    with open('./input/args_sim.json', 'w') as fh:
        json.dump(dict, fh, indent=True)


    proc = subprocess.call('etas-run ./input/args_sim.json', shell=True)


