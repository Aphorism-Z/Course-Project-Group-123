from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent.parent
raw = root / "data" / "raw"
results = root / "results"

files = {
    "gdp": "API_NY.GDP.MKTP.CD_DS2_en_csv_v2_512.xlsx",
    "life_exp": "API_SP.DYN.LE00.IN_DS2_en_csv_v2_1528.xlsx",
    "elec": "API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_987.xlsx"
}

def load(name):
    df = pd.read_excel(raw / files[name], header=4)
    df.columns = [str(int(c)) if isinstance(c, (int,float)) else c for c in df.columns]
    return df
def year_columns(df):
    return [c for c in df.columns if c.isdigit()]
def long_format(df,name):
    out = df.melt(id_vars = ["Country Code, Country Name"], value_vars=year_columns(df),
                  var_name = "year", value_name = name)
    out['year'] = out['year'].astype(int)
    return out.dropna(subset=[name])
def main():
    results.mkdir(exist_ok=True)
    data = {name: load(name) for name in files}
    report = ['# Raw data quality report', '']
    for name, df in data.items():
        print(name, df.shape, df.columns[:6].tolist(), year_columns(df)[:10])
    (results / "quality_report_raw.md").write_text("\n".join(report), encoding="utf-8")
if __name__ == "__main__":
    main()


