class EvaluatorAgent:
    def validate(self, hypotheses, summary):
        """
        Validates hypotheses using dataset summary statistics.
        Adjusts confidence scores.
        """

        validated = []

        for h in hypotheses:
            new_conf = h["confidence"]

            # Rule 1 — Higher ROAS mean increases confidence
            if summary["roas_mean"] > 3:
                new_conf += 0.05
            
            # Rule 2 — Higher CTR mean increases confidence in CTR hypothesis
            if "CTR" in h["hypothesis"] and summary["ctr_mean"] > 0.015:
                new_conf += 0.1
            
            # Rule 3 — Penalty for weak evidence
            if summary["spend_mean"] < 100:
                new_conf -= 0.05

            validated.append({
                "hypothesis": h["hypothesis"],
                "evidence": h["evidence"],
                "validated_confidence": round(min(max(new_conf, 0), 1), 2)
            })

        return validated
