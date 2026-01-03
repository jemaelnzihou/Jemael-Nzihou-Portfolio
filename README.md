# Data Science Portfolio

# 📊 Project 1: Oath–Outcome Alignment Analysis

### *From Constitutional Promises to Measurable Outcomes*

---

## 📌 Project Overview

This project applies **data science, statistical modeling, and natural language processing (NLP)** to evaluate whether **real-world institutional outcomes align with the constitutional obligations defined in official government oaths**.

Public institutions in the United States—military, law enforcement, judiciary, and civil government—derive their authority from oaths sworn to the U.S. Constitution. While these oaths establish clear legal and ethical obligations, there is limited quantitative research measuring how closely **institutional behavior aligns with those commitments**.

This project addresses that gap by converting **normative legal principles into measurable signals** and comparing them against **observed institutional outcomes**.

---

## 🎯 Research Question

> **Do institutional outcomes align with the constitutional obligations defined in official oaths?**

---

## 🧠 Why This Matters

* Converts **normative constitutional law** into **quantifiable metrics**
* Bridges **law, ethics, governance, and data science**
* Moves beyond anecdotal accountability toward **evidence-based oversight**
* Rarely studied quantitatively in academic or policy literature

This work is relevant to:

* Oversight bodies
* Inspectors General
* Civil rights organizations
* Policy analysts
* Academic researchers

---

## 🏗️ Project Architecture

### Conceptual Framework

```text
Oath Language
   ↓
Legal Obligations
   ↓
Accountability Mechanisms
   ↓
Observed Institutional Outcomes
   ↓
Oath–Outcome Alignment
```

---

## 📂 Data Sources

### 1. Oath Obligations (Normative Data)

Derived from official oath texts and legal interpretations for:

* Military
* Law Enforcement
* Judiciary
* Civil & Elected Government

**Features extracted**

* Constitutional priority
* Lawful-order constraints
* Impartiality requirements
* Civil rights emphasis
* Accountability mechanisms
* Scope of authority

---

### 2. Outcome Data (Empirical Data)

| Institution     | Example Data Sources                                  | Outcome Indicators                   |
| --------------- | ----------------------------------------------------- | ------------------------------------ |
| Law Enforcement | DOJ Civil Rights Division, police misconduct datasets | Civil rights violations, settlements |
| Military        | Court-martial records                                 | Unlawful orders, UCMJ violations     |
| Judiciary       | Ethics boards, disciplinary actions                   | Bias, misconduct, reversals          |
| Government      | Congressional ethics investigations                   | Ethics violations, sanctions         |

---

## 📐 Core Metric: Oath–Outcome Alignment Score (OOAS)

A novel metric introduced in this project.

```text
OOAS = Expected Constitutional Compliance − Observed Violations
```

### Interpretation

* **Positive score** → Strong alignment between oath and outcomes
* **Near zero** → Mixed or inconsistent alignment
* **Negative score** → Systemic accountability gaps

---

## 🔬 Methodology

* **Text Analysis (NLP)**

  * Oath language extraction
  * Constraint density and clarity scoring
* **Feature Engineering**

  * Accountability strength
  * Power–constraint ratios
* **Statistical Modeling**

  * Regression analysis
  * Institutional comparison
* **Visualization**

  * Heatmaps
  * Radar charts
  * Trend analysis

---

## 📊 Deliverables

* 📄 Research paper (academic / policy-oriented)
* 📈 Interactive dashboard (Power BI / Tableau / Dash)
* 🧪 Reproducible codebase
* 📁 Structured datasets
* 📘 Documentation and methodology notes

---

## 🗂️ Repository Structure

```text
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── oath_text_analysis.ipynb
│   ├── outcome_analysis.ipynb
│
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── modeling.py
│
├── dashboards/
│
├── docs/
│   ├── methodology.md
│   ├── limitations.md
│
└── README.md
```

---

## ⚖️ Ethics & Limitations

* This project **does not assign individual guilt**
* Focuses on **institutional patterns**, not personal attribution
* Outcome data may be incomplete or uneven across institutions
* Correlation ≠ causation (addressed through robustness checks)

---

## 🚀 Future Work

* Causal inference (policy reforms, oversight interventions)
* Time-series analysis of accountability trends
* Cross-national comparison of oath frameworks
* Expanded NLP using transformer models (BERT)

---

## 👤 Author

**Jemael Nzihou**
PhD Student — Data Science
Background in Chemical Engineering, Business Analytics, and Governance
Focus: decision-making, accountability systems, and data-driven public oversight

---

## 📜 License

This project is released for **research and educational use**.
Please cite appropriately if used in academic or policy work.

