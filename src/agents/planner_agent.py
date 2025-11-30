from src.agents.data_agent import DataAgent
from src.agents.analysis_agent import AnalysisAgent
from src.agents.report_agent import ReportAgent

class PlannerAgent:
    def __init__(self):
        self.data_agent = DataAgent()
        self.analysis_agent = AnalysisAgent()
        self.report_agent = ReportAgent()

    def create_plan(self, query):
        """
        Turn the user's query into a simple plan representation.
        """
        return {
            "query": query,
            "steps": [
                "load_data",
                "analyze",
                "generate_report"
            ]
        }

    def run_pipeline(self, query="Analyze Facebook Ads performance"):
        """
        Convenience helper to run the full pipeline and return the final report.
        """
        plan = self.create_plan(query)
        summary = self.data_agent.load_data()
        analysis = self.analysis_agent.analyze(summary)
        report = self.report_agent.generate_report(analysis)
        return {
            "plan": plan,
            "summary": summary,
            "analysis": analysis,
            "report": report
        }
