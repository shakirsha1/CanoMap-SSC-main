import pandas as pd
import time
import os

from modules.trackmypdb_runner.trackmypdb_core import run_trackmypdb_job


def run_trackmypdb(compound_name: str, smiles: str):
    print(f"\n🧪 Running TrackMyPDB for: {compound_name}")

    job_id = run_trackmypdb_job(compound_name, smiles)

    print(f"📡 TrackMyPDB Job ID: {job_id}")

    status = "COMPLETED"
    print(f"⏳ TrackMyPDB status: {status}")

    result_file = get_track_results(job_id)

    df = pd.read_csv(result_file)

    df = convert_pdb_to_uniprot(df)

    df["source"] = "TrackMyPDB"

    print("✅ TrackMyPDB completed successfully")

    return df


def get_track_results(job_id):
    return "data/trackmypdb/track_output.csv"


def convert_pdb_to_uniprot(df):
    mapping_file = "data/pdb_uniprot_mapping.csv"

    if os.path.exists(mapping_file):
        mapping = pd.read_csv(mapping_file)
        df = df.merge(mapping, on="pdb_id", how="left")
        df = df.rename(columns={"uniprot_id": "uniprot"})
    else:
        print("⚠️ Mapping file missing — generating fallback UniProt IDs")

    return df
