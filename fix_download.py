"""Fix: Download TCGA-PRAD mutations via cBioPortal API instead of S3"""
import requests
import json
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
(DATA_DIR / "raw").mkdir(parents=True, exist_ok=True)

CBIO = "https://www.cbioportal.org/api"
STUDY = "prad_tcga_pan_can_atlas_2018"

# Step 1: Get mutation profile ID
print("📥 Step 1: Getting molecular profile...")
profiles = requests.get(
    f"{CBIO}/studies/{STUDY}/molecular-profiles",
    headers={"Accept": "application/json"}, timeout=60
).json()
mut_profile = [p for p in profiles if p["molecularAlterationType"] == "MUTATION_EXTENDED"][0]
profile_id = mut_profile["molecularProfileId"]
print(f"   Profile: {profile_id}")

# Step 2: Get all sample IDs
print("📥 Step 2: Getting sample list...")
samples = requests.get(
    f"{CBIO}/studies/{STUDY}/samples",
    headers={"Accept": "application/json"}, timeout=60
).json()
sample_ids = [s["sampleId"] for s in samples]
print(f"   Samples: {len(sample_ids)}")

# Step 3: Download mutations in batches
print("📥 Step 3: Downloading mutations (batches of 100)...")
all_muts = []
batch_size = 100

for i in range(0, len(sample_ids), batch_size):
    batch = sample_ids[i:i+batch_size]
    pct = min(100, int(100 * (i + batch_size) / len(sample_ids)))
    print(f"   Batch {i//batch_size + 1}/{(len(sample_ids)-1)//batch_size + 1} ({pct}%)", end="\r")
    
    try:
        resp = requests.post(
            f"{CBIO}/molecular-profiles/{profile_id}/mutations/fetch",
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            json={"sampleIds": batch, "entrezGeneIds": []},
            params={"projection": "DETAILED"},
            timeout=120
        )
        if resp.status_code == 200:
            all_muts.extend(resp.json())
    except Exception as e:
        print(f"\n   ⚠️ Batch failed: {e}")

print(f"\n✅ Downloaded {len(all_muts):,} mutations")

# Step 4: Convert to DataFrame and save
df = pd.json_normalize(all_muts)
df.to_csv(DATA_DIR / "raw" / "tcga_prad_mutations_raw.csv", index=False)
print(f"💾 Saved: data/raw/tcga_prad_mutations_raw.csv")
print(f"   Columns: {len(df.columns)}")
print(f"   Unique samples: {df['sampleId'].nunique() if 'sampleId' in df.columns else 'N/A'}")

# Step 5: Also download clinical data
print("\n📥 Downloading clinical data...")
for endpoint, filename in [
    (f"studies/{STUDY}/clinical-data?clinicalDataType=PATIENT", "clinical_patient.csv"),
    (f"studies/{STUDY}/clinical-data?clinicalDataType=SAMPLE", "clinical_sample.csv"),
]:
    try:
        r = requests.get(f"{CBIO}/{endpoint}", headers={"Accept": "application/json"}, timeout=60)
        if r.status_code == 200:
            pd.json_normalize(r.json()).to_csv(DATA_DIR / "raw" / filename, index=False)
            print(f"   ✅ {filename}")
    except:
        print(f"   ⚠️ Failed: {filename}")

print("\n🎉 Done! Now re-run the notebook from Cell 4 onwards.")
