# Agentic Facebook Ads Analyst — Multi-Agent System  
### by Sreeja Mandhadapu

This project implements a multi-agent system that automatically analyzes Facebook Ads performance, explains ROAS fluctuations, and generates new creative recommendations using both quantitative metrics and creative messaging data.

---

## 📌 Agents Used
- **Planner Agent** – breaks problem into subtasks  
- **Data Agent** – loads & summarizes dataset  
- **Insight Agent** – generates hypotheses  
- **Evaluator Agent** – validates hypotheses with evidence  
- **Creative Agent** – generates new creative ideas for low-CTR campaigns  
- **Reporting Agent** – produces final report  

---

## 📁 Required Project Structure
README.md
requirements.txt
config/config.yaml
src/
agents/
orchestrator/
utils/
prompts/
data/
logs/
reports/
tests/
Makefile or run.sh

yaml
Copy code

---

## ▶ How to Run
Install dependencies:
pip install -r requirements.txt

sql
Copy code

Run full pipeline:
python run.py

yaml
Copy code

---

## 📊 Output Files (Generated Automatically)
### reports/insights.json
Hypotheses with evidence & confidence.

### reports/creatives.json
Creative ideas for low-CTR campaigns.

### reports/report.md
Final marketer-friendly report summarizing:
- dataset stats  
- ROAS/CTR changes  
- validated insights  
- creative recommendations  

---

## 🔄 Reproducibility
- seed = 42  
- versions pinned in `requirements.txt`  
- sample dataset included in `data/`  
- config flag for sample/full dataset switch  

---

## 📎 Submission Details
- **Release Tag:** v1.0  
- **Pull Request:** self-review  
- **Command Used:**  
python run.py
