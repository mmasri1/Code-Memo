## ✅ STEP 5: High-Level Architecture

* **1:1 chats**, **group chats**, **voice/video calls**, **real-time delivery**, and **end-to-end encryption (E2EE)**
* High **availability**, **low latency**, and **scalability** to billions of users

## 🔧 1. **Key Architectural Principles**

| Principle                          | Explanation                                                                |
| ---------------------------------- | -------------------------------------------------------------------------- |
| **Microservices**                  | Separate concerns like messaging, users, media, notifications, etc.        |
| **Async Communication**            | Message queues for reliable delivery and offline handling                  |
| **Data Partitioning**              | Shard users and messages for horizontal scalability                        |
| **End-to-End Encryption (E2EE)**   | Messages are encrypted client-side before being sent                       |
| **High Availability & Redundancy** | Data replicated across regions, active-active setup                        |
| **Eventually Consistent**          | Some operations (like message delivery receipts) can tolerate slight delay |

## 🧩 2. **Major Components Overview**

We split the architecture into **Client**, **Edge**, and **Backend services**.

```
[ Mobile Client ]
       |
       v
[ Load Balancer / API Gateway ]
       |
       v
+------------------------+
|      Edge Services     |
|------------------------|
| Auth Service           |
| Session Service        |
| Notification Gateway   |
+------------------------+
       |
       v
+------------------------+
|     Core Backend       |
|------------------------|
| User Service           |
| Chat Service           |
| Group Service          |
| Presence Service       |
| Message Router         |
| Media Service          |
+------------------------+
       |
       v
+------------------------+
|     Async Systems      |
|------------------------|
| Kafka / Pulsar         |
| Notification Workers   |
| Delivery Workers       |
+------------------------+
       |
       v
+------------------------+
|     Storage Layer      |
|------------------------|
| User DB (e.g. MySQL)   |
| Messages DB (Cassandra)|
| Media Store (S3-like)  |
| Redis / Memcached      |
+------------------------+
```

## 🧱 3. **Component Breakdown**

### ✅ 3.1. **Client (iOS, Android, Web)**

* Encrypts messages before sending
* Stores the encryption keys securely
* Sends/receives messages over TLS
* Handles media, notifications, and local state
* Listens for push notifications (via APNs/FCM)

### ✅ 3.2. **API Gateway / Load Balancer**

* TLS termination
* Routes requests to appropriate microservices
* Performs rate limiting, auth header validation
* Supports sticky sessions (e.g. via Redis)

### ✅ 3.3. **Edge Services**

| Service                  | Description                              |
| ------------------------ | ---------------------------------------- |
| **Auth Service**         | Handles login/signup, OTP verification   |
| **Session Service**      | Manages device tokens, sessions, refresh |
| **Push Gateway**         | Sends push notifications via FCM/APNs    |
| **Throttler / Firewall** | Mitigates abuse, spam, or DDOS           |

### ✅ 3.4. **Core Backend Services**

| Service              | Role                                               |
| -------------------- | -------------------------------------------------- |
| **User Service**     | User profile, settings, contacts                   |
| **Chat Service**     | Direct message metadata, chat history references   |
| **Group Service**    | Group metadata (members, admins, etc.)             |
| **Presence Service** | Tracks online/offline status (ephemeral, in Redis) |
| **Message Router**   | Core of real-time delivery, uses async queues      |
| **Media Service**    | Handles upload/download of images, voice, videos   |

### ✅ 3.5. **Async Systems (via Kafka/Pulsar)**

| Worker Type            | Role                                              |
| ---------------------- | ------------------------------------------------- |
| **Message Dispatcher** | Routes message to recipients                      |
| **Delivery Worker**    | Ensures message is delivered to online users      |
| **Store-and-Forward**  | Saves messages for offline users                  |
| **Push Worker**        | Sends push for offline recipients                 |
| **Analytics Worker**   | Logs message metadata (not content) for analytics |

### ✅ 3.6. **Storage Systems**

| Type              | Tech                     | Usage                                 |
| ----------------- | ------------------------ | ------------------------------------- |
| **Relational DB** | MySQL / Postgres         | User data, group metadata             |
| **NoSQL**         | Cassandra / ScyllaDB     | Messages, as they scale horizontally  |
| **Blob Store**    | S3 / MinIO               | Media (voice notes, images, videos)   |
| **In-Memory**     | Redis                    | Presence, session tokens, rate limits |
| **Search Engine** | ElasticSearch (optional) | Message search (if allowed)           |

### ✅ 3.7. **Encryption Handling**

* **Messages are encrypted client-side** (Signal Protocol)
* Server does **not store encryption keys**
* Only the recipient can decrypt the message
* Group messages are encrypted per member

### ✅ 3.8. **Realtime Messaging Path**

```plaintext
1. Client encrypts message ➝ sends to Message API
2. API Gateway forwards to Message Router
3. Router places it on Kafka topic
4. Worker picks up and:
   a. If user online ➝ push via WebSocket
   b. If offline ➝ store in DB ➝ send push
5. Recipient client receives ➝ decrypts locally
```

## 🌍 4. **Global Deployment Architecture**

| Region                      | Component                                      |
| --------------------------- | ---------------------------------------------- |
| **Multi-region Deployment** | US-East, Europe, Asia replicas                 |
| **Active-Active**           | Uses consistent hashing & quorum-based writes  |
| **Geo DNS**                 | Routes traffic to nearest region               |
| **Data Replication**        | Cassandra, S3, Redis replicated across regions |
| **Disaster Recovery**       | Leader election + auto-failover in DB clusters |

## 📲 5. **Media Upload Architecture**

1. Client requests upload URL (via presigned S3 URL)
2. Uploads encrypted media directly to blob store
3. Sends media metadata + encryption keys via message
4. Recipient uses URL + key to fetch/decrypt

## 🧠 6. **Smart Offline Strategy**

* Messages are stored until **recipient comes online**
* Support **multi-device sync** (like WhatsApp Web)
* Uses **device-linked keys** for each device

## 🧪 7. **Design Considerations**

| Concern          | Strategy                                    |
| ---------------- | ------------------------------------------- |
| **Latency**      | Global POPs, edge push nodes, Redis         |
| **Durability**   | Write-ahead logging, data replication       |
| **E2EE Support** | Signal Protocol, no server key storage      |
| **Device Loss**  | Client must backup keys locally             |
| **Group Sync**   | Uses "sender keys" for efficient encryption |
| **Throttling**   | Redis counters for abuse detection          |

## 📊 High-Level Diagram (Textual)

```
+--------------+       +------------------+       +-----------------+
|   Client A   | <---> |  API Gateway / LB | <---> |  Message Router |
+--------------+       +------------------+       +-----------------+
                                                       |
                                                       v
                    +------------------- Kafka -------------------+
                    |                      |                      |
              +-----------+         +-------------+         +--------------+
              | Push Worker|         | Store Worker|         | Online Router|
              +-----------+         +-------------+         +--------------+
                    |                      |                      |
               [Push]             [Persist DB]         [Send to Client B]
```
