# AI Study Companion

AI Study Companion is a full-stack web app that delivers personalized tutoring, quizzes, and study plans using long-term memory. The backend pulls the student’s Hindsight memory, injects it into every Groq prompt, and saves new insights back after each interaction.

**Features**
- Chat tutor with memory-aware responses
- Personalized 5-question quizzes targeting weak topics
- Weekly study plan generation with a day-by-day schedule

**Setup**
1. Clone the repository.
2. Fill in `.env` with your API keys and pipeline ID.
3. Run `docker-compose up --build`.
4. Open `http://localhost:3000`.

**Hindsight API**
- `pip` (API only): `pip install hindsight-api` then `hindsight-api` (runs on `http://localhost:8888`).
- Docker (full): included as `hindsight` service in `docker-compose.yml`.
- LLM envs for Hindsight:
  - `GROQ_API_KEY`
  - `GROQ_BASE_URL=https://api.groq.com/openai/v1`
  - `HINDSIGHT_API_LLM_MODEL=gpt-oss-20b`
  - `HINDSIGHT_API_LLM_API_KEY` (set same as `GROQ_API_KEY`)

**Local Dev (No Docker)**
1. Ensure Python 3.11+ and Node 20+ are installed.
2. Run `scripts/dev.ps1` (PowerShell) or `scripts/dev.bat` (Command Prompt).
3. Open `http://localhost:3000`.

**How Memory Is Used**
- Every request reads the latest Hindsight memory for the user.
- The memory is injected directly into the Groq system prompt to personalize responses.
- After chats and quizzes, new learning insights and mistakes are appended and saved back to Hindsight.

**Docs**
- Hindsight: `https://hindsight.vectorize.io`
- Groq Console: `https://console.groq.com`

**CI/CD**
- CI workflow: `.github/workflows/ci.yml`
  - Backend dependency install + Python compile check
  - Frontend dependency install + production build
- CD workflow: `.github/workflows/cd.yml`
  - Builds and pushes backend/frontend Docker images to GHCR on `main` or manual trigger
  - Image names:
    - `ghcr.io/<owner>/ai-study-companion-backend`
    - `ghcr.io/<owner>/ai-study-companion-frontend`
