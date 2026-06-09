# Technical Roadmap & Specification: Fleet Management SaaS (AI_progect)

## 1. Executive Summary
A multi-tenant SaaS platform designed for small-scale transport rental companies. The system provides a centralized management interface to track vehicle fleets, manage rentals, and handle customer data with strict isolation between different company tenants.

---

## 2. System Architecture
### 2.1 Technical Stack
*   **Backend**: Python 3.12+, FastAPI (Asynchronous API).
*   **Frontend**: React 18+, Vite, Tailwind CSS, shadcn/ui (Modern, high-performance UI).
*   **Database**: PostgreSQL (Relational, ACID compliant, robust JSONB support).
*   **ORM**: SQLAlchemy 2.0 (Async mode) + Alembin (Migration management).
*   **State Management**: Python `transitions` library (for business logic enforcement).
*   **Infrastructure**: Docker & Docker Compose (Containerized environment).

### 2.2 Multi-Tenancy Strategy
**Pattern: Discriminator Column (Shared Schema)**
Every table related to business data (`Vehicle`, `Rental`, `Customer`, `Status`) will contain a `company_id` column. 
*   **Enforcement**: A FastAPI middleware/dependency will extract `company_id` from the JWT token and inject it into all database queries to prevent cross-tenant data leakage.

---

## 3. Data Architecture (ERD Specification)

### 3.1 Core Entities
| Entity | Key Attributes | Relationships |
| :--- | :--- | :--- |
| **Company** | `id` (UUID), `name`, `owner_email`, `created_at` | Has many Users, Vehicles, Statuses |
| **User** | `id`, `company_id` (FK), `role` (Owner/Staff), `email`, `hashed_pw` | Belongs to Company |
| **Vehicle** | `id`, `company_id` (FK), `vin`, `model`, `current_status_id` (FK) | Belongs to Company, Has one Status |
| **Status** | `id`, `company_id` (FK), `name` (e.g., 'Repair'), `color` | Belongs to Company |
| **Customer**| `id`, `company_id` (FK), `full_name`, `phone`, `passport_data` | Belongs to Company, Linked to Rentals |
| **Rental** | `id`, `vehicle_int_id` (FK), `customer_id` (FK), `start_date`, `end_date`, `prepayment` | Links Vehicle, Customer, and Company |

---

## 4. Implementation Roadmap

### Phase 1: Foundation & Identity (The "Core")
**Goal**: Establish the secure environment and authentication flow.
*   **Infrastructure**: Dockerize PostgreSQL, FastAPI, and React. Setup Alembic migrations.
*   **Auth Module**: 
    *   JWT-based authentication.
    ...
*   **DoD**: A user can register a company, create a staff member, and authenticate via API.

### Phase 2: Fleet & State Machine (The "Engine")
...

### Phase 3: Rental & Financials (The "Transaction")
...

### Phase 4: UI/UX implementation (The "Window")
...

---

## 5. Quality Assurance (QA) Plan
...

---

### Current Active Task
- [x] **task-01-init-structure**: Initialize project structure for AI_progect.
- [ ] **task-02-db-setup**: Setup PostgreSQL in Docker and define initial SQLAlchemy models (Company, User).
