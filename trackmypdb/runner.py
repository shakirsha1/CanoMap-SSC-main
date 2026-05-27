import pandas as pd
from .pdb_mapper import pdb_to_uniprot


def run_trackmypdb(name, smiles):

    print(f"\n🧪 TrackMyPDB REAL MODE: {name}")

    # MOCK docking output (replace later with real docking engine)
    data = {
        "pdb_id": ["1TUP", "4MNE", "2ACD"],
        "score": [0.82, 0.78, 0.75]
    }

    df = pd.DataFrame(data)

    # REAL mapping step
    df["uniprot"] = df["pdb_id"].apply(pdb_to_uniprot)

    df = df.explode("uniprot")

    df["source"] = "TrackMyPDB"

    return df
