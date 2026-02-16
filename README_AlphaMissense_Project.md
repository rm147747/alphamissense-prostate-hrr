# 🧬 AlphaMissense VUS Reclassification in Prostate Cancer HRR Genes

## Quick Start (5 minutes)

### Step 1: Open in Google Colab
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Upload notebook**
3. Upload `Notebook1_AlphaMissense_PRAD_HRR.ipynb`

### Step 2: Run
1. Click **Runtime → Run all** (or Ctrl+F9)
2. Wait ~15 minutes for everything to complete
3. Your annotated dataset will be in `results/annotated_hrr_variants.csv`

### Step 3: Download results
1. In the Colab left sidebar, click the **folder icon** 📁
2. Navigate to `results/`
3. Right-click → Download each CSV file

---

## What this notebook does

| Step | What happens | Time |
|------|-------------|------|
| 1. Setup | Installs packages | ~30s |
| 2. Gene panel | Defines 25 HRR genes (PROfound/TRITON trials) | instant |
| 3. TCGA download | Downloads prostate cancer mutations from cBioPortal | ~1min |
| 4. Filter | Keeps only missense mutations in HRR genes | instant |
| 5. Parse | Extracts protein change info (e.g., R175H) | instant |
| 6. UniProt map | Maps gene names to UniProt IDs | instant |
| 7. AlphaMissense | Downloads AI pathogenicity predictions | ~5min |
| 8. ClinVar | Downloads known variant classifications | ~2min |
| 9. Merge | Combines everything into one table | instant |
| 10. Clinical data | Downloads survival/clinical data | ~30s |
| 11-12. Output | Creates final annotated tables | instant |

## Output files

- `results/annotated_hrr_variants.csv` — Every HRR missense variant with AlphaMissense scores
- `results/patient_hrr_summary.csv` — Patient-level summary
- `data/raw/clinical_patient.csv` — Clinical/survival data
- `data/processed/alphamissense_hrr_genes.csv` — Reusable AlphaMissense lookup for HRR genes

## Troubleshooting

**AlphaMissense download times out?**
The file is ~450MB. On slow connections:
1. Download manually from https://zenodo.org/records/8208688
2. Get `AlphaMissense_aa_substitutions.tsv.gz`
3. Upload to Colab (drag & drop to the file panel)
4. Re-run Section 7C

**cBioPortal is slow?**
Try running during US nighttime (off-peak). The S3 download is usually reliable.

## Project roadmap

- [x] **Notebook 1** — Data download & annotation (this file)
- [ ] **Notebook 2** — Statistical analysis (Cox, KM, sensitivity)
- [ ] **Notebook 3** — Validation in PARP inhibitor cohort
- [ ] **Notebook 4** — Publication-ready figures

## References

- AlphaMissense: Cheng et al., Science 2023. DOI: 10.1126/science.adg7492
- PROfound trial: de Bono et al., NEJM 2020. DOI: 10.1056/NEJMoa1911440
- TCGA-PRAD: Cancer Genome Atlas Research Network, Cell 2015
- cBioPortal: Cerami et al., Cancer Discov 2012
