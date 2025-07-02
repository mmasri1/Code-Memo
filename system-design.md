notes:
- list of questions to ask the interviewer with the answers
- add non-func req like number of users, avg size of vid/tweet (1kb), how much GB per day, ratio of upload/watch (R/W), amount of reads per day
- storage type: object / db / file system
- db pick: do we need joins? -> relational db

1. Step 1: Requirements Gathering:
- Functional Requirements
- Non-Functional Requirements
2. Step 2: High-Level Architecture
3. Step 3: Database Design (Simplified)
4. Step 4: Scaling and Performance

<br>

### System Design and Architecture

System design is the art of figuring out how to build software that works well at scale. It’s all about making the right choices for how everything holds up under real world pressure.

<br>

##### System Design Concepts

1. [Main Concepts](/systemdesign/system-design-concepts.md)

<br>

### 🚀 Designing Real World Systems

<br>

#### Core Social Platforms

| System        | Concepts Covered                                     |
| ------------- | ---------------------------------------------------- |
| [Facebook](/systemdesign/facebook.md)  | News Feed, Graph DB, caching, massive fan-out        |
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

