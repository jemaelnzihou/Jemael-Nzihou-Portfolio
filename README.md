Great portfolio — the content is strong, it just needs **structural and stylistic consistency** so it reads like a **cohesive GitHub flagship README**, not stitched sections.

Below is a **cleaned, consistent, and unified version** that:

* Uses **one hierarchy** of headings
* Standardizes **project naming, emojis, and tone**
* Keeps **technical rigor** while improving readability
* Makes each project feel part of a **Data Science + Engineering program**, not standalone notes

You can paste this directly as your **root `README.md`**.

---

# 📊 Data Science Projects

### *Engineering-Driven Analytics, Physics-Aware AI, and Real-World Systems Modeling*

This repository showcases a curated set of **data science, AI, and engineering analytics projects** spanning:

* Chemical & thermal systems
* Manufacturing & semiconductor processes
* Reliability & survival analysis
* Data center operations
* Communication & network performance
* Governance & institutional accountability

Each project integrates **domain physics, statistical reasoning, and machine learning** to support **decision-making in complex real-world systems**.

---

## 🧠 Project 1 — Physics-Informed Neural Networks (PINNs)

### *Heat Transfer Modeling in Chemical Reactors*

### 🔍 Overview

This project implements a **Physics-Informed Neural Network (PINN)** to solve the **1D transient heat diffusion equation**:

[
\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}
]

Unlike purely data-driven models, PINNs embed **first-principles physics directly into the learning process**, enabling accurate predictions with **sparse or noisy data**.

---

### 🎯 Problem Statement

Traditional numerical methods (FDM, FVM, CFD) are computationally expensive for:

* Iterative design
* Real-time optimization
* Digital-twin deployment

This project demonstrates how **PINNs act as fast, physics-consistent surrogate models** for transient heat transfer problems in chemical reactors.

---

### ⚗️ Chemical Engineering Context

Temperature profiles govern:

* Reaction kinetics (Arrhenius behavior)
* Catalyst activity and degradation
* Hot-spot formation
* Thermal runaway risk

PINNs preserve **physical fidelity** while enabling **machine-learning acceleration**.

---

### 📐 Governing Equations

**Heat diffusion (1D, transient):**
[
T_t = \alpha T_{xx}
]

**Boundary conditions:**
[
T(0,t) = 0,\quad T(1,t) = 0
]

**Initial condition:**
[
T(x,0) = \sin(\pi x)
]

**Analytical validation solution:**
[
T(x,t) = e^{-\alpha \pi^2 t} \sin(\pi x)
]

---

### 📊 Data & Assumptions

**Assumptions**

* One-dimensional conduction
* Constant thermal properties
* No internal heat generation (baseline case)

**Training inputs**

* Physics collocation points
* Boundary and initial condition points
* Optional sparse sensor data

---

### 🧠 Model Development

* Neural network: Multi-Layer Perceptron (MLP)
* Inputs: spatial coordinate (x), time (t)
* Output: temperature (T(x,t))

**Loss components**

* PDE residual loss
* Boundary condition loss
* Initial condition loss
* Optional data loss

---

### 📈 Results & Interpretation

Outputs include:

* Loss convergence curves
* PINN vs analytical temperature profiles
* Absolute error heatmaps
* Quantitative metrics (RMSE, max error)

Results are stored in the `results/` directory.

---

### 💼 Business & Operational Impact

**Chemical & Industrial**

* Hot-spot detection
* Reduced sensor requirements
* Faster design iteration

**Data Centers**

* Thermal digital twins
* Cooling optimization (CRAC/CRAH, liquid loops)

**Energy & Aerospace**

* Lightweight thermal solvers
* Rapid what-if analysis

---

### 🔮 Future Extensions

* 2D / 3D geometries
* Convection & reaction heat generation
* Inverse problems (estimate ( \alpha ), heat flux)
* Reinforcement-learning-based control
* Streamlit or cloud dashboards

---

## 🌡️ Project 2 — Dynamic Temperature & Velocity Analysis

### *Heat Exchangers and Chemical Reactors*

### Overview

This project applies **EDA, physics-based simulation, and predictive analysis** to study **thermal and fluid dynamic behavior** in:

* Heat exchangers
* Chemical reactors

**Key goals**

* Monitor system stability
* Detect deviations
* Support operational decisions

---

## 📊 Project 3 — Photolithography Yield Risk Prediction

### *AI-Driven Pass/Fail Modeling for Semiconductor Manufacturing*

This project develops an **explainable AI model** to predict **manufacturing yield risk** using the SECOM semiconductor dataset.

**Highlights**

* High-dimensional, imbalanced industrial data
* Ensemble learning (Random Forest)
* ROC-AUC improvement from ~0.64 → ~0.78
* Explainability via sensor importance
* Drift monitoring using PSI

---

## 🛠 Project 4 — Reliability Analysis & Survival Modeling

### *Kaplan–Meier, Hazard Functions, and Batch Comparison*

Focuses on **time-to-failure modeling** using:

* Kaplan–Meier survival estimation
* Censoring analysis
* Hazard function comparison

Applied to **manufacturing batch reliability assessment**.

---

## ⚖️ Project 5 — Oath–Outcome Alignment Analysis

### *From Constitutional Promises to Measurable Outcomes*

A unique project combining **data science, NLP, and policy analytics** to quantify alignment between **constitutional oaths** and **institutional outcomes**.

Uses:

* Radar charts
* Heatmaps
* Distribution analysis

---

## 🏢 Project 6 — Data Center Insights

### *Operational Intelligence, Reliability, and Performance Optimization*

Applies engineering-aware analytics to:

* Thermal behavior
* Power consumption
* Communication latency

Directly relevant to **modern hyperscale data centers**.

---

## 📡 Project 7 — Wi-Fi Optimization & Communication Performance

### *Signal Quality, Reliability, and Network Efficiency*

Analyzes:

* SNR vs BER relationships
* Spatial Wi-Fi coverage quality
* Throughput optimization

Grounded in **communication theory and network engineering**.

---

## 👤 Author

**Jemael Nzihou**
PhD Student — Data Science
Chemical Engineer | Business Analytics | Quality Champion

🔗 Portfolio: [https://jemaelnzihou.github.io/Jemael-Nzihou-Portfolio/](https://jemaelnzihou.github.io/Jemael-Nzihou-Portfolio/)
🔗 LinkedIn: [https://www.linkedin.com/in/jemaelnzihou](https://www.linkedin.com/in/jemaelnzihou)

---

## 📜 License

Released for **research and educational use**.
Please cite appropriately if used in academic or professional work.

---
# Data Science Projects

#  📊 Project 1 - Physics-Informed Neural Networks (PINNs) for Heat Transfer Modeling in Chemical Reactors

This repository implements a **Physics-Informed Neural Network (PINN)** to solve the **1D transient heat diffusion equation**:

\[
\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}
\]

with Dirichlet boundary conditions and an initial condition.  
Unlike purely data-driven models, PINNs embed **first-principles physics directly into the learning process**, enabling accurate solutions even with sparse or noisy data.

---

## 📌 Problem Statement

Traditional numerical methods such as **Finite Difference (FDM)**, **Finite Volume (FVM)**, or **Computational Fluid Dynamics (CFD)** can be computationally expensive and slow, especially for:

- Iterative design
- Real-time optimization
- Digital twin deployment

This project demonstrates how **Physics-Informed Neural Networks** can serve as a **fast, physics-consistent surrogate model** for transient heat transfer problems in chemical reactors.

---

## ⚗️ Chemical Engineering Background

Temperature distribution inside reactors critically affects:

- Reaction kinetics (Arrhenius dependence)
- Catalyst activity and degradation
- Hot-spot formation
- Thermal runaway and safety risks

Classically, these systems are modeled using **energy balances and PDEs**.  
PINNs offer a modern alternative that preserves physical fidelity while enabling **machine-learning-based acceleration**.

---

## 📐 Governing Equations

### Heat Diffusion Equation (1D, Transient)

\[
T_t = \alpha T_{xx}
\]

Where:

- \( T(x,t) \) = temperature  
- \( \alpha = \frac{k}{\rho c_p} \) = thermal diffusivity  

### Boundary Conditions
\[
T(0,t) = 0, \quad T(1,t) = 0
\]

### Initial Condition
\[
T(x,0) = \sin(\pi x)
\]

### Analytical Solution (Validation Case)
\[
T(x,t) = e^{-\alpha \pi^2 t} \sin(\pi x)
\]

This analytical form allows direct comparison between **PINN predictions and ground truth**.

---

## 📊 Data & Assumptions

**Assumptions**
- One-dimensional conduction
- Constant thermal properties
- No internal heat generation (baseline case)

**Training Data**
- Physics collocation points sampled across space–time
- Boundary condition points
- Initial condition points
- Optional sparse synthetic sensor data

PINNs allow learning **without full-field labeled datasets**.

---

## 🧠 Model Development

- Neural network: Multi-Layer Perceptron (MLP)
- Inputs: spatial coordinate \(x\), time \(t\)
- Output: temperature \(T(x,t)\)

### Loss Function Components
- **PDE residual loss** (physics enforcement)
- **Boundary condition loss**
- **Initial condition loss**
- *(Optional)* data loss from sensors

Automatic differentiation is used to compute \( T_t \) and \( T_{xx} \).

---

## 📈 Results & Interpretation

The training script produces:

- Loss convergence curves
- Temperature profile comparisons (PINN vs analytical)
- Absolute error heatmap over space and time
- Quantitative metrics (RMSE, max error)

Results are saved to the `results/` directory after training.

---

## 💼 Business / Operational Impact

**Chemical & Industrial Systems**
- Hot-spot detection
- Reduced sensor requirements
- Faster design iteration

**Data Centers**
- Thermal digital twins
- Cooling optimization (CRAC/CRAH, liquid loops)
- Reliability and energy efficiency analysis

**Energy & Aerospace**
- Lightweight thermal solvers
- Rapid what-if scenario testing
- Predictive reliability modeling

---

## 🔮 Future Improvements

- Extend to **2D / 3D geometries**
- Add **convection and reaction heat generation**
- Solve **inverse problems** (estimate \( \alpha \), heat flux)
- Integrate **reinforcement learning** for control optimization
- Deploy as a **Streamlit or cloud-based dashboard**

---

## 🚀 Quickstart

### 1️⃣ Create a virtual environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# 📊 Project 2 — Dynamic Temperature & Velocity Analysis in Engineering Systems

## 🔍 Overview
This project applies **data science, exploratory data analysis (EDA), and predictive modeling** to analyze **thermal and fluid dynamic behavior** in two critical engineering systems:

- **Heat Exchangers**
- **Chemical Reactors**

By combining **physics-based simulation**, **statistical summaries**, and **predictive trend analysis**, the project demonstrates how data science can be used to **monitor system stability**, **detect deviations**, and **support operational decision-making** in industrial environments.

---

## 🎯 Objectives
- Model **temperature distribution** across time and space  
- Analyze **dynamic temperature control** in a reactor  
- Perform **EDA across multiple physical systems**  
- Compare **observed vs predicted velocity profiles**  
- Evaluate **prediction accuracy for reactor temperature**

---

## 🧪 System 1 — Heat Exchanger Temperature Distribution
This visualization shows how temperature evolves over **time** and **distance** inside a heat exchanger.

![Temperature Distribution in Heat Exchanger](Temperature_distribution_in_heat_exchanger.png)

### Key Insights
- Temperature decays with both **time** and **axial distance**
- Highlights **thermal efficiency loss**
- Useful for detecting **ineffective heat transfer zones**

---

## 🔥 System 2 — Dynamic Temperature Control in a Chemical Reactor
A spatio-temporal view of temperature regulation inside a reactor.

![Dynamic Temperature Control](dynamic_temperature_in_reactor.png)

### Key Insights
- Oscillatory behavior indicates **active control dynamics**
- Spatial damping shows **heat dissipation stability**
- Applicable to **process control and safety monitoring**

---

## 📈 Exploratory Data Analysis (EDA) Across Systems
Summary statistics across three subsystems:
- Reactor Temperature
- Pipe Velocity
- Heat Exchanger Temperature
  
![EDA Summary](EDA_summary_across_systems.png)

### Metrics Analyzed
- Minimum
- Maximum
- Mean
- Standard Deviation

### Why It Matters
- Identifies **variability and risk**
- Supports **threshold setting**
- Enables **cross-system comparison**

---

## 🚰 Pipe Flow Analysis — Velocity vs Radius
Observed vs predicted velocity distribution along pipe radius.

![Velocity Profile](Velocity_and-pipe_Radius_plot.png)

### Key Insights
- Near-parabolic profile consistent with **laminar flow**
- Prediction deviation near pipe wall highlights **model limitations**
- Useful for **hydraulic efficiency validation**
---

## 🤖 Predictive Modeling — Reactor Mid-Position Temperature
Comparison between observed and predicted reactor temperature over time.

![Reactor Temperature Prediction](Reactor_position_plot.png)

### Key Insights
- Model captures **trend but smooths oscillations**
- Demonstrates bias–variance tradeoff
- Foundation for **advanced ML control models**

---

## 🧠 Data Science Techniques Used
- Exploratory Data Analysis (EDA)
- Time-series trend analysis
- Physics-informed simulation
- Model vs observation comparison
- Visualization with Matplotlib & NumPy

---

## 🛠 Tools & Technologies
- Python
- NumPy
- Matplotlib
- Jupyter Notebook
- Statistical Analysis
- Engineering Modeling

📂 Notebook:

Heat Exchangers vs. Reactors – The Role of Dynamic Temperature & Fluid Velocity Profiles.ipynb

---

## 🚀 Applications
- Process Engineering
- Chemical & Thermal Systems
- Manufacturing Optimization
- Predictive Maintenance
- Data-Driven Engineering Decisions

---

## ⭐ Why This Project Matters
This project demonstrates how **data science bridges theory and real-world engineering systems**, enabling:
- Better control
- Higher efficiency
- Safer operations
- Smarter decision-making
  
---

# 📊 Project 3: Photolithography Yield Risk Prediction  
## AI-Driven Pass/Fail Modeling for Semiconductor Manufacturing

  **Project Type:** Industrial Data Science · Manufacturing AI · Explainable ML  
  **Dataset:** SECOM Semiconductor Manufacturing Dataset (UCI ML Repository)

---

## 🧰 Tools & Technologies

- **Programming:** Python  
- **Libraries:** Scikit-Learn, Pandas, NumPy, Matplotlib  
- **Methods:** Classification, Ensemble Learning, Explainable AI, Drift Monitoring  

---

## 🔬 Project Overview

Modern semiconductor manufacturing—especially **photolithography**—operates under extremely tight process windows. Small deviations in **exposure, focus, thermal stability, or tool health** can lead to **critical dimension (CD)** or **overlay excursions**, resulting in yield loss.

This project develops an **AI-driven pass/fail risk prediction system** using real semiconductor process sensor data.  
The objective is to **identify yield risk before downstream metrology**, enabling:

- Earlier intervention  
- Higher throughput  
- Improved fab stability  

---

## 🎯 Business & Engineering Objective

### Problem Statement
**Can we predict whether a manufacturing run will PASS or FAIL specification using high-dimensional process sensor data—before final inspection?**

### Why This Matters
- AI chips require **near-perfect yield**
- Lithography tools are **capital-intensive bottlenecks**
- Early risk detection reduces:
  - Scrap
  - Rework
  - Tool downtime
  - Throughput loss

---

## 🧠 Dataset Description

**Source:** UCI Machine Learning Repository – SECOM Dataset  

| Attribute | Value |
|---------|------|
| Samples | 1,567 manufacturing runs |
| Sensors | 590 process variables |
| Target  | Pass / Fail |

### Key Characteristics
- High dimensionality (**p ≫ n**)  
- Severe class imbalance (~93% FAIL, ~7% PASS)  
- Structured missing data (conditional sensors)  
- Strong subsystem correlations  

> ✅ This makes the dataset **highly realistic** for semiconductor manufacturing analytics.

---

## 🔄 Data Science Lifecycle (Photolithography Context)

### 1️⃣ Problem Definition
- Predict yield risk (PASS/FAIL) prior to metrology  
- Analogous to CD or overlay out-of-spec prediction  

### 2️⃣ Data Collection
Process telemetry representing:
- Exposure & focus proxies  
- Thermal and environmental signals  
- Tool subsystem health  

### 3️⃣ Data Understanding
- Sensor completeness analysis  
- Missingness patterns  
- Variability and correlation checks  

### 4️⃣ Data Cleaning & Wrangling
- Median imputation for missing values  
- Retention of conditionally active sensors  
- Stratified train/test split  

### 5️⃣ Exploratory Data Analysis (EDA)

![class_distribution](class_distribution.png)

![missing_fraction_histogram](missing_fraction_histogram.png)

![sensor_correlation_heatmap](sensor_correlation_heatmap.png)
  

**EDA highlights:**
- Severe class imbalance  
- Mostly complete core sensors with conditional diagnostics  
- Strong subsystem-level correlations  

---

### 6️⃣ Feature Engineering
- Robust scaling  
- Imputation pipelines  
- Preparation for nonlinear models  

---

### 7️⃣ Modeling
- **Logistic Regression** – baseline, interpretable  
- **Random Forest** – nonlinear, subsystem-aware  

---

### 8️⃣ Model Evaluation

![roc_curves_logreg_vs_rf](roc_curves_logreg_vs_rf.png)

| Model | ROC-AUC |
|-----|--------|
| Logistic Regression | ~0.64 |
| Random Forest | ~0.78 |

**Interpretation**
- Yield risk is **not linearly separable**
- Nonlinear interactions between tool subsystems dominate
- Ensemble models better capture lithography behavior

---

### 9️⃣ Operational Insight: Confusion Matrix

![rf_confusion_matrix](rf_confusion_matrix.png)
  

At default thresholds, the Random Forest behaves **conservatively**, flagging nearly all runs as FAIL.

  **Prediction ≠ Decision**  
> Threshold tuning is essential to balance **yield protection vs throughput**.

---

## 🔍 Explainability & Root-Cause Insight

![top_sensor_importances](top_sensor_importances.png)

**Key observations:**
- Only **~10–20 sensors dominate** model decisions  
- Reflect real lithography subsystems:
  - Illumination stability  
  - Focus control  
  - Thermal regulation  
  - Stage dynamics  

---

## 📡 Deployment & Drift Monitoring

![psi_drift_monitoring](psi_drift_monitoring.png)

- Drift monitored using **Population Stability Index (PSI)**
- Early-stage drift detected in key sensors
- No catastrophic shifts, but signals of:
  - Tool aging
  - Process change
  - Recipe evolution  

> This mirrors how fabs monitor equipment health in production.

---

## 🚀 Why This Project Stands Out

✔ Real semiconductor manufacturing data  
✔ High-dimensional, imbalanced industrial ML problem  
✔ Strong focus on explainability and deployment readiness  
✔ Direct relevance to **AI chip production and advanced nodes**

---

## 📌 Future Enhancements
- Threshold optimization for fab decision policies  
- Precision-Recall analysis  
- Risk banding (Green / Yellow / Red)  
- SHAP-based local explanations  
- Dashboard integration (Power BI / Plotly Dash)

---

### 📁 Project Files

📓 Photolithography_Project.ipynb

---

# Project 4: Reliability Analysis & Survival Modeling

### Kaplan–Meier, Hazard Functions, and Batch Comparison

---

## 📌 Project Overview

This project focuses on reliability engineering and time-to-event analysis using survival analysis techniques. The objective is to model failure behavior over time, quantify survival probabilities, and compare reliability performance across manufacturing batches.

The analysis applies industry-standard statistical methods widely used in manufacturing, aerospace, defense, and semiconductor reliability studies.

---

## 🎯 Objectives

- Model time-to-failure behavior using Kaplan–Meier survival estimation

- Distinguish failure vs. censored observations

- Compare survival performance between Batch A and Batch B

- Analyze hazard (failure) rates over time

- Support data-driven reliability and quality decisions

---

## 🧠 Methods & Techniques

- Kaplan–Meier Estimator

- Censoring analysis

- Survival curve comparison by group

- Hazard function estimation

- Exploratory distribution analysis

- Confidence interval visualization

---

## 📊 Key Visualizations & Insights

### 1️⃣ Kaplan–Meier Survival Curve

This plot estimates the probability that a unit survives beyond a given time.

Steep early decline indicates early-life failures

Gradual tail suggests wear-out behavior

Confidence bands show estimation uncertainty over time

![Kaplan–Meier Survival Curve](kaplan_meier_survival_curve.png)

---

### 2️⃣ Time-to-Event Distribution (Failure vs. Censored)

This visualization contrasts observed failures against censored observations.

Failures dominate early time periods

Censored observations increase at later times

Confirms the need for survival modeling vs. simple averages

![Time to Event Distribution](time_to_event_distribution_failure_vs_censored.png)

---

### 3️⃣ Survival Probability Comparison (Batch A vs. Batch B)

This comparison highlights reliability differences between manufacturing batches.

Batch A demonstrates consistently higher survival probability

Batch B experiences earlier degradation

Confidence intervals reflect statistical uncertainty

![Survival Curve by Batch](batch_comparison_survival_curve.png)

---

### 4️⃣ Smoothed Survival Trends

Smoothed curves help reveal underlying reliability trends.

Batch A shows delayed failure onset

Batch B exhibits faster reliability decay

Useful for management-level interpretation

![Survival Curve by Batch](survival_curve_by_batch.png)

---

### 5️⃣ Hazard Function Analysis

The hazard function represents the instantaneous failure rate.

Increasing hazard rate indicates aging or wear-out failure mode

Critical for maintenance planning and lifecycle decisions

![Hazard Function](hazard_function_by_batch.png)

---

## 📈 Business & Engineering Impact

- Enables predictive maintenance strategies

- Supports supplier and batch qualification

- Reduces unexpected failures and downtime

- Improves manufacturing reliability and quality control

- Applicable to aerospace, defense, electronics, and semiconductor systems

---

## 🛠 Tools & Technologies

- Python

- NumPy, Pandas

- Matplotlib / Seaborn

- Lifelines (Survival Analysis)

- Jupyter Notebook
  
---

📁 Notebook:
Reliability Analysis Using Weibull Modeling.ipynb

---

### 🔍 Key Takeaway

Survival analysis provides a statistically robust framework to evaluate reliability, account for censored data, and compare manufacturing performance across batches—far beyond traditional MTBF metrics.

---

# 📊 Project 5: Oath–Outcome Alignment Analysis  
### *From Constitutional Promises to Measurable Outcomes*

---

## 📌 Project Overview

This project applies **data science, statistical modeling, and natural language processing (NLP)** to evaluate whether real-world institutional outcomes align with the **constitutional obligations defined in official government oaths**.

Public institutions in the United States—**military, law enforcement, judiciary, and civil government**—derive their authority from oaths sworn to the U.S. Constitution. While these oaths establish clear legal and ethical obligations, there is limited **quantitative research** measuring how closely institutional behavior aligns with those commitments.

This project addresses that gap by converting **normative legal principles into measurable signals** and comparing them against observed institutional outcomes.

---

## 🎯 Research Question

**Do institutional outcomes align with the constitutional obligations defined in official oaths?**

---

## 🧠 Why This Matters

- Converts normative constitutional law into **quantifiable metrics**
- Bridges **law, ethics, governance, and data science**
- Moves beyond anecdotal accountability toward **evidence-based oversight**
- Rarely studied quantitatively in academic or policy literature

**Relevant to:**
- Oversight bodies  
- Inspectors General  
- Civil rights organizations  
- Policy analysts  
- Academic researchers  

---

## 📊 Key Visualizations

### 🔵 Oath vs Outcome Radar Chart (Law Enforcement Example)

### 🔵 Oath vs Outcome Radar Chart

![Oath vs Outcome Radar Chart](https://github.com/jemaelnzihou/Jemael-Nzihou-Portfolio/blob/main/radar%20plot%20.png?raw=true)

**Interpretation**
- Large gaps between oath commitments and outcomes indicate **institutional misalignment**
- Collapsed outcome area signals **enforcement or accountability failure**
- Symmetry would indicate constitutional compliance

---

### 📉 Distribution of OOAS Across Agencies

![OOAS Distribution](https://github.com/jemaelnzihou/Jemael-Nzihou-Portfolio/blob/main/distribution%20of%20OOAS.png?raw=true)

**Insight**
- Left-skewed distributions highlight **systemic negative alignment**
- Outliers identify institutions requiring immediate oversight attention

---

### 🔥 OOAS Heatmap by Agency & State

![OOAS Heatmap](https://github.com/jemaelnzihou/Jemael-Nzihou-Portfolio/blob/main/Heatmap%20OOAS.png?raw=true)

**Insight**
- Enables **cross-jurisdictional comparison**
- Reveals geographic and institutional accountability disparities

---

## 🔬 Methodology

**Text Analysis (NLP)**
- Oath language extraction
- Constraint density and clarity scoring

**Feature Engineering**
- Accountability strength
- Power–constraint ratios

**Statistical Modeling**
- Regression analysis
- Institutional comparison

**Visualization**
- Radar charts  
- Heatmaps  
- Trend analysis  
---

## 📊 Project 6: Data Center Insights with Data Science & Engineering

### *Operational Intelligence, Reliability, and Performance Optimization*

---

## 📌 Project Overview

This project applies **data science methods grounded in engineering principles** to analyze and interpret **data center operational behavior**, focusing on **thermal stability, energy consumption, and communication efficiency**.

Modern data centers function as tightly coupled cyber-physical systems. Small deviations in temperature, power usage, or communication latency can propagate into **equipment stress, efficiency loss, or reliability risk**. This project demonstrates how **engineering-aware analytics** can support **proactive monitoring and decision-making**.

---

## 🎯 Analytical Objectives

* Monitor and interpret **thermal system behavior**
* Evaluate **power consumption patterns** over operational cycles
* Compare **communication latency** across physical transmission media
* Translate engineering signals into **data-driven operational insights**

---

## 📈 Key Visual Analyses

### 🌡️ Reactor / Equipment Temperature Monitoring (24-Hour Cycle)

![Simulated Reactor Temperature Over 24 Hours](reactor%20temperature%20plot.png)


**Insight**

* Shows diurnal temperature variation and peak thermal loading
* Dashed threshold highlights **risk zones** requiring alerts or control actions
* Demonstrates how time-series monitoring supports **preventive intervention**
* Directly applicable to **thermal management of racks, cooling loops, and DAHUs**

---

### ⚡ Power Consumption Patterns in a Data Center

![Power Consumption Over a Day](Power%20comsumption%20per%20day.png)

**Insight**

* Captures cyclical load behavior across a 24-hour operational window
* Peak demand periods correlate with increased cooling and compute activity
* Supports:

  * Energy efficiency optimization
  * Capacity planning
  * PUE-oriented performance analysis

---

### 🚀 Communication Latency: Optical vs Electrical Transmission
![Latency Comparison: Light vs Electrical Communication](Latency%20comparison.png)

**Insight**

* Quantifies latency growth as a function of distance
* Demonstrates superior scalability of **optical fiber** for low-latency environments
* Reinforces engineering trade-offs in **network design for data centers**
* Relevant to:

  * High-performance computing
  * Low-latency cloud services
  * Backbone infrastructure planning

---

## 🧠 Engineering + Data Science Integration

This project explicitly connects:

* **Physical system behavior** (temperature, power, signal propagation)
* **Data science tools** (EDA, visualization, trend analysis)
* **Engineering constraints** (thresholds, efficiency limits, reliability curves)

Rather than treating data as abstract, each variable is interpreted within its **physical and operational context**.

---

## 🧪 Deliverables

* 📓 Jupyter Notebook with reproducible analysis
* 📊 Engineering-driven visual analytics
* 🧠 Operational insights for infrastructure optimization
* 📘 Documentation linking analytics to real data center systems

---

## 🚀 Future Extensions

* Predictive maintenance models (thermal & electrical)
* Time-series forecasting of energy demand
* Anomaly detection for early fault identification
* Integration with real sensor telemetry (IoT / BMS / EPMS)

---

## 📁 Project Files

📓 The Data Center insights with Data science and engineering (1).ipynb

---

## 📡 Project 7: Wi-Fi Optimization & Communication Performance Analysis

### *Signal Quality, Reliability, and Network Efficiency*

---

## 📌 Project Overview

This project applies **data science, signal processing concepts, and network engineering principles** to analyze **wireless communication performance**, with a focus on **signal reliability, coverage quality, and user-level optimization**.

Wireless networks are fundamental to modern digital infrastructure, yet their performance is constrained by **noise, interference, distance, and infrastructure placement**. This project demonstrates how **engineering-informed analytics** can be used to evaluate and optimize Wi-Fi performance using **quantitative signal metrics**.

---

## 🎯 Analytical Objectives

* Quantify the relationship between **Signal-to-Noise Ratio (SNR)** and **Bit Error Rate (BER)**
* Analyze **spatial Wi-Fi coverage quality** across a service area
* Evaluate **user-level throughput optimization** under SNR constraints
* Support data-driven decisions for **access-point placement and network tuning**

---

## 📈 Key Visual Analyses

### 📉 Bit Error Rate vs Signal-to-Noise Ratio (QPSK)

![QPSK BER vs SNR](Bit%20Error%20Rate%20vs%20SNR%20plot%20.png)

**Insight**

* Demonstrates the exponential reduction in **bit errors** as SNR increases
* Highlights the reliability threshold required for stable digital communication
* Reinforces theoretical expectations from **digital modulation and communication theory**
* Relevant to network design, error control, and quality-of-service planning

---

### 🗺️ Wi-Fi Coverage Map: Average SNR by Region

![Wi-Fi Coverage Map](Wifi%20coverage%20map%20plot%20.png)

**Insight**

* Visualizes spatial variation in **signal quality**
* Identifies low-SNR regions requiring infrastructure improvement
* Supports **access-point optimization** and coverage gap detection
* Applicable to enterprise networks, campuses, and data center environments

---

### 🚀 User Optimization: SNR vs Throughput

![Wi-Fi Optimization: SNR vs Throughput](wifi%20optimization%20plotpng.png)

**Insight**

* Shows throughput sensitivity to SNR degradation
* Threshold lines highlight **performance drop-off zones**
* Enables classification of **low-quality user experiences**
* Supports intelligent AP assignment and load balancing strategies

---

## 🧠 Engineering & Data Science Integration

This project integrates:

* **Communication theory** (SNR, BER, modulation efficiency)
* **Statistical visualization and analysis**
* **Network performance engineering**
* **Optimization logic** grounded in real-world constraints

Each result is interpreted in the context of **physical signal behavior and network performance limits**.

---

## 🧪 Deliverables

* 📓 Jupyter Notebook with reproducible simulations
* 📊 Communication performance visualizations
* 📡 Network optimization insights
* 📘 Engineering-aware documentation

---

## 🚀 Future Enhancements

* Adaptive modulation and coding analysis
* Machine-learning-based AP selection
* Time-varying interference modeling
* Integration with real Wi-Fi telemetry data

---

## 📁 Project Files

📓 Wifi optimization (1).ipynb

---

## 👤 Author

**Jemael Nzihou**
PhD Student — Data Science 
Chemical Engineer | Business Analytics | Quality Champion certified  
🔗 Portfolio: https://jemaelnzihou.github.io/Jemael-Nzihou-Portfolio/  
🔗 LinkedIn: https://www.linkedin.com/in/jemaelnzihou
---

## 📜 License

This project is released for **research and educational use**.
Please cite appropriately if used in academic or policy work.

