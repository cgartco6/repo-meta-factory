# 🤖 Multi-Agent Software Factory Monorepo

An enterprise-grade, fully automated, standalone-modular, AI-driven agency structured with Human-in-the-Loop (HITL) gatekeepers. 

## 📁 Repository Map Reference
- `/backend`: Core FastAPI asynchronous server controlling independent agency studios.
- `/frontend`: Next.js 15 operational interface web views optimized for Vercel deployment.
- `orchestrator.py`: Multi-agent code compiler and state healing supervisor engine.
- `dashboard.py`: Streamlit console metrics tracker for rapid local development.

## 🛠️ Global Activation Sequence
1. Standardize dependencies across your local environment:
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Launch your local tracking dashboard console view:
   ```bash
   streamlit run dashboard.py
   ```
3. Initialize the multi-agent code compilation routines:
   ```bash
   python orchestrator.py
   ```
