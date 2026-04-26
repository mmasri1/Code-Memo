# Designing Facebook

## ✅ STEP 1: CLARIFY THE PROBLEM

Facebook is a **social network** that includes many features.

#### Core Modules:
* User sign up/login
* Friendships
* Creating posts (text + image)
* Liking and commenting
* Feed
* Notifications
* Search

### Who Are the Users?

* Global audience: 3 billion users (1 billion daily active users). On average, each user reads 10 posts per day but only posts once per week — a 70:1 read-to-post ratio, so the platform is read-heavy.
* Device variety: phones, desktops, tablets, low-bandwidth devices.

### Product Goals

> What does the business care about?

* High user engagement
* Fast response times (low-latency feed)
* Personalization and relevance
* Trust (privacy, safety, abuse detection)
* Reliability (no post loss, feed always loads)

### Constraints and Priorities

| Constraint / Priority  | Notes                                                                |
| ---------------------- | -------------------------------------------------------------------- |
| Latency                | Sub-200ms for most UI interactions (especially feed loading)         |
| Scalability            | Billions of users, posts, likes — horizontally scalable architecture |
| Consistency            | Relaxed for feed, stronger for friends or user settings              |
| Availability           | 99.99%+ SLA                                                          |
| Privacy & Security     | Users control post visibility, robust auth and permissions           |
| Write frequency        | Lower than reads (more people consume than post)                     |
| Read frequency         | Very high — especially for feed, likes, comments                     |

### Key Use Cases

1. User creates account
2. User logs in
3. User sends/accepts friend requests
4. User makes a post (text/image)
5. User likes/comments on a post
6. User sees a ranked feed of friend posts
7. User receives notifications on interactions

### High-Level Metrics to Support

| Metric                    | Notes                                                 |
| ------------------------- | ----------------------------------------------------- |
| Requests per second (RPS) | Feed reads could be 10–100× post writes               |
| Feed latency              | Target <200ms P95                                     |
| Storage growth            | TBs to PBs daily                                      |
| Cache hit ratio           | >90% for hot user/feed data                           |
| System uptime             | 99.99% or better                                      |
| Eventual consistency lag  | Acceptable within seconds for feed and likes/comments |

### Personas

* **Heavy user**: posts, likes, comments, high feed expectations
* **Passive user**: mostly reads, never posts
* **New user**: no friends yet, cold-start feed challenge
* **Celebrities**: millions of followers, huge fan-out
* **Spammer**: system needs to rate-limit and detect abuse

## ✅ STEP 2: Define Functional Requirements

> Functional requirements define **what** the system should do — features and behaviors that are visible to users and that drive the architecture.

### Detailed Functional Requirements (User Stories)

#### User & Auth

* A user can register with an email, password, and name.
* A user can log in and log out securely.
* A user can reset their password.
* A user can update their profile (name, avatar, bio).

#### Friend System

* A user can send a friend request to another user.
* A user can accept or reject a friend request.
* A user can view their list of friends.
* A user can unfriend another user.

#### Post System

* A user can create a new post with text (optionally image).
* A user can delete their own post.
* A user can view their own posts.
* A user can view a friend's posts (if accepted).

#### Like System

* A user can like or unlike a post.
* A user can view how many likes a post has.

#### Comment System

* A user can add a comment on a post.
* A user can delete their own comment.
* A user can view comments on a post.

#### News Feed

* A user sees a feed of recent and relevant posts from their friends.
* The feed is paginated or scrollable.
* The feed is ranked (recency or engagement-based).
* The feed updates with new content when refreshed.

#### Notification System

* A user is notified when:

  * They receive a friend request
  * Someone likes their post
  * Someone comments on their post
* A user can view unread/read notifications.
* Notifications can be sent via push/email (optional).

#### Search

* A user can search for other users by name or email.
* A user can search their own posts.

### System APIs (Sketch)

| API Endpoint           | Method   | Description                    |
| ---------------------- | -------- | ------------------------------ |
| `/signup`              | POST     | Register a new user            |
| `/login`               | POST     | Log in and receive a token     |
| `/user/profile`        | GET/PUT  | View or update profile         |
| `/friends/request/:id` | POST     | Send friend request            |
| `/friends/respond/:id` | POST     | Accept/reject friend request   |
| `/posts`               | POST     | Create a new post              |
| `/posts/:id`           | DELETE   | Delete a post                  |
| `/feed`                | GET      | Get personalized feed          |
| `/posts/:id/like`      | POST     | Like/unlike post               |
| `/posts/:id/comments`  | GET/POST | View/add comments              |
| `/notifications`       | GET      | View unread/read notifications |


## ✅ STEP 3: Define Non-Functional Requirements (NFRs)

> Non-functional requirements describe the **system's quality attributes**: performance, scalability, reliability, availability, security, and more.

### **Scalability**

* System must support **billions of users**, millions online concurrently.
* Should handle **millions of posts, likes, and comments daily**.
* **Reads >> Writes** → feed reads, post reads, comment reads will be extremely frequent.
* Must be **horizontally scalable**.

#### Design Implications:

* Shard databases
* Partition users/posts
* Use distributed caching (e.g., Redis)
* Use load balancers and stateless services

### **Availability**

* Core services must achieve **99.99% availability** (4.38 minutes/month of downtime).
* Feed, post, and profile systems should be **highly available**.
* Temporary unavailability of likes or notifications is acceptable.

#### Design Implications:

* Use redundant servers and failover mechanisms
* Geo-distributed data centers
* Health checks and circuit breakers
* Graceful degradation (e.g., fallback to partial feed)

### **Latency / Performance**

| Operation             | Target Latency (P95) |
| --------------------- | -------------------- |
| Feed load             | ≤ 200ms              |
| Post submission       | ≤ 500ms              |
| Like/comment action   | ≤ 150ms              |
| Friend request        | ≤ 100ms              |
| Notification delivery | ≤ 1s                 |

#### Design Implications:

* Use caching (user profile, feed, post data)
* Precompute feed for fast delivery
* Async processing for heavy operations (notifications, fan-out)

### **Consistency**

* **Eventual consistency** is acceptable for:

  * News feed (slight delays are okay)
  * Likes/comments counts
* **Strong consistency** is required for:

  * Auth
  * Friendship status
  * Privacy settings
  * Deleting posts/comments

### **Durability**

* **No data loss** for posts, comments, friendships, etc.
* All user content should be **backed up and replicated**.

#### Design Implications:

* Write-ahead logs (WAL)
* Replication across availability zones
* Blob storage for media (S3, GCS) with versioning

### **Security**

* All user data should be encrypted at rest and in transit.
* Support for:

  * JWT/OAuth2 session tokens
  * Password hashing (bcrypt, Argon2)
  * Rate limiting to prevent brute force
* Protect against:

  * XSS, CSRF, SQL injection
  * Abuse (e.g. fake likes, bot comments)

#### Design Implications:

* HTTPS for all traffic
* RBAC/ownership checks on APIs
* Input validation, escaping

### **Privacy**

* Posts should be visible only to intended audiences (friends-only, private, etc).
* Friend lists and activity logs should respect privacy settings.
* Comply with **GDPR** and **data deletion** requests.

#### Design Implications:

* Enforce permissions in the post read/feed generation logic
* Metadata indexing (e.g., visibility level) in DB
* Audit logs for privacy actions

### **Maintainability & Modularity**

* System should be built in a **microservices-friendly** way.
* Easy to update individual features (like feed or notifications).
* Clean APIs between components.

### **Testability**

* Must support:

  * Unit tests
  * Integration tests
  * Load testing (simulate thousands of users)
  * Canary/staged deployments

### **Observability**

* Engineers must be able to:

  * Track failures and slowdowns
  * View logs per request/user/session
  * Alert on anomalies

#### Design Implications:

* Structured logging (JSON logs)
* Metrics (Prometheus/Grafana)
* Tracing (OpenTelemetry, Jaeger)
* Alerting systems (PagerDuty, Slack)

### **Cost Efficiency**

* Infrastructure should scale cost-efficiently.
* CDN, cache, and media delivery should be optimized for cold/warm/hot access.

#### Design Implications:

* Use CDN for all media and profile pictures
* Use tiered storage (hot Redis, warm disk, cold archive)
* Use autoscaling


## ✅ STEP 4: Define System Interfaces / APIs

### API Design Principles

* RESTful (for most endpoints)
* Resource-oriented (nouns over verbs)
* Stateless
* Support **pagination, filtering, sorting, throttling**
* Versioned: `api/v1/...`
* Return standard codes: `200`, `201`, `400`, `403`, `404`, `429`, `500`

### Authentication APIs

| Endpoint          | Method | Description                |
| ----------------- | ------ | -------------------------- |
| `/api/v1/signup`  | POST   | Create a new account       |
| `/api/v1/login`   | POST   | Log in, returns auth token |
| `/api/v1/logout`  | POST   | Invalidate session/token   |
| `/api/v1/refresh` | POST   | Refresh token (if used)    |

### User Profile APIs

| Endpoint            | Method | Description                 |
| ------------------- | ------ | --------------------------- |
| `/api/v1/users/me`  | GET    | Get current user's profile  |
| `/api/v1/users/me`  | PUT    | Update profile info         |
| `/api/v1/users/:id` | GET    | View another user's profile |

### Friendship APIs

| Endpoint                           | Method | Description                     |
| ---------------------------------- | ------ | ------------------------------- |
| `/api/v1/friends/requests`         | GET    | View incoming/outgoing requests |
| `/api/v1/friends/request/:user_id` | POST   | Send friend request             |
| `/api/v1/friends/respond/:user_id` | POST   | Accept/reject friend request    |
| `/api/v1/friends/list`             | GET    | Get list of friends             |
| `/api/v1/friends/remove/:user_id`  | DELETE | Unfriend a user                 |

### Post APIs

| Endpoint                  | Method | Description             |
| ------------------------- | ------ | ----------------------- |
| `/api/v1/posts`           | POST   | Create a new post       |
| `/api/v1/posts/:id`       | GET    | Get a specific post     |
| `/api/v1/posts/:id`       | DELETE | Delete your own post    |
| `/api/v1/users/:id/posts` | GET    | Get all posts by a user |

### News Feed APIs

| Endpoint       | Method | Description           |
| -------------- | ------ | --------------------- |
| `/api/v1/feed` | GET    | Get personalized feed |

#### Query Params:

* `limit`: number of items (default 10)
* `cursor` or `page`: for pagination

### Likes APIs

| Endpoint                  | Method | Description             |
| ------------------------- | ------ | ----------------------- |
| `/api/v1/posts/:id/like`  | POST   | Like or unlike a post   |
| `/api/v1/posts/:id/likes` | GET    | Get list/count of likes |

### Comments APIs

| Endpoint                     | Method | Description             |
| ---------------------------- | ------ | ----------------------- |
| `/api/v1/posts/:id/comments` | GET    | View comments on a post |
| `/api/v1/posts/:id/comments` | POST   | Add a comment to a post |
| `/api/v1/comments/:id`       | DELETE | Delete a comment        |

### Notification APIs

| Endpoint                         | Method | Description                 |
| -------------------------------- | ------ | --------------------------- |
| `/api/v1/notifications`          | GET    | Get all notifications       |
| `/api/v1/notifications/:id/read` | POST   | Mark a notification as read |

### Search API

| Endpoint               | Method | Description                    |
| ---------------------- | ------ | ------------------------------ |
| `/api/v1/search/users` | GET    | Search for users by name/email |

### Internal Microservice APIs

These are not exposed to the frontend but help for **internal service-to-service communication**:

* `POST /internal/fanout/post` — Called by Post Service → Feed Service to trigger push
* `POST /internal/notify` — Send real-time notifications
* `POST /internal/user-sync` — Update search index / graph db on profile change

### 4.12 Media Upload APIs

* `GET /api/v1/upload-url` → Get a signed URL for image/video upload
* Upload image directly to CDN
* Return URL and attach to post


## ✅ STEP 5: High-Level Architecture

> High-level means we are not yet choosing specific tools, but rather defining **the main components**, **their responsibilities**, and how data and requests **flow** across the system.

### Core Components

```
                    ┌────────────┐
                    │   Client   │ (Web/iOS/Android)
                    └─────┬──────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ API Gateway / LB│
                 └────┬───────┬────┘
                      ▼       ▼
     ┌────────────────────┐ ┌────────────────────┐
     │ Authentication Svc │ │  User/Profile Svc  │
     └────────────────────┘ └────────────────────┘
                      ▼
     ┌────────────────────┐ ┌────────────────────┐
     │ Friend Graph Svc   │ │     Post Svc       │
     └────────────────────┘ └────────────────────┘
                      ▼
     ┌────────────────────┐ ┌────────────────────┐
     │ Feed/Timeline Svc  │ │  Like/Comment Svc   │
     └────────────────────┘ └────────────────────┘
                      ▼
               ┌──────────────┐
               │ Notification │
               └─────┬────────┘
                     ▼
           ┌────────────────────┐
           │ Media/CDN Service  │
           └────────────────────┘

        (All backed by databases and caches)
```

### Service Responsibilities

| Service                  | Responsibility                                        |
| ------------------------ | ----------------------------------------------------- |
| **API Gateway**          | Entry point, auth/token check, rate limit, routing    |
| **Auth Service**         | Login, signup, JWT issuing, token validation          |
| **User Service**         | Profile CRUD, avatar, bio, privacy settings           |
| **Friendship Service**   | Send/accept/remove friend requests, check mutuals     |
| **Post Service**         | Create/delete posts, store metadata and media links   |
| **Feed Service**         | Fan-out on write, ranking, retrieve paginated feed    |
| **Like/Comment Service** | Handle post likes, unlikes, comments CRUD             |
| **Notification Service** | Send real-time/email notifications, track read/unread |
| **Media Service**        | Handles signed URLs, uploads to CDN, proxying         |

### Supporting Infrastructure

| Component        | Role                                                                |
| ---------------- | ------------------------------------------------------------------- |
| **Databases**    | Stores structured data (users, posts, likes, friendships)           |
| **Blob Storage** | Stores images/videos (S3, GCS, etc.)                                |
| **Cache Layer**  | Redis or Memcached — speed up reads (feeds, posts, profiles)        |
| **CDN**          | Serve static content globally (profile pictures, post images)       |
| **Queue System** | Kafka, RabbitMQ — async processing (notifications, feed generation) |
| **Monitoring**   | Prometheus, Grafana, logs/metrics/tracing                           |

### Request Flows

#### News Feed Load (Fan-out model)

```
Client → API Gateway → Feed Service
         ↓
     Cache (User Feed Cache)
         ↓ (if cache miss)
     DB or Fan-out Store → Return top 20 posts → Client
```

#### Post Creation

```
Client → API Gateway → Post Service
                        ↓
                   Store in DB
                        ↓
            Push to Feed Service (via queue)
                        ↓
         Update friend feed caches or async storage
                        ↓
         Trigger Notifications via Notification Service
```

#### Friend Request Flow

```
Client → API Gateway → Friendship Service
                        ↓
                   Update DB
                        ↓
             Trigger Notification Service
```

#### Like Flow

```
Client → API Gateway → Like Service
                        ↓
                   Update DB
                        ↓
             Update like count in cache
                        ↓
        Notify post owner (optional)
```

### Deployment Architecture

* **Stateless app servers** behind load balancers
* Each service **independently scalable**
* Services communicate via **REST/gRPC** internally
* Use **containers (Docker)** + **Kubernetes** for orchestration
* Deployed across **multiple regions/zones**
* All services monitored and alerting enabled

### Scaling Strategy

| Component         | Scaling Strategy                             |
| ----------------- | -------------------------------------------- |
| **API Gateway**   | Horizontally scale stateless proxies         |
| **Post/Feed DBs** | Shard by user\_id                            |
| **Feed Service**  | Use async queues + precomputed feed cache    |
| **Media**         | Use CDN edge caching                         |
| **Notification**  | Decouple via pub/sub queue                   |
| **Friends**       | Graph partitioning if needed (for big users) |

### Caching Strategy

| Cached Entity        | Layer | TTL / Invalidation Strategy            |
| -------------------- | ----- | -------------------------------------- |
| User profile         | Redis | 5 min TTL or on update                 |
| News feed            | Redis | Precomputed and updated on new posts   |
| Post details         | Redis | 10–30 min TTL                          |
| Friends list         | Redis | Cached and synced periodically         |
| Likes/comments count | Redis | Async updates from DB or write-through |

###  ML & Ranking

If you want intelligent feeds:

* Use a **Feed Ranking Service** (separate microservice)
* Takes post, user features as input (recency, engagement, friend proximity)
* Outputs relevance score per post


## ✅ STEP 6: Database Design & Schema (ERD)

### Key Entities

The main things we need to store:

* Users
* Friendships
* Posts
* Media
* Likes
* Comments
* Notifications

### Entity Relationship Diagram (ERD)

```
[User]
 ├─ user_id (PK)
 ├─ name
 ├─ email
 ├─ password_hash
 ├─ bio
 └─ avatar_url

[Friendship]
 ├─ user_id_1 (FK → User)
 ├─ user_id_2 (FK → User)
 ├─ status (pending, accepted)
 └─ created_at

[Post]
 ├─ post_id (PK)
 ├─ user_id (FK → User)
 ├─ text
 ├─ image_url
 ├─ visibility (public, friends)
 ├─ created_at
 └─ updated_at

[Like]
 ├─ like_id (PK)
 ├─ post_id (FK → Post)
 ├─ user_id (FK → User)
 ├─ created_at

[Comment]
 ├─ comment_id (PK)
 ├─ post_id (FK → Post)
 ├─ user_id (FK → User)
 ├─ text
 ├─ created_at

[Notification]
 ├─ notification_id (PK)
 ├─ user_id (FK → User)
 ├─ type (like, comment, friend_request)
 ├─ source_user_id (FK → User)
 ├─ post_id (optional FK → Post)
 ├─ seen (boolean)
 ├─ created_at

[Media]  (optional if offloaded to S3/CDN)
 ├─ media_id (PK)
 ├─ post_id (FK → Post)
 ├─ url
 ├─ type (image, video)
 ├─ uploaded_at
```

### Relationship Summary

| Relationship                     | Type         |
| -------------------------------- | ------------ |
| One User → Many Posts            | 1\:N         |
| One Post → Many Comments         | 1\:N         |
| One Post → Many Likes            | 1\:N         |
| One User ↔ One User (Friendship) | Many-to-Many |
| One Post ↔ Media (Optional)      | 1\:N         |
| One User → Many Notifications    | 1\:N         |

### Schema Normalization Notes

* Fully normalized for **consistency and clarity**
* Optionally denormalize in caching or analytic layers (e.g. precomputed like count)
* Maintain **write-heavy and read-heavy** tables separately

### Indexing Strategy

| Table        | Indexes                                             |
| ------------ | --------------------------------------------------- |
| User         | `email` (unique), `user_id` (PK)                    |
| Post         | `user_id`, `created_at`                             |
| Like         | `post_id`, `user_id`, `(post_id, user_id)` (unique) |
| Comment      | `post_id`, `created_at`                             |
| Friendship   | `(user_id_1, user_id_2)` (unique), `status`         |
| Notification | `user_id`, `seen`, `created_at`                     |

### Partitioning / Sharding Strategy

For scale, the following partitioning ideas help:

| Table        | Shard Key   | Notes                             |
| ------------ | ----------- | --------------------------------- |
| Post         | `user_id`   | Most posts are read by friends    |
| Comment      | `post_id`   | Comments only shown per-post      |
| Like         | `post_id`   | Many likes per post               |
| Friendship   | `user_id_1` | Graph partitioning later optional |
| Notification | `user_id`   | Each user sees only their own     |

### Feed Storage Strategy (Precomputed Feed)

You can store feed entries in a separate table:

```
[FeedEntry]
 ├─ user_id (owner of feed)
 ├─ post_id
 ├─ score (for ranking)
 ├─ inserted_at
```

* This is filled by **fan-out on write**
* Supports **quick pagination**
* Can be cached in Redis (per user)

### User Graph (Social Graph DB)

To support more complex relationships (e.g. mutual friends, friend recommendations):

* Use **Graph DB** (like Neo4j) or **adjacency list in SQL**
* Or build social graph index in memory / Redis

### Media Storage Strategy

* Store images/videos on S3 or CDN
* Just keep metadata + links in DB
* Use signed URLs for uploads


## ✅ STEP 7: Component Design (Low-Level Design)

### 🎯 Goal:

Define **how each core service works internally**, including:

* Internal classes/modules
* Request flows
* Caching strategies
* DB interactions
* Pub/Sub or queues (if needed)

## 7.1 Post Service

* Create, read, delete posts
* Store post metadata
* Trigger feed update and notifications

### Internal Components:

```
PostService
├── PostController         # Handles HTTP requests
├── PostManager            # Business logic (create, delete)
├── PostRepository         # Interface to Post DB
├── MediaServiceClient     # Upload images/videos
├── FeedPublisher          # Publishes new post event to Feed queue
├── NotificationPublisher  # Sends notification events
```

### Sample Flow: Create Post

```
1. Controller receives POST /posts
2. Validates payload
3. Stores post in DB via PostRepository
4. Publishes "NewPostEvent" to Kafka → FeedService
5. Publishes notification to user followers (async)
6. Returns post ID and metadata
```

### Caching:

* Cache post content (hot posts) in Redis: `post:{post_id}`
* TTL: 15 minutes, refreshed on access

## 7.2 Feed Service

* Generate user feed (fan-out or pull)
* Score and rank posts
* Read from post DB or feed cache

### Internal Components:

```
FeedService
├── FeedController
├── FeedManager
├── FeedStore              # DB or Redis-based precomputed feed
├── RankerModule           # Sorts by recency + popularity
├── FeedFanOutWorker       # Listens to "NewPostEvent"
```

### Sample Flow: Load Feed

```
1. Controller receives GET /feed?cursor=...
2. Checks Redis cache: feed:{user_id}
3. If cache miss:
   a. Pulls friend list
   b. Pulls N recent posts
   c. Ranks posts
   d. Stores result in cache
4. Returns top posts with pagination
```

### Caching:

* Redis: `feed:{user_id}` = list of post\_ids (sorted)
* TTL = 60 seconds
* Background job refreshes hot feeds (active users)

## 7.3 Friendship Service

* Manage friendships (bidirectional)
* Support friend request lifecycle
* Validate friendship in other services

### Internal Components:

```
FriendService
├── FriendController
├── FriendManager
├── FriendshipRepository
├── NotificationPublisher
```

### Flow: Send Friend Request

```
1. User A sends request to B
2. Store in Friendship table: (A, B, pending)
3. Notify B via NotificationPublisher
```

### Caching:

* Cache friends list: `friends:{user_id}`
* Invalidate on accept/remove

## 7.4 Like & Comment Service

* Like/unlike post
* Add/view comments
* Update like/comment count

### Internal Components:

```
InteractionService
├── LikeController / CommentController
├── LikeManager / CommentManager
├── LikeRepository / CommentRepository
├── PostStatUpdater
├── NotificationPublisher
```

### Flow: Like a Post

```
1. POST /posts/:id/like
2. Add entry in Like table
3. Update post's like count (write-through cache)
4. Send notification to post owner (optional)
```

### Caching:

* Redis: `post_likes:{post_id}`, `post_comments:{post_id}`
* Use sorted sets for comments if ordered

## 7.5 Notification Service

* Receive events (like, comment, friend request)
* Generate and store notifications
* Support unread/read views

### Internal Components:

```
NotificationService
├── NotificationController
├── NotificationManager
├── NotificationRepository
├── EventConsumer (Kafka listener)
```

### Flow: Handle Like Event

```
1. EventConsumer receives "PostLikedEvent"
2. Creates notification row in DB
3. Optionally pushes real-time notification (websocket)
```

### Caching:

* Optional: Cache last 10 unread notifications: `notif:{user_id}`

## 7.6 Media Service (Optional External)

* Generate signed URLs for upload
* Store file metadata
* Serve static URLs via CDN

### Flow: Upload Image

1. GET `/upload-url`
2. Returns pre-signed S3 URL
3. Client uploads image to S3
4. Client POSTs the image URL with post content

## 7.7 User Service

* Manage user profiles
* Avatar, bio, privacy settings

### Internal Components:

```
UserService
├── UserController
├── UserManager
├── UserRepository
```

### Caching:

* Redis: `user:{id}` profile (5 min TTL or on update)

## 7.8 Auth Service

* Handle login/signup
* Issue and validate tokens

### Internal Components:

```
AuthService
├── AuthController
├── TokenManager (JWT or session)
├── UserAuthRepository
```

## 7.9 Event & Queue System

Use Kafka or RabbitMQ to send events like:

* `PostCreatedEvent`
* `FriendRequestSentEvent`
* `PostLikedEvent`

Each service listens to **only the events it needs**.

### Sample Event Structure

```json
{
  "type": "PostCreated",
  "user_id": "u123",
  "post_id": "p456",
  "created_at": "2025-07-01T12:00:00Z"
}
```


## ✅ STEP 8: Scaling & Optimization

### 8.1 Database Scaling

**Challenges:**

* Billions of users and posts → DB size explodes
* High read/write load

**Strategies:**

* **Vertical Scaling:** Increase hardware capacity (limited)
* **Horizontal Scaling:** Partition data (sharding)

**Sharding Strategies:**

* User-based sharding: partition data by `user_id`
* Functional sharding: separate DBs for users, posts, likes, comments
* Time-based sharding for logs/analytics

**Replication:**

* Master-slave replication for reads
* Multi-region replication for availability

### 8.2 Caching

**Types:**

* **User/profile cache:** Store frequent reads of user data
* **Feed cache:** Precompute and cache user feeds in Redis
* **Post cache:** Hot posts cached to reduce DB hits
* **Like/comment counts:** Cache counts to avoid count(\*) queries

**Techniques:**

* TTL eviction strategies
* Cache invalidation on writes
* Write-through or write-back caches depending on consistency needs

### 8.3 Feed Generation Optimization

**Fan-out on Write vs Fan-out on Read**

* **Fan-out on Write:** When a user posts, push to all friends’ feeds immediately (high write cost, low read latency)
* **Fan-out on Read:** Compute feed on demand (low write cost, high read latency)

**Hybrid Approach:**

* Use fan-out on write for users with small friend counts
* Use fan-out on read for users with huge friend counts (celebrities)

### 8.4 Rate Limiting & Throttling

Prevent abuse and overload:

* Per-user API rate limiting (e.g., 100 requests/min)
* Global rate limiting per API endpoint
* Exponential backoff on retries
* Use token buckets or leaky bucket algorithms

### 8.5 Load Balancing

* Use DNS-level and application-level load balancers
* Sticky sessions if needed, but better to keep services stateless
* Health checks and circuit breakers

### 8.6 Asynchronous Processing

* Use message queues (Kafka/RabbitMQ) for:

  * Feed updates
  * Notification dispatch
  * Media processing (image resizing)
* Avoid blocking main request flow

### 8.7 Hot Key Mitigation

* Popular posts or users can create hot keys that overload DB/cache
* Mitigations:

  * Use multi-level caches (L1 in-memory, L2 distributed)
  * Rate limit heavy users
  * Pre-aggregate counts and stats
  * Separate hot user shards or dedicated caches

### 8.8 Data Compression & Storage Optimization

* Compress text and media payloads
* Use efficient storage formats (e.g., Parquet) for analytics
* Archive cold data to cheaper storage tiers

### 8.9 CDN Usage

* Offload static media (profile pics, post images/videos) to CDN
* Use edge caching globally
* Use signed URLs for secure media access

### 8.10 Monitoring & Auto-scaling

* Monitor latency, error rates, traffic patterns
* Auto-scale app servers and cache clusters based on load
* Use predictive scaling if possible

### 8.11 Security Optimizations

* Encrypt data at rest/in transit without performance bottlenecks
* Use WAFs, DDOS protection at the edge
* Periodic security audits and penetration testing

Great choice! Security and privacy are absolutely critical, especially for a platform like Facebook handling tons of sensitive personal data.


## ✅ STEP 9: Security & Privacy Considerations

### Authentication & Authorization

* **Strong authentication**:

  * Use OAuth2 / JWT tokens for session management
  * Enforce multi-factor authentication (MFA) optionally
* **Password security**:

  * Store passwords hashed with strong algorithms (bcrypt, Argon2)
  * Implement password strength policies and rate limiting login attempts
* **Authorization**:

  * Enforce role-based access control (RBAC)
  * Fine-grained permission checks (e.g., post visibility, editing rights)
  * Verify ownership before edits/deletes

### Data Encryption

* **Encrypt data at rest**:

  * Database encryption (AES-256)
  * Encrypted blob storage (S3 server-side encryption)
* **Encrypt data in transit**:

  * Enforce HTTPS/TLS everywhere (including internal services)
* **Key management**:

  * Use dedicated key management services (KMS)
  * Rotate encryption keys regularly

### Input Validation & Injection Protection

* Sanitize and validate all user inputs to prevent:

  * SQL injection
  * Cross-site scripting (XSS)
  * Cross-site request forgery (CSRF)
* Use prepared statements and ORM safeguards
* Implement Content Security Policy (CSP) headers in the frontend

### Rate Limiting & Abuse Prevention

* Limit API calls per user/IP to prevent brute force or scraping
* Monitor and flag suspicious behavior (rapid requests, spam)
* Use CAPTCHAs for suspicious flows (e.g., signups, comments)
* Implement abuse detection algorithms for fake accounts, fake likes/comments

### Privacy Controls & Compliance

* Let users set **privacy preferences** on posts (public, friends-only, custom lists)
* Support **data portability** and **right to be forgotten** (GDPR compliance)
* Audit access logs for user data
* Allow users to **download their data** securely
* Ensure compliance with **regional laws** (GDPR, CCPA, etc.)

### Secure Logging & Monitoring

* Log security-relevant events (login attempts, data access, permission changes)
* Mask or avoid logging sensitive data (passwords, tokens)
* Monitor logs for unusual access patterns and potential breaches

### Infrastructure Security

* Use firewalls and DDoS protection at the network edge
* Secure all service-to-service communication (mutual TLS)
* Regular vulnerability scanning and penetration testing
* Harden server OS and container images (minimal base images)

### Incident Response & Recovery

* Define incident response plans for data breaches
* Encrypt backups and test recovery procedures regularly
* Notify users and regulators promptly on breaches per legal requirements


## ✅ STEP 10: Monitoring, Logging & Alerting

### Monitoring

**Goals:** Track system health, performance, and usage metrics in real time.

* **Key metrics to monitor:**

  * **Infrastructure:** CPU, memory, disk IO, network bandwidth
  * **Application:** Request rate, error rate, latency, throughput
  * **Database:** Query latency, connection counts, cache hit/miss ratio
  * **Queues:** Message lag, processing rates, failure rates
  * **Business:** User signup rate, posts created, friend requests, active users

* **Tools:**

  * Prometheus + Grafana (metrics collection and dashboards)
  * Cloud provider monitoring (AWS CloudWatch, GCP Stackdriver)
  * New Relic, Datadog, or similar APMs

* **Dashboards:**

  * Visualize trends, spot anomalies quickly
  * Drill down from high-level health to specific service or endpoint

### Logging

**Goals:** Capture detailed logs for debugging, auditing, and compliance.

* **Types of logs:**

  * **Access logs:** Every request with status, response time, IP, user agent
  * **Error logs:** Exceptions, stack traces, failed database calls
  * **Audit logs:** Changes to critical data (profile updates, permissions)
  * **Event logs:** Business events like user signup, post creation

* **Best practices:**

  * Structured logging (JSON format) for easier parsing
  * Centralized logging system (e.g., ELK stack: Elasticsearch, Logstash, Kibana)
  * Retention policies depending on log type and compliance needs

* **Security:**

  * Avoid logging sensitive data (passwords, tokens)
  * Secure access to logs

### Alerting

**Goals:** Detect issues early and notify responsible teams instantly.

* **Alert triggers:**

  * High error rates or latency spikes
  * Infrastructure resource exhaustion (CPU, disk)
  * Queue backlogs or consumer failures
  * Security incidents (e.g., repeated failed logins)
  * Business KPIs deviation (drop in active users)

* **Alert channels:**

  * Email, SMS, Slack, PagerDuty, Opsgenie

* **Alert management:**

  * Define severity levels and escalation policies
  * Avoid alert fatigue: tune thresholds carefully
  * Postmortems for incident resolution and continuous improvement

### Distributed Tracing

* Trace requests across microservices to identify bottlenecks and failures
* Tools: Jaeger, Zipkin, AWS X-Ray

### Health Checks & Self-Healing

* Services expose health endpoints (`/healthz`)
* Load balancers and orchestrators (K8s) auto-restart unhealthy instances
* Circuit breakers to isolate failing services

### Monitoring Data Retention & Privacy

* Store logs and metrics for a reasonable retention period (e.g., 30-90 days)
* Comply with privacy laws around data storage and deletion


## ✅ STEP 11: Cost & Infrastructure Planning

### Infrastructure Components & Cost Drivers

| Component            | Description                                | Cost Drivers                           |
| -------------------- | ------------------------------------------ | -------------------------------------- |
| Compute              | App servers, microservices                 | Number of instances, CPU, RAM, uptime  |
| Database             | SQL/NoSQL clusters                         | Storage size, IOPS, replication        |
| Cache                | Redis/Memcached clusters                   | Memory size, number of nodes           |
| Storage              | Blob storage (images, videos)              | Data size, bandwidth, PUT/GET requests |
| Network              | Data transfer (between regions, CDN usage) | Egress bandwidth, number of requests   |
| CDN                  | Content delivery network                   | Requests served, bandwidth             |
| Messaging Queues     | Kafka, RabbitMQ                            | Throughput, retention time             |
| Monitoring & Logging | Metrics, logs, tracing                     | Data volume stored, query volume       |

### Cost Optimization Strategies

* **Right-sizing:** Match instance types to workload, avoid over-provisioning
* **Auto-scaling:** Automatically scale up/down based on demand
* **Reserved Instances / Savings Plans:** Commit for discounts on compute
* **Data lifecycle policies:** Archive or delete cold data to cheaper storage tiers
* **Cache aggressively:** Reduce DB load and bandwidth cost
* **Batch processing:** Aggregate writes/updates to reduce calls
* **Use spot/preemptible instances:** For non-critical workloads (e.g., analytics)
* **Use CDNs:** Reduce direct origin traffic, save on egress costs
* **Optimize media assets:** Compress images/videos to reduce storage and transfer costs

### Infrastructure Sizing Guidelines (Example)

| Service          | Initial Setup                          | Scaling Metric                    |
| ---------------- | -------------------------------------- | --------------------------------- |
| API Servers      | 10 instances (4 vCPU, 16GB RAM)        | Requests per second, CPU load     |
| Database Cluster | 3-node primary + 3 replicas            | Storage & read/write throughput   |
| Cache Cluster    | 5-node Redis cluster (128GB total RAM) | Cache hit ratio, memory usage     |
| Blob Storage     | S3 or equivalent                       | Total GB stored, monthly requests |
| Message Queue    | Kafka cluster with 5 brokers           | Messages per second, retention    |

### Budgeting & Forecasting

* Estimate **monthly costs** per component based on:

  * Expected user base size
  * Average request rate per user
  * Average data size per user (posts, media)
* Use cloud provider cost calculators (AWS, GCP, Azure)
* Monitor actual spend and adjust architecture or scale accordingly

### Multi-Region Deployment Costs

* Cross-region data transfer fees
* Additional replication costs
* Deploying redundant services per region for low latency and disaster recovery

### Disaster Recovery & Backup Costs

* Backups storage and retrieval costs
* Secondary DR sites or cloud regions
* Snapshots and recovery automation

### Team & Operational Costs

* Cost of DevOps and SRE teams managing infrastructure
* Cost of third-party services (monitoring, logging, security)


## ✅ STEP 12: Testing & Deployment Strategies

### Testing Strategies

**Goal:** Ensure quality, catch bugs early, and maintain system stability.

#### A. Unit Testing

* Test individual components (e.g., PostService, FeedService logic)
* Mock external dependencies (DB, queues)
* Use frameworks like Jest (JS), JUnit (Java), PyTest (Python)

#### B. Integration Testing

* Test interactions between components (e.g., Post creation triggers Feed update)
* Use test databases and queues
* Verify API contracts and event flows

#### C. End-to-End (E2E) Testing

* Simulate real user workflows via UI or API calls
* Tools: Selenium, Cypress, Postman/Newman

#### D. Load & Stress Testing

* Simulate high traffic to identify bottlenecks and breaking points
* Tools: JMeter, Locust, k6

#### E. Security Testing

* Automated scans for vulnerabilities (OWASP top 10)
* Manual penetration testing

#### F. Chaos Engineering (Advanced)

* Introduce controlled failures to verify resilience (e.g., shutting down services)

### Continuous Integration (CI)

* Automate building, testing, and validating code on each commit or PR
* Tools: GitHub Actions, Jenkins, GitLab CI/CD
* Run unit, integration tests automatically before merging

### Continuous Deployment / Delivery (CD)

* Automate deployment pipelines with zero or minimal downtime
* Blue/Green or Canary deployments for safer rollouts
* Tools: Spinnaker, ArgoCD, Flux, Jenkins

### Deployment Architecture

* Containerize services (Docker)
* Orchestrate with Kubernetes or ECS/Fargate
* Use Helm charts or Terraform for infrastructure as code (IaC)
* Use config management for environment-specific settings

### Rollback & Recovery

* Versioned deployments to easily rollback on failure
* Automated monitoring triggers rollback for failed deployments
* Backup and restore mechanisms for DBs and storage

### Monitoring Post-Deployment

* Use health checks, logging, and alerting to ensure new releases don’t degrade service
* Collect user feedback and crash reports

### Documentation & Runbooks

* Maintain updated docs for setup, deployment, and troubleshooting
* Create runbooks for common incidents and outages
