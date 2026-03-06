## Master files (reference)

### `data/master/ttc_delay_code_description.csv`

| Column | Type | Example | Description |
|---|---:|---|---|
| id | integer | 1 | internal id |
| CODE | string | EUAC | TTC delay code short id |
| DESCRIPTION | string | AIR CONDITIONING | Full description of the code |

Purpose: authoritative mapping from TTC codes to human readable descriptions.

---

### `data/master/ttc_subway_station_master.csv`

| Column | Type | Example | Description |
|---|---:|---|---|
| station | string | Finch | Canonical station name |
| line | string | Yonge-University | Line name |
| location | string | North York | Borough / area |
| grade | string | Underground | Station structure/type |

Purpose: canonical station metadata used for joins and grouping.

---

## Processed datasets (data dictionary)

### `data/processed/mapping_ttc_delay_code.csv`

| Column | Type | Example | Description |
|---|---:|---|---|
| delay_code | string | MUSC | Raw code as found in source data |
| row_count | integer | 22482 | Frequency in the dataset |
| mapped_delay_code | string | MUSC | Mapped/normalized code |
| fuzzy_score | integer | 100 | Fuzzy-match score used during mapping |
| include_code | integer (0/1) | 1 | Flag to include this code in analysis |
| remarks | string | (optional) | Manual notes about mapping decisions |

Purpose: keep track of code normalization and filtering decisions.

---

### `data/processed/mapping_ttc_station.csv`

| Column | Type | Example | Description |
|---|---:|---|---|
| station | string | KENNEDY BD STATION | Raw station text from source |
| station_clean | string | KENNEDY BD | Short/clean tokenized station text |
| row_count | integer | 9893 | Frequency |
| mapped_station | string | Kennedy | Canonical mapped station name |
| score | integer | 95 | Matching score |
| include_station | integer (0/1) | 1 | Include this station in analysis |
| remarks | string | BD is for Bloor Danforth | Optional notes |

Purpose: document station normalization and mapping decisions.

---

### `data/processed/ttc_subway_delay_data_combined.csv` (core event dataset)

This is the cleaned, canonical event-level file used for analysis and modelling.

| Column | Type | Example | Description |
|---|---:|---|---|
| date | date (YYYY-MM-DD) | 2024-01-01 | Event date |
| time | hh:mm | 02:00 | Event time |
| day | string | Monday | Day of week |
| station | string | SHEPPARD STATION | Station text as recorded |
| code | string | MUI | Delay code |
| delayed_minutes | integer | 0 | Delay length |
| gap_minutes | integer | 0 | Service gap length |
| bound | string | N | Direction (N/S/E/W or empty) |
| line | string | YU | Line code |
| vehicle | integer | 5491 | Vehicle id (if available) |
| year | integer | 2024 | Year extracted from date |
| datetime | timestamp | 2024-01-01 02:00:00 | Combined timestamp |
| hour | integer | 2 | Hour of day |
| weekday | integer | 0 | Weekday indicator (dataset-specific) |
| is_weekend | integer | 0 | Weekend indicator |
| month | integer | 1 | Month number |
| week | integer | 1 | Week number |
| peak_hour | integer (0/1) | 0 | Peak hour flag |

Sample row:
```
2024-01-01,02:00,Monday,SHEPPARD STATION,MUI,0,0,N,YU,5491,2024,2024-01-01 02:00:00,2,0,0,1,1,0
```

Purpose: use this file as the baseline event table for aggregations and simple analyses.

---

### `data/processed/ttc_subway_delay_data_obt.csv`

This file extends the combined dataset with mapping metadata (station and code mapping results) used for quality checks.

Principal additional columns (beyond `combined`):
- `mapped_station`, `station_score`, `include_station`, `station_remarks`
- `delay_code`, `mapped_delay_code`, `fuzzy_score`, `include_code`, `delay_code_remarks`
- `line_clean`, `bound_clean`

Truncated sample (event + mapping fields):
```
2024-01-01,02:08,Monday,DUNDAS STATION,MUPAA,4,10,N,YU,6051,2024,2024-01-01 02:08:00,2,0,0,1,1,0,Dundas West,90,1.0,,MUPAA,MUPAA,100,1.0,,Bloor-Danforth,N
```

Purpose: helpful when you need to inspect mapping choices alongside events.

---

### `data/processed/ttc_subway_delay_data_weather_obt.csv`

This is the `obt` dataset joined to hourly weather observations (taken from `data/raw/csv/toronto_weather_data/*`). It contains the event fields, mapping metadata and appended weather columns such as temperature, precipitation, wind, visibility and station pressure.

Event/mapping prefix columns are the same as `ttc_subway_delay_data_obt.csv`. Weather columns appended (examples):

`Longitude (x),Latitude (y),Station Name,Climate ID,Date/Time (LST),Year,Month,Day,Time (LST),Flag,Temp (°C),Temp Flag,Dew Point Temp (°C),Dew Point Temp Flag,Rel Hum (%),Precip. Amount (mm),Wind Dir (10s deg),Wind Spd (km/h),Visibility (km),Stn Press (kPa),Hmdx,Wind Chill,Weather`

Sample row (truncated):
```
2024-01-01,02:08,Monday,DUNDAS STATION,MUPAA,4,10,N,YU,6051,2024,2024-01-01 02:00:00,2,0,0,1,1,0,...,-79.4,43.63,TORONTO CITY CENTRE,6158359,2024-01-01 02:00:00,2024,1,1,02:00,,-1.2,...,0.0,...,3.0,...,24.0,...,4.8,...,100.79,...,Snow
```

Purpose: use this file for analyses that require weather context per event.

---

## Raw files

### `data/raw/TTC Subway Delay Data since 2025.csv`

| Column | Type | Example | Description |
|---|---:|---|---|
| _id | integer | 1 | Original row id in the extract |
| Date | date | 2025-01-01 | Event date |
| Time | hh:mm | 02:10 | Event time |
| Day | string | Wednesday | Day of week |
| Station | string | BATHURST STATION | Station text |
| Code | string | MUSAN | TTC delay code |
| Min Delay | integer | 5 | Reported delay minutes |
| Min Gap | integer | 9 | Reported gap minutes |
| Bound | string | E | Direction |
| Line | string | BD | Line code |
| Vehicle | integer | 5227 | Vehicle id |

Notes: raw extracts may have different column names/casing than the processed files. The processing pipeline normalizes these fields into the `processed/` datasets.

---

### `data/raw/csv/toronto_weather_data/` (many `YYYY_M.csv` files)

All weather CSVs share the same columns. Example header (from `2014_1.csv`):

| Column | Description |
|---|---|
| Longitude (x) | longitude of weather station |
| Latitude (y) | latitude of weather station |
| Station Name | station label |
| Climate ID | numeric station id |
| Date/Time (LST) | local timestamp (YYYY-MM-DD hh:mm) |
| Year,Month,Day,Time (LST) | split timestamp parts |
| Flag | quality flag |
| Temp (°C) | air temperature |
| Temp Flag | quality flag for temp |
| Dew Point Temp (°C) | dew point |
| Dew Point Temp Flag | flag |
| Rel Hum (%) | relative humidity |
| Precip. Amount (mm) | hourly precipitation |
| Wind Dir (10s deg) | wind direction (tenths of degrees) |
| Wind Spd (km/h) | wind speed |
| Visibility (km) | visibility |
| Stn Press (kPa) | station pressure |
| Hmdx | humidex |
| Wind Chill | wind chill |
| Weather | text weather summary (e.g., Snow) |

Purpose: hourly weather observations used to enrich event records. Files are named by year and month (e.g. `2014_1.csv` = January 2014).

---

## How to work with this data

- For regular analysis, use `data/processed/ttc_subway_delay_data_combined.csv` (or the `*_obt.csv` variants if you need mapping/debug metadata).
- Use `data/master/*` to map codes or to add station-level metadata.
- If you add files that should be ignored, add patterns to `.gitignore` and untrack previously tracked files (example):

```bash
# stop tracking a single file but keep it locally
git rm --cached path/to/file
git commit -m "stop tracking path/to/file"

# re-index and re-add respecting .gitignore
| 2023 | 22,949 | 14 | 177 |
| 2024 | 26,467 | 22 | 125 |
| 2025 | 25,713 | 18 | 131 |
```

## Next steps / optional extras
- I can produce a machine-readable `data/data_dictionary.json` containing this same information.
- I can append per-file row counts and small previews (first 3 rows) for every CSV in the `data/` tree if you want more exhaustive documentation.

---

If you want me to add row counts and the first few sample rows for every file (including all `toronto_weather_data` files), say "yes, include previews" and I'll append them.
| 2026* | 2,478 | 8 | 100 |

*Note: 2026 appears to contain partial-year data.*

---

## Notes on the Data

- Each row represents a **single delay incident**.
- Delay codes correspond to operational issues such as mechanical failures, signal problems, passenger incidents, or external factors.
- The `Min Delay` field indicates the **duration of the delay**, while `Min Gap` represents the **service disruption gap** created between trains.
- Some stations or operational locations may appear with slightly different naming conventions across years.

---

## Potential Applications

This dataset can support analyses such as:

- Transit reliability studies
- Delay trend analysis over time
- Station-level delay hotspots
- Operational incident categorization
- Predictive modeling of subway delays

---

## Source

Data originates from the **Toronto Transit Commission (TTC)** delay reporting system and has been compiled into yearly datasets.