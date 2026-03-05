# TTC Subway Delay Dataset (2024–2026)

## Data Overview

This dataset contains recorded subway delay incidents for the Toronto Transit Commission (TTC) between **2024 and 2026**. Each record represents a reported delay event and includes temporal information, operational details, and categorical delay codes describing the cause of the incident.

The dataset consists of yearly CSV files containing individual delay events across TTC subway lines and stations.

---

## Dataset Files

The dataset contains one file per year:

- `ttc-subway-delay-data-2024.csv`
- `ttc-subway-delay-data-2025.csv`
- `ttc-subway-delay-data-2026.csv`

Additional documentation files:

- `ttc-subway-delay-codes.xlsx` – descriptions of TTC delay codes
- `ttc-subway-delay-data-readme.xlsx` – official dataset documentation

---

## Data Structure

Each dataset contains the same columns describing the delay event.

| Field | Description |
|------|-------------|
| Date | Date of the delay event (e.g., 2024-01-01)|
| Time | Time when the delay was reported (e.g., 02:22)|
| Day | Day of the week (e.g., Monday)|
| Station | Station where the delay occurred (e.g., BLOOR STATION)|
| Code | TTC delay code describing the cause of the delay (e.g., MUPAA)|
| Min Delay | Length of delay in minutes (e.g., 5)|
| Min Gap | Service gap created by the delay in minutes (e.g., 9)|
| Bound | Direction of travel (e.g., N, S, E, W) |
| Line | Subway line identifier (e.g., BD)|
| Vehicle | Vehicle number associated with the delay (e.g., 5227) |

---

## Dataset Summary

| Year | Number of Records | Unique Lines | Unique Delay Codes |
|------|-------------------|--------------|--------------------|
| 2014 | 20,424 | 11 | 159 |
| 2015 | 21,474 | 17 | 162 |
| 2016 | 21,162 | 16 | 165 |
| 2017 | 18,885 | 20 | 177 |
| 2018 | 20,737 | 15 | 184 |
| 2019 | 19,222 | 23 | 185 |
| 2020 | 14,782 | 22 | 184 |
| 2021 | 16,370 | 17 | 173 |
| 2022 | 19,895 | 21 | 179 |
| 2023 | 22,949 | 14 | 177 |
| 2024 | 26,467 | 22 | 125 |
| 2025 | 25,713 | 18 | 131 |
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