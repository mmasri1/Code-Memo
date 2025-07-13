# ✅ STEP 5: High-Level Architecture — **YouTube**

We’re designing a **globally distributed video platform** like YouTube, supporting:

* Video uploads & processing (compression, encoding, thumbnails)
* Video streaming (adaptive bitrate)
* Subscriptions, notifications, comments
* Real-time analytics
* Ads & monetization
* Live streaming
* Billions of users and petabytes of content

## 🔧 1. **Key Architectural Principles**

| Principle                         | Description                                    |
| --------------------------------- | ---------------------------------------------- |
| **Service-Oriented Architecture** | Media, metadata, comments, ads, etc. decoupled |
| **Edge Caching/CDN**              | Deliver videos with minimal latency            |
| **Pub/Sub (Kafka)**               | For decoupling video events, views, uploads    |
| **Batch + Streaming Analytics**   | Real-time + offline recommendations, stats     |
| **Scalable Storage**              | Blob stores, metadata DBs, search engines      |
| **Asynchronous Workflows**        | Upload → Transcode → Store → Notify            |

## 🧩 2. **System Overview (High-Level)**

We divide YouTube into:

* **Client Layer**
* **API Gateway**
* **Core Backend Services**
* **Video Processing Pipeline**
* **Delivery/Streaming Infrastructure**
* **Search & Recommendation Engines**
* **Analytics & Ads Pipeline**
* **Storage Layers**

## 📦 3. **Component Breakdown**

### ✅ 3.1. **Client Layer (Web, iOS, Android, TV)**

* Upload, browse, search, stream videos
* Local buffering & ABR (adaptive bitrate streaming)
* Communicates via REST/gRPC & WebSockets
* Implements playback analytics (view %, pause, skip, etc.)

### ✅ 3.2. **API Gateway**

* Rate limiting, authentication, routing
* Request routing to services: search, comments, video info, etc.
* Tracks session tokens (JWT or OAuth)

### ✅ 3.3. **Core Backend Services**

| Service                    | Purpose                                         |
| -------------------------- | ----------------------------------------------- |
| **User Service**           | Profile, channels, subscriptions                |
| **Video Service**          | Metadata, privacy, state (processing/published) |
| **Upload Service**         | Handles multipart/resumable uploads             |
| **Playback Service**       | Generates playback URLs & tokens                |
| **Comment Service**        | Stores threaded comments, likes                 |
| **Notification Service**   | Notifies subscribers, creators                  |
| **Monetization Service**   | Tracks watch-time, eligibility, revenue         |
| **Live Streaming Service** | WebRTC/RTMP ingestion and broadcast             |
| **Admin & Moderation**     | Abuse detection, content flags                  |

### ✅ 3.4. **Video Processing Pipeline**

| Stage                    | Tool/Tech                                                         |
| ------------------------ | ----------------------------------------------------------------- |
| **Upload**               | Multipart resumable (HTTP/S3-like)                                |
| **Queue**                | Kafka topic for `video_uploaded`                                  |
| **Transcoding**          | FFmpeg-based workers, encode to multiple resolutions (144p to 4K) |
| **Thumbnail Generation** | Frame sampling (FFmpeg) + face/scene detection                    |
| **Metadata Extraction**  | Duration, resolution, audio bitrate, etc.                         |
| **Storage**              | Encoded chunks → S3/GCS + CDN edge cache                          |
| **Publish Event**        | Message sent to `video_ready` topic → notify, index               |

### ✅ 3.5. **Streaming & Delivery**

| Component               | Role                                                    |
| ----------------------- | ------------------------------------------------------- |
| **CDN**                 | Cloudflare, Akamai, or custom CDN (Google Global Cache) |
| **Chunked Streaming**   | HLS / DASH formats, adaptive bitrate                    |
| **Signed URLs**         | Time-limited, anti-hotlink                              |
| **Edge Load Balancers** | Serve closest replica to the user                       |
| **Pre-Fetching Layer**  | Prefetch next few seconds of video proactively          |
| **Live Edge Nodes**     | For real-time broadcasts (WebRTC or HLS live)           |

### ✅ 3.6. **Search & Recommendation Engines**

| System                        | Description                                                       |
| ----------------------------- | ----------------------------------------------------------------- |
| **Search Indexer**            | Elasticsearch or custom engine, indexes titles, tags, transcripts |
| **Trending Engine**           | Based on views, geo, social signals                               |
| **Watch History Graph**       | User-video similarity using collaborative filtering               |
| **ML Ranking Engine**         | TensorFlow/PyTorch-based personalized model                       |
| **Experimentation Framework** | A/B test rec algorithms per user/session                          |

### ✅ 3.7. **Analytics Pipeline**

| Type                 | Tool/Tech                         |
| -------------------- | --------------------------------- |
| **Real-time Events** | Kafka + Flink/Spark Streaming     |
| **Batch Processing** | Daily rollups in Hive/Snowflake   |
| **User Metrics**     | Watch time, CTR, bounce rate      |
| **Ad Metrics**       | Impression, clicks, revenue split |
| **Data Lake**        | Raw logs stored in S3/Parquet     |

### ✅ 3.8. **Ads & Monetization**

* Ads inserted based on:

  * User history, video category, CPM
  * Creator eligibility, location
* Auctions occur in real time (\~100ms)
* Ad video segments streamed with main video
* Payments to creators stored in revenue service

### ✅ 3.9. **Storage Systems**

| Data Type               | Storage                                    |
| ----------------------- | ------------------------------------------ |
| **Video Blobs**         | S3 / GCS (multi-region replication)        |
| **Thumbnails**          | S3 / CloudFront                            |
| **Metadata**            | MySQL / Spanner (videos, users, playlists) |
| **Comments**            | Cassandra or MongoDB                       |
| **Cache**               | Redis / Memcached                          |
| **Search Index**        | Elasticsearch / Lucene                     |
| **Logs & Analytics**    | S3 → Hive/Snowflake                        |
| **Graph DB (optional)** | Neo4j for social/subscription graphs       |

## 🧪 4. **Video Upload → View Flow**

```plaintext
1. User uploads video (multipart)
2. Upload Service stores raw video in temp bucket
3. Kafka publishes `video_uploaded`
4. Worker picks up:
   - Transcodes to 240p, 360p, 720p, 1080p, etc.
   - Extracts metadata, generates thumbnails
5. Stores processed videos in permanent blob storage
6. Video Service updates status → "ready"
7. Notifies followers/subscribers
8. CDN distributes chunks to edge nodes
9. Viewer requests video:
   - Playback Service returns signed chunk URLs
   - Video streamed via HLS/DASH
```

## 🌍 5. **Deployment Strategy**

| Layer                    | Strategy                                     |
| ------------------------ | -------------------------------------------- |
| **Upload/Processing**    | Centralized (optimized for write throughput) |
| **Playback/CDN**         | Edge-located for proximity                   |
| **Metadata DB**          | Region-replicated (Spanner style)            |
| **Live Chat / Comments** | Sharded by video ID                          |
| **Cache**                | Redis instances close to CDNs                |
| **Kafka Clusters**       | Separated for events, analytics, processing  |

## 🔐 6. **Security & Abuse Protection**

| Area                   | Tooling                                               |
| ---------------------- | ----------------------------------------------------- |
| **Upload Validation**  | Virus scanning, size/type limits                      |
| **DMCA & Copyright**   | Content ID matching                                   |
| **Comment Moderation** | Auto-filters, spam ML models                          |
| **Anti-Hotlinking**    | Signed URLs, user-based throttling                    |
| **Account Security**   | 2FA, CAPTCHA, login throttling                        |
| **Child Protection**   | Age restrictions, face detection, audio content scans |

## 📊 System Diagram (Detailed - Text-Based)

```
+-----------------+       +-------------------+       +----------------------+
| Client (Web/iOS)| <-->  |    API Gateway    | <-->  |   Core Services      |
+-----------------+       +-------------------+       |----------------------|
                                                     | User Service         |
                                                     | Video Service        |
                                                     | Upload Service       |
                                                     | Comment Service      |
                                                     | Notification Service |
                                                     +----------+-----------+
                                                                |
                                                                v
     +------------------ Kafka: video_uploaded --------------------------+
     |                                                                 |
     v                                                                 v
+---------------------+                                   +----------------------+
| Transcode Workers   | -- FFmpeg, GPU optimized --→      | Thumbnail Generator |
+---------------------+                                   +----------------------+
        |                                                          |
        v                                                          v
+---------------------+                                  +------------------------+
| Video Blob Storage  | <------------------------------+ | Metadata Extractor     |
| (S3 / GCS)          |                                  +------------------------+
+---------+-----------+
          |
          v
  +---------------------+         +---------------------+
  |   CDN Edge Nodes    |  <--->  |   Playback Service   |
  +---------------------+         +---------------------+
                                         |
         +----------------------+        v
         | Search + Recommend   | <----+ User profile, history
         +----------------------+

```

## 🧠 Additional Design Considerations

* **Storage Tiering**: Hot vs cold video tiers (frequently vs rarely accessed)
* **Previews**: Tiny GIF previews stored separately for hover-thumbnails
* **Streaming Optimization**: Start with low bitrate, then upgrade
* **Live Chat**: Separate microservice, scaled independently
* **Multi-CDN Strategy**: Fall back between providers (Cloudflare, Akamai)
