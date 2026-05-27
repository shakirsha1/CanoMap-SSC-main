"""
Canine RBH Ortholog Filtering Engine
CanoMap-SSC Phase 2 Core Biology Layer
"""

import pandas as pd


def load_rbh_database(path="data/canine_db/validated_orthologs.tsv"):
    """
    Load RBH ortholog database (Human ↔ Dog)
    """
    return pd.read_csv(path, sep="\t")


def filter_canine_targets(df, rbh_db=None):
    """
    Keep only proteins that are validated human–dog orthologs
    """

    print("\n🐶 Applying Canine RBH Ortholog Filter...")

    if rbh_db is None:
        rbh_db = load_rbh_database()

    # Normalize column names
    df = df.rename(columns={"uniprot": "human_uniprot"})
    rbh_db = rbh_db.rename(columns={"human_acc": "human_uniprot"})

    # ---------------------------
    # INNER JOIN (core filtering)
    # ---------------------------
    merged = df.merge(
        rbh_db,
        on="human_uniprot",
        how="inner"
    )

    # ---------------------------
    # Add biological confidence
    # ---------------------------
    merged["canine_ortholog_confidence"] = 1.0

    # Optional: boost reviewed proteins
    if "dog_reviewed" in merged.columns:
        merged["canine_review_boost"] = merged["dog_reviewed"].apply(
            lambda x: 1.2 if str(x).lower() == "true" else 1.0
        )
    else:
        merged["canine_review_boost"] = 1.0

    print(f"✅ Canine-filtered targets: {len(merged)}")

    return merged
