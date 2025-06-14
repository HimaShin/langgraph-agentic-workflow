# 🧠 LangGraph Agentic Workflow with Together.ai

This project demonstrates an **agentic workflow using LangGraph**, where user queries are automatically broken into sub-tasks and solved using cloud-hosted LLMs via **Together.ai**.

## 📌 Features

- 🧩 PlanAgent: Splits user query into multiple sub-tasks
- 🛠️ ToolAgent: Solves each sub-task using LLM
- 🔁 Feedback loop ready structure
- 🤖 Uses `Mixtral` model from Together.ai
- 🌐 Built with **LangGraph + Streamlit**
- 🚀 Deployable on Render / Cloudflare

## 🛠️ Tech Stack

- Python 🐍
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Together.ai](https://platform.together.xyz/)
- Streamlit
- dotenv

## 🚀 How to Run Locally

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/langgraph-agentic-workflow.git
   cd langgraph-agentic-workflow
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` file** with your Together API key:
   ```
   TOGETHER_API_KEY=your-api-key-here
   ```

4. **Run the app**:
   ```bash
   streamlit run streamlit_app.py
   ```

## 🔑 Example Query

```
Give 3 popular Python frameworks, explain each in one line
```

## 📂 Project Structure

```
langgraph-agentic-workflow/
├── agents/
│   ├── plan_agent.py
│   └── tool_agent.py
├── app.py
├── streamlit_app.py
├── requirements.txt
├── .env (not committed)
└── README.md
```

## 📦 Hosting

You can deploy this on platforms like **Render**, **Cloudflare Pages**, or **HuggingFace Spaces** (with adjustments).

## 👨‍💻 Author

Pendlimarri Himakar  
[GitHub](https://github.com/HimaShin) | [LinkedIn](https://linkedin.com/in/pendlimarri-himakar-2a6177230)

## 🛡️ Note

- `.env` is gitignored
- API keys should be kept secret
- Use responsibly, as Together.ai is a free service
