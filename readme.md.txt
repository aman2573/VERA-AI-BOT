# VERA V2: Context-Aware Triggered Engagement Engine

A production-ready, end-to-end AI system engineered to move away from passive, standard conversational frameworks and transition into a dynamic, **event-driven engagement bot**. Powered by the Gemini 2.5 Flash model, VERA autonomously evaluates multi-layered scenario contexts, intercepts real-time simulation datasets, and executes precision-triggered interactions.

---

## 🏗️ System Architecture & Workflow

Unlike conventional AI assistants that remain idle until a user initiates input, VERA operates on a **proactive, condition-triggered architectural lifecycle**.

[System Core Engine]
│
├── 1. Ingests Simulation Seeds (Customers, Merchants, Event Triggers)
├── 2. Parses Contextual Rules & Scenario Guardrails
│
▼
[Context-Aware Processing Pipeline]
│
▼ (Understands implicit conditions, location metadata, history)
[Gemini 2.5 Flash Inference Core]
│
▼ (Evaluates if constraints are met; rejects noise)
[Precision Trigger Output Execution] ───► Logs to Local Metrics

---

## 🎯 The Challenge: Beyond Standard Conversational AI

### The Core Problem
Most modern customer engagement systems rely on static, linear rule-trees or passive chat configurations. When an event happens (e.g., a customer walks into a specific store category, or structural operational anomalies occur), traditional systems either broadcast generic, unpersonalized alerts or wait for the user to search for help. This results in notification fatigue and extremely low conversion or resolution metrics.

### What VERA Solves
The goal of this system was to engineer an intelligent agent capable of autonomous contextual synthesis. VERA reads raw environment logs, matches user data tracking structures against merchant states, and makes a real-time binary decision: **Should an engagement trigger?** 

If yes, it structures a hyper-contextualized payload. If no, it gracefully suppresses the event, protecting the endpoint from unnecessary throughput and keeping resource utilization tightly bounded.

---

## 🛠️ Deep Dive: The Codebase Structure

The repository is divided cleanly into execution scripts and static validation resources to keep code logical and modular:

```text
VERA-AI-BOT/
│
├── CHALLENGE_RESOURCES/           # System Rules & Test Datasets
│   ├── dataset/                   # Synthetic structural environments
│   │   ├── categories/            # Merchant schemas (Gyms, Restaurants, etc.)
│   │   ├── customers_seed.json    # Target user metadata profiles
│   │   ├── merchants_seed.json    # Merchant profiles and states
│   │   └── triggers_seed.json     # Pre-configured event logs
│   ├── examples/                  # API Payload contract references
│   └── *.md                       # Original architectural design briefs
│
├── .env.example                   # Secure configuration template
├── .gitignore                     # Rigorous file tracking isolation
├── judge_simulator.py             # Validation and performance evaluation runner
├── requirements.txt               # Managed dependencies
└── VERA_AI_BOT.py                 # Core AI Engine & Decision Pipeline

🚀 Getting Started
1. Prerequisites
Ensure you have a virtual environment configured with Python 3.10+ installed.

2. Dependency Configuration
Install all required runtime libraries using pip:

	pip install -r requirements.txt

3. Manage Environment Variables
The repository isolates runtime configurations from the source files. Create a local environment profile by copying the template file:

	cp .env.example .env

4. Open your newly created .env file and append your secure backend credentials:

	Plaintext
	GEMINI_API_KEY=your_actual_private_api_key_here
	MODEL_NAME=gemini-2.5-flash
	DEBUG=False

5. Running the Local Validation Test Suite
To stress-test VERA’s triggered capabilities against the comprehensive seed matrices inside the dataset folder, run the deterministic simulation framework:

	python judge_simulator.py