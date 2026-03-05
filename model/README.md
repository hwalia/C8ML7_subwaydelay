### Random Forest vs. XGBoost — Summary of Findings

---

## 1. Model Performance

| Metric | Random Forest | XGBoost |
|--------|--------------|---------|
| MAE (minutes) | 2.0151 | 1.9871 |
| RMSE (minutes) | 2.6552 | 2.6252 |
| MAPE (%) | 41.61% | 40.76% |
| R² | 0.1066 | 0.1267 |
| Best CV MAE | 2.0560 | 2.0123 |

**XGBoost** outperforms **Random Forest** across all metrics, though the margins are small (MAE difference of ~0.03 minutes). Both models are practically similar in accuracy.

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


## 5. Plot Model Interpretation and Discussion (XGboost)

![Importance](../Images\XGboostImportancePlot.png)

The XGBoost feature importance analysis indicates that operational variables, particularly `code_enc`, are the dominant drivers of subway delay predictions. Temporal features such as `hour`, `peak_hour`, and station-related variables also contribute meaningfully, while broader seasonal indicators like `month` and `is_weekend` have comparatively smaller effects. This suggests that delay severity is influenced more by incident type and immediate operating conditions than by long-term seasonal patterns.

![RD](../Images\XGboostResidualDistribution.png)

The residual distribution shows that most prediction errors are concentrated within a small range, indicating reasonable performance for typical delay events. However, the distribution is slightly right-skewed, with a long positive tail, suggesting the model tends to underpredict extreme delay cases. This highlights a limitation in capturing rare but high-impact disruptions.

![SHAP](../Images\XGboostSHAP.png)

The SHAP analysis reinforces these findings by providing insight into both the magnitude and direction of feature effects. Incident code, time of day, and station characteristics consistently demonstrate the strongest global influence on predictions. Overall, the model captures key operational drivers of delay but may require further tuning or additional features to better model extreme events.