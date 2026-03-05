import billboard
import pandas as pd
from datetime import datetime, timedelta

start_date = datetime(2010, 1, 2)  ## Must be on a Saturday
end_date = datetime(2000, 1, 1)

rows = []
current_date = start_date

while current_date >= end_date:
    try:
        chart = billboard.ChartData('hot-100', date=current_date.strftime("%Y-%m-%d"))

        for entry in chart[:10]:
            rows.append({
                "week": chart.date,
                "rank": entry.rank,
                "title": entry.title,
                "artist": entry.artist
            })

        print(f"Processed week: {chart.date}")

        ## Move back one week
        current_date -= timedelta(weeks=1)

    except Exception as e:
        print(f"Error on {current_date}: {e}")
        current_date -= timedelta(weeks=1)

df_billboard = pd.DataFrame(rows)
df_billboard.to_csv("billboard_top10.csv", index=False)

print("Done. Total rows:", len(df_billboard))