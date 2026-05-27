import pandas as pd

def merge_targets(net_df, track_df):

    print("\n🔗 Merging NetInfer + TrackMyPDB targets...")

    net_df["uniprot"] = net_df.get("uniprot_list", net_df.get("uniprot"))
    track_df["uniprot"] = track_df.get("uniprot")

    combined = pd.concat([net_df, track_df], ignore_index=True)

    combined = combined.dropna(subset=["uniprot"])
    combined = combined.drop_duplicates(subset=["uniprot"])

    print(f"✅ Merged targets: {len(combined)}")

    return combined
