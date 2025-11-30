# 🧠 Multi-Agent System Architecture — Facebook Ads Diagnosis

This document explains the flow and purpose of each agent in the system.

---

## 📌 Overview
The system automatically:

1. Diagnoses ROAS fluctuations  
2. Finds performance drivers (audience, creative, spend, CTR)  
3. Generates new creative recommendations  

All agents collaborate in a structured pipeline.

---

## 🔄 **Agent Flow Diagram (Text Format)**

       ┌─────────────────┐
       │   User Query    │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │  Planner Agent   │
       │ - Breaks query   │
       │   into tasks     │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │   Data Agent     │
       │ - Loads CSV      │
       │ - Cleans data    │
       │ - Summarizes     │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────────────┐
       │      Insight Agent       │
       │ - Generates hypotheses   │
       │   on ROAS/CTR changes   │
       └────────┬────────────────┘
                │
                ▼
       ┌─────────────────────────┐
       │    Evaluator Agent       │
       │ - Validates hypotheses   │
       │   using data stats       │
       │ - Adjusts confidence     │
       └────────┬────────────────┘
                │
                ▼
       ┌─────────────────────────┐
       │   Creative Agent         │
       │ - Generates new ad       │
       │   ideas for low CTR      │
       └────────┬────────────────┘
                │
                ▼
       ┌─────────────────────────┐
       │      Final Output        │
       │ insights.json            │
       │ creatives.json           │
       └─────────────────────────┘

---

## 🧩 Agent Roles Summary

### **1. Planner Agent**
- Decides the steps needed
- Converts query → actionable subtasks

### **2. Data Agent**
- Loads CSV dataset
- Fixes missing values
- Provides average CTR, ROAS, spend
- Detects lowest CTR campaign
- Finds best creative type

### **3. Insight Agent**
- Generates hypotheses such as:
  - “Creative type impacts ROAS”
  - “Low CTR campaign pulls ROAS down”
  - “Spend efficiency varies”

### **4. Evaluator Agent**
- Uses real data statistics to validate or reject insights
- Adjusts confidence score

### **5. Creative Agent**
- Creates new ad concepts for low-CTR campaigns
- Uses best-performing creative type

---

## ✔ Output Files

| File | Purpose |
|------|---------|
| `insights.json` | validated hypotheses & confidence |
| `creatives.json` | improved creative ideas |
| `report.md` | final marketer-friendly summary |
| `logs/` | trace logs for each step |

---

Your multi-agent workflow is now clearly documented.  
Let me know when you're ready for:

### **“next” → report.md**
