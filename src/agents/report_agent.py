class ReportAgent:
    def generate_report(self, analysis):
        """
        Produces a simple report dict from analysis results.
        """
        title = "Facebook Ads Analysis Report"
        body_lines = [
            f"ROAS trend: {analysis.get('roas_trend')}",
        ]
        if analysis.get("anomalies"):
            body_lines.append("Anomalies: " + ", ".join(analysis["anomalies"]))

        return {
            "title": title,
            "body": "\n".join(body_lines),
            "analysis": analysis
        }