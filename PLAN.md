# Technical Roadmap & Specification: Fleet Management SaaS (AI_progect)

## 1. Executive Summary
A multi-tenant SaaS platform designed for small-scale transport rental companies. The system provides a centralized management interface to track vehicle fleets, manage rentals, and handle customer data with strict isolation between different company tenants.

---

## 2. System Architecture
### 2.1 Technical Stack
*   **Backend**: Python 3.12+, FastAPI (Asynchronous API).
*   **Frontend**: React 18+, Vite, Tailwind CSS, shadcn/ui (Modern, high-performance UI).
*   **Database**: PostgreSQL (Relational, ACID compliant, robust JSONB support).
*   **ORM**: SQLAlchemy 2.0 (Async mode) + Alembic (Migration management).
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
    *   Password hashing (Argon2/Bcrypt).
    *   RBAC (Role-Based Access Control): Owner vs Staff.
*   **Tenant Logic**: Middleware for `company_id` injection.
*   **DoD**: A user can register a company, create a staff member, and authenticate via API.

### Phase 2: Fleet & State Machine (The "Engine")
**Goal**: Implement the lifecycle of a vehicle.
*   **CRUD Operations**: Full management of `Vehicle` and `Status` entities.
*   **State Engine**: Implementation of `transitions` library.
    *   *Rule Example*: `Status: Repair` $\rightarrow$ *Action: Rent* = **FORBIDDEN**.
    *   *Rule Example*: `Status: Available` $\rightarrow$ *Action: Rent* = **ALLOWED**.
*   **DoD**: Ability to create a vehicle and change its status via API while respecting business rules.

###Phase 3: Rental & Financials (The "Transaction")
**Goal**: Handle the business value of the platform.
*   **Customer Registry**: Management of client profiles.
*   **Rental Module**: Logic for calculating rental duration, verifying availability, and recording prepayment.
*   **Payment Interface (Adapter Pattern)**: Create an abstract `PaymentProvider` interface to allow future integration with Stripe/Square/etc.
*   **DoD**: A completed rental record exists in the DB linking a customer, vehicle, and payment amount.

### Phase Phase 4: UI/UX implementation (The "Window")
**Goal**: Translate API logic into a professional dashboard.
*   **Dashboard Layout**: Sidebar navigation, multi-tab view (Fleet, Active Rentals, Clients).
*   **Live Components**: Real-time status indicators using Tailwind color coding.
*   **Forms & Wizards**: Multi-step forms for complex rental creation.
*   **DoD**: A fully functional web interface that mirrors all backend capabilities.

---

## 5. Quality Assurance (QA) Plan
*   **Unit Testing**: Pytest for business logic (especially the State Machine and Auth middleware).
*   **Integration Testing**: Testing the interaction between FastAPI and PostgreSQL using Testcontainers.
*   **E2E Testing**: Playwright/Cypress to verify critical user flows (Login $\rightarrow$ Create Vehicle $\rightarrow$ Start Rental).
*   **Security Audit**: Automated scanning of JWT implementation and SQL injection prevention.

### Current Active Task
- [x] **task-02-db-setup**: Setup PostgreSQL in Docker and define SQLAlchemy models for Company and User.
- [/] **task-01-db-models**: Define core SQLAlchemy models (Companies, Vehicles, etc.). Status: __in_progress__