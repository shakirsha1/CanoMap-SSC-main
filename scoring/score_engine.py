def score_targets(df):

    def bio_score(row):

        base = row.get("score", 0)

        rbh = row.get("rbh_score", 0.5)

        identity = row.get("identity", 80) / 100

        # biological weighting (IMPORTANT)
        return (0.5 * base) + (0.3 * rbh) + (0.2 * identity)


    df["final_score"] = df.apply(bio_score, axis=1)

    return df.sort_values("final_score", ascending=False)
