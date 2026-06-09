# Fleet Management SaaS Development Plan

## Project Overview
Building a multi-tenant SaaS for small transport rental companies.

## Architecture
- **Backend**: FastAPI (Python 3.12)
- **Frontend**: React + Vite + Tailwind + shadcn/ui
- **DB**: PostgreSQL
- **Infrastructure**: Docker Compose

## Roadmap

### Phase 1: Core & Auth (Current)
- [ ] Project directory structure setup
- [ ] Docker orchestration (Postgres, Backend, Frontend)
- [ ] Database Schema: `Company`, `User` (Owner/Staff)
- [ ] Authentication: JWT + Password Hashing + Session management
- [ ] Tenant Isolation: Middleware to filter data by `company_id`

### Phase 2: Fleet & Status Engine
- [ ] CRUD for `Vehicle`
- [ ] Custom `Status` system with business logic (State Machine)
- [ ] API for adding/removing vehicles

### Phase 3: Rental Module
- [ ] `Customer` management
- [ ] Rental transaction engine (Start/End rental)
- [ ] Payment placeholder (Interface for future acquiring)

### Phase 4: Frontend implementation
- [ ] Dashboard Layout with multi-tenancy support
- [ ] Vehicle Management UI (Tables, Forms)
- [ ] Rental Process UI (Step-by-step wizards)
- [ ] Internal Notification Center
