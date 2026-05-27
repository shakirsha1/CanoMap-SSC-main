import pandas as pd
import os


def generate_report(df, compound_name="CannflavinA"):
    """
    Generates final CanoMap output files
    """

    print("\n📄 Generating CanoMap report...")

    # Ensure output folder exists
    os.makedirs("outputs", exist_ok=True)

    # ---------------------------
    # 1. Save full dataset
    # ---------------------------
    full_path = f"outputs/{compound_name}_full_results.tsv"
    df.to_csv(full_path, sep="\t", index=False)

    # ---------------------------
    # 2. Save ranked targets only
    # ---------------------------
    if "final_score" in df.columns:
        ranked = df.sort_values(by="final_score", ascending=False)
    else:
        ranked = df

    ranked_path = f"outputs/{compound_name}_ranked_targets.tsv"
    ranked.to_csv(ranked_path, sep="\t", index=False)

    # ---------------------------
    # 3. Summary report
    # ---------------------------
    summary_path = f"outputs/{compound_name}_summary.txt"

    with open(summary_path, "w") as f:
        f.write("CanoMap-SSC Report\n")
        f.write("===================\n\n")
        f.write(f"Compound: {compound_name}\n")
        f.write(f"Total targets: {len(df)}\n")

        if "final_score" in df.columns:
            f.write(f"Top score: {df['final_score'].max()}\n")
            f.write(f"Average score: {df['final_score'].mean()}\n")

    print("✅ Report generated successfully")

    return {
        "full": full_path,
        "ranked": ranked_path,
        "summary": summary_path
    }
