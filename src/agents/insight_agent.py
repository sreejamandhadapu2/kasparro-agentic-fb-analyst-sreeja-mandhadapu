class InsightAgent:
    def generate(self, summary, plan):
        """
        Generates hypotheses explaining ROAS changes
        based on dataset summary.
        """

        hypotheses = []

        # Hypothesis 1: Creative type influence
        hypotheses.append({
            "hypothesis": "ROAS is influenced by creative type performance.",
            "evidence": f"Best performing creative type: {summary['best_creative_type']}",
            "confidence": 0.7
        })

        # Hypothesis 2: Low CTR campaign hurting ROAS
        hypotheses.append({
            "hypothesis": "Campaign with lowest CTR may be pulling overall ROAS down.",
            "evidence": f"Lowest CTR campaign: {summary['lowest_ctr_campaign']}",
            "confidence": 0.65
        })

        # Hypothesis 3: Spend efficiency issue
        hypotheses.append({
            "hypothesis": "ROAS fluctuations may be due to inconsistent spend efficiency.",
            "evidence": f"Average spend: {summary['spend_mean']}",
            "confidence": 0.6
        })

        return hypotheses
