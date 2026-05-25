# insurance-risk-analytics# Insurance Risk Analytics & Predictive Modeling

**AlphaCare Insurance Solutions (ACIS)** - South Africa  
**End-to-End Insurance Risk Analytics Project**

This project analyzes 18 months of car insurance data (Feb 2014 – Aug 2015) to identify low-risk customer segments, optimize premiums, and support data-driven marketing decisions.

---

## Project Overview

As a Marketing Analytics Engineer at AlphaCare, the goal is to move from intuition-based pricing to analytics-driven risk-based pricing using historical claim data.

**Key Objectives:**
- Understand risk drivers (Province, Gender, Vehicle Type, etc.)
- Perform statistical hypothesis testing
- Build predictive models for claim severity and probability
- Enable dynamic, risk-based premium calculation

---

## Project Structure

```bash
insurance-risk-analytics/
├── data/                          # Data files (tracked by DVC)
├── notebooks/
│   ├── 01_eda.ipynb              # Task 1: Exploratory Data Analysis
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── data_loader.py            # Task 2: Data loading & cleaning
│   ├── eda_utils.py
│   └── hypothesis_tests.py
├── reports/
│   └── final_report.md
├── github/workflows/ci.yml      # GitHub Actions CI
├── dvc.yaml                      # DVC Pipeline
├── requirements.txt
└── README.md