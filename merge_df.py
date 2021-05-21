import pandas as pd
import glob

filelist = [i for i in glob.glob("*.csv")]

combined_csv = pd.concat([pd.read_csv(f, dtype=str) for f in filelist])

combined_csv.to_csv("allusernames.csv")