# REST API Automation Framework

A modular REST API test automation framework built with **Python**, **Pytest**, and **Requests**. Designed with a layered service-object architecture, centralized route configuration, and fixture-driven session and authentication management.

---

## Architecture & Project Structure

```
api-automation-framework/
├── apiTest/                       # Test suites & Pytest fixtures
│   ├── conftest.py                # Session-scoped fixtures (HTTP client, auth tokens, test data)
│   ├── test_loginTest.py          # Authentication & token validation tests (200, 400, 401)
│   ├── test_postExtraction.py     # CRUD lifecycle & negative tests for Post resources
│   └── test_restapi.py            # Object/User lifecycle tests (POST, PATCH, DELETE)
├── data/
│   └── data.json                  # Externalized test data, environments, and payloads
├── src/
│   ├── apiClient/                 # Service layer / API abstraction
│   │   ├── api_client.py          # Base API client (session handling, URL builder, HTTP verbs)
│   │   ├── authentication.py      # Auth service client (login, profile, session state)
│   │   ├── postHandling.py        # Post service operations
│   │   └── userHandling.py        # User/Resource service operations
│   └── config/
│       └── endpoints.py           # Centralized endpoint registry & URI builders
└── pytest.ini                     # Pytest configuration & custom marker declarations
```

---

## Core Engineering Features

### 1. Layered Service-Object Architecture
- **Base Client (`baseAPI`):** Wraps `requests.Session` for persistent connections, auto-injects default headers (`application/json`), normalizes base URLs, and encapsulates core HTTP verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
- **Domain Clients (`loginAPI`, `postAPI`, `userAPI`):** Subclass `baseAPI` to expose high-level business methods, decoupling test logic from network and serialization concerns.

### 2. Centralized Endpoint Management (`Endpoints`)
- All API routes and parameterized URI builders (e.g., `post_by_id`, `user_by_id`) reside in a single registry, eliminating hardcoded URLs and isolating route maintenance.

### 3. Fixture-Driven Session & Auth Lifecycle
- **Connection Pooling:** Session-scoped `http_client` fixture manages a persistent `requests.Session` with proper cleanup (`session.close()`) on test teardown.
- **Automated Token Management:** `token_auth` fixture authenticates upfront, validates response integrity, and injects Bearer JWT tokens into protected test suites without duplicate setup code.

### 4. Data-Driven Testing (DDT)
- Target base URLs, auth credentials, and request payloads reside in `data/data.json` and are consumed via Pytest fixtures, decoupling test scenarios from hardcoded payloads.

### 5. Multi-Scenario & Negative Testing
- Validates full HTTP response semantics: status codes (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`).
- Covers complete resource lifecycles: Create -> Patch -> Delete -> Verification.

### 6. Granular Test Orchestration (Pytest Markers)
- Pre-configured markers in `pytest.ini` (`smoke`, `correctlogin`, `createPost`, etc.) enable selective execution and CI/CD pipeline filtering.

---

## Setup & Execution

### Prerequisites
```bash
pip install pytest requests
```

### Test Execution Commands

```bash
# Execute full test suite
pytest -v

# Run smoke tests
pytest -m smoke -v

# Run authentication and authorization suite
pytest apiTest/test_loginTest.py -v

# Run specific functional test markers
pytest -m "createPost or updatePost" -v
```
