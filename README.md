# Insurance Risk Analytics & Predictive Modeling

**AlphaCare Insurance Solutions (ACIS)** – South Africa  
**End-to-End Car Insurance Risk Analytics Project**

This project analyzes 18 months of historical insurance data (Feb 2014 – Aug 2015) to identify low-risk segments, optimize premiums, and build data-driven marketing and pricing strategies.

---

## Project Objectives
- Perform Exploratory Data Analysis (EDA)
- Use statistical hypothesis testing to validate risk drivers
- Build predictive models for claim severity and probability
- Develop a **Risk-Based Pricing Framework**
- Ensure reproducibility using DVC and clean code practices

---

## Project Structure

```bash
insurance-risk-analytics/
├── data/                          # Raw & cleaned data (tracked by DVC)
├── notebooks/
│   ├── 01_eda.ipynb               # Task 1: EDA & Insights
│   ├── 02_hypothesis_testing.ipynb # Task 3: Statistical Testing
│   └── 03_modeling.ipynb          # Task 4: Predictive Modeling
├── src/
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── reports/
│   └── final_report.md
├── dvc.yaml
├── .github/workflows/ci.yml
├── requirements.txt
└── README.md