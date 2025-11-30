import os

class DataAgent:
    def __init__(self, csv_path=None):
        # default path still available, but can be overridden
        self.csv_path = csv_path or r"C:\Users\mandh\Downloads\facebook_ads_multi_agent\data\synthetic_fb_ads_undergarments.csv"
        self.df = None

    def _ensure_deps(self):
        try:
            import pandas as pd
            import numpy as np
            return pd, np
        except ImportError as e:
            raise ImportError("Missing dependency: install pandas and numpy (pip install pandas numpy)") from e

    def load_data(self):
        """Loads CSV into memory and returns summary."""
        pd, _ = self._ensure_deps()
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"CSV not found at: {self.csv_path}")
        self.df = pd.read_csv(self.csv_path)
        return self.summarize()

    def summarize(self):
        """Returns dataset statistics for other agents."""
        pd, _ = self._ensure_deps()
        if self.df is None:
            # load if not already loaded
            self.load_data()

        df = self.df.copy()

        # Handle missing spend values
        if "spend" in df.columns:
            df["spend"] = df["spend"].fillna(df["spend"].median())

        # safe guards for missing columns
        get_mean = lambda col: float(df[col].mean()) if col in df.columns else None
        best_creative = None
        if "creative_type" in df.columns and "roas" in df.columns:
            best_creative = df.groupby("creative_type")["roas"].mean().idxmax()

        lowest_ctr_campaign = None
        if "ctr" in df.columns and "campaign_name" in df.columns:
            lowest_ctr_campaign = df.sort_values("ctr").head(1)["campaign_name"].values[0]

        summary = {
            "columns": list(df.columns),
            "rows": len(df),
            "spend_mean": get_mean("spend"),
            "ctr_mean": get_mean("ctr"),
            "roas_mean": get_mean("roas"),
            "best_creative_type": best_creative,
            "lowest_ctr_campaign": lowest_ctr_campaign,
            "dataset_head": df.head(5).to_dict(orient="records")
        }

        return summary

if __name__ == "__main__":
    # quick local debug: instantiate and try loading the default CSV (prints errors)
    agent = DataAgent()
    try:
        summary = agent.load_data()
        print("Loaded dataset summary:")
        print(summary)
    except Exception as e:
        print("Error while loading data:", repr(e))
