"""
CanoMap-SSC FULL EXECUTION ENGINE
Input: Cannflavin A
Output: Ranked Canine Cancer Targets
"""

from modules.netinfer_runner.netinfer_runner import run_netinfer
from modules.trackmypdb_runner.trackmypdb_runner import run_trackmypdb
from modules.integration_engine import merge_targets
from modules.canine_rbh.canine_rbh_engine import filter_canine_targets
from modules.scoring_engine.scoring_engine import score_targets
from modules.report_generator import generate_report


def main():

    compound_name = "Cannflavin A"
    smiles = "INSERT_CANNFLAVIN_A_SMILES_HERE"

    print("\n🧬 Starting CanoMap Pipeline...\n")

    # 1. NetInfer
    netinfer_df = run_netinfer(compound_name, smiles)

    # 2. TrackMyPDB
    track_df = run_trackmypdb(compound_name, smiles)

    # 3. Merge
    merged = merge_targets(netinfer_df, track_df)

    # 4. Canine filtering
    canine_targets = filter_canine_targets(merged)

    # 5. Scoring
    scored = score_targets(canine_targets)

    # 6. Report
    generate_report(scored)

    print("\n✅ CanoMap Pipeline Completed Successfully")


if __name__ == "__main__":
    main()
