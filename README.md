# AlphaMissense-Guided Reclassification of HRR Variants of Uncertain Significance: A Pan-Cancer Benchmarking Study

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)

## Overview

This repository contains the complete analysis pipeline for the manuscript:

> **AlphaMissense-Guided Reclassification of Variants of Uncertain Significance in Homologous Recombination Repair Genes: A Pan-Cancer Benchmarking Study**
>
> Raphael B. Moreira and Vamsi K. Velcheti
>
> *Submitted to Diagnostics (MDPI)*

## Key Findings

| Metric | Value |
|--------|-------|
| ClinVar agreement (Cohen's κ) | 0.733 (95% CI 0.714–0.752) |
| VUS reclassification rate | 90.1% (66,912 / 74,246) |
| Pan-cancer stratified Cox HR | 0.85 (95% CI 0.72–1.01, p = 0.057) |
| Meta-analytic HR (FE, I² = 0%) | 0.86 (95% CI 0.73–1.02) |
| Tumor types analyzed | 31 TCGA PanCancer Atlas |
| Patients with HRR missense | 1,939 |

## Repository Structure

```
├── Notebook1_AlphaMissense_PRAD_HRR.ipynb   # Data acquisition + annotation
├── Notebook2_Concordance_VUS.ipynb           # ClinVar concordance + VUS reclassification
├── Notebook3_mCRPC_Validation.ipynb          # SU2C/PCF mCRPC feasibility analysis
├── Notebook4_PanCancer_v2_FIX.ipynb          # Pan-cancer TCGA analysis (31 tumor types)
├── requirements.txt                          # Python dependencies (pinned versions)
├── manifest.json                             # Reproducibility manifest (seeds, dates, checksums)
├── data/                                     # Generated data (created by notebooks)
│   ├── processed/                            # AlphaMissense lookup tables
│   └── pancancer/                            # Per-study intermediate files
├── results/                                  # Analysis outputs
│   ├── pancancer_hrr_variants.csv            # All 4,301 annotated variants
│   ├── pancancer_cox_results.csv             # Per-tumor Cox results
│   ├── Table_S_sensitivity.csv               # Sensitivity analyses
│   └── Table_S_tumor_imbalance.csv           # Tumor-type distribution by AM status
├── figures/                                  # Publication-quality figures
└── LICENSE
```

## Reproducibility

### Quick Start

```bash
# Clone
git clone https://github.com/rm147747/alphamissense-prostate-hrr.git
cd alphamissense-prostate-hrr

# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
jupyter notebook Notebook1_AlphaMissense_PRAD_HRR.ipynb
```

### Environment

- **Python:** 3.12.3
- **Random seed:** 42 (set globally in every notebook)
- **Data access date:** February 16, 2026
- **Key packages:** pandas 2.3.3, lifelines 0.30.1, scikit-learn 1.8.0, scipy 1.17.0

All package versions are pinned in `requirements.txt`. A complete reproducibility manifest including data access dates and random seeds is in `manifest.json`.

### Notebook Execution Order

Notebooks must be run in order (1 → 2 → 3 → 4), as each depends on outputs from the previous:

1. **Notebook 1:** Downloads TCGA-PRAD mutations, filters HRR missense variants, annotates with AlphaMissense
2. **Notebook 2:** Compares AlphaMissense with ClinVar, computes concordance metrics, reclassifies VUS
3. **Notebook 3:** Applies pipeline to SU2C/PCF mCRPC cohort (exploratory feasibility)
4. **Notebook 4:** Pan-cancer analysis across 31 TCGA tumor types with survival analysis

### GitHub Codespaces

This repository is configured for GitHub Codespaces. Click the green "Code" button → "Codespaces" → "Create codespace on main" for a ready-to-use environment.

## Data Sources

| Source | Access | Date |
|--------|--------|------|
| TCGA PanCancer Atlas | cBioPortal API | Feb 2026 |
| AlphaMissense | Public database | Feb 2026 |
| ClinVar | NCBI | Feb 2026 |
| SU2C/PCF mCRPC | cBioPortal | Feb 2026 |

## HRR Gene Panel (25 genes)

- **Cohort A** (established): BRCA1, BRCA2, ATM
- **Cohort B** (PROfound): PALB2, BRIP1, BARD1, CDK12, CHEK1, CHEK2, FANCL, RAD51B, RAD51C, RAD51D, RAD54L
- **Extended DDR**: FANCA, FANCC, FANCD2, FANCE, FANCF, FANCG, NBN, MRE11, RAD50, ATR, ATRX

## Statistical Methods

- **Primary analysis:** True stratified Cox model (strata = tumor type; separate baseline hazards)
- **Meta-analysis:** Fixed-effect inverse-variance + REML random-effects + Hartung–Knapp CI + prediction interval
- **Concordance:** Cohen's κ with 2,000-iteration bootstrap 95% CI
- **Sensitivity:** Event threshold (≥3/5/10), ridge penalty sweep (λ = 0.001–0.5)

## Citation

If you use this code or data, please cite:

```
Moreira, R.B.; Velcheti, V.K. AlphaMissense-Guided Reclassification of Variants of
Uncertain Significance in Homologous Recombination Repair Genes: A Pan-Cancer
Benchmarking Study. Diagnostics 2026, X, XX. https://doi.org/10.3390/diagnosticsXXXXXXXX
```

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## Contact

- **Raphael B. Moreira** — rb@firstsaude.com — São Camilo Hospital / UNIFESP
- **Vamsi K. Velcheti** — Mayo Clinic, Jacksonville, FL
