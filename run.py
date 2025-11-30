import argparse
import json
import os
import sys

from src.agents.planner_agent import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?", default="Analyze Facebook Ads performance", type=str,
                        help="Analysis query (optional — uses default when omitted)")
    parser.add_argument("--data", type=str, required=False, default=None,
                        help="Path to CSV (optional — DataAgent default used when omitted)")
    parser.add_argument("--outdir", type=str, default="./reports",
                        help="Directory where outputs (insights/creatives) are written")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    planner = PlannerAgent()
    data_agent = DataAgent(args.data) if args.data else DataAgent()
    insight_agent = InsightAgent()
    evaluator = EvaluatorAgent()
    creative_agent = CreativeAgent()

    plan = planner.create_plan(args.query)
    try:
        dataset_summary = data_agent.load_data()
    except ImportError:
        print("Missing dependency: install pandas and numpy into the project's venv:")
        print(r"& .\.venv\Scripts\python.exe -m pip install pandas numpy")
        sys.exit(1)
    except Exception as e:
        print("Failed to load data:", e)
        sys.exit(1)

    hypotheses = insight_agent.generate(dataset_summary, plan)
    validated = evaluator.validate(hypotheses, dataset_summary)
    creative_messages = creative_agent.generate(dataset_summary)

    insights_path = os.path.join(args.outdir, "insights.json")
    creatives_path = os.path.join(args.outdir, "creatives.json")
    with open(insights_path, "w", encoding="utf-8") as f:
        json.dump(validated, f, indent=2)
    with open(creatives_path, "w", encoding="utf-8") as f:
        json.dump(creative_messages, f, indent=2)

    print(f"Files saved: {insights_path}, {creatives_path} (directory: {args.outdir})")
    print("Run completed.")

if __name__ == "__main__":
    main()
