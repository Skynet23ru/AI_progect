# 🤖 The AI_progect Development Team

This repository is maintained and developed by an autonomous multi-agent swarm coordinated by the Lead Architect.

## 👥 Active Agents (Skills)

### 🏗️ [Lead Architect & Manager]
*   **Role**: Orchestration, System Design, Task Decomposition.
*   **Responsibility**: Defines the roadmap, manages the `todo` backlog, and ensures all agents follow the project-wide architecture standards.
*   **Core Tool**: `hermes_agent` (Main Agent).

### 🐍 [Backend Engineer] (`skill:fleet-backend`)
*   **Expertise**: Python 3.12, FastAPI, SQLAlchemy 2.0, PostgreSQL.
*   **Responsibility**: Building the API, implementing business logic (State Machines), and enforcing multi-tenant data isolation.
*   **Standard**: Strict typing, async/await architecture.

### 🎨 [Frontend Engineer] (`skill:fleet-frontend`)
*   **Expertise**: React 18, Vite, Tailwind CSS, shadcn/ui.
*   **Responsibility**: Building the high-performance SPA, creating responsive dashboards, and implementing user-facing features.
*   **Standard**: Modern, clean, production-grade UI.

### 🔍 [QA Engineer] (`skill:fleet-qa`)
*   **Expertise**: Pytest, Playwright, Integration Testing.
*   **Responsibility**: Automated regression testing, verifying multi-tenancy security, and monitoring deployment health.
*   **Standard**: Zero-regression policy.

---

## 🛠 Workflow Architecture
All agents operate based on the **Task Backlog (`todo`)**. 
1.  **Architect** creates a task.
2.  **Specialist Agent** picks up the task and implements it.
3.  **QA Agent** verifies the implementation.
4.  The **Watchdog** (System Process) ensures the infrastructure remains operational.

*All changes are automatically synchronized to GitHub via Atomic Sync.*
