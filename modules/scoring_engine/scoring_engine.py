"""
CanoMap-SSC Final Scoring Engine
Phase 2 Core Intelligence Layer
"""

import pandas as pd


def score_targets(df):
    """
    Multi-factor biological scoring system
    Produces publication-ready ranking score
    """

    print("\n📊 Running CanoMap Scoring Engine...")

    def compute(row):

        score = 0

        # ---------------------------
        # 1. NetInfer contribution
        # ---------------------------
        if row.get("source") == "NetInfer":
            score += 0.30
        elif row.get("source") == "TrackMyPDB":
            score += 0.20

        # ---------------------------
        # 2. Canine ortholog support
        # ---------------------------
        if row.get("canine_ortholog_confidence", 0) == 1:
            score += 0.30

        # ---------------------------
        # 3. Structural evidence (PDB support)
        # ---------------------------
        if pd.notna(row.get("pdb_id")) or pd.notna(row.get("pdb")):
            score += 0.15

        # ---------------------------
        # 4. Cancer relevance boost
        # ---------------------------
        protein_text = str(row.get("protein_name", "")).lower()

        cancer_keywords = [
            "kinase", "tumor", "oncogene", "egfr",
            "ras", "tp53", "apoptosis", "cell cycle"
        ]

        if any(k in protein_text for k in cancer_keywords):
            score += 0.10

        # ---------------------------
        # 5. Safety normalization
        # ---------------------------
        return round(min(score, 1.0), 4)

    df["final_score"] = df.apply(compute, axis=1)

    # Sort results
    df = df.sort_values(by="final_score", ascending=False)

    print("✅ Scoring completed")

    return df
