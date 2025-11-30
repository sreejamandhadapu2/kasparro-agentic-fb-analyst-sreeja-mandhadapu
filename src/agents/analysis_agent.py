class AnalysisAgent:
    def analyze(self, summary):
        """
        Lightweight analysis used by PlannerAgent.run_pipeline.
        Keeps logic simple so pipeline can run without external deps.
        """
        roas = summary.get("roas_mean")
        if roas is None:
            trend = "unknown"
        elif roas > 3:
            trend = "strong"
        elif roas > 1.5:
            trend = "moderate"
        else:
            trend = "weak"

        anomalies = []
        if summary.get("rows", 0) < 50:
            anomalies.append("small dataset")

        return {
            "roas_trend": trend,
            "anomalies": anomalies,
            "summary": summary
        }