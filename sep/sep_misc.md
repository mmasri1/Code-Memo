#### Quick random notes

<br>

##### SDLC

The Software Development Life Cycle, or SDLC, is a structured process used to design, develop, test, and deploy software systems. SDLC includes a series of steps and phases:

- Requirement Analysis
- System Design
- Implementation (Coding)
- Testing
- Deployment
- Maintenance

SDLC Methodologies:

- Waterfall: A linear and sequential approach where each phase must be completed before the next begins. Works best for well-defined, unchanging requirements.

- Agile: An iterative and flexible approach that delivers small, working software increments regularly.

- Scrum: A type of Agile methodology that organizes work into sprints (usually 2–4 weeks), involves roles like Scrum Master and Product Owner with regular stand-up meetings.

- Kanban: Focuses on continuous delivery and visual task tracking using boards and cards.

- Spiral: Combines iterative development with risk assessment.

- V-Model (Validation & Verification): An extension of Waterfall where each development phase has a corresponding testing phase, emphasizes early test planning and strict discipline.

<br>

##### Issue Types in Jira:

- Epic: Large feature or goal split into stories; spans multiple sprints.
- Story: User-focused functionality; completed in one sprint.
- Task: Specific work item, often part of a story or epic.
- Sub-task: Smaller unit of a task; used for detailed breakdown.
- Bug: Issue to be fixed.
- Spike: Research task to resolve uncertainty.

<br>

##### Software Development Approaches

1. Domain-Driven Design (DDD): Understanding the problem and modeling the software around the real world (domain).

2. Test-Driven Development (TDD): Writing tests first to guide your coding. Keep refactoring code while keeping tests green.

3. Behavior-Driven Development (BDD): Describing how software should behave in plain language to connect business and development.

<br>

##### CI/CD

- Continuous Integration: Developers regularly merge their code changes into a shared main branch, and every time code is merged, automated tests and checks run immediately to make sure nothing breaks.

- Continuous Delivery (CD): After passing these tests, code is automatically prepared to be released to production.

- Continuous Deployment (CD): Making every change that passes tests is automatically deployed.

<br>

##### Authentication and Authorization

Authentication is the process of verifying the identity of a user or system. Authentication Methods:

- Username + Password
- MFA (Multi-Factor Authentication) (e.g., SMS, authentication app).
- OAuth2: An open standard for token-based authentication that allows third-party applications to access user data without exposing credentials, example: “Continue with Google” button.
- Single Sign-On (SSO): Instead of creating a new account on each site, you get one shared account, example: Google, Gmail, YouTube..

<br>

Authorization determines what actions an authenticated user is allowed to perform. Authorization Methods:

1. Role-Based Access Control (RBAC).
2. Attribute-Based Access Control (ABAC) (e.g, Policies and Attributes)
3. Access Control Lists (ACLs)

<br>

##### Architecture Styles

- Monolithic Architecture: A single unified application where all parts are tightly connected, simple to build and deploy but hard to scale or update parts independently.

- Microservices Architecture: Breaks app into small independent services that communicate over APIs.

- Event-Driven Architecture: Components communicate asynchronously by sending and reacting to events.

- Service-Oriented Architecture: Uses reusable services connected by standardized protocols, supports complex business workflows and integration.

<br>

##### Naming Conventions

1. Variables and Properties: `snake_case` or `camelCase`.
2. Constants: `UPPER_SNAKE_CASE`.
3. Functions and Methods: `camelCase`.
4. Classes, Namespaces, and Modules: `PascalCase`.
5. Files and Folders: `kebab-case` or `snake_case`.

<br>

##### HTTP Methods

- `GET`: Retrieves data from the server (no modifications).
- `POST`: Creates a new resource.
- `PUT`: Replaces or creates a resource.
- `DELETE`: Removes a resource.
- `PATCH`: Applies partial updates to a resource.
- `OPTIONS`: Returns the HTTP methods and communication options supported by a resource.
- `HEAD`: Retrieves only the headers of a resource without the body, used for metadata checks.

<br>

##### Server Codes

`100 Continue`: Server received initial request part; client should continue sending.

`101 Switching Protocols`: Server is changing protocol as requested (to WebSocket for example).

`102 Processing`: Server is working on the request but no response yet (used to avoid timeouts).

`200 OK`: Request succeeded and the response contains the requested data.

`201 Created`: Request succeeded and a new resource was created.

`204 No Content`: Request succeeded but no content is returned in the response.

`218 This is fine`: Request was successful, but things may not actually be fine :P

`301 Moved Permanently`: Resource permanently moved; future requests should use new URL.

`307 Temporary Redirect`: Request should temporarily redirect; future requests still use original URL.

`400 Bad Request`: Invalid request syntax or malformed data.

`401 Unauthorized`: Authentication required to access resource.

`403 Forbidden`: Server refuses to authorize the request despite understanding it.

`404 Not Found`: Resource not found at the requested URL.

`405 Method Not Allowed`: HTTP method used is not supported by the resource.

`429 Too Many Requests`: Client has sent too many requests in a given timeframe (rate limiting).

`500 Internal Server Error`: Server encountered an unexpected error.

`501 Not Implemented`: Server does not support the requested functionality.

`502 Bad Gateway`: Server acting as proxy received invalid response from upstream.

`503 Service Unavailable`: Server is overloaded or down for maintenance.

<br>

##### HTTP vs HTTPS

HTTP is the HyperText Transfer Protocol used for unsecured communication over the web, while HTTPS is HTTP Secure which adds encryption via TLS/SSL to ensure data confidentiality, integrity, and authentication between client and server.

#### SLA Levels

| SLA %       | Max Downtime/Year   | Typical Use Case                             | Considered Good? |
| ----------- | ------------------- | -------------------------------------------- | ---------------- |
| **99.9%**   | \~8.76 hours/year   | Mid-tier apps, internal tools                | Decent           |
| **99.95%**  | \~4.38 hours/year   | SaaS apps, e-commerce                        | Good             |
| **99.99%**  | \~52.6 minutes/year | High-availability systems (APIs, DBs)        | **Very Good**    |
| **99.999%** | \~5.26 minutes/year | Mission-critical (finance, healthcare)       | **Excellent**    |
| **100%**    | 0 minutes/year      | Unrealistic in practice (no one offers this) | ❌ Not realistic  |

#### What's *Generally* Considered Good?

* **99.9%** is the bare minimum for most production-level software.
* **99.99%** is expected for most cloud services (AWS, Google Cloud, Azure).
* **99.999% ("five nines")** is considered "enterprise-grade" and used in critical systems.

#### Throttling vs Rate limiting

Throttling: Gradually slows down user requests to control traffic flow.
Rate limiting: Strictly caps the number of user requests allowed in a time window.