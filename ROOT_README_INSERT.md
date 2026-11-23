## Databricks Lakehouse & AI/BI Dashboard — Engineering and Business KPIs

**Live dashboard (Databricks):** [Open Industrial Wastewater Optimization — Engineering & Business KPIs](https://dbc-c0b76d43-142e.cloud.databricks.com/dashboardsv3/01f1e6b686eb133885ed3b67842e0964/published?o=7474660769183521)  
**Original analysis notebook:** [Open `wastewater_optimization.ipynb`](https://github.com/jemaelnzihou/Jemael-Nzihou-Portfolio/blob/main/wastewater_optimization.ipynb)

> **Synthetic case study:** The linked dashboard uses illustrative wastewater-treatment observations; results are not actual plant savings, regulatory compliance evidence, or proof of causality. The Databricks dashboard may require workspace authentication and sharing permissions. Screenshots below provide a static public portfolio preview.

### Data engineering and analytics architecture

```text
Synthetic wastewater data / engineering measurements
                |
                v
Bronze Delta table — raw measurements
                |
                v
Silver Delta table — validated and derived features
                |
                v
Gold Delta table — engineering and cost KPIs
                |
                +--> Databricks SQL --> AI/BI dashboard
                +--> Python / PySpark --> exploratory modeling
                +--> PMP benefits tracking and stakeholder reporting
```

- **Catalog / schema:** `workspace.wastewater_optimization`
- **Bronze:** `bronze_wastewater`
- **Silver:** `silver_wastewater`
- **Gold:** `gold_wastewater_kpis`
- **Practiced skills:** PySpark DataFrames, Delta Lake managed tables, Medallion Architecture, Unity Catalog organization, SQL KPI queries, data transformation, visual business intelligence, dashboard publishing, operational-cost modeling, and benefits realization.
- **AI-era relevance:** The reusable, governed data architecture provides a starting point for anomaly detection, predictive modeling, workload automation, and AI-assisted analysis. The dashboard itself is not proof of a deployed or validated machine-learning system.

### Dashboard results — baseline vs. illustrative pilot

| Indicator | Baseline | Illustrative pilot | Interpretation |
|:---|---:|---:|:---|
| Treatment throughput | 1,500.777 m³/day | 1,503.643 m³/day | Nearly unchanged (+0.19%) |
| Energy intensity | 0.715 kWh/m³ | 0.551 kWh/m³ | Approx. 22.9% lower |
| Chemical cost | $0.281/m³ | $0.136/m³ | Approx. 51.6% lower |
| Effluent quality index | 0.674 | 0.622 | Approx. 7.7% lower; assuming lower is preferable |
| Estimated annual gross savings | — | **~$89,998/year** | Dashboard scenario, not observed savings |
| Simple payback on $160,000 project budget | — | **~1.78 years** | Illustrative ratio before ongoing expenses |

**Business-case reconciliation:** The original project charter contains a **$174,880/year benefit *target*** and a **0.91-year target payback**, based partly on an assumed avoided-rework benefit. The Databricks dashboard instead estimates about **$89,998/year** of simulated energy and reagent savings and a **1.78-year simple payback**. These two scenarios have different assumptions and must not be reported as equivalent or achieved results. The dashboard's two savings components (approximately $10,711 for electricity and $79,286 for chemicals) should be summed once; do not stack the total as a third additional contribution.

### Databricks dashboard screenshots

**Flow and energy intensity —** Similar modeled throughput with reduced energy use per cubic meter.

![Databricks screenshot: wastewater flow and energy intensity by phase](assets/wastewater/dashboard-flow-energy.webp)

**Chemical treatment cost and effluent index —** Illustrative operating-expense improvement and the accompanying treatment quality index.

![Databricks screenshot: chemical cost and effluent quality charts](assets/wastewater/dashboard-chemical-quality.webp)

**Annual operating expenses and savings —** Modeled financial outcome and component-level savings visualization; see the double-counting note above.

![Databricks screenshot: annual operating costs and savings](assets/wastewater/dashboard-financial.webp)

### Source README previews supplied with the project

These four captures document the project's existing GitHub README presentation. The Markdown source remains the authoritative, editable description.

<details>
<summary>View four README screenshots</summary>

![Portfolio README screenshot 1](assets/wastewater/readme-preview-01.webp)

![Portfolio README screenshot 2](assets/wastewater/readme-preview-02.webp)

![Portfolio README screenshot 3](assets/wastewater/readme-preview-03.webp)

![Portfolio README screenshot 4](assets/wastewater/readme-preview-04.webp)

</details>

### Project management and career relevance

This extension connects **chemical engineering metrics** to **data engineering**, **business intelligence**, and **PMP-style reporting**: baselines, control metrics, KPI verification, cost-benefit evaluation, risk communication, and stakeholder-ready visual reporting. Future extensions can include project milestones, earned value, anomaly detection, sensor streaming, and verified engineering acceptance criteria.
