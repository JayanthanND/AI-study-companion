# Hindsight Setup

## Option 1: pip (API only)

1. Install and run local Hindsight API:
   - `pip install hindsight-api`
   - `hindsight-api`
2. Set LLM provider key env vars:
   - `GROQ_API_KEY=gsk-...`
   - `GROQ_BASE_URL=https://api.groq.com/openai/v1`
   - `HINDSIGHT_API_LLM_MODEL=gpt-oss-20b`
   - `HINDSIGHT_API_LLM_API_KEY=$GROQ_API_KEY`
3. API should be available at `http://localhost:8888`.

## Option 2: Docker (full experience)

1. Set root `.env` values:
   - `GROQ_API_KEY`
   - `GROQ_BASE_URL=https://api.groq.com/openai/v1`
   - `HINDSIGHT_API_LLM_MODEL=gpt-oss-20b`
   - `HINDSIGHT_API_LLM_API_KEY`
   - `HINDSIGHT_API_KEY` (optional, if your pipeline requires auth)
   - `HINDSIGHT_PIPELINE_ID` (optional, if your pipeline requires a fixed ID)
2. Start the stack:
   - `docker compose up --build`
3. Services:
   - Hindsight API: `http://localhost:8888`
   - Backend API: `http://localhost:8000`
   - Frontend: `http://localhost:3000`

## Notes

- The backend uses `HINDSIGHT_BASE_URL` and defaults to local API in `.env`.
- In Docker, backend automatically points to `http://hindsight:8888` via compose override.
- Set `HINDSIGHT_API_LLM_API_KEY` to the same value as `GROQ_API_KEY` when using Groq for all LLM calls.
