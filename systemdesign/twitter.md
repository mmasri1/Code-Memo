# Designing Twitter

## ✅ STEP 1: CLARIFY THE PROBLEM

Twitter is a microblogging and social networking platform focused on short messages called *tweets*, which can include text, media (images, videos), and links.

### Core Features:

* User registration, login, profile management
* Tweet creation (up to 280 characters), retweet, reply, like
* Follow/unfollow other users
* Home timeline feed (tweets from followed users)
* Mentions and notifications
* Search (users, tweets, hashtags)
* Trending topics / hashtags
* Direct Messages (DMs) (optional, but core in real Twitter)
* User lists (optional)
* Tweet threads / conversations

### Who Are the Users?

* Global audience: hundreds of millions of users, with \~200 million daily active users (DAUs)
* Device variety: smartphones (majority), web, tablets
* Usage patterns:

  * High read/write ratio, but less extreme than Facebook because tweets are short and frequent
  * Many users "lurk" (read mostly), others tweet very frequently
  * Celebrity/brand users with millions of followers (high fan-out)
  * Bots and spammers exist (needs detection)

### Product Goals / Business Goals

* Fast and real-time delivery of tweets and notifications
* High user engagement and retention
* Scalable system to handle high read/write loads
* Personalization of timeline (ranking and filtering)
* Trust and safety: prevent abuse, spam, misinformation
* Availability and reliability
* Support live events and breaking news in real-time

### Constraints and Priorities

| Constraint / Priority | Notes                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| Latency               | Tweets and timeline updates should appear with minimal delay (<200ms ideal)                          |
| Scalability           | Millions of tweets per second at peak, billions of total tweets                                      |
| Consistency           | Strong consistency for tweet posting, follow/unfollow; eventual consistency acceptable for timelines |
| Availability          | 99.99% SLA or better                                                                                 |
| Rate limiting         | Prevent spam and abuse with rate limits and throttling                                               |
| Privacy & Security    | Protect user data, allow private accounts, enforce content policies                                  |
| Read/Write Ratio      | More balanced than Facebook; tweets are more frequent                                                |
| Real-time delivery    | Critical for notifications, mentions, trends                                                         |

### Key Use Cases

1. User creates account and logs in
2. User posts a tweet (with optional media)
3. User follows/unfollows others
4. User views their home timeline with recent tweets from followed users
5. User likes, retweets, or replies to tweets
6. User searches tweets, users, or hashtags
7. User views notifications (mentions, likes, retweets)
8. User views trending topics and hashtags
9. User sends/receives Direct Messages (optional)
10. User manages profile, privacy settings

### High-Level Metrics to Support

| Metric                    | Notes                                 |
| ------------------------- | ------------------------------------- |
| Requests per second (RPS) | Millions of tweets per second at peak |
| Timeline load latency     | <200ms P95                            |
| Tweet posting latency     | <500ms                                |
| Like/retweet latency      | <150ms                                |
| System uptime             | 99.99%+                               |
| Fan-out scale             | Millions of followers for top users   |
| Cache hit ratio           | >90% for hot timelines and tweets     |
| Data volume growth        | TBs per day, petabytes over time      |

### Personas

| Persona              | Behavior and Needs                                               |
| -------------------- | ---------------------------------------------------------------- |
| Casual user          | Reads timeline, tweets occasionally                              |
| Power user           | Tweets often, engages with many tweets                           |
| Celebrity/influencer | Millions of followers, high fan-out challenge                    |
| Brand/organization   | Scheduled tweets, analytics, high engagement                     |
| Bot/spammer          | Automated tweeting and abuse, rate limiting and detection needed |
| New user             | No followers yet, cold-start timeline challenge                  |

### Discussion & Questions to Clarify Further

* What features of Twitter do we want to support initially? (e.g., DMs, lists, polls?)
* Should the timeline be strictly reverse chronological or ranked by relevance?
* How real-time do timeline updates and notifications need to be?
* How will media (images, videos) be handled?
* Are we building only the public-facing API or also internal analytics and moderation tools?
* How do we handle abuse and spam detection? Basic rate limiting or advanced ML?
* What scale do we want to support initially? Millions or billions of users?


## ✅ STEP 2: Define Functional Requirements

### 1. User & Authentication

* Users can register with email, username, password.
* Users can log in and log out securely.
* Users can reset their password via email.
* Users can update their profile:

  * Display name
  * Username (@handle)
  * Profile picture
  * Bio
  * Location
  * Website URL
  * Birthday
  * Privacy settings (public/private account)
* Users can deactivate or delete their accounts.

### 2. Follow System

* Users can follow other users.
* Users can unfollow other users.
* Users can see the list of who they follow and their followers.
* Users with private accounts must approve follow requests.
* Users can block/unblock other users.
* Users can mute/unmute users or conversations.

### 3. Tweet System

* Users can create a tweet with:

  * Text content (up to 280 characters)
  * Media attachments (images, GIFs, videos)
  * Polls (optional)
  * Location tagging (optional)
  * Reply to another tweet (threading support)
* Users can delete their own tweets.
* Users can view their tweets.
* Users can view tweets of other users (respecting privacy).
* Users can view tweet threads and conversations.
* Tweets have metadata:

  * Creation timestamp
  * Reply/retweet/like counts
  * Language
  * Sensitive content flag
  * Visibility (public, followers-only, private DM)

### 4. Engagement System

* Users can like/unlike tweets.
* Users can retweet (share) or undo retweet.
* Users can quote retweet (retweet with comment).
* Users can reply to tweets.
* Users can view counts of likes, retweets, and replies on tweets.
* Users can view lists of users who liked/retweeted a tweet.

### 5. Timeline / Feed System

* User sees a home timeline with tweets from users they follow.
* Timeline is either:

  * Reverse chronological OR
  * Ranked based on relevance/engagement (algorithmic feed)
* Timeline supports infinite scrolling / pagination.
* Timeline updates with new tweets in near real-time.
* Users can switch to Latest Tweets or Home view.
* Users can view individual tweet details and threads.
* Support filtering options:

  * Hide retweets
  * Show only tweets with media
  * Show only replies or original tweets

### 6. Notifications System

* Users receive notifications for:

  * New followers
  * Likes on their tweets
  * Retweets and quote retweets
  * Replies to their tweets
  * Mentions (@username) in tweets or replies
* Notifications are marked read/unread.
* Notifications support push, email, or in-app delivery.
* Users can manage notification preferences.

### 7. Search System

* Users can search tweets by:

  * Keywords / hashtags
  * Usernames or display names
  * Trending topics or hashtags
* Search results can be filtered by:

  * People
  * Latest tweets
  * Photos/videos
* Support autocomplete/suggestions as users type.
* Support trending topics display on homepage or search.

### 8. Direct Messaging (DM) \[Optional for MVP]

* Users can send private messages to one or multiple users.
* Users can view message history.
* Users can delete messages.
* Users can block message senders.

### 9. Media Handling

* Users can upload images, GIFs, and videos with tweets or DMs.
* System stores and serves media efficiently (CDN-backed).
* Support resizing, thumbnail generation, video transcoding.
* Enforce media upload limits (size, formats, duration).
* Users can view media in tweets inline or full-screen.

### 10. Account Settings & Privacy

* Users can toggle account privacy (public/private).
* Users can manage blocked and muted users.
* Users can manage email and push notification preferences.
* Users can export or download their data.
* Users can report tweets, users, or messages for abuse.

### 11. Moderation & Abuse Prevention

* System supports reporting of abusive content.
* System automatically detects spam or bot behavior (rate limiting).
* Admins or moderators can suspend or ban accounts.
* Content flagged for review is queued for manual inspection.

### 12. Analytics & Insights (Optional)

* Users can view tweet impressions, engagements.
* Track follower growth over time.
* Provide insights for power users and brands.

### 13. APIs (public/internal)

* Provide REST or GraphQL APIs for all above actions.
* Secure APIs with authentication (OAuth2, JWT).
* Rate limit APIs to prevent abuse.

### Sample API Endpoints Sketch

| Endpoint              | Method     | Description                  |
| --------------------- | ---------- | ---------------------------- |
| `/signup`             | POST       | Register new user            |
| `/login`              | POST       | User login                   |
| `/users/:id`          | GET/PUT    | Get/update user profile      |
| `/users/:id/follow`   | POST       | Follow a user                |
| `/users/:id/unfollow` | POST       | Unfollow a user              |
| `/tweets`             | POST       | Post a new tweet             |
| `/tweets/:id`         | GET/DELETE | Get/delete a tweet           |
| `/tweets/:id/like`    | POST       | Like/unlike a tweet          |
| `/tweets/:id/retweet` | POST       | Retweet or undo retweet      |
| `/tweets/:id/reply`   | POST       | Reply to a tweet             |
| `/timeline/home`      | GET        | Get user's home timeline     |
| `/notifications`      | GET        | Get user's notifications     |
| `/search`             | GET        | Search tweets/users/hashtags |
| `/messages`           | POST/GET   | Send and get DMs             |
| `/media/upload`       | POST       | Upload media                 |


## ✅ STEP 3: Define Non-Functional Requirements (NFRs)

### 1. **Scalability**

* **User Scale:** Must support **hundreds of millions of users**, with millions of concurrent active users.
* **Data Volume:** Handle **billions of tweets**, plus retweets, likes, and replies generated daily.
* **Traffic Patterns:** System must handle traffic spikes during major events (e.g., breaking news, sports).
* **Horizontal Scalability:** Services should scale horizontally to add capacity without downtime.
* **Partitioning:** Data (tweets, users, follows) should be partitioned/sharded effectively to avoid hotspots.
* **Caching:** Aggressive caching of hot data (timelines, tweets, user profiles) to reduce DB load.

### 2. **Availability**

* **SLA:** Target **99.99%+ uptime** (less than \~5 minutes downtime per month).
* **Fault Tolerance:** System components should be redundant, with failover and graceful degradation.
* **Data Replication:** Data replicated across multiple availability zones and data centers.
* **Graceful Degradation:** Timeline or notifications can degrade gracefully (e.g., partial timeline) during failures.

### 3. **Latency / Performance**

| Operation             | Target Latency (P95)        |
| --------------------- | --------------------------- |
| Tweet posting         | < 500 ms                    |
| Timeline loading      | < 200 ms                    |
| Like/retweet actions  | < 150 ms                    |
| Follow/unfollow       | < 100 ms                    |
| Notification delivery | < 1 second (near real-time) |

* **Real-Time Updates:** Near real-time updates on timeline and notifications (using push or WebSockets).
* **Batching & Async:** Use asynchronous processing for non-critical tasks (e.g., fan-out of tweets to followers).
* **Efficient Indexing:** Fast indexing for tweets, hashtags, and search.

### 4. **Consistency**

* **Strong Consistency:**

  * Authentication and authorization
  * Follow/unfollow state
  * Tweet creation and deletion
  * Privacy settings and access controls
* **Eventual Consistency:**

  * Timeline updates (some delay acceptable in feed fan-out)
  * Likes, retweets, and reply counts
  * Notifications delivery (may have slight lag)

### 5. **Durability**

* **No Data Loss:** Tweets, user data, follows, and engagement data must be reliably stored.
* **Backups:** Regular backups and disaster recovery plans.
* **Media Storage:** Media files stored durably in blob/object storage (S3 or equivalent) with replication.
* **Write-Ahead Logs:** Use WAL for databases to protect from crashes.

### 6. **Security**

* **Data in Transit and at Rest:** All data encrypted using TLS/SSL and encrypted storage.
* **Authentication:** Support OAuth2, JWT tokens, multi-factor authentication (MFA).
* **Password Storage:** Use strong hashing algorithms like bcrypt or Argon2.
* **API Security:** Rate limiting, throttling, and quota enforcement.
* **Input Validation:** Protect against XSS, CSRF, SQL injection, and other injection attacks.
* **Access Control:** Enforce role-based and ownership-based access permissions.
* **Audit Logs:** Maintain logs of critical actions for forensic analysis.
* **Abuse Detection:** Detect and throttle spammers, bots, and fake accounts.
* **Privacy Compliance:** GDPR, CCPA compliance, data deletion requests.

### 7. **Privacy**

* **Account Privacy Controls:** Allow users to set accounts private, control who can follow or see tweets.
* **Tweet Visibility:** Support public, followers-only, and protected tweet settings.
* **Data Retention & Deletion:** Users can delete tweets, account data; data removed from all views promptly.
* **Data Minimization:** Collect only necessary user data and secure it.
* **Consent & Transparency:** Clear privacy policies and user consent management.

### 8. **Maintainability & Modularity**

* **Microservices Architecture:** Design components as independent services to allow iterative deployment.
* **Loose Coupling:** Clear API contracts between services.
* **Code Quality:** Enforce coding standards, automated tests.
* **Extensibility:** Support adding new features (polls, spaces, fleets) without major rewrites.
* **Configuration Management:** Centralized configuration with feature flags for easy rollouts.

### 9. **Testability**

* **Unit Testing:** Each module must be unit tested.
* **Integration Testing:** Test interactions between components (e.g., tweet posting triggers timeline updates).
* **Load Testing:** Simulate high read/write loads to benchmark performance.
* **Chaos Testing:** Inject failures to ensure fault tolerance.
* **Security Testing:** Regular penetration testing and vulnerability scanning.
* **Canary Deployments:** Gradual rollout of new features to minimize risk.

### 10. **Observability**

* **Logging:** Structured, centralized logging (e.g., ELK stack).
* **Metrics:** Collect metrics on latency, throughput, errors, resource utilization (e.g., Prometheus + Grafana).
* **Tracing:** Distributed tracing for debugging across microservices (e.g., Jaeger, OpenTelemetry).
* **Alerting:** Automated alerts on SLA breaches, unusual activity, errors.
* **User Analytics:** Track engagement metrics and usage patterns.

### 11. **Cost Efficiency**

* **Resource Utilization:** Autoscale services up/down based on load.
* **Caching:** Use CDN for media delivery and cache hot timelines.
* **Storage Tiers:** Use cold storage for old tweets/media.
* **Multi-Region Deployment:** Balance cost and latency by selective regional replication.
* **Batch Processing:** Use batch jobs for analytics and heavy computation off-peak.


## ✅ STEP 4: Define System Interfaces / APIs

### General Guidelines

* **API Type:** RESTful APIs with JSON payloads (optionally GraphQL later)
* **Auth:** OAuth 2.0 / JWT Bearer tokens for secure access
* **Versioning:** Use versioning in URLs, e.g., `/api/v1/`
* **Rate limiting:** Per-user/IP limits and burst controls to prevent abuse
* **Pagination:** Cursor-based pagination for lists (timeline, tweets, followers)
* **Error codes:** Use standard HTTP status codes plus error messages in body
* **Idempotency:** POST actions that can be retried safely have idempotency keys

## 1. User & Authentication APIs

| Endpoint                         | Method | Request Body / Query Parameters                                | Response                                   | Description                    |
| -------------------------------- | ------ | -------------------------------------------------------------- | ------------------------------------------ | ------------------------------ |
| `/api/v1/signup`                 | POST   | `{ email, username, password, name }`                          | `{ userId, token, profile }`               | Register new user              |
| `/api/v1/login`                  | POST   | `{ email/username, password }`                                 | `{ token, user }`                          | Login, returns JWT token       |
| `/api/v1/logout`                 | POST   | (Auth token in header)                                         | `{ message: "Logged out" }`                | Logout user                    |
| `/api/v1/password-reset/request` | POST   | `{ email }`                                                    | `{ message: "Reset email sent" }`          | Request password reset email   |
| `/api/v1/password-reset/confirm` | POST   | `{ token, newPassword }`                                       | `{ message: "Password reset successful" }` | Confirm password reset         |
| `/api/v1/users/:id`              | GET    | (Auth token)                                                   | `{ userProfile }`                          | Get user profile               |
| `/api/v1/users/:id`              | PUT    | `{ name, bio, location, website, avatarUrl, privacySettings }` | `{ updatedProfile }`                       | Update user profile            |
| `/api/v1/users/:id/follow`       | POST   | (Auth token)                                                   | `{ message: "Followed user" }`             | Follow user                    |
| `/api/v1/users/:id/unfollow`     | POST   | (Auth token)                                                   | `{ message: "Unfollowed user" }`           | Unfollow user                  |
| `/api/v1/users/:id/followers`    | GET    | `?cursor=xxx&limit=20`                                         | `{ followers: [...], nextCursor }`         | Get user followers (paginated) |
| `/api/v1/users/:id/following`    | GET    | `?cursor=xxx&limit=20`                                         | `{ following: [...], nextCursor }`         | Get users this user follows    |
| `/api/v1/users/:id/block`        | POST   | (Auth token)                                                   | `{ message: "User blocked" }`              | Block user                     |
| `/api/v1/users/:id/unblock`      | POST   | (Auth token)                                                   | `{ message: "User unblocked" }`            | Unblock user                   |

## 2. Tweet APIs

| Endpoint                         | Method | Request Body / Query Parameters                            | Response                                  | Description                             |
| -------------------------------- | ------ | ---------------------------------------------------------- | ----------------------------------------- | --------------------------------------- |
| `/api/v1/tweets`                 | POST   | `{ text, mediaUrls[], poll?, replyToTweetId?, location? }` | `{ tweetId, createdAt, tweetData }`       | Create new tweet                        |
| `/api/v1/tweets/:id`             | GET    | (Auth token optional, depends on tweet visibility)         | `{ tweetData }`                           | Get tweet by ID                         |
| `/api/v1/tweets/:id`             | DELETE | (Auth token)                                               | `{ message: "Tweet deleted" }`            | Delete tweet (owner only)               |
| `/api/v1/tweets/:id/like`        | POST   | (Auth token)                                               | `{ message: "Tweet liked" }`              | Like or unlike a tweet (toggle)         |
| `/api/v1/tweets/:id/retweet`     | POST   | `{ comment? }`                                             | `{ message: "Retweeted", retweetId }`     | Retweet or quote retweet                |
| `/api/v1/tweets/:id/replies`     | GET    | `?cursor=xxx&limit=20`                                     | `{ replies: [...], nextCursor }`          | Get replies to a tweet (paginated)      |
| `/api/v1/tweets/:id/engagements` | GET    |                                                            | `{ likeCount, retweetCount, replyCount }` | Get engagement counts                   |
| `/api/v1/tweets/:id/likers`      | GET    | `?cursor=xxx&limit=20`                                     | `{ users: [...], nextCursor }`            | Get users who liked a tweet (paginated) |

## 3. Timeline / Feed APIs

| Endpoint                        | Method | Query Parameters                      | Response                        | Description                   |                                 |                                                                         |
| ------------------------------- | ------ | ------------------------------------- | ------------------------------- | ----------------------------- | ------------------------------- | ----------------------------------------------------------------------- |
| `/api/v1/timeline/home`         | GET    | \`?cursor=xxx\&limit=50\&filter=media | replies                         | retweets\`                    | `{ tweets: [...], nextCursor }` | Get home timeline (tweets from followed users, ranked or chronological) |
| `/api/v1/timeline/user/:userId` | GET    | `?cursor=xxx&limit=50`                | `{ tweets: [...], nextCursor }` | Get tweets by a specific user |                                 |                                                                         |

## 4. Notification APIs

| Endpoint                         | Method | Query Parameters       | Response                                     | Description                          |
| -------------------------------- | ------ | ---------------------- | -------------------------------------------- | ------------------------------------ |
| `/api/v1/notifications`          | GET    | `?cursor=xxx&limit=50` | `{ notifications: [...], nextCursor }`       | Get notifications for logged-in user |
| `/api/v1/notifications/:id/read` | POST   |                        | `{ message: "Notification marked as read" }` | Mark notification as read            |

## 5. Search APIs

| Endpoint         | Method | Query Parameters          | Response | Description                      |                                  |                                   |
| ---------------- | ------ | ------------------------- | -------- | -------------------------------- | -------------------------------- | --------------------------------- |
| `/api/v1/search` | GET    | \`?q=keyword\&type=tweets | users    | hashtags\&limit=20\&cursor=xxx\` | `{ results: [...], nextCursor }` | Search tweets, users, or hashtags |

## 6. Direct Message APIs (Optional MVP)

| Endpoint               | Method | Request Body / Query Parameters           | Response                          | Description      |
| ---------------------- | ------ | ----------------------------------------- | --------------------------------- | ---------------- |
| `/api/v1/messages`     | POST   | `{ recipientId, messageText, mediaUrl? }` | `{ messageId, timestamp }`        | Send a DM        |
| `/api/v1/messages`     | GET    | `?cursor=xxx&limit=50&chatWithUserId=xxx` | `{ messages: [...], nextCursor }` | Fetch DM history |
| `/api/v1/messages/:id` | DELETE |                                           | `{ message: "Message deleted" }`  | Delete a message |

## 7. Media APIs

| Endpoint               | Method | Request Body / Query Parameters           | Response                          | Description                       |
| ---------------------- | ------ | ----------------------------------------- | --------------------------------- | --------------------------------- |
| `/api/v1/media/upload` | POST   | Multipart form data: image/video/gif file | `{ mediaUrl, mediaId, metadata }` | Upload media (used in tweets/DMs) |

## 8. Account Settings & Privacy APIs

| Endpoint                  | Method | Request Body / Query Parameters                                  | Response              | Description                                 |
| ------------------------- | ------ | ---------------------------------------------------------------- | --------------------- | ------------------------------------------- |
| `/api/v1/account/privacy` | GET    |                                                                  | `{ privacySettings }` | Get user privacy settings                   |
| `/api/v1/account/privacy` | PUT    | `{ isPrivate, mutedUsers[], blockedUsers[], notificationPrefs }` | `{ updatedSettings }` | Update privacy and notification preferences |

## API Error Handling Examples

| HTTP Status | Meaning                        | Response Body Example                             |
| ----------- | ------------------------------ | ------------------------------------------------- |
| 200         | Success                        | `{ "status": "ok", "data": {...} }`               |
| 400         | Bad Request (validation)       | `{ "error": "Invalid tweet content" }`            |
| 401         | Unauthorized (no token)        | `{ "error": "Authentication required" }`          |
| 403         | Forbidden (access denied)      | `{ "error": "Not allowed to delete this tweet" }` |
| 404         | Not Found                      | `{ "error": "Tweet not found" }`                  |
| 429         | Too Many Requests (rate limit) | `{ "error": "Rate limit exceeded" }`              |
| 500         | Server error                   | `{ "error": "Internal server error" }`            |


## ✅ STEP 5: High-Level Architecture

### Key Goals of Architecture

* **Scalability:** Handle millions of users and high throughput of tweets, likes, and timeline reads
* **Availability:** Redundant services, fault tolerance, zero downtime deployment
* **Performance:** Low-latency timeline loading, fast tweet posting
* **Modularity:** Microservices design for independent feature scaling and deployments
* **Consistency:** Strong consistency for critical data; eventual consistency for timelines and likes

### 1. Major Components Overview

| Component                             | Responsibility                                                              |
| ------------------------------------- | --------------------------------------------------------------------------- |
| **Client Apps**                       | Web, iOS, Android apps, third-party clients consuming APIs                  |
| **API Gateway**                       | Entry point for all client requests, handles auth, routing, rate limiting   |
| **User Service**                      | Manages user profiles, authentication, privacy settings                     |
| **Follow Service**                    | Manages follow/unfollow relationships, blocks, mutes                        |
| **Tweet Service**                     | Create, read, update, delete tweets, including media metadata               |
| **Timeline Service**                  | Generates and serves user timelines (feeds), supports fan-out/fan-in models |
| **Engagement Service**                | Handles likes, retweets, replies, counts, notifications                     |
| **Notification Service**              | Delivers notifications (push, email, in-app)                                |
| **Search Service**                    | Indexes tweets, users, hashtags for search queries                          |
| **Media Service**                     | Stores, processes, and serves images, videos, GIFs                          |
| **Direct Message Service** (optional) | Manages private messaging                                                   |
| **Admin & Moderation Tools**          | Content reporting, abuse detection, user banning                            |
| **Analytics Service**                 | Tracks metrics and user behavior for insights                               |
| **Caching Layer**                     | Redis or Memcached clusters for hot data (timelines, tweets)                |
| **Database Layer**                    | Multiple databases for user data, tweets, relationships, engagements        |
| **CDN**                               | Content delivery network for media and static content                       |
| **Message Queue**                     | Kafka, RabbitMQ for asynchronous processing (fan-out, notifications)        |
| **Monitoring & Logging**              | Observability infrastructure for metrics, tracing, alerts                   |

### 2. High-Level Architecture Diagram (Conceptual)

```
  +--------------------+
  |   Client Apps      | <-- iOS, Android, Web, 3rd party
  +--------------------+
            |
            v
  +--------------------+
  |    API Gateway     | -- Auth, Routing, Rate Limiting
  +--------------------+
     |       |       |       \
     v       v       v        v
+-------+ +-------+ +--------+ +---------+
| User  | |Tweet  | |Follow  | |Timeline |   <-- Microservices
|Service| |Service| |Service | |Service  |
+-------+ +-------+ +--------+ +---------+
     |        |         |          |
     |        |         |          v
     |        |         |   +-------------+
     |        |         |   | Cache (Redis)|
     |        |         |   +-------------+
     |        |         |          |
     |        |         |          v
     |        |         |   +-------------+
     |        |         |   | Databases    | -- Users DB, Tweets DB, Follows DB
     |        |         |   +-------------+
     |        |         |
     |        |         +----------------+
     |        |                          |
     |        |                          v
     |        |                  +---------------+
     |        |                  | Message Queue | <-- Kafka/RabbitMQ
     |        |                  +---------------+
     |        |                          |
     |        |                          v
     |        |                 +--------------------+
     |        |                 | Notification Service|
     |        |                 +--------------------+
     |        |
     |        +----------------------------------+
     |                                       |
     v                                       v
+--------------+                      +----------------+
| Media Service|                      | Search Service |
+--------------+                      +----------------+

```

### 3. Data Stores and Technologies (Example Choices)

| Service              | Data Store                                    | Notes                                      |
| -------------------- | --------------------------------------------- | ------------------------------------------ |
| User Service         | Relational DB (Postgres)                      | Strong consistency, complex queries        |
| Tweet Service        | Distributed NoSQL (Cassandra, DynamoDB)       | High write throughput, time-series data    |
| Follow Service       | Graph DB (Neo4j, RedisGraph) or relational    | Efficient follower/following queries       |
| Timeline Service     | Cache-heavy (Redis), also reads from Tweet DB | Precompute timelines or fan-out on read    |
| Engagement Service   | NoSQL or key-value store                      | For likes, retweets counts                 |
| Notification Service | NoSQL or Queue System                         | For event-driven notifications             |
| Media Service        | Object Storage (S3, GCS)                      | Scalable media storage and CDN integration |
| Search Service       | Elasticsearch                                 | Full-text search, hashtag, user search     |
| Message Queue        | Kafka, RabbitMQ                               | Asynchronous processing and decoupling     |

### 4. Communication Patterns

* **Synchronous API calls**: Client <-> API Gateway <-> Services (User, Tweet, Follow, Timeline)
* **Asynchronous processing**: Services publish events (new tweet, new follow) to message queue → consumed by Timeline, Notification services
* **Cache updates:** Timeline and tweet caches updated asynchronously on events
* **Search indexing:** Search service consumes tweet/user events to update indices

### 5. Fan-out Strategies for Timeline Generation

* **Fan-out on write:** When user posts a tweet, system pushes tweet IDs to followers’ timeline feeds (Redis, cache, or DB).

  * Pros: Fast timeline reads
  * Cons: High write amplification for celebrities with millions of followers
* **Fan-out on read:** Timelines assembled at read time by querying recent tweets of followed users.

  * Pros: Less write amplification
  * Cons: Higher latency on timeline reads, complex caching needed
* **Hybrid approach:** Fan-out on write for most users, fan-out on read for celebrities.

### 6. Additional Considerations

* **API Gateway** for authentication, SSL termination, rate limiting
* **Load Balancers** in front of all service clusters
* **CDN** to serve static and media content efficiently worldwide
* **Auto-scaling groups** for microservice containers or VMs
* **Monitoring & Alerting** using Prometheus, Grafana, ELK stack
* **Distributed Tracing** (Jaeger) for debugging
* **Security Layers** at API Gateway and individual services (auth, permissions)


## ✅ STEP 6: Database Design & Schema (ERD)

### Key Design Considerations

* Use relational DB (Postgres/MySQL) for structured data with strong consistency: Users, Followers, Privacy, Auth.
* Use distributed NoSQL (e.g., Cassandra, DynamoDB) for high-write, time-series data: Tweets, Engagements, Timeline cache.
* Media stored separately in object storage (S3), referenced by URLs.
* Use indexes for fast lookups (usernames, tweet IDs, timestamps).
* Schema optimized for read-heavy use cases, especially timeline queries.

## Core Entities and Relations

### 1. **User**

| Field          | Type          | Notes                      |
| -------------- | ------------- | -------------------------- |
| user\_id (PK)  | UUID / bigint | Primary key                |
| username       | varchar(15)   | Unique, indexed            |
| email          | varchar       | Unique                     |
| password\_hash | varchar       | Secure hashed password     |
| display\_name  | varchar(50)   | User’s full name           |
| bio            | text          | Nullable                   |
| location       | varchar       | Nullable                   |
| website\_url   | varchar       | Nullable                   |
| avatar\_url    | varchar       | Nullable                   |
| is\_private    | boolean       | Account privacy setting    |
| created\_at    | timestamp     | Account creation timestamp |
| updated\_at    | timestamp     | Profile last update        |
| deleted\_at    | timestamp     | Soft delete                |

### 2. **Followers / Followings**

| Field             | Type          | Notes                |
| ----------------- | ------------- | -------------------- |
| follower\_id (PK) | UUID / bigint | User who follows     |
| followed\_id (PK) | UUID / bigint | User who is followed |
| is\_approved      | boolean       | For private accounts |
| created\_at       | timestamp     | When follow created  |

*Composite primary key: (follower\_id, followed\_id)*

### 3. **Tweets**

| Field              | Type          | Notes                               |
| ------------------ | ------------- | ----------------------------------- |
| tweet\_id (PK)     | UUID / bigint | Primary key                         |
| user\_id (FK)      | UUID / bigint | Author of tweet                     |
| text               | varchar(280)  | Tweet content                       |
| created\_at        | timestamp     | Timestamp                           |
| in\_reply\_to\_id  | UUID / bigint | Nullable, if reply to another tweet |
| is\_deleted        | boolean       | Soft delete                         |
| sensitive\_content | boolean       | Flag for content warning            |
| language           | varchar(10)   | Language code                       |
| visibility         | enum          | 'public', 'followers', 'private'    |

### 4. **Tweet Media**

| Field          | Type          | Notes                          |
| -------------- | ------------- | ------------------------------ |
| media\_id (PK) | UUID / bigint | Primary key                    |
| tweet\_id (FK) | UUID / bigint | Associated tweet               |
| media\_url     | varchar       | URL to media in object storage |
| media\_type    | enum          | 'image', 'video', 'gif'        |
| order          | int           | Display order                  |

### 5. **Likes**

| Field          | Type          | Notes          |
| -------------- | ------------- | -------------- |
| tweet\_id (PK) | UUID / bigint | Tweet liked    |
| user\_id (PK)  | UUID / bigint | User who liked |
| created\_at    | timestamp     | When liked     |

### 6. **Retweets**

| Field               | Type          | Notes                          |
| ------------------- | ------------- | ------------------------------ |
| retweet\_id (PK)    | UUID / bigint | Primary key                    |
| original\_tweet\_id | UUID / bigint | Tweet being retweeted          |
| user\_id            | UUID / bigint | Who retweeted                  |
| comment             | varchar(280)  | Optional quote retweet comment |
| created\_at         | timestamp     | When retweeted                 |

### 7. **Replies**

Replies are stored as tweets with `in_reply_to_id` linking to parent tweet. For fast lookup:

| Field            | Type          | Notes        |
| ---------------- | ------------- | ------------ |
| reply\_id (PK)   | UUID / bigint | Primary key  |
| tweet\_id (FK)   | UUID / bigint | Parent tweet |
| reply\_tweet\_id | UUID / bigint | Reply tweet  |

### 8. **Notifications**

| Field                 | Type          | Notes                                           |
| --------------------- | ------------- | ----------------------------------------------- |
| notification\_id (PK) | UUID / bigint | Primary key                                     |
| user\_id (FK)         | UUID / bigint | User to notify                                  |
| type                  | enum          | 'follow', 'like', 'retweet', 'reply', 'mention' |
| source\_user\_id      | UUID / bigint | User who triggered notification                 |
| tweet\_id (nullable)  | UUID / bigint | Related tweet if applicable                     |
| created\_at           | timestamp     | When notification created                       |
| is\_read              | boolean       | Read/unread flag                                |

### 9. **Blocks / Mutes**

| Field                  | Type          | Notes                      |
| ---------------------- | ------------- | -------------------------- |
| user\_id (PK)          | UUID / bigint | User performing block/mute |
| blocked\_user\_id (PK) | UUID / bigint | User being blocked/muted   |
| is\_block              | boolean       | true=block, false=mute     |
| created\_at            | timestamp     | When action occurred       |

### 10. **Direct Messages (Optional)**

| Field              | Type          | Notes              |
| ------------------ | ------------- | ------------------ |
| message\_id (PK)   | UUID / bigint | Primary key        |
| sender\_id (FK)    | UUID / bigint | User sending       |
| recipient\_id (FK) | UUID / bigint | User receiving     |
| text               | text          | Message content    |
| media\_url         | varchar       | Optional media URL |
| created\_at        | timestamp     | Timestamp          |
| is\_deleted        | boolean       | Soft delete        |

## ERD Diagram (Simplified)

```
User ---< Followers >--- User
  |
  |---< Tweet >---< TweetMedia
  |            \
  |             ---< Like >--- User
  |             ---< Retweet >--- User
  |             ---< Reply >--- Tweet (self-join)
  |
  |---< Notification >--- User (source_user_id FK)
  |
  |---< BlockMute >--- User (blocked_user_id FK)
  |
  |---< DirectMessage >--- User (sender & recipient)
```

## Indexes & Keys

* Index on `User.username` for fast lookup.
* Composite PK on `Followers(follower_id, followed_id)`.
* Index `Tweet.created_at` for timelines.
* Index on `Likes(tweet_id, user_id)`.
* Index on `Retweets(original_tweet_id)`.
* Full-text index on `Tweet.text` for search (or handled by Search Service).
* Partition Tweets by creation date or user\_id for scaling.


## ✅ STEP 8: Scaling & Optimization

### Goals for Scaling & Optimization

* Support **billions of users** and **millions of requests per second**
* Handle **burst traffic spikes** (e.g., viral tweets, major events)
* Maintain **low latency** under heavy load
* Optimize **storage** and **network bandwidth**
* Ensure **cost-effective** use of resources
* Provide **elastic scalability** for growth

### 1. Scaling Strategies Overview

| Aspect          | Strategy                                       |
| --------------- | ---------------------------------------------- |
| Compute         | Horizontal scaling via stateless microservices |
| Data Storage    | Partitioning (sharding), replication, caching  |
| Network         | Load balancing, CDNs for media                 |
| Messaging       | Distributed message queues (Kafka)             |
| Caching         | Multi-layered caching (Redis, CDN)             |
| Data Processing | Asynchronous and batch processing              |

### 2. Compute & Microservices Scaling

* **Stateless Services:**
  All core services (Tweet, User, Timeline, etc.) should be stateless, enabling easy horizontal scaling by adding/removing instances behind load balancers.

* **Auto-scaling:**
  Use cloud autoscaling groups (AWS ECS, Kubernetes HPA) to adjust service instances based on CPU, memory, or custom metrics like request latency.

* **Service Mesh:**
  Use service mesh (e.g., Istio) for efficient service discovery, routing, and fault injection.

### 3. Database Scaling

* **Sharding / Partitioning:**

  * **Users & Followers DB:** shard by user ID ranges or hash for even distribution.
  * **Tweets DB:** time-based or user-based partitioning (wide rows in Cassandra).
  * **Engagement Data:** partition by tweet ID or user ID.

* **Replication:**

  * Use leader-follower replication for availability and read scaling.
  * Multi-region replication for disaster recovery and geo locality.

* **Multi-model Storage:**

  * Use specialized DBs for different data: graph DB for followers, wide-column store for tweets, relational for users.

* **CQRS (Command Query Responsibility Segregation):**
  Separate write and read models for high throughput — writes go to main DB; reads served from optimized replicas or caches.

### 4. Caching Optimization

* **Multi-layer Caching:**

  * **In-memory caches (Redis/Memcached):** for hot data like timelines, user profiles, and tweet metadata.
  * **CDN (Content Delivery Network):** for static and media assets (images, videos, profile pictures).
  * **Browser caching:** leverage HTTP cache headers for static content.

* **Cache Invalidation:**

  * Use event-driven invalidation when tweets update/delete or engagement counts change.
  * Use TTLs (time-to-live) for eventual consistency.

* **Cache Aside Pattern:**

  * Services check cache first; if miss, query DB and update cache.

### 5. Fan-out Optimization for Timelines

* **Fan-out on Write:**

  * Push tweet IDs to followers’ timelines asynchronously via message queues.
  * Efficient for users with small to medium follower counts.

* **Fan-out on Read:**

  * For celebrities or users with millions of followers, assemble timelines dynamically by querying recent tweets from followed users to avoid massive fan-out writes.

* **Hybrid Approach:**

  * Fan-out on write for most users, fan-out on read for high-fanout users.

* **Partial Caching:**

  * Cache top N tweets or recent tweets only, fill rest on demand.

### 6. Load Balancing & Traffic Routing

* **Global Load Balancers:**
  Route user requests to nearest regional data center to minimize latency.

* **Service-level Load Balancers:**
  Distribute requests evenly across microservice instances.

* **API Rate Limiting:**
  Prevent abuse and protect services from overload.

### 7. Asynchronous Processing & Queues

* **Message Queues (Kafka/RabbitMQ):**

  * Decouple services for high throughput and resilience.
  * Used for fan-out, notifications, search indexing, analytics.

* **Batch Processing:**

  * Use Spark, Flink, or Hadoop for offline data aggregation, analytics, and ML model training.

### 8. Data Compression & Storage Optimization

* **Compression:**

  * Store tweets, logs, and analytics data compressed to reduce storage costs.

* **Archiving:**

  * Move old tweets, logs, and metrics to cold storage (S3 Glacier).

* **Media Storage:**

  * Optimize media file sizes, transcoding videos to multiple bitrates.

### 9. Network Optimization

* **CDN Usage:**

  * Use CDN aggressively for media and static content to reduce origin server load and latency.

* **Connection Reuse:**

  * Keep-alive connections between microservices.

* **Protocol Optimization:**

  * Use HTTP/2 or gRPC for internal service communication.

### 10. Monitoring & Autoscaling Feedback Loop

* Set up fine-grained monitoring (latency, error rates, CPU/memory) to trigger autoscaling or throttling.

### 11. Cost Optimization

* **Spot Instances / Preemptible VMs:**

  * Use for batch jobs and non-critical workloads.

* **Right-sizing Resources:**

  * Continuous analysis to adjust instance sizes and counts.

* **Efficient Storage Tiers:**

  * Use hot storage for recent tweets; cold for archival.

Got it! Let’s deep dive into **STEP 9: Security & Privacy Considerations** for Twitter. This is crucial to protect user data, maintain trust, and comply with legal requirements.


## ✅ STEP 9: Security & Privacy Considerations

### 1. Authentication & Authorization

* **Secure Authentication**

  * Use industry-standard protocols: OAuth 2.0, OpenID Connect for user login and token issuance.
  * Support multi-factor authentication (MFA) for sensitive accounts.
  * Password storage with strong hashing algorithms (bcrypt, Argon2).
  * Token management with short-lived JWTs and refresh tokens.

* **Authorization & Access Control**

  * Implement Role-Based Access Control (RBAC) for internal users/admins.
  * Enforce per-user and per-resource permissions (e.g., who can view/edit a tweet).
  * Ownership checks on all modifying API calls.

### 2. Data Protection

* **Encryption**

  * Encrypt data at rest using AES-256 or equivalent in databases and storage.
  * Use TLS (HTTPS) for all data in transit (client-server and inter-service).

* **Data Minimization & Retention**

  * Store only necessary user data; avoid unnecessary personal info.
  * Define clear data retention policies; delete data on user request (GDPR Right to Erasure).
  * Anonymize or pseudonymize data where possible for analytics.

### 3. Privacy Controls & User Settings

* **Content Visibility**

  * Allow users to set tweet visibility: public, followers-only, private.
  * Enforce privacy settings strictly at read and write layers.

* **Follow / Block / Mute Management**

  * Blocked users can’t see or interact with blocker’s content.
  * Muted users’ tweets hidden from timelines without unfollowing.

* **User Consent**

  * Explicit consent for collecting sensitive info, cookies, targeted ads.

### 4. Abuse Prevention & Rate Limiting

* **Rate Limiting**

  * Protect APIs against brute force, spamming, scraping.
  * Different limits for unauthenticated vs authenticated users.

* **Spam & Abuse Detection**

  * Use machine learning to detect spam accounts, bot-like behavior, fake likes, and retweets.
  * Automatic and manual content moderation workflows.

* **Reporting & Enforcement**

  * Allow users to report abusive content/accounts.
  * Suspend or ban abusive users promptly.

### 5. API Security

* **Input Validation & Sanitization**

  * Prevent SQL injection, XSS, CSRF attacks by sanitizing all inputs.
  * Use prepared statements/ORMs for DB queries.

* **API Throttling & Quotas**

  * Limit API usage per user/IP to prevent abuse.

* **Secure Headers**

  * Set HTTP headers like Content-Security-Policy, X-Content-Type-Options, X-Frame-Options.

### 6. Infrastructure & Network Security

* **Network Segmentation**

  * Separate internal service network from public endpoints.

* **Firewalls & WAF**

  * Web Application Firewall to filter malicious traffic.

* **Secrets Management**

  * Store API keys, tokens, credentials securely using vaults (HashiCorp Vault, AWS Secrets Manager).

* **DDoS Protection**

  * Use cloud provider’s DDoS mitigation (AWS Shield, Cloudflare).

### 7. Logging & Monitoring for Security

* **Audit Logs**

  * Track user activities related to sensitive operations (login, password change, tweet deletion).
  * Immutable logs with tamper-evidence.

* **Security Incident Detection**

  * Monitor for unusual patterns (failed logins, rapid posting).
  * Integrate with SIEM tools for alerting and response.

### 8. Compliance & Legal

* **GDPR, CCPA Compliance**

  * Data access and portability features for users.
  * Privacy policy disclosures and cookie management.

* **Data Residency**

  * Store data according to regional regulations (e.g., EU users’ data in EU data centers).

### 9. Backup & Disaster Recovery

* **Regular Backups**

  * Encrypt backups and test restore procedures.

* **Incident Response Plan**

  * Prepare for data breaches, leaks, or compromise.
  * Communication protocols for notifying users and regulators.


## ✅ STEP 10: Monitoring, Logging & Alerting

### 1. Objectives

* **Real-time visibility** into system health and performance
* **Early detection** of anomalies, failures, and security incidents
* **Detailed diagnostics** to troubleshoot issues quickly
* **Capacity planning** and optimization insights
* **Compliance and audit trails**

### 2. Monitoring

**Types of Metrics:**

* **Infrastructure Metrics:** CPU, memory, disk I/O, network traffic on servers, containers, databases.
* **Application Metrics:** Request rates, latency (P50, P95, P99), error rates, queue depths, cache hit ratios.
* **Business Metrics:** Number of tweets created, timeline loads, user signups, active users.
* **Security Metrics:** Failed logins, rate limit breaches, suspicious IP activity.

**Tools:**

* **Prometheus:** Time-series metrics collection
* **Grafana:** Visual dashboards and alerting
* **Cloud-native options:** AWS CloudWatch, Google Stackdriver

**Best Practices:**

* Define **SLIs (Service Level Indicators)** like error rate < 0.1%, latency < 200ms.
* Set **SLOs (Service Level Objectives)** to track performance goals.
* Use **tags/labels** for dimensional metrics (service, region, instance).

### 3. Logging

**Types of Logs:**

* **Access Logs:** HTTP requests and responses with status codes and latencies.
* **Application Logs:** Info, warning, error logs from microservices with context (request ID, user ID).
* **Audit Logs:** Security-relevant actions (logins, permission changes, data access).
* **System Logs:** OS-level logs, container runtime logs.

**Logging Infrastructure:**

* Centralized log aggregation using tools like **ELK Stack (Elasticsearch, Logstash, Kibana)**, **Fluentd**, or cloud solutions (AWS Elasticsearch, Datadog).
* Structured logging (JSON format) to enable powerful querying and filtering.
* Correlation IDs for tracing request flow across microservices.

### 4. Distributed Tracing

* Trace requests end-to-end across services to identify bottlenecks or failures.
* Tools: **Jaeger**, **Zipkin**, **OpenTelemetry** instrumentation.
* Capture spans for DB queries, RPC calls, cache accesses.

### 5. Alerting

* Define **threshold-based alerts** (e.g., CPU > 80%, error rate > 5%) and anomaly detection alerts (sudden spikes).
* Use alerting platforms like **PagerDuty**, **Opsgenie**, or integrated Grafana alerts.
* Alert routing to the right teams (on-call engineers, SREs, security).
* Use **escalation policies** and **runbooks** for consistent incident response.

### 6. Incident Management & Postmortems

* Tools for tracking incidents and coordinating response (Jira, Statuspage).
* Postmortems to document causes, impacts, fixes, and preventive actions.

### 7. Security Monitoring

* Monitor for brute force attempts, suspicious API usage patterns.
* Integrate with SIEM (Security Information and Event Management) systems for correlation and advanced analytics.

### 8. Capacity Planning & Forecasting

* Use historical metrics to predict scaling needs.
* Automate scale-up/down based on observed trends.


## ✅ STEP 11: Cost & Infrastructure Planning

### 1. Infrastructure Components to Budget For

| Component            | Description                           | Cost Factors                               |
| -------------------- | ------------------------------------- | ------------------------------------------ |
| Compute Resources    | Microservice servers, API gateways    | Number of instances, CPU, memory, uptime   |
| Database Storage     | Relational DB, NoSQL DB, backups      | Storage volume, IOPS, replication          |
| Caching Layer        | Redis/Memcached clusters              | Memory usage, cluster size                 |
| Messaging Queues     | Kafka or RabbitMQ                     | Throughput, partitions, retention duration |
| CDN & Media Storage  | Serving images, videos, static assets | Data transfer, storage volume              |
| Network              | Load balancers, bandwidth costs       | Data egress, regional routing              |
| Monitoring & Logging | Metrics storage, log aggregation      | Volume of data ingested and stored         |
| Security Services    | WAF, DDoS protection                  | Protection tier, traffic volume            |

### 2. Cost Optimization Strategies

* **Right-sizing compute instances:** Match instance sizes/types to workload (CPU, memory, burst capacity). Use autoscaling to reduce idle resources.
* **Spot/Preemptible instances:** Use for batch jobs, analytics, or fault-tolerant workloads to cut costs significantly.
* **Data lifecycle policies:** Archive old data (tweets, logs) to cheaper cold storage (AWS Glacier).
* **Multi-region replication trade-offs:** Replicate critical data but limit less critical replication to save costs.
* **Use serverless components:** For occasional workloads like password resets, notifications, or media processing where applicable.
* **Cache aggressively:** Minimize costly DB reads by maximizing cache hit rates.
* **Optimize media storage:** Compress images/videos; choose CDN providers with competitive pricing.

### 3. Cost Estimation Example (Very Rough)

| Resource             | Unit Cost Example     | Estimated Usage            | Monthly Cost Estimate |
| -------------------- | --------------------- | -------------------------- | --------------------- |
| EC2 Instances        | \$0.10/hr (t3.medium) | 50 instances \* 24\*30 hrs | \~\$3600              |
| Database Storage     | \$0.10/GB-month (SSD) | 10 TB                      | \~\$1000              |
| Redis Cache          | \$0.20/GB-month       | 1 TB                       | \~\$200               |
| Kafka Cluster        | \$0.15/hr per broker  | 5 brokers                  | \~\$540               |
| CDN (Data Transfer)  | \$0.08 per GB         | 50 TB                      | \~\$4000              |
| Logging Storage      | \$0.03 per GB         | 10 TB                      | \~\$300               |
| Network Egress       | \$0.05 per GB         | 20 TB                      | \~\$1000              |
| Security (WAF, DDoS) | Fixed + usage-based   | Depends                    | \$500+                |

### 4. Infrastructure Planning

* **Cloud Provider Choice:** AWS, GCP, Azure — balance cost, features, and regional availability.
* **Region Selection:** Locate data centers near largest user bases for latency and regulatory compliance.
* **High Availability Setup:** Multi-AZ or multi-region for redundancy, factoring in cost.
* **Disaster Recovery:** Backup frequency and restore SLAs impact storage and compute.
* **CI/CD Pipeline:** Automate deployments to minimize operational overhead.

### 5. Budgeting for Growth

* Build a **scalable cost model** tied to user growth and activity metrics.
* Monitor **cost per active user** and optimize components with high cost-to-benefit ratio.
* Plan for **burst capacity** during major events without overprovisioning all the time.

### 6. Cost Monitoring & Alerting

* Use cloud provider cost monitoring tools (AWS Cost Explorer, GCP Billing) with budgets and alerts.
* Analyze monthly bills by service and optimize bottlenecks.
* Enable cost anomaly detection to catch unexpected spikes early.


## ✅ STEP 12: Testing & Deployment Strategies

### 1. Testing Strategies

#### a) Unit Testing

* Test individual functions, modules in isolation (e.g., Tweet creation logic, user authentication).
* Use mocks/stubs for dependencies (DB, external APIs).
* High coverage on critical modules.

#### b) Integration Testing

* Test interactions between components (e.g., User Service + Tweet Service).
* Validate API contracts and data flow.
* Use real or sandbox databases.

#### c) End-to-End (E2E) Testing

* Simulate real user scenarios (sign up, tweet, follow, timeline load).
* Use tools like Selenium, Cypress, or Playwright.
* Run in staging environment similar to production.

#### d) Load and Performance Testing

* Simulate thousands to millions of concurrent users.
* Identify bottlenecks and max capacity.
* Use tools like JMeter, Locust, Gatling.

#### e) Security Testing

* Penetration testing for vulnerabilities.
* Static code analysis for security flaws.
* Fuzz testing inputs.

#### f) Regression Testing

* Automated suites to catch unintended side effects after code changes.
* Run tests on every commit (CI pipeline).

### 2. Deployment Strategies

#### a) Continuous Integration / Continuous Deployment (CI/CD)

* Automated pipelines to build, test, and deploy code.
* Integrate testing phases into the pipeline.
* Tools: Jenkins, GitHub Actions, GitLab CI, CircleCI.

#### b) Canary Releases

* Deploy new version to a small subset of users.
* Monitor errors and performance before full rollout.
* Roll back quickly if issues detected.

#### c) Blue-Green Deployments

* Maintain two identical production environments (blue & green).
* Route traffic to new version once verified.
* Fast rollback by switching traffic back.

#### d) Rolling Updates

* Gradually update instances in the cluster without downtime.
* Monitor health checks during rollout.

### 3. Infrastructure as Code (IaC)

* Define infrastructure and deployment environments in code (Terraform, CloudFormation).
* Version-controlled infrastructure to ensure consistency.

### 4. Feature Flags & Dark Launches

* Enable/disable features at runtime without deployment.
* Test features with internal users before public launch.

### 5. Monitoring Post-Deployment

* Use monitoring tools to detect regressions or errors immediately after deploy.
* Automated rollback triggers if error rates spike.

### 6. Backup & Rollback Plans

* Automated backups before deploy.
* Clear rollback procedures documented and rehearsed.
