class CreativeAgent:
    def generate(self, summary):
        """
        Generates improved creative ideas for low CTR campaigns.
        Based on dataset messaging patterns.
        """

        low_ctr_campaign = summary["lowest_ctr_campaign"]

        return {
            "campaign": low_ctr_campaign,
            "recommendations": [
                "Add stronger benefit-focused headline.",
                "Emphasize comfort and breathability.",
                "Use UGC-style video with testimonials.",
                "Highlight product durability and real-world usage.",
                "Add a clear call-to-action like 'Shop Now' or 'Upgrade Comfort'."
            ],
            "based_on_best_creative_type": summary["best_creative_type"]
        }
