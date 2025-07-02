### System Design Main

<br>

##### Fundamentals

1. Scalability: Ability of a system to handle increased load by scaling vertically or horizontally.
2. Latency: Time taken to process a single request or operation.
3. Throughput: Number of requests a system can handle per unit time.
4. Availability: Percentage of time the system is operational and accessible.
5. Reliability: Ability of a system to function correctly over time without failure.
6. Maintainability: Ease with which a system can be modified or extended.
7. Fault Tolerance: System’s ability to remain functional despite failures.
8. Redundancy: Duplication of components to ensure availability in case of failure.
9. Load Balancing: Distributes incoming network traffic across multiple servers.
10. Caching: Temporarily storing data for faster access on repeated requests.
11. Data Partitioning (Sharding): Splitting data across multiple databases or nodes.
12. Replication: Copying data across multiple machines for fault tolerance and read scalability.
13. Consistency: Ensures every read returns the most recent write.
14. CAP Theorem: In distributed systems, you can only guarantee two of Consistency, Availability, and Partition Tolerance.
15. ACID: Atomicity, Consistency, Isolation, Durability; guarantees for database transactions.
16. BASE: Basically Available, Soft state, Eventually consistent; common in distributed NoSQL systems.
17. Concurrency: Ability to handle multiple operations or users at the same time.
18. Idempotency: Performing the same operation multiple times results in the same effect.
19. Rate Limiting: Restricting the number of operations per user or client in a given time frame.
20. Backpressure: Mechanism to handle overwhelming input by slowing down producers.

##### Architectural

21. Monolithic Architecture: A single unified codebase where all functionality is packaged together.
22. Microservices: Architecture where functionalities are split into independent, deployable services.
23. Service-Oriented Architecture: Similar to microservices but with more emphasis on enterprise services and interoperability.
24. Event-Driven Architecture: Systems communicate using events rather than direct API calls.
25. Serverless Architecture: Backend is managed by the cloud provider, and developers focus only on code.
26. Layered Architecture: Divides responsibilities into layers like presentation, business, and data access.
27. Hexagonal Architecture (Ports and Adapters): Isolates the core logic from outside dependencies.
28. Domain-Driven Design (DDD): Designing software based on real-world business models.
29. Command Query Responsibility Segregation (CQRS): Separates read and write operations into different models.
30. Event Sourcing: Storing all changes to application state as a sequence of events.
31. Model-View-Controller (MVC): Separates an application into three interconnected components.
32. Model-View-ViewModel (MVVM): Enhances MVC for modern UIs with better state management.

##### Distributed Systems

33. Leader Election: Selecting a coordinator node among peers in a cluster.
34. Heartbeat: Regular signal sent to indicate a system is alive.
35. Gossip Protocol: Spreading information through decentralized communication between nodes.
36. Vector Clocks: Tracking causality between events in distributed systems.
37. Quorum: Minimum number of votes required to proceed with an operation (e.g. read/write).
38. Distributed Consensus: Agreement among distributed nodes, e.g., using Paxos or Raft.
39. Replication Lag: Delay between primary and secondary node updates.
40. Data Locality: Keeping data close to where it is processed to reduce latency.
41. Distributed Locking: Mechanism to safely manage access to shared resources across nodes.
42. Anti-Entropy: Process of synchronizing inconsistent replicas.

##### Communication & APIs

43. REST: Representational State Transfer; uses HTTP for stateless communication.
44. GraphQL: Query language for APIs allowing clients to request only needed data.
45. gRPC: High-performance RPC framework using Protocol Buffers.
46. WebSockets: Bi-directional communication between client and server over a single TCP connection.
47. Message Queues: Asynchronous communication via queues (e.g., RabbitMQ, Kafka).
48. Pub/Sub: Publisher-subscriber model for event-based messaging.

##### Databases & Storage

49. Relational Databases: Structured data stored in tables with defined schemas (e.g., PostgreSQL).
50. NoSQL Databases: Schema-less or flexible schema databases (e.g., MongoDB, Cassandra).
51. Columnar Storage: Data stored by columns, optimized for analytical queries.
52. Key-Value Stores: Data stored as key-value pairs (e.g., Redis).
53. Document Stores: Data stored as JSON-like documents (e.g., MongoDB).
54. Time-Series Databases: Optimized for storing time-stamped data (e.g., InfluxDB).
55. Full-Text Search Engines: Specialized databases for search (e.g., Elasticsearch).
56. Write-Ahead Logging (WAL): Logs changes before applying to ensure durability.
57. Compaction: Process of cleaning up redundant/deleted data in log-structured systems.
58. Cold vs Hot Storage: Trade-off between access speed and cost of storing data.

##### Testing & Observability

59. Monitoring: Collecting system metrics for performance and health.
60. Logging: Capturing events and errors during system execution.
61. Tracing: Following the flow of a request across multiple services.
62. Health Checks: Endpoints or processes to validate system readiness and liveness.
63. Canary Releases: Gradually rolling out a new version to a subset of users.
64. Blue-Green Deployment: Switching between two environments for zero-downtime deployment.
65. Chaos Engineering: Intentionally introducing failures to test system resilience.

##### Performance & Optimization

66. Content Delivery Network (CDN): Caches and delivers content closer to users.
67. Edge Computing: Performing computation near the data source to reduce latency.
68. Lazy Loading: Loading data only when it’s needed.
69. Pre-fetching: Loading data in advance to improve perceived performance.
70. Compression: Reducing size of data to improve transfer speed.
71. Connection Pooling: Reusing existing DB connections instead of creating new ones.
72. Database Indexing: Speeds up data retrieval by indexing certain fields.

##### Security

73. Authentication: Verifying the identity of a user.
74. Authorization: Granting access to resources based on permissions.
75. OAuth: Open standard for delegated authorization.
76. JWT (JSON Web Tokens): Compact way to transmit identity and claims between parties.
77. TLS/SSL: Encrypts communication over networks.
78. HMAC: Ensures message integrity and authenticity.
79. Rate Limiting for Abuse Prevention: Prevents DoS and bot abuse.
80. CSRF/XSS Prevention: Mitigating cross-site request forgery and scripting attacks.

##### DevOps & CI/CD

81. Infrastructure as Code (IaC): Managing infrastructure through version-controlled code.
82. Containerization: Isolating apps and dependencies (e.g., Docker).
83. Orchestration: Managing containers and workloads (e.g., Kubernetes).
84. CI/CD Pipelines: Automating testing and deployment processes.
85. Secrets Management: Securely storing and accessing credentials and keys.

##### Design & Tradeoffs

86. Vertical Scaling vs Horizontal Scaling: Adding power vs adding more machines.
87. Strong Consistency vs Eventual Consistency: Immediate accuracy vs eventual synchronization.
88. Latency vs Throughput: Speed vs capacity tradeoff.
89. Read vs Write Optimization: Prioritizing data access or data mutation.
90. Precomputed Data vs On-the-Fly Computation: Speed vs flexibility.


#### Misc

Background
1. Computer Architecture:
CPU vs GPU: roles, multitasking, parallelism: CPU handles complex sequential tasks, GPU excels at massive parallel processing.
Memory hierarchy: Registers → L1/L2/L3 cache → RAM → Disk: The closer to the CPU, the faster and smaller the memory.
I/O and Buses: how data moves in/out: Buses are data highways connecting the CPU to the outside world.
Instruction cycle: fetch → decode → execute → write-back: Each instruction runs through a loop of getting, understanding, doing, and saving.
Virtual memory and paging: Virtual memory tricks programs into thinking they have more RAM by swapping pages with disk.
Multicore and threads: Multiple cores and threads divide and conquer tasks for faster performance.
Cache coherence and consistency issues: Caches must stay synchronized to ensure all cores see the same data.

2. Application Architecture:
- Monolith vs Microservices vs Serverless: Monoliths are all-in-one systems, microservices split functionality into independent services, and serverless runs isolated functions on demand without managing servers.
- 3-tier architecture: Presentation, Application, Data: A layered model separating user interface, business logic, and data storage for modularity and scalability.
- Clean architecture / hexagonal / onion: Architecture styles that place business logic at the core and isolate it from external frameworks, databases, and interfaces.
- Service-oriented architecture (SOA): A design where loosely coupled, reusable services communicate over a network to perform business functions.
- REST vs gRPC vs GraphQL: REST is resource-based and human-readable, gRPC is binary and high-performance, GraphQL allows flexible, client-defined queries.
- Synchronous vs asynchronous communication: Synchronous communication waits for a response before continuing, while asynchronous proceeds independently and handles responses later.
- Stateful vs stateless services: Stateful services retain session information across requests; stateless services handle each request independently without memory of previous interactions.
- Event-driven architecture: A system where components respond to events, enabling decoupling and real-time responsiveness.
- Message queues (Kafka, RabbitMQ, etc.): Infrastructure for decoupling producers and consumers by buffering and reliably delivering messages between systems.

3. Design Requirements:
- Functional vs Non-functional requirements: Functional defines what the system should do; non-functional defines how well it does it.
- Scalability (horizontal, vertical): Scalability is the ability to handle increased load by adding more machines (horizontal) or upgrading existing ones (vertical).
- Availability (uptime), Reliability, Durability: Availability is system uptime, reliability is consistent correct behavior, and durability is data persistence despite failures.
- Latency vs Throughput: Latency is the time to process a single request; throughput is the number of requests processed per unit of time.
- Security, Compliance, Auditing: Security protects systems and data, compliance ensures adherence to standards, and auditing tracks actions for accountability.
- Maintainability, Extensibility: Maintainability is ease of fixing or improving a system; extensibility is ease of adding new features.
- SLAs, SLOs, SLIs: SLAs are external commitments, SLOs are internal goals, and SLIs are the metrics used to measure them.
- Capacity planning: Capacity planning is forecasting and provisioning resources to meet future demand without over- or under-provisioning.
- Traffic estimates, read/write ratios: Traffic estimation predicts request volume; read/write ratios help design for balanced or skewed data access patterns.

Networking
4. Networking Basics:
- What is a network?: A network is a collection of connected devices that communicate and share resources using standard protocols.
- IP addresses (IPv4, IPv6): IP addresses uniquely identify devices on a network; IPv4 uses 32-bit addresses, while IPv6 uses 128-bit for a larger address space.
- MAC addresses: MAC addresses are unique hardware identifiers assigned to network interfaces for communication within a local network.
- Ports (e.g., HTTP → port 80): Ports are numerical identifiers for specific services on a device, enabling multiple services to run on the same IP address.
- LAN vs WAN: LAN covers a small local area like a home or office, while WAN spans large geographical areas, connecting multiple LANs.
- NAT (Network Address Translation): NAT maps private IP addresses to a public IP, allowing multiple devices to share a single public address.
- Firewall and packet filtering: Firewalls control network traffic by allowing or blocking packets based on security rules and packet content.
- Routing and switching: Routers direct traffic between networks, while switches connect devices within a local network and forward packets based on MAC addresses.
- HTTP, HTTPS basics: HTTP is an application-layer protocol for web communication; HTTPS adds encryption for secure data transfer using SSL/TLS.
- Ping, traceroute, and ICMP: Ping and traceroute use ICMP to test connectivity and trace the path packets take across a network.

5. TCP and UDP:
- What is TCP vs UDP?: TCP is reliable, ordered, and connection-based; UDP is unreliable, unordered, and connectionless.
- Three-way handshake (SYN → SYN-ACK → ACK): A three-step process TCP uses to establish a reliable connection between sender and receiver.
- Congestion control and retransmission: TCP reduces transmission speed when the network is congested and retransmits lost packets to ensure delivery.
- Flow control and sliding window: Flow control prevents overwhelming the receiver, and the sliding window manages how much data can be sent before requiring acknowledgment.
- Packet segmentation and reassembly: Large data is broken into packets for transmission and reassembled at the destination in the correct order.
- Ports and sockets: Ports identify specific processes on a device, and sockets are endpoints for sending and receiving data over a network.
- Common uses of each: TCP is used for applications needing reliability like HTTP, FTP, and email; UDP is used for speed-sensitive tasks like DNS, video calls, and gaming.

6. DNS:
- What is DNS?: DNS translates human-readable domain names into IP addresses for locating servers on the internet.
- DNS resolution flow: DNS resolution checks the browser cache, OS cache, router, ISP DNS server, and if needed, queries root DNS, TLD DNS, and authoritative DNS servers.
- A, AAAA, CNAME, MX, NS records: A maps to IPv4, AAAA to IPv6, CNAME to aliases, MX to mail servers, and NS to name servers for a domain.
- TTL (Time to Live): TTL defines how long a DNS record is cached before it must be re-queried.
- DNS propagation: DNS propagation is the time it takes for DNS record changes to update across the internet due to cached TTLs.
- DNS over HTTPS (DoH): DoH encrypts DNS queries over HTTPS to enhance privacy and prevent eavesdropping or manipulation.
- Tools: dig, nslookup: dig and nslookup are command-line tools used to query DNS records and troubleshoot resolution issues.

APIs
7. HTTP:
- HTTP (Hypertext Transfer Protocol): The foundational protocol for the web using a request-response model.
- HTTP Methods: Common methods include GET, POST, PUT, DELETE, PATCH, OPTIONS, and HEAD.
- Status Codes:
    - 1xx: Informational
    - 2xx: Success (e.g., 200 OK, 201 Created)
    - 3xx: Redirects
    - 4xx: Client errors (e.g., 404 Not Found, 401 Unauthorized)
    - 5xx: Server errors (e.g., 500 Internal Server Error)
- Headers: Metadata such as Content-Type, Authorization, and Cache-Control included in requests and responses.
- Cookies and Sessions: Techniques for maintaining state and user authentication in an otherwise stateless protocol.
- Statelessness: Each HTTP request is independent with no stored context between requests.
- HTTPS (TLS/SSL) basics: Secure version of HTTP that encrypts data in transit using TLS/SSL.
- Caching mechanisms: Use of ETag and Cache-Control headers to optimize response reuse and reduce bandwidth.
- HTTP/1.1 vs HTTP/2 vs HTTP/3: Protocol versions differing mainly in performance, multiplexing, and transport mechanisms, with HTTP/3 built on QUIC over UDP.

8. WebSockets:
- WebSockets: A full-duplex communication channel over a single TCP connection enabling real-time bidirectional data exchange.
- Differences from HTTP: WebSockets provide persistent, bidirectional communication unlike the stateless, request-response model of HTTP.
- Use cases: Commonly used for chat applications, live notifications, gaming, and stock tickers.
- Handshake process: Begins as an HTTP upgrade request to establish the WebSocket connection.
- Message frames and control frames: Data is transmitted in frames that carry messages or control signals like ping/pong.
- Connection lifecycle: Includes states such as open, message exchange, close, and heartbeat via ping/pong frames.
- Scaling WebSockets: Requires handling sticky sessions and presents challenges for load balancing due to persistent connections.

9. API Paradigms:
- API Paradigms: Different architectural styles and protocols for designing APIs and data exchange.
- REST (Representational State Transfer): Stateless, resource-based, uses HTTP verbs with JSON or XML payloads.
- GraphQL: Allows clients to define queries, enabling efficient data fetching through a single endpoint.
- gRPC: Remote procedure call (RPC) based, uses Protobuf for serialization, high performance, and supports streaming.
- SOAP: An older XML-based protocol, more rigid with built-in standards for security and transactions.
- Event-Driven APIs: Use message queues or publish/subscribe models to communicate asynchronously.
- API versioning: Managing changes and backward compatibility of APIs over time.
- API documentation and tools: OpenAPI/Swagger provide standardized ways to document and test APIs.

10. API Design:
- API Design: Principles and best practices for creating effective and maintainable APIs.
- Design principles: Focus on consistency, simplicity, predictability, and security.
- Resource modeling: Defining clear and logical representations of entities in the API.
- URL design: Use nouns, hierarchical structure, support filtering and pagination for resource endpoints.
- Request and response structure: Standardized formats for inputs and outputs, typically JSON.
- Error handling: Clear and consistent error codes and messages for client understanding.
- Authentication and authorization: Mechanisms like OAuth, JWT, and API keys to secure access.
- Rate limiting and throttling: Controls to prevent abuse and ensure fair resource use.
- API gateway role: Acts as a proxy for routing, security, rate limiting, and analytics.
- Versioning strategies: Techniques to manage API evolution without breaking clients.
- Idempotency: Ensuring repeated requests have the same effect as a single request.
- Testing and monitoring APIs: Continuous validation of functionality and performance.

Caching Basics
11. Caching:
- Caching: Storing copies of data closer to where it’s needed to reduce latency and system load.
- Cache Types: Includes in-memory caches (Redis, Memcached), distributed caches, browser caches, and database caches.
- Cache Hierarchy: Multiple layers such as CPU cache, application cache, and CDN cache.
- Cache eviction policies: Strategies to remove old data, including LRU (Least Recently Used), LFU (Least Frequently Used), and FIFO (First In First Out).
- Cache invalidation: Methods to update or remove stale cache data, including time-based TTL, write-through, write-back, write-around, and manual invalidation.
- Cache consistency and stale data issues: Challenges in keeping cache synchronized with the source of truth.
- Cache stampede (thundering herd) problem and solutions: Occurs when many requests try to update expired cache simultaneously; mitigated by locking or request coalescing.
- Cache aside pattern vs read-through vs write-through: Different caching strategies controlling when data is loaded or written in cache.
- What to cache?: Typically database query results, API responses, and computed data to improve performance.

12. CDNs:
- CDNs (Content Delivery Networks): A globally distributed network of servers that cache static content close to users to improve performance.
- How CDNs work: Edge servers cache static assets like images, JavaScript, CSS, and videos; user requests are served from the nearest edge location, with the origin server contacted only on cache misses.
- CDN benefits: Reduced latency worldwide, decreased bandwidth and load on origin servers, and improved availability and fault tolerance.
- Cache control headers and CDN behavior: Headers control how content is cached and refreshed by CDN servers.
- CDN invalidation and purging: Mechanisms to remove or update cached content before expiration.
- Dynamic content vs static content caching: Static content is easily cached, while dynamic content caching requires special handling or is often bypassed.
- Popular CDNs: Examples include Cloudflare, Akamai, AWS CloudFront, and Fastly.
- Security features: Many CDNs provide DDoS protection, Web Application Firewalls (WAF), and SSL termination.
- CDN & API caching considerations: Strategies differ for caching APIs versus static assets to ensure freshness and performance.

Proxies
13. Proxies and Load Balancing:
- Proxies and Load Balancing: Intermediary servers that manage traffic between clients and backend servers to improve performance, security, and scalability.

- What is a proxy?: An intermediary server between clients and backend servers.
    - Forward Proxy: Acts on behalf of clients, hiding client IPs.
    - Reverse Proxy: Acts on behalf of servers, hiding backend servers from clients.
- Common proxy uses: Load balancing, security (firewall, filtering, SSL termination), caching, compression, authentication, and access control.
- Load Balancer types:
    - Layer 4 (Transport Layer): Routes based on IP address and TCP/UDP ports; fast but with limited logic.
    - Layer 7 (Application Layer): Routes based on HTTP(S) data like URLs, headers, cookies; supports sticky sessions and advanced routing.
- Load balancing algorithms: Round Robin, Least Connections, IP Hash (sticky sessions), and Weighted balancing.
- Health checks and failover: Regular checks to ensure backend servers are healthy and rerouting traffic if not.
- Sticky sessions (session persistence): Ensures a client’s requests are consistently sent to the same backend server.

14. Consistent Hashing:
- Consistent Hashing: A hashing technique that minimizes key remapping when servers are added or removed.
- Why is it needed?: Traditional modulo hashing causes many keys to remap on server count changes, causing instability.
- How it works: Both servers and keys are hashed onto a circular hash ring; each key is assigned to the next server clockwise on the ring.
- Virtual nodes: Servers are represented multiple times on the ring to improve load balancing.
- Use cases: Common in distributed caching (e.g., memcached), distributed databases, and load balancing in distributed systems.
- Trade-offs and challenges: Managing uneven load distribution and handling server failures and rebalancing.

Storage
15. SQL:
- SQL (Relational Databases): Databases based on the relational model using tables with rows, columns, schemas, and constraints like primary and foreign keys.
- ACID properties: Guarantees for reliable transactions: Atomicity, Consistency, Isolation, and Durability.
- SQL language: Commands include SELECT, INSERT, UPDATE, DELETE, JOINs, GROUP BY, and transaction control.
- Normalization vs Denormalization: Normalization reduces redundancy and improves integrity; denormalization improves read performance by adding redundancy.
- Indexes and query optimization: Techniques to speed up data retrieval by creating efficient access paths.
- Use cases: Ideal for transactional systems requiring strong consistency and complex queries.
- Popular systems: Examples include MySQL, PostgreSQL, Oracle, and Microsoft SQL Server.

16. NoSQL:
- NoSQL (Non-Relational Databases): Databases that store data in non-tabular formats designed for flexibility and scalability.
- Types of NoSQL:
    - Document stores (e.g., MongoDB, CouchDB)
    - Key-Value stores (e.g., Redis, DynamoDB)
    - Wide-column stores (e.g., Cassandra, HBase)
    - Graph databases (e.g., Neo4j)
- Eventual consistency and BASE properties: Guarantees Basically Available, Soft state, and Eventual consistency rather than strict ACID.
- Schemaless or flexible schema: Allows data structure to evolve without predefined schemas.
- Horizontal scalability: Designed to scale out easily by adding more servers.
- Use cases: Suitable for large-scale, high-throughput systems, flexible data models, and caching scenarios.

17. Replication and Sharding:
- Replication and Sharding: Techniques to distribute data across multiple nodes for scalability and fault tolerance.
- Replication: Copying data to multiple nodes to improve redundancy and availability; includes master-slave and master-master configurations; can be synchronous or asynchronous.
- vSharding (Partitioning): Splitting data horizontally across nodes based on key ranges or hashes to scale out write and read throughput.
- Benefits and challenges: Replication boosts availability but can cause consistency challenges; sharding improves throughput but complicates querying and management.
- Rebalancing shards: Moving data between shards to maintain balance as cluster size or load changes.
- Failover and recovery: Automatic or manual processes to maintain availability when nodes fail.

18. CAP Theorem:
- CAP Theorem: In distributed systems, you can only guarantee two out of three: Consistency, Availability, and Partition Tolerance.
- Consistency (C): All nodes see the same data at the same time.
- Availability (A): Every request receives a response, successful or failed.
- Partition Tolerance (P): The system continues to operate despite network partitions or failures.
- Trade-offs:
    - CA (Consistency + Availability): no tolerance for partitions, rare in distributed systems.
    - CP (Consistency + Partition Tolerance): prioritizes consistency, may reduce availability during partitions.
    - AP (Availability + Partition Tolerance): prioritizes availability, may have eventual consistency.
- Examples: Different distributed databases and systems prioritize different pairs depending on use case.

19. Object Storage:
- Object Storage: A storage architecture that manages data as objects, each containing the data itself, metadata, and a unique identifier.
- Differences from block and file storage: Unlike block storage (used by disks) or file storage (hierarchical), object storage is flat, metadata-rich, and accessed via APIs.
- Highly scalable: Designed to store large amounts of unstructured data such as images, videos, and backups.
- Examples: Amazon S3, Google Cloud Storage, Azure Blob Storage.
- Features: Supports extensive metadata, accessed via RESTful APIs, and provides high durability through replication across regions.
- Use cases: Commonly used for media hosting, backups, and big data analytics.

Big Data
20. Message Queues:
- Message Queues: A system that enables asynchronous communication between components by passing messages.
- Core properties: Decouples producers and consumers, buffers load spikes, and ensures reliable message delivery.
- Common messaging patterns:
    - Point-to-point: Messages are sent to a queue and consumed by one receiver.
    - Publish-subscribe: Messages are broadcast to multiple subscribers via topics.
- Message durability and acknowledgments: Messages can be persisted to disk, and acknowledgments confirm successful processing to prevent loss.
- Ordering guarantees: Some systems preserve message order, while others prioritize speed and scalability over strict ordering.
- Message brokers: Popular systems include RabbitMQ, Kafka, AWS SQS, and Google Pub/Sub.
- Use cases: Suitable for task queues, event streaming, log aggregation, and communication between microservices.
- Challenges: Achieving exactly-once delivery is complex; systems often choose between at-least-once and at-most-once delivery. Scaling consumers and managing retention and compaction also require careful design.

21. MapReduce:
- MapReduce: A programming model for processing large data sets using a distributed and parallel algorithm.
- Two phases:
    - Map: Transforms input data into key-value pairs.
    - Reduce: Aggregates and summarizes key-value pairs by key.
- How it works: Input data is split into chunks, processed in parallel across nodes, with built-in fault tolerance through task re-execution.
- Common implementations: Hadoop MapReduce and Apache Spark (which improves on performance and usability).
- Use cases: Ideal for log analysis, large-scale data transformation, counting, sorting, and filtering data.
- Limitations: High latency due to batch processing and not suitable for real-time or low-latency applications.


#### AWS Components:

### Core Compute & Networking 

1. EC2 (Elastic Compute Cloud) 

   * Virtual servers in the cloud.
   * Used to run web servers, apps, background jobs.
   * *Ex: Host a Django backend or run a custom script 24/7.*

2. ELB (Elastic Load Balancer) 

   * Distributes traffic across multiple servers.
   * Ensures scalability and fault tolerance.
   * *Ex: Split user traffic between 3 backend EC2 instances.*

3. Lambda 

   * Serverless function execution.
   * Runs backend logic on-demand without managing servers.
   * *Ex: Resize an image when uploaded to S3.*

4. VPC (Virtual Private Cloud) 

   * Isolated network in the cloud.
   * Used to secure and route resources like EC2, RDS, etc.
   * *Ex: Place database in private subnet, expose app in public subnet.*

### Storage 

5. S3 (Simple Storage Service) 

   * Object storage for any file or media.
   * Used for backups, static files, user uploads.
   * *Ex: Store profile pictures, videos, or logs.*

6. EBS (Elastic Block Store) 

   * Block-level storage attached to EC2.
   * Used as hard drives for EC2 VMs.
   * *Ex: Attach persistent storage to a Linux EC2 instance.*

7. EFS (Elastic File System) 

   * Shared file system for multiple servers.
   * Ideal for concurrent read/write access.
   * *Ex: Web servers sharing uploaded media files.*

### Databases 

8. RDS (Relational Database Service) 

   * Managed SQL databases (PostgreSQL, MySQL, etc.)
   * Used for structured, transactional data.
   * *Ex: Store user accounts and transactions in PostgreSQL.*

9. DynamoDB 

   * Fully managed NoSQL key-value/document DB.
   * Used for fast, scalable reads/writes.
   * *Ex: Store session tokens, leaderboard scores.*

10. ElastiCache (Redis / Memcached) 

    * In-memory cache for fast data access.
    * Used to reduce DB load and improve performance.
    * *Ex: Cache recent search results or API responses.*

### Messaging & Event Systems 

11. SQS (Simple Queue Service) 

    * Message queue for decoupling components.
    * Used for background job processing.
    * *Ex: Queue tasks like sending emails or processing uploads.*

12. SNS (Simple Notification Service) 

    * Pub/sub messaging and alerts.
    * Used for push notifications or service events.
    * *Ex: Notify user when payment is received.*

13. EventBridge 

    * Event bus for routing events between services.
    * Supports complex workflows and triggers.
    * *Ex: Trigger Lambda when an S3 upload happens.*

### Delivery & CDN 

14. CloudFront 

    * Global CDN that caches content at edge locations.
    * Speeds up delivery of static & dynamic content.
    * *Ex: Serve your React app faster globally using S3 + CloudFront.*

15. API Gateway 

    * Front door for APIs (HTTP, REST, WebSocket).
    * Used to expose and secure backend services.
    * *Ex: Create public API for a mobile app that triggers Lambda.*

### Security & Identity 

16. IAM (Identity & Access Management) 

    * Manages users, roles, and permissions.
    * Used to control access to AWS resources.
    * *Ex: Allow EC2 to access S3 but deny DynamoDB access.*

17. Cognito 

    * User authentication and user pools.
    * Used for login/signup flows without building your own.
    * *Ex: Enable social login for a web app.*

### Monitoring & Deployment 

18. CloudWatch 

    * Logs, metrics, alerts, and dashboards.
    * Used for monitoring app health and performance.
    * *Ex: Set alarm if CPU usage on EC2 goes over 80%.*

19. CloudFormation 

    * Infrastructure-as-code service.
    * Used to script and version your AWS setup.
    * *Ex: Deploy an entire VPC, EC2, and RDS stack from one YAML file.*

20. CodePipeline + CodeDeploy 

    * CI/CD pipeline tools.
    * Used to automate deployments to EC2, Lambda, etc.
    * *Ex: Auto-deploy Django app to EC2 after GitHub push.*
