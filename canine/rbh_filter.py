import pandas as pd

def filter_canine_targets(df):

    try:
        db = pd.read_csv("data/canine_db/validated_orthologs.tsv", sep="\t")

        valid = set(db["human_acc"])

        return df[df["uniprot"].isin(valid)]

    except:
        print("⚠️ Canine DB missing — skipping filter")
        return df
