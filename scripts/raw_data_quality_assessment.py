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
    out = df.melt(id_vars = ["Country Code", "Country Name"], value_vars=year_columns(df),
                  var_name = "year", value_name = name)
    out['year'] = out['year'].astype(int)
    return out.dropna(subset=[name])

def assess_completeness(name,df):
    years = year_columns(df)
    missing = df[years].isna()
    per_year = missing.mean()
    per_year.rename("missing_share").rename_axis("year").to_csv(results / f"missing_by_year_{name}.csv")
    empty_years = per_year[per_year == 1].index.tolist()
    nodata = df.loc[missing.all(axis=1), ["Country Code", "Country Name"]]

    df.assign(missing_years=missing.sum(axis=1))[["Country Code", "Country Name", "missing_years"]] \
      .to_csv(results / f"missing_by_record_{name}.csv", index=False)

    lines = [
        f"{name}: completeness", "",
        f"- Records: {len(df)}, year columns: {len(years)}",
        f"- Ovr missing pct: {missing.mean().mean():.1%}",
        f"- Years w no data in any record: {len(empty_years)}" + (f"({empty_years[0]} to {empty_years[-1]})" if empty_years else ""),
        f"- Records w no data in any year: {len(nodata)}",
    ]
    if len(nodata) > 0:
        lines.append(" -" + ", ".join(nodata["Country Name"]))
    lines.append("")
    return lines

def assess_timeliness(name,df):
    years = year_columns(df)
    hasdata = df[years].notna()
    populated = [int(y) for y in years if hasdata[y].any()]
    release = pd.read_excel(raw / files[name]).iloc[2,1]
    last3 = hasdata[years[-3:]].sum().to_dict()
    return [
        f"{name}: timeliness", "",
        f"- Release date: {release}",
        f"- First / Last year data shown: {min(populated)} / {max(populated)}",
        f"- Records w data in past 3 yrs: {last3}",
        "",
    ]

def assess_consistency(data):
    codes = {n: set(d["Country Code"]) for n, d in data.items()}
    same_codes = len({frozenset(s) for s in codes.values()}) == 1
    dupes = {n: int(d["Country Code"].duplicated().sum()) for n, d in data.items()}
    base = data["gdp"][["Country Code", "Country Name"]]
    name_diffs = {}
    for n in ("life_exp", "elec"):
        m = base.merge(data[n][["Country Code", "Country Name"]], on="Country Code", suffixes = ("", "_other"))
        name_diffs[n] = int((m["Country Name"] != m["Country Name_other"]).sum())
    base.to_csv(results / "records_for_agg_review.csv", index=False)
    return [
        "CONSISTENCY ACROSS DATASETS", "",
        f"- Same set of country codes in all files: {same_codes}",
        f"- Dupe country codes per file: {dupes}",
        f"- Country names that differ from the GDP file: {name_diffs}",
        "",
    ]

rules = {
    "gdp": lambda v: v <= 0,
    "life_exp": lambda v: (v < 20) | (v > 90),
    "elec": lambda v: (v < 0) | (v > 100),
}
def assess_accuracy(name, df):
    long = long_format(df, name).sort_values(["Country Code", "year"])
    low, high = long.loc[long[name].idxmin()], long.loc[long[name].idxmax()]
    long["pct_change"] = long.groupby("Country Code")[name].pct_change()
    jumps = long[long["pct_change"].abs() > 0.5]
    jumps.to_csv(results / f"large_jumps_{name}.csv", index=False)
    return [
        f"- {name}: accuracy", "",
        f"- Lowest value: {low[name]} ({low['Country Name']}, {low['year']})",
        f"- Highest value: {high[name]} ({high['Country Name']}, {high['year']})",
        f"- Yearly changes above 50%: {len(jumps)}",
        "",
    ]
def main():
    results.mkdir(exist_ok=True)
    data = {name: load(name) for name in files}
    report = ['# Raw data quality report', '']
    for name, df in data.items():
        print(name, df.shape, df.columns[:6].tolist(), year_columns(df)[:10])
        report += assess_completeness(name,df)
        report += assess_timeliness(name,df)
        report += assess_consistency(data)
        report += assess_accuracy(name,df)
    (results / "quality_report_raw.md").write_text("\n".join(report), encoding="utf-8")
if __name__ == "__main__":
    main()


