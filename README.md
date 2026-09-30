# ⚽ Football Mercato Application

> A full-stack football transfer intelligence application that collects, processes, stores, and presents football transfer news and rumours from multiple sources.

The project was built as a practical experiment combining **web scraping, REST APIs, MongoDB, React, Node.js, Python automation, and AI-assisted content processing**.

The long-term goal is to evolve the application from a collection of scrapers and a web interface into a more complete **football data and transfer-news platform**, with automated ingestion, normalization, enrichment, search, AI processing, and eventually automated publishing.

---

## 📌 Project Overview

The Football Mercato Application is designed around a simple idea:

**Collect football transfer information → clean and structure it → store it → expose it through APIs → display it through a web application → enrich it with AI and automation.**

The application can gather information from several sources, including:

- Football/news APIs
- Transfermarkt-related data
- Tuttomercato-style football news
- Transfer rumours
- Player and transfer information
- Future AI-agent generated/enriched content

The architecture is intentionally split into several components so that data collection, backend services, frontend presentation, and automation can evolve independently.

---

# 🏗️ High-Level Architecture

```text
                         ┌─────────────────────────┐
                         │       Data Sources      │
                         │                         │
                         │ Football APIs           │
                         │ News APIs               │
                         │ Transfermarkt           │
                         │ Tuttomercato            │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │     Data Collection     │
                         │                         │
                         │ Python scripts          │
                         │ Web scraping             │
                         │ API ingestion            │
                         │ Scheduled jobs           │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       Processing        │
                         │                         │
                         │ Cleaning / filtering    │
                         │ Regex extraction        │
                         │ Deduplication           │
                         │ Date/time filtering     │
                         │ AI enrichment           │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │        MongoDB          │
                         │                         │
                         │ News collections        │
                         │ Transfer data           │
                         │ Player data              │
                         │ Processed content       │
                         └────────────┬────────────┘
                                      │
                         ┌────────────┴────────────┐
                         │                         │
                         ▼                         ▼
                ┌──────────────────┐      ┌──────────────────┐
                │ Backend / APIs   │      │ Python API       │
                │ Node.js          │      │ FastAPI/Uvicorn  │
                │ Express          │      │ where applicable │
                └────────┬─────────┘      └────────┬─────────┘
                         │                         │
                         └────────────┬────────────┘
                                      ▼
                         ┌─────────────────────────┐
                         │      React Frontend     │
                         │                         │
                         │ Pages                   │
                         │ Components              │
                         │ Services / API calls    │
                         │ Styles                  │
                         └─────────────────────────┘
```

---

# 📁 Project Structure

The repository contains several major areas:

```text
Football-Mercato-Application/
│
├── backend/
│   ├── ...                         # Backend application
│   └── node_modules/               # Generated dependency directory
│
├── public/
│   └── images/                     # Frontend/public assets
│
├── src/
│   ├── components/
│   │   └── rumoursComponents/
│   ├── pages/
│   ├── services/
│   └── styles/
│
├── scripts/
│   └── ...                         # Utility/automation scripts
│
└── web_scraping/
    ├── ai_agents/
    ├── football_api/
    ├── news_api/
    └── transfermarkt/
        ├── latest_transfers/
        └── tuttomercato/
```

### Important note about `node_modules`

`node_modules/` is a generated dependency directory and should normally **not be committed to Git**.

The repository should contain `package.json` and, preferably, a lock file such as:

```text
package-lock.json
```

or the equivalent for the package manager being used.

After cloning, dependencies should be installed locally rather than copying `node_modules` between machines.

---

# 🧰 Technologies

## Frontend

- **JavaScript**
- **React**
- HTML
- CSS
- React components
- API service layer
- Client-side page/component architecture

The frontend is responsible for presenting football information and communicating with backend services.

Main areas include:

```text
src/components/
src/pages/
src/services/
src/styles/
```

---

## Backend

The repository contains a backend layer using the Node.js ecosystem.

Main technologies/components include:

- **Node.js**
- **Express**
- **MongoDB**
- **Mongoose**
- REST API concepts
- Environment-based configuration

The backend acts as an application/API layer between the database and frontend.

---

## Python Data Layer

Python is used for the data-collection and automation side of the project.

The repository contains dedicated areas for:

```text
web_scraping/
├── ai_agents/
├── football_api/
├── news_api/
└── transfermarkt/
```

Python is particularly useful here because of its ecosystem for:

- HTTP requests
- HTML parsing
- web scraping
- text processing
- automation
- data transformation
- AI/LLM integrations

---

## FastAPI + Uvicorn

Some Python API functionality can be exposed through **FastAPI** and served with **Uvicorn**.

Typical development startup:

```bash
python -m uvicorn <module>:app --reload
```

For example, if the FastAPI application is inside `main.py`:

```bash
python -m uvicorn main:app --reload
```

Swagger UI is then normally available at:

```text
http://127.0.0.1:8000/docs
```

OpenAPI JSON:

```text
http://127.0.0.1:8000/openapi.json
```

This allows API endpoints to be tested interactively without requiring Postman.

---

# 🗄️ Database

The application uses **MongoDB** as the main data-storage technology.

The project was designed around collections for different categories of football information.

Examples from the project's data model include concepts such as:

```text
news-api-results
tuttomercato-news
*-players-list
```

The database approach is useful because football news and transfer data are semi-structured and can evolve over time.

MongoDB also makes it convenient to store source-specific fields while progressively normalizing important information.

---

# 🔄 Data Processing Strategy

The project is not simply a scraper.

The intended pipeline is:

```text
Source
  ↓
Collection
  ↓
Raw data
  ↓
Filtering
  ↓
Cleaning
  ↓
Normalization
  ↓
Deduplication
  ↓
Storage
  ↓
API
  ↓
Frontend
```

This separation is important.

For example, a scraper should primarily be responsible for **collecting data**, while processing logic can determine:

- whether an article is relevant
- whether it is recent
- whether it is duplicated
- which player/club is mentioned
- whether it represents a transfer rumour
- whether it should be stored
- whether AI processing should be triggered

---

# 🧠 Techniques Used

## 1. Web Scraping

The application collects information from football websites where appropriate.

Typical scraping tasks include:

- retrieving pages
- parsing HTML
- extracting article titles
- extracting URLs
- extracting publication dates
- extracting player names
- extracting club names
- extracting transfer information

Scrapers should be isolated from the rest of the application so that changes to one website do not break the complete system.

---

## 2. API Ingestion

External football/news APIs can provide structured data without requiring HTML scraping.

The application can therefore combine:

```text
API data
+
Scraped data
```

instead of depending on a single source.

---

## 3. Regex-Based Extraction

Regular expressions can be used to identify structured information inside unstructured football text.

Examples:

- player names
- transfer phrases
- dates
- clubs
- keywords
- source-specific patterns

Regex is particularly useful as an initial deterministic processing layer before AI enrichment.

---

## 4. Time-Based Filtering

Football transfer news becomes obsolete quickly.

The project therefore benefits from filtering based on:

- publication timestamp
- ingestion timestamp
- transfer-window period
- article age

This helps prevent old rumours from continuously appearing as fresh information.

---

## 5. Deduplication

The same transfer story can appear across many sources.

A useful future/production strategy is to calculate a fingerprint using fields such as:

```text
source
+
URL
+
normalized title
+
publication date
```

and prevent duplicate documents from being inserted.

---

## 6. MongoDB Data Modeling

MongoDB is used to separate different types of information into appropriate collections.

This makes it possible to maintain:

```text
Raw source data
        ↓
Processed data
        ↓
Application-ready data
```

rather than forcing every source into exactly the same structure from the beginning.

---

# 🤖 AI Integration

AI is intended to become an important processing layer rather than simply a chatbot feature.

Potential AI tasks include:

### News classification

Determine whether an article is:

- transfer rumour
- confirmed transfer
- contract news
- injury news
- managerial news
- unrelated football content

### Entity extraction

Identify:

```text
Player
Club
Previous club
Destination club
Agent
Competition
Transfer status
```

### Content summarization

Convert long articles into concise transfer updates.

### Source aggregation

Multiple articles reporting the same rumour can potentially be grouped into one transfer story.

### Automated content generation

AI can eventually transform structured data into:

- website articles
- Telegram posts
- social-media posts
- transfer roundups
- player summaries

The `web_scraping/ai_agents/` directory is intended to become the foundation for this type of automation.

---

# ⚙️ Configuration

Sensitive configuration should **never be hard-coded** in source files.

Use environment variables.

A typical `.env` configuration may contain values similar to:

```env
MONGODB_URI=mongodb://localhost:27017/football-mercato

PORT=5000

FOOTBALL_API_KEY=your_api_key
NEWS_API_KEY=your_api_key

GEMINI_API_KEY=your_api_key
```

The exact variables depend on the implementation of each service.

### Important

Do not commit:

```text
.env
```

to Git.

Instead commit:

```text
.env.example
```

containing safe placeholders:

```env
MONGODB_URI=
PORT=
FOOTBALL_API_KEY=
NEWS_API_KEY=
GEMINI_API_KEY=
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

Enter the project:

```bash
cd Football-Mercato-Application
```

---

# 🐍 Python Environment

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not currently maintained, generate one after installing the required packages:

```bash
pip freeze > requirements.txt
```

---

# 🟢 Uvicorn / FastAPI

Install the API server and framework if required:

```bash
python -m pip install fastapi uvicorn
```

Verify Uvicorn:

```bash
python -m uvicorn --version
```

Start the FastAPI service using the actual module containing the `FastAPI()` object:

```bash
python -m uvicorn <module>:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to:

1. Select an endpoint.
2. Click **Try it out**.
3. Enter parameters.
4. Click **Execute**.
5. Inspect the HTTP status code.
6. Inspect the JSON response.

---

# 🟩 Node.js Backend

Install Node.js and npm.

From the backend directory:

```bash
cd backend
npm install
```

Start the backend using the script defined in `package.json`.

Common development commands are:

```bash
npm start
```

or:

```bash
npm run dev
```

The exact command should follow the project's `package.json`.

---

# ⚛️ React Frontend

Install frontend dependencies from the directory containing the frontend `package.json`.

For a standard React setup:

```bash
npm install
```

Then:

```bash
npm start
```

or the appropriate development command defined in `package.json`.

The frontend will normally be available on a local development port such as:

```text
http://localhost:3000
```

The exact port depends on the project configuration.

---

# 🗃️ MongoDB Setup

The application requires a MongoDB instance for local development.

You can use:

- MongoDB Community Server
- MongoDB Atlas
- A Dockerized MongoDB instance

Configure the connection string through an environment variable:

```env
MONGODB_URI=...
```

Make sure MongoDB is running before starting services that query the database.

---

# 🧪 Development Workflow

A typical development session can involve several terminals.

### Terminal 1 — MongoDB

Run the local MongoDB service or connect to MongoDB Atlas.

### Terminal 2 — Node backend

```bash
cd backend
npm run dev
```

### Terminal 3 — Python API / scraper

```bash
cd web_scraping
.\.venv\Scripts\Activate.ps1
python -m uvicorn <module>:app --reload
```

or execute the required Python collection script.

### Terminal 4 — React frontend

```bash
npm start
```

The resulting architecture becomes:

```text
Browser
   │
   ▼
React
   │
   ▼
Backend/API
   │
   ├──────────────► MongoDB
   │
   └──────────────► Python services
                         │
                         ├── Football APIs
                         ├── News APIs
                         ├── Transfermarkt
                         └── AI agents
```

---

# 🧪 API Testing

FastAPI automatically provides Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger is useful for verifying:

```text
Request
   ↓
Endpoint
   ↓
Backend logic
   ↓
Database/API
   ↓
JSON response
```

This makes it possible to validate the Python service independently from the React frontend.

For example:

```text
GET /players/...
GET /transfers/...
GET /news/...
```

The exact endpoints depend on the current implementation.

---

# 🔐 Security and Good Practices

Before publishing the repository:

- Never commit API keys.
- Never commit MongoDB credentials.
- Never commit `.env`.
- Add `.env` to `.gitignore`.
- Do not commit `node_modules`.
- Avoid committing Python `__pycache__`.
- Avoid committing generated build directories unless intentionally required.
- Respect website terms of service and robots policies when scraping.
- Add rate limiting/delays where appropriate.
- Handle HTTP errors and unavailable sources gracefully.

A useful `.gitignore` should include:

```gitignore
.env
.venv/
venv/
__pycache__/
*.pyc
node_modules/
dist/
build/
```

---

# 🧩 Design Philosophy

The project follows several important engineering ideas.

## Separation of concerns

Scraping, processing, persistence, API delivery, and presentation should not be tightly coupled.

```text
Scraper
   ↓
Processor
   ↓
Database
   ↓
API
   ↓
Frontend
```

Each layer can therefore evolve independently.

---

## Automation over manual work

Transfer news is continuously changing.

The long-term objective is therefore to replace manual execution with automated workflows:

```text
Scheduler
   ↓
Collect
   ↓
Process
   ↓
Validate
   ↓
Store
   ↓
Enrich
   ↓
Publish
```

---

## Data first

The application is fundamentally a data pipeline.

The React interface is the presentation layer; the real value of the system comes from reliable:

- collection
- normalization
- filtering
- storage
- enrichment
- retrieval

---

# 🔮 Future Roadmap

The project can evolve in stages.

## Phase 1 — Stabilize

- [ ] Clean repository structure
- [ ] Verify Python environment
- [ ] Verify FastAPI/Uvicorn
- [ ] Verify Node backend
- [ ] Verify React frontend
- [ ] Verify MongoDB connection
- [ ] Document API endpoints
- [ ] Add `.env.example`
- [ ] Add `requirements.txt`
- [ ] Clean `.gitignore`

## Phase 2 — Data Pipeline

- [ ] Improve scraper reliability
- [ ] Add duplicate detection
- [ ] Normalize player names
- [ ] Normalize club names
- [ ] Improve date parsing
- [ ] Add source metadata
- [ ] Add error logging
- [ ] Add retry mechanisms

## Phase 3 — Automation

- [ ] Introduce scheduled jobs
- [ ] Integrate n8n
- [ ] Automate data collection
- [ ] Automate cleanup
- [ ] Automate AI processing
- [ ] Add notifications

## Phase 4 — AI

- [ ] AI article classification
- [ ] Entity extraction
- [ ] Rumour classification
- [ ] Article summarization
- [ ] Story clustering
- [ ] AI-generated transfer updates
- [ ] AI agents for specialized data-processing tasks

## Phase 5 — Platform

- [ ] Advanced search
- [ ] Player pages
- [ ] Club pages
- [ ] Transfer timelines
- [ ] Rumour tracking
- [ ] Source reliability metadata
- [ ] User-facing dashboards
- [ ] Telegram publishing
- [ ] Social-media automation

## Phase 6 — Infrastructure

- [ ] Dockerize services
- [ ] Docker Compose
- [ ] CI/CD
- [ ] Automated testing
- [ ] Monitoring
- [ ] Logging
- [ ] Cloud deployment
- [ ] Reverse proxy
- [ ] Production database strategy

---

# 🐳 Challenge: Containerize the Python Service

This repository intentionally leaves an infrastructure challenge for developers who clone the project.

## 🎯 Challenge Objective

Take the Python component of the project and turn it into a **Docker container**.

The goal is to transform:

```text
Python source code
+
Python dependencies
+
Runtime configuration
```

into:

```text
Dockerfile
      ↓
Docker Image
      ↓
Docker Container
      ↓
Running API / scraper
```

---

## Challenge Requirements

### 1. Create a Dockerfile

Create:

```text
Dockerfile
```

for the Python service.

The image should:

- use an appropriate Python base image
- install the project's Python dependencies
- copy the application code
- configure the working directory
- expose the API port if using FastAPI
- start the application correctly

---

### 2. Create a requirements file

Make sure the Python service has:

```text
requirements.txt
```

containing its runtime dependencies.

For a FastAPI/Uvicorn service, this may include:

```text
fastapi
uvicorn
```

plus the project's other required packages.

---

### 3. Build the Docker image

Example:

```bash
docker build -t football-mercato-python .
```

---

### 4. Run the container

For a FastAPI service:

```bash
docker run --rm -p 8000:8000 football-mercato-python
```

Then test:

```text
http://localhost:8000/docs
```

---

### 5. Environment variables

Do not put API keys inside the Dockerfile.

Pass configuration through environment variables:

```bash
docker run --rm \
  -p 8000:8000 \
  --env-file .env \
  football-mercato-python
```

---

### ⭐ Bonus Challenge

Go beyond a single container.

Create a:

```text
docker-compose.yml
```

containing:

```text
React
   │
Node/Express
   │
MongoDB
   │
Python service
```

The final objective is to start the development environment with:

```bash
docker compose up
```

---

# 🧠 Advanced Challenge

Once the Python service works inside Docker, try to improve the solution.

### Level 1

Containerize the Python API.

### Level 2

Containerize the scraper.

### Level 3

Add MongoDB.

### Level 4

Add the Node backend.

### Level 5

Add the React frontend.

### Level 6

Connect everything through Docker Compose.

### Level 7

Add health checks.

### Level 8

Add persistent MongoDB storage.

### Level 9

Add a reverse proxy.

### Level 10

Create a CI/CD pipeline that:

```text
Git push
   ↓
Build
   ↓
Test
   ↓
Docker image
   ↓
Registry
   ↓
Deployment
```

This turns the project into a practical **DevOps + software engineering portfolio project**.

---

# 💡 Why This Challenge Matters

The Docker challenge is not just about learning Docker syntax.

It teaches the complete deployment lifecycle:

```text
Application
    ↓
Dependencies
    ↓
Reproducible environment
    ↓
Docker image
    ↓
Container
    ↓
Service
    ↓
Networking
    ↓
Persistent data
    ↓
Automation
    ↓
CI/CD
```

This makes the Football Mercato Application useful not only as a football project, but also as a practical demonstration of:

- Python development
- Backend development
- API development
- Web scraping
- Data engineering
- MongoDB
- AI integration
- Docker
- DevOps
- CI/CD
- Cloud deployment

---

# 🤝 Contributing

Contributions are welcome.

A good contribution should ideally:

1. Explain the problem.
2. Describe the proposed solution.
3. Keep components separated.
4. Avoid hard-coded secrets.
5. Include tests where appropriate.
6. Update documentation when behavior changes.

---

# ⚠️ Disclaimer

This project is intended for educational, experimental, and software-engineering purposes.

When collecting data from third-party websites or APIs, users are responsible for respecting the relevant:

- Terms of Service
- API usage policies
- robots.txt directives
- copyright/licensing requirements
- rate limits

---

# 📜 Project Vision

The long-term vision is to transform the project from a personal transfer-news application into an automated football information pipeline:

```text
                ┌────────────────────┐
                │   Multiple Sources │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Automated Ingestion│
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Data Processing    │
                │ + Normalization    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ MongoDB            │
                └──────────┬─────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
      ┌──────────────┐          ┌──────────────┐
      │ REST APIs    │          │ AI Agents    │
      └──────┬───────┘          └──────┬───────┘
             │                         │
             └────────────┬────────────┘
                          ▼
                 ┌──────────────────┐
                 │ React Application│
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
        Web Application          Future Channels
                                Telegram / Social
```

The next major milestone is **stabilization first, automation second, containerization third, and production infrastructure after that**.

---

## 👨‍💻 Project

**Football Mercato Application**

A personal full-stack project exploring football data collection, transfer intelligence, automation, AI, and modern software/DevOps practices.
