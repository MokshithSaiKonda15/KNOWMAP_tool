import pandas as pd

def load_ai_dataset(filepath="arxiv_ai.csv", max_rows=500):
    """
    Loads ArXiv AI dataset.
    We use 'title' + 'summary' columns as our text.
    max_rows = use only 500 rows to keep it fast during dev
    """
    df = pd.read_csv(filepath)
    df = df[['title', 'summary']].dropna()
    df = df.head(max_rows)

    # Combine title + summary into one text per row
    df['text'] = df['title'] + ". " + df['summary']
    df['domain'] = 'AI'

    print(f"✅ AI Dataset loaded: {len(df)} rows")
    return df[['text', 'domain']]


def load_climate_dataset(filepath1="climate-fever.csv", max_rows=500):
    """
    Loads Climate FEVER dataset.
    We use 'claim' + 'evidences/0/evidence' columns as our text.
    """
    df = pd.read_csv(filepath1)

    # Use claim + evidence as text
    df['text'] = df['claim'].fillna('') + ". " + df['evidences/0/evidence'].fillna('')
    df['domain'] = 'Climate'

    df = df[['text', 'domain']].dropna()
    df = df.head(max_rows)

    print(f"✅ Climate Dataset loaded: {len(df)} rows")
    return df[['text', 'domain']]


def load_combined_dataset(ai_path="arxiv_ai.csv", climate_path="climate-fever.csv", max_rows=500):
    """
    Loads both datasets and combines them into one DataFrame.
    """
    ai_df = load_ai_dataset(ai_path, max_rows)
    climate_df = load_climate_dataset(climate_path, max_rows)

    combined = pd.concat([ai_df, climate_df], ignore_index=True)
    combined = combined.dropna()

    print(f"\n✅ Combined Dataset: {len(combined)} total rows")
    print(f"   AI rows     : {len(combined[combined['domain']=='AI'])}")
    print(f"   Climate rows: {len(combined[combined['domain']=='Climate'])}")
    return combined


# ── TEST ──────────────────────────────────────────────
if __name__ == "__main__":
    df = load_combined_dataset()
    print("\n--- Sample AI text ---")
    print(df[df['domain'] == 'AI']['text'].iloc[0][:300])
    print("\n--- Sample Climate text ---")
    print(df[df['domain'] == 'Climate']['text'].iloc[0][:300])
