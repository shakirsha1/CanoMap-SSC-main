

# 🧬 CanoMap-SSC

### Comparative Oncology Canine Protein Target Identification System

---

## 📌 Overview

**CanoMap-SSC** is a hybrid computational drug discovery pipeline designed to identify and prioritize **canine protein targets** for bioactive compounds using an integrated multi-system inference framework.

It combines:

* 🧠 **NetInfer (WGSDTNBI-based inference system)**
* 🧪 **TrackMyPDB (structure-based docking & similarity screening)**
* 🧬 **Human–Dog Cancer Ortholog RBH Pipeline**
* 🐶 **Custom Canine Protein Database**
* 📊 **Integrated scoring + ranking engine**

The system is optimized for **comparative oncology**, enabling translation of human cancer biology into canine disease models.

---

## 🎯 Key Objectives

* Predict protein targets for small molecules
* Cross-validate predictions using:

  * Network-based inference (NetInfer)
  * Structure-based docking (TrackMyPDB)
* Map all targets to **UniProt identifiers**
* Filter using **Reciprocal Best Hit (RBH) canine orthologs**
* Prioritize biologically relevant canine cancer targets
* Generate publication-ready ranked target reports

---

## 🧪 Test Compound

The system is validated using:

> **Cannflavin A**

A natural flavonoid with reported anti-inflammatory and potential anti-cancer properties.

---

## ⚙️ System Architecture

```text
SMILES Input
     │
     ├── NetInfer (Network-Based Prediction)
     │        └── Top 10 UniProt Targets
     │
     ├── TrackMyPDB (Structure-Based Screening)
     │        └── PDB → UniProt Mapping
     │
     ├── Integration Engine
     │        └── Merge + Deduplication
     │
     ├── Canine RBH Filter
     │        └── Ortholog Validation
     │
     ├── Scoring Engine
     │        └── Target Prioritization
     │
     └── Report Generator
              └── TSV + Summary Output
```

---

## 📁 Repository Structure

```text
CanoMap-SSC/
│
├── pipelines/
│   └── run_canomap.py              # Main execution pipeline
│
├── modules/
│   ├── netinfer_runner/           # NetInfer integration
│   ├── trackmypdb_runner/         # PDB docking system
│   ├── integration_engine/        # Merging logic
│   ├── canine_rbh/                # Ortholog filtering
│   ├── report_generator/          # Output generation
│
├── data/
│   ├── canine_db/
│   │     └── validated_orthologs.tsv
│   ├── netinfer/
│   ├── trackmypdb/
│
├── outputs/
│   ├── final_ranked_targets.tsv
│   ├── full_results.tsv
│   └── summary.txt
│
├── requirements.txt
└── README.md
```

---

## 🔬 Pipeline Modules

### 1. 🧠 NetInfer Module

* Input: SMILES structure
* Output:

  * Top UniProt protein targets
  * Network-based inference scores

---

### 2. 🧪 TrackMyPDB Module

* Performs structure-based screening
* Converts PDB hits → UniProt IDs
* Returns docking scores

---

### 3. 🔗 Integration Engine

* Merges NetInfer + TrackMyPDB outputs
* Removes duplicates
* Standardizes UniProt identifiers

---

### 4. 🐶 Canine RBH Filter

* Uses **Reciprocal Best Hit (RBH)** ortholog database
* Filters only biologically valid canine proteins
* Ensures translational relevance

---

### 5. 📊 Scoring Engine

* Combines:

  * NetInfer confidence
  * Docking score
  * RBH validation strength
* Produces final ranked targets

---

### 6. 📄 Report Generator

Outputs:

* `full_results.tsv`
* `ranked_targets.tsv`
* `summary.txt`

---

## 🧬 Output Format

| Column         | Description                |
| -------------- | -------------------------- |
| UniProt ID     | Target protein identifier  |
| Gene           | Gene symbol                |
| NetInfer Score | Network inference score    |
| Docking Score  | TrackMyPDB score           |
| RBH Status     | Canine ortholog validation |
| Final Score    | Integrated ranking score   |

---

## 🚀 How to Run

### 1. Clone repository

```bash
git clone https://github.com/Standard-Seed-Corporation/CanoMap-SSC.git
cd CanoMap-SSC
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run pipeline

```bash
python pipelines/run_canomap.py
```

---

## 🧪 Example Input

```python
compound_name = "Cannflavin A"
smiles = "O=C1C=CC(O)=C2..."
```

---

## 📈 Example Output

```text
Top Canine Cancer Targets (Cannflavin A)

1. EGFR   — High confidence (RBH + docking)
2. KRAS   — Strong network + structural support
3. TP53   — Tumor suppressor validation
4. BRAF   — MAPK pathway involvement
```

---

## 🧠 Scientific Applications

* Comparative oncology drug discovery
* Canine cancer biomarker identification
* Cross-species target validation
* In-silico drug repurposing
* Veterinary oncology research

---

## ⚠️ Current Status

### 🟡 Development Phase

* NetInfer integration ✔
* TrackMyPDB integration ✔
* RBH filtering ✔
* Scoring engine ✔
* Pipeline debugging in progress ⚙️
* Artifact optimization required

---

## 🔧 Known Issues

* GitHub Actions artifact storage limits
* Mock API placeholders for NetInfer & TrackMyPDB
* RBH database must be present locally
* Minor pipeline stability fixes ongoing

---

## 🧬 Future Work

### Phase 3 — Publication Engine

* Automated figures
* Target-pathway visualization
* Manuscript-ready tables

### Phase 4 — AI Docking Engine

* Deep docking score refinement
* Protein-ligand interaction prediction
* AlphaFold structure integration

---

## 📚 Citation

If you use this system:

> CanoMap-SSC: A Comparative Oncology Pipeline for Canine Protein Target Identification using Integrated Network and Structure-Based Inference.

---

## 👨‍🔬 Author

**Standard Seed Corporation (SSC)**
Comparative Oncology Research Division


