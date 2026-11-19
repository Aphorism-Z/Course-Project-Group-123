from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"

df = pd.read_excel(RAW / "API_NY.GDP.MKTP.CD_DS2_en_csv_v2_512.xlsx", header=4)
print(df.shape)


