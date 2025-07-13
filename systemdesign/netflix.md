# ✅ STEP 5: High-Level Architecture — **Netflix**

* On-demand & live video playback
* Personalized recommendations
* User profiles, payments, and multi-device playback
* Resilient video delivery over edge/CDN
* High throughput, ultra-low latency

## 🔧 1. **Key Architectural Principles**

| Principle                      | Description                                                    |
| ------------------------------ | -------------------------------------------------------------- |
| **Microservices**              | Video, playback, auth, billing, recommendation, etc. decoupled |
| **Edge Streaming**             | Open Connect CDN delivers video as close to user as possible   |
| **Asynchronous Pipelines**     | Upload → Transcode → Package → Distribute                      |
| **Real-Time Telemetry**        | Tracks playback, buffering, failures in milliseconds           |
| **Personalization at Scale**   | ML models per user, per device                                 |
| **Cloud-Native & Auto-Scaled** | AWS-hosted, zone-resilient, fault-tolerant systems             |

## 🧩 2. **System Overview**

Netflix is composed of:

* **Client Devices (Web, TV, Mobile)**
* **API Gateway**
* **Backend Services**
* **Video Processing Pipeline**
* **Playback & Streaming Infrastructure**
* **Recommendation & Personalization Systems**
* **Billing & Security**
* **Analytics, Events & Monitoring**
* **Storage Systems**

## 📦 3. **Component Breakdown**

### ✅ 3.1. **Client Layer (Web, Android, iOS, TV, Xbox, etc.)**

* Interacts with APIs to fetch:

  * Personalized home screen (rows, posters)
  * Metadata (titles, episodes, languages)
  * Watch progress, preferences
* Streaming via adaptive bitrate (ABR)
* Local player handles buffering & fallback
* Embedded telemetry collects QoE metrics

### ✅ 3.2. **API Gateway**

* Routes to backend services
* Handles user auth, tokens, session tracking
* Supports versioning and A/B feature toggles
* Rate limiting, resilience (circuit breakers)

### ✅ 3.3. **Core Backend Microservices**

| Service                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| **User Service**           | Profile, devices, watch history               |
| **Catalog Service**        | Metadata, genres, tags, series, collections   |
| **Playback Service**       | Validates license, returns playback URLs      |
| **Subscription Service**   | Billing, plans, entitlements                  |
| **Authentication Service** | OAuth2, multi-device login, MFA               |
| **Progress Tracker**       | Watch resume, playback position               |
| **Notification Service**   | Email, in-app, push messages                  |
| **Search Service**         | Full-text and semantic search                 |
| **Admin Panel**            | Internal UI to manage assets, ban, flag, etc. |

### ✅ 3.4. **Video Processing Pipeline**

| Stage                   | Tool/Tech                                     |
| ----------------------- | --------------------------------------------- |
| **Ingest**              | Upload via studio tools / encoder agents      |
| **Transcode**           | FFmpeg, AWS MediaConvert (H.264, VP9, AV1)    |
| **Packaging**           | MPEG-DASH, HLS (multiple bitrates)            |
| **Encryption/DRM**      | Widevine, PlayReady, FairPlay                 |
| **Thumbnail Generator** | Sample preview stills, scene detection        |
| **Metadata Extractor**  | Duration, codec, language, resolution         |
| **Upload to CDN**       | Final media pushed to Open Connect appliances |

### ✅ 3.5. **Playback & Streaming (Open Connect CDN)**

| Layer                    | Function                                            |
| ------------------------ | --------------------------------------------------- |
| **Video CDN**            | Netflix-owned edge appliances in ISPs worldwide     |
| **Segmented Streaming**  | Chunks (e.g., 5 sec) in 144p–4K encoded resolutions |
| **Adaptive Bitrate**     | Player chooses bitrate based on device + network    |
| **Signed URLs / Tokens** | Anti-piracy, geo-restriction enforcement            |
| **Fallback Mechanisms**  | Retry from another CDN, another resolution          |
| **Edge Metrics**         | Rebuffer rate, stall time, throughput reporting     |

### ✅ 3.6. **Recommendation Engine**

| Subsystem                    | Description                                |
| ---------------------------- | ------------------------------------------ |
| **User Embedding Generator** | Collaborative filtering via watch behavior |
| **Ranking Pipeline**         | Ranks candidates for homepage rows         |
| **Artwork Personalization**  | Changes thumbnails based on interest       |
| **Diversity Filters**        | Ensures varied genres, pacing              |
| **Model Training**           | TensorFlow, PyTorch, Spark ML              |
| **AB Testing Framework**     | Real user buckets, rollout testing         |

### ✅ 3.7. **Billing, Payments & Security**

| Component             | Description                               |
| --------------------- | ----------------------------------------- |
| **Billing Gateway**   | Subscriptions, renewals, invoices         |
| **Payment Processor** | Credit cards, PayPal, Apple/Google Pay    |
| **Fraud Detection**   | Detects shared accounts, bot abuse        |
| **Region Control**    | Geo-locking of titles based on IP/license |
| **Token Service**     | JWT tokens, session refresh               |
| **DRM Key Vault**     | Stores encryption keys for playback       |

### ✅ 3.8. **Analytics, Events & Monitoring**

| Type                    | Tool/Tech                                  |
| ----------------------- | ------------------------------------------ |
| **QoE Metrics**         | Startup delay, rebuffer %, bitrate changes |
| **Real-time Events**    | Kafka, Flink, Spark Streaming              |
| **Playback Logs**       | Watched %, skipped intro, resume points    |
| **A/B Testing Results** | User splits, conversion funnels            |
| **Security Logs**       | Device registration, token misuse          |
| **Alerting Systems**    | Sentry, Prometheus, custom tools           |

### ✅ 3.9. **Storage Systems**

| Data Type            | Storage                                     |
| -------------------- | ------------------------------------------- |
| **Video Segments**   | S3 / Glacier → Open Connect CDN             |
| **User Metadata**    | MySQL / CockroachDB / Spanner               |
| **Playback State**   | Redis / DynamoDB                            |
| **Telemetry Events** | Kafka → S3 / BigQuery                       |
| **Recommendations**  | Precomputed and stored in Redis / Cassandra |
| **DRM Keys**         | HSMs or KMS vaults                          |

## 🧪 4. **User Flow: Browse → Watch**

```plaintext
1. User opens app
2. API Gateway → Recommendation Service
   - Returns personalized rows
3. User selects a title
4. Playback Service:
   a. Authenticates session
   b. Fetches license (DRM)
   c. Returns signed HLS/DASH URLs
5. Player streams video from CDN (closest Open Connect node)
6. Client sends telemetry (buffering, stalls)
7. Progress Tracker records position
```

## 🌍 5. **Deployment & Scaling**

| Layer                  | Strategy                                            |
| ---------------------- | --------------------------------------------------- |
| **CDN (Open Connect)** | Distributed globally in major ISPs                  |
| **API Services**       | Autoscaled in AWS (ECS/K8s)                         |
| **Kafka Clusters**     | Global, zonal clusters for ingestion                |
| **Metadata Stores**    | Regionally sharded + replicated                     |
| **Recommendations**    | Pre-baked results per user for low-latency delivery |
| **Playback State**     | Redis for fast resume/sync                          |
| **Search**             | Elasticsearch / Pinecone for vector similarity      |

## 🔐 6. **Security & Rights Enforcement**

| Concern             | Solution                                  |
| ------------------- | ----------------------------------------- |
| **DRM Enforcement** | Widevine, FairPlay, PlayReady             |
| **Token Abuse**     | Short TTLs, device fingerprints           |
| **Content Piracy**  | Watermarking, fingerprinting, signed URLs |
| **Geo-restriction** | Based on IP + license metadata            |
| **Account Sharing** | Device limits, ML fraud detection         |
| **Billing Fraud**   | Velocity limits, card fingerprinting      |

## 📊 System Diagram (Text-Based)

```
+-------------------+        +------------------------+        +-------------------------+
|  Client (TV/Web)  | <--->  |     API Gateway        | <--->  |   Core Microservices   |
+-------------------+        +------------------------+        |-------------------------|
                                                               | - Catalog Service       |
                                                               | - Playback Service      |
                                                               | - Subscription Service  |
                                                               | - Recommendation Engine |
                                                               | - Progress Tracker      |
                                                               +------------+------------+
                                                                            |
                     +-------------------- Kafka (Telemetry, Playback) ---------------------+
                     |                    |                     |                         |
                     v                    v                     v                         v
             +----------------+   +----------------+     +----------------+       +----------------+
             | Video Pipeline |   | Analytics Store|     | AB Testing     |       | Billing System |
             +----------------+   +----------------+     +----------------+       +----------------+

                     +----------------------------+
                     | Open Connect CDN (Video)   |
                     +----------------------------+

                     +----------------------------+
                     | DRM / Token / Key Vault    |
                     +----------------------------+

                     +----------------------------+
                     | Redis (Playback Resume)    |
                     +----------------------------+

```

## 🧠 Special Considerations

| Feature                   | Implementation                                            |
| ------------------------- | --------------------------------------------------------- |
| **Multi-profile support** | Separate recommendation + playback state per profile      |
| **Skip Intro**            | ML detects intro boundaries via waveform/video analysis   |
| **Offline Downloads**     | Encrypted files, limited duration/license keys            |
| **4K / Dolby / Atmos**    | Specific encodings, device detection                      |
| **Global Rollouts**       | Canary deploys, phased regional releases                  |
| **High Availability**     | Zone-aware services + retry logic across failover regions |
