# TTC Subway Delay Prediction
### Random Forest vs. XGBoost — Summary of Findings

---

## 1. Model Performance

| Metric | Random Forest | XGBoost | Winner |
|--------|--------------|---------|--------|
| MAE (minutes) | 2.0151 | 1.9871 | XGBoost ✅ |
| RMSE (minutes) | 2.6552 | 2.6252 | XGBoost ✅ |
| MAPE (%) | 41.61% | 40.76% | XGBoost ✅ |
| R² | 0.1066 | 0.1267 | XGBoost ✅ |
| Best CV MAE | 2.0560 | 2.0123 | XGBoost ✅ |

XGBoost outperforms Random Forest across all metrics, though the margins are small (MAE difference of ~0.03 minutes). Both models are practically similar in accuracy.

---

## 2. What Both Models Agree On

Despite being different algorithms, both models point to the same conclusions:

- **`code_enc` (delay code)** is the most important predictor — the type of incident (mechanical, passenger, signal, etc.) is the strongest signal for how long a delay will last.
- **`station_enc`** also carries meaningful weight — certain stations are associated with systematically longer or shorter delays.
- **Time-based features** (`hour`, `weekday`, `peak_hour`) have modest but consistent influence across both models.
- **`Temp (°C)`** and `week`/`month` features contribute relatively little predictive power.

---

## 3. Key Findings

### MAE ~2 minutes — both models are practically close
XGBoost (MAE: 1.9871) edges out Random Forest (MAE: 2.0151) by just 0.03 minutes. In real-world terms, both models predict delay duration to within about 2 minutes on average.

### RMSE reveals similar error on large delays
RMSE of ~2.63–2.66 minutes shows neither model struggles significantly with outlier delays, and XGBoost handles them marginally better.

### MAPE is inflated by short delays
The ~41% MAPE looks alarming but is misleading. Many delays are only 1–3 minutes long, so even a 1-minute error produces a large percentage. MAE is the more reliable measure of practical accuracy.

### R² is low but consistent across both models
R² of 0.11–0.13 means both models explain only about 10–13% of the variance in delay duration. This reflects a genuinely hard prediction problem — many factors that affect delay length (crew response, track conditions) are not in the dataset.

### Cross-validation MAE closely matches test MAE
Both models show Best CV MAE and Test MAE within ~0.03 minutes of each other (e.g. XGBoost: 2.0123 vs 1.9871), confirming neither model is overfitting and both generalise well to unseen data.

---

## 4. Recommendation

XGBoost is the recommended model. For future improvement, consider adding lag features such as recent delay history at the same station or line, which could meaningfully increase predictive power beyond what static features alone can provide.
