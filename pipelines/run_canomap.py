"""
CanoMap v2 - Main Pipeline Runner
"""

from modules.netinfer.runner import run_netinfer
from modules.trackmypdb.runner import run_trackmypdb
from modules.integration.merge import merge_targets
from modules.canine.rbh_filter import filter_canine_targets
from modules.scoring.score_engine import score_targets

import pandas as pd


def main():

    compound_name = "Cannflavin A"
    smiles = "OC1=CC(CCC)=CC(O)=C1"   # example SMILES

    print("\n🧬 Starting CanoMap Pipeline...\n")

    # 1. NetInfer
    net_df = run_netinfer(compound_name, smiles)

    # 2. TrackMyPDB
    track_df = run_trackmypdb(compound_name, smiles)

    # 3. Merge
    print("\n🔗 Merging NetInfer + TrackMyPDB targets...")
    merged = merge_targets(net_df, track_df)

    # 4. Canine filter
    print("\n🐶 Applying Canine RBH Ortholog Filter...")
    filtered = filter_canine_targets(merged)

    # 5. Scoring
    print("\n📊 Scoring biological relevance...")
    scored = score_targets(filtered)

    # 6. Save output
    scored.to_csv("canoMap_final_output.csv", index=False)

    print("\n✅ Pipeline Completed Successfully!")
    print(scored.head())


if __name__ == "__main__":
    main()
