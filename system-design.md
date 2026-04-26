notes:
- avg size of vid/tweet (1kb), how much GB per day, ratio of upload/watch (R/W), amount of reads per day

STEP 1: CLARIFY THE PROBLEM
STEP 2: Define Functional Requirements
STEP 3: Define Non-Functional Requirements (NFRs)
STEP 4: Define System Interfaces / APIs
STEP 5: High-Level Architecture
STEP 6: Database Design & Schema (ERD)
STEP 7: Component Design (Low-Level Design)
STEP 8: Scaling & Optimization
STEP 9: Security & Privacy Considerations
STEP 10: Monitoring, Logging & Alerting
STEP 11: Cost & Infrastructure Planning
STEP 12: Testing & Deployment Strategies

<br>

### System Design and Architecture

System design is the art of figuring out how to build software that works well at scale. It’s all about making the right choices for how everything holds up under real world pressure.

<br>

##### System Design Concepts

1. [Main Concepts](systemdesign/system-design-concepts)

<br>

### [My Massive System](systemdesign/mymassivesystem)

### 🚀 Designing Real World Systems

<br>

#### Core Social Platforms


| #  | System                   | Why Focus? Key Concepts Covered                                              |
| -- | ------------------------ | ---------------------------------------------------------------------------- |
| 1  | [Facebook](systemdesign/facebook)             | Graph DB, News Feed, caching, massive fan-out, social graph, complex feeds   |
| 2  | [Twitter](systemdesign/twitter)             | Real-time feed, timeline fan-out, rate limiting, streaming updates           |
| 3  | [WhatsApp](systemdesign/whatsapp)             | Messaging: end-to-end encryption, offline delivery, message queues           |
| 4  | [Uber](systemdesign/uber)                 | Geo-location, live tracking, trip matching, surge pricing, real-time systems |
| 5  | [YouTube](systemdesign/youtube)              | Media streaming, CDN, recommendation system, video encoding                  |
| 6  | [Amazon](systemdesign/amazon)               | E-commerce: catalog, search, recommendations, cart, large-scale ops          |
| 7  | [GitHub](systemdesign/github)               | Developer tools: version control, PRs, code storage, collaboration           |
| 8  | [Google Search](systemdesign/googlesearch)        | Search system: crawling, indexing, ranking, autocomplete                     |
| 9  | [Netflix](systemdesign/netflix)              | Advanced media streaming: adaptive bitrate, caching, A/B testing             |
| 10 | [Kafka (Queue System)](systemdesign/kafka) | Infrastructure: messaging queue, pub/sub, partitioning, durability           |


| System        | Concepts Covered                                     |
| ------------- | ---------------------------------------------------- |
| [Facebook](systemdesign/facebook)  | News Feed, Graph DB, caching, massive fan-out        |
| Instagram | Media storage, user-generated content, notifications |
| Twitter   | Timeline fan-out, real-time feed, rate limiting      |
| LinkedIn  | Search, connections, job recommendation, analytics   |
| Reddit    | Community moderation, voting, thread hierarchy       |
| TikTok    | Infinite scroll, video CDN, AI recommendation engine |
| Snapchat  | Ephemeral media, streaks, Bitmoji integration        |


#### Messaging Systems

| System        | Concepts Covered                                               |
| ------------- | -------------------------------------------------------------- |
| WhatsApp  | End-to-end encryption, message queueing, offline delivery      |
| Messenger | Real-time chat, delivery receipts, typing indicators           |
| Slack     | Workspace isolation, channels, real-time events                |
| Discord   | Voice + text, low latency, event buses                         |
| Signal    | Privacy-focused, secure storage, no cloud backup               |
| iMessage  | Rich content, Apple-specific integrations, sync across devices |


#### On-Demand + Geo-Location

| System                                | Concepts Covered                                         |
| ------------------------------------- | -------------------------------------------------------- |
| Uber                              | Live geolocation, trip matching, surge pricing           |
| Lyft                              | Driver-passenger assignment, location tracking           |
| Google Maps                       | Route optimization, location indexing, real-time traffic |
| Food Delivery (DoorDash/UberEats) | Order tracking, batching, delivery optimization          |
| Airbnb                            | Listings, booking calendar, host ratings                 |


#### Media Streaming / Sharing

| System            | Concepts Covered                                      |
| ----------------- | ----------------------------------------------------- |
| YouTube       | Video encoding, CDN, recommendation system            |
| Netflix       | Adaptive bitrate, content caching, A/B testing        |
| Spotify       | Streaming + offline, user playlists, music rec engine |
| Twitch        | Live streaming, chat overlay, moderation              |
| Google Photos | Image deduplication, face detection, storage tiering  |


#### E-Commerce / Payments

| System              | Concepts Covered                               |
| ------------------- | ---------------------------------------------- |
| Amazon          | Catalog service, recommendations, search, cart |
| eBay            | Auction engine, bid updates, seller ratings    |
| Shopify         | SaaS multitenancy, custom storefronts          |
| Stripe          | Payment gateway, idempotency, fraud detection  |
| PayPal          | Account linking, transaction logs, refunds     |
| Razorpay/Square | POS integration, payouts, invoices             |


#### Developer Tools / SaaS

| System            | Concepts Covered                              |
| ----------------- | --------------------------------------------- |
| GitHub        | Versioning, code storage, PR system           |
| Dropbox       | File syncing, delta sync, sharing permissions |
| Figma         | Real-time collaboration, canvas syncing       |
| Notion        | Block storage model, real-time updates        |
| Google Docs   | OT (Operational Transform), user cursors      |
| Trello / Jira | Kanban boards, task linking, workflows        |
| Postman       | API storage, team collaboration, workspaces   |


#### Search / Knowledge Systems

| System             | Concepts Covered                            |
| ------------------ | ------------------------------------------- |
| Google Search  | Crawling, indexing, ranking, autocomplete   |
| Wikipedia      | Edit history, content graph, anti-vandalism |
| Quora          | Q\&A ranking, topic modeling, upvotes       |
| Stack Overflow | Tagging, gamification, moderation queue     |


#### Recommendation Systems

| System                  | Concepts Covered                          |
| ----------------------- | ----------------------------------------- |
| Netflix             | User-item matrix, collaborative filtering |
| Amazon Recs         | Co-purchase patterns, behavioral tracking |
| YouTube/TikTok Recs | Watch time-based ranking, feedback loop   |


#### Infrastructure Systems

| System                            | Concepts Covered                                 |
| --------------------------------- | ------------------------------------------------ |
| Dropbox / Google Drive        | File deduplication, sync, sharing                |
| Load Balancer                 | L4 vs L7, sticky sessions, HAProxy/Nginx         |
| Rate Limiter                  | Token bucket, leaky bucket, Redis counter        |
| Queue System (Kafka/RabbitMQ) | Pub/sub, partitioning, durability                |
| Notification System           | Email/SMS/Push pipelines, retries                |
| Monitoring/Logging System     | Alerting, metric collection, Grafana, Prometheus |
| API Gateway                   | Auth, rate limiting, routing, logging            |


#### Analytics & Big Data

| System                  | Concepts Covered                               |
| ----------------------- | ---------------------------------------------- |
| Google Analytics    | Event tracking, funnel analysis                |
| Mixpanel            | User flows, segmentation                       |
| Snowflake           | Data warehousing, scaling reads/writes         |
| Hadoop/Spark System | MapReduce, job queues, batch/stream processing |


#### Other Real-World Systems

| System                    | Concepts Covered                                   |
| ------------------------- | -------------------------------------------------- |
| Booking.com / Expedia | Availability syncing, pricing engines              |
| Calendly              | Scheduling with time zone awareness, calendar sync |
| Zoom                  | Real-time audio/video, participant control         |
| Kahoot / Quizizz      | Real-time sync for quizzes                         |
| Medium                | Drafts, editor, publishing workflow                |
| Pinterest             | Visual search, board management                    |
| Coursera / Udemy      | Video lessons, progress tracking                   |
| Duolingo              | Gamified learning, streak tracking, leaderboards   |

