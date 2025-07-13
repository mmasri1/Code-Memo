# ✅ STEP 5: High-Level Architecture — **Amazon (E-Commerce Platform)**

We’ll design for:

* Product listings
* Cart & checkout
* Payments
* Order management
* Search
* Recommendations
* Reviews
* High availability and global scale

## 🔧 1. **Key Architectural Principles**

| Principle                 | Purpose                                             |
| ------------------------- | --------------------------------------------------- |
| **Microservices**         | Separate concerns: search, cart, orders, etc.       |
| **Event-Driven**          | Decouple checkout, payments, notifications          |
| **CQRS**                  | Use separate read/write models for scalability      |
| **Geo-Sharded**           | Data and traffic split by region                    |
| **Eventually Consistent** | Allow eventual sync where strict ACID is not needed |
| **High Availability**     | Fault-tolerant, replicated services and storage     |

## 🧩 2. **System Overview**

Major domains:

* **Client Layer**
* **API Gateway**
* **Core Backend Services**
* **Product Catalog & Inventory**
* **Search & Recommendations**
* **Order Processing Pipeline**
* **Payment & Billing**
* **Notifications & Reviews**
* **Infra & Storage**

## 📦 3. **Component Breakdown**

### ✅ 3.1. **Client Layer**

| Platform          | Function                                       |
| ----------------- | ---------------------------------------------- |
| Web, iOS, Android | Browse, search, add to cart, checkout          |
| Admin Panels      | Seller portals, inventory mgmt, order tracking |

### ✅ 3.2. **API Gateway**

* Auth (OAuth2/JWT)
* Request routing
* Rate limiting
* A/B testing and feature flags

### ✅ 3.3. **Core Backend Services**

| Service               | Description                                       |
| --------------------- | ------------------------------------------------- |
| **User Service**      | User profiles, addresses, preferences             |
| **Product Service**   | Product metadata, categories, variations          |
| **Inventory Service** | Tracks real-time stock availability               |
| **Cart Service**      | Add/update/remove items                           |
| **Checkout Service**  | Validates cart, reserves stock, creates order     |
| **Order Service**     | Tracks order state (placed → shipped → delivered) |
| **Payment Service**   | Handles card/wallet/EMI integrations              |
| **Shipment Service**  | Assigns carriers, tracks deliveries               |
| **Review Service**    | Stores reviews, verifies purchases                |
| **Seller Service**    | Merchant data, pricing, offers, compliance        |
| **Promotion Service** | Coupons, lightning deals, Prime offers            |

### ✅ 3.4. **Product Catalog & Inventory**

| Component           | Description                                                 |
| ------------------- | ----------------------------------------------------------- |
| **Catalog DB**      | Stores product metadata (title, description, price, images) |
| **Inventory DB**    | Real-time stock per SKU/warehouse                           |
| **Image CDN**       | Optimized image delivery via CloudFront/S3                  |
| **Versioned Index** | Supports rollback during updates                            |

### ✅ 3.5. **Search & Recommendation Systems**

| Subsystem                 | Technology                                |
| ------------------------- | ----------------------------------------- |
| **Search Engine**         | Elasticsearch / OpenSearch                |
| **Auto-suggest Engine**   | Trie or ML-based on history               |
| **Recommendation Engine** | Collaborative filtering + ML              |
| **Trending Engine**       | Real-time + batch analytics               |
| **Personalization**       | Vector embeddings of user-product context |

### ✅ 3.6. **Order Processing Pipeline**

```plaintext
Cart Checkout →
- Validate inventory
- Create Order
- Reserve stock
- Process payment
- Trigger fulfillment
```

| Stage                   | Tool/Tech                                   |
| ----------------------- | ------------------------------------------- |
| **Event Bus**           | Kafka (`order_placed`, `payment_confirmed`) |
| **Fulfillment Service** | Assigns warehouse, prints label             |
| **Packing & Dispatch**  | Tracks via carrier API                      |
| **Order Lifecycle**     | Updates customer, triggers notifications    |
| **Return/Refund**       | Reverse transaction + inventory sync        |

### ✅ 3.7. **Payment & Billing**

| Service             | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Payment Gateway** | Card, wallet, EMI, UPI, etc.                                 |
| **Tokenization**    | Secure vault for card details                                |
| **Fraud Detection** | Heuristics + ML models (e.g. location mismatch, bulk orders) |
| **Ledger Service**  | Tracks debit/credit per transaction                          |
| **Billing Service** | Generates invoices, tax calculations                         |

### ✅ 3.8. **Notifications & Messaging**

* Email, SMS, push (order placed, shipped, etc.)
* Kafka-backed async message triggers
* Delayed retries with exponential backoff
* Firebase (push), Twilio (SMS), SES (email)

### ✅ 3.9. **Storage Systems**

| Data Type       | Storage                              |
| --------------- | ------------------------------------ |
| Product Catalog | MySQL / Spanner                      |
| Inventory       | Redis (real-time) + DB (durable)     |
| Orders          | Cassandra (append-only), or DynamoDB |
| Payments        | SQL + secure vault                   |
| Reviews         | MongoDB / Document DB                |
| Search Index    | Elasticsearch                        |
| Cache           | Redis / Memcached                    |
| Image/Media     | S3 + CDN (CloudFront)                |

## 🧪 4. **User Journey: Browse → Buy**

```plaintext
1. User browses → Product Service
2. Search suggestions → Search Service
3. Adds to cart → Cart Service (stored in Redis)
4. Checkout:
   a. Cart validated
   b. Inventory reserved
   c. Order created
   d. Payment processed
5. Kafka → Fulfillment Service assigns warehouse
6. Shipping scheduled, user notified
7. Kafka → Notification + Analytics + Recommendations
```

## 🌍 5. **Deployment & Scale Strategy**

| Component           | Strategy                                                |
| ------------------- | ------------------------------------------------------- |
| **Product Catalog** | Sharded by product ID prefix                            |
| **Order Services**  | Sharded by region & order ID                            |
| **Kafka**           | Topic-per-domain, regional clusters                     |
| **Payment**         | Global ledger + regional gateways                       |
| **Search**          | Global index per region, merged for cross-border search |
| **Inventory**       | Stored per-warehouse, synced globally                   |
| **CDN**             | Edge caches for images, videos, and product pages       |

## 🔐 6. **Security & Compliance**

| Concern              | Approach                                               |
| -------------------- | ------------------------------------------------------ |
| **PII/PCI Security** | Tokenization, encryption at rest, SOC2 compliant vault |
| **Rate Limiting**    | IP/User based limits on sensitive APIs                 |
| **KYC for Sellers**  | Required by Seller Service                             |
| **Audit Logs**       | Append-only event store per user/session               |
| **Data Retention**   | Configurable per region (GDPR, CCPA)                   |

## 📊 System Diagram (Highly Detailed)

```
+-----------------+         +-------------------+         +---------------------------+
|  Client (Web)   | <--->   |    API Gateway    | <--->   | Core Microservices       |
+-----------------+         +-------------------+         |---------------------------|
                                                           | - User Service           |
                                                           | - Product Service        |
                                                           | - Cart Service           |
                                                           | - Inventory Service      |
                                                           | - Order Service          |
                                                           | - Checkout Service       |
                                                           | - Payment Service        |
                                                           | - Review Service         |
                                                           | - Notification Service   |
                                                           +------------+-------------+
                                                                        |
                +------------------ Kafka ------------------------------+
                |                   |                  |               |
                v                   v                  v               v
    +------------------+  +------------------+   +-----------------+  +-----------------+
    | Fulfillment Svc  |  | Analytics Engine |   | Notification Svc|  | Recommendation  |
    +------------------+  +------------------+   +-----------------+  +-----------------+

                           +-----------+         +--------------------+
                           |  Elasticsearch       |  Redis (Inventory, Carts)|
                           +-----------+         +--------------------+

                           +--------------------------------------------+
                           |     S3 + CloudFront (images/media/CDN)    |
                           +--------------------------------------------+
```

## 🧠 Special Design Considerations

| Feature                 | Note                                                  |
| ----------------------- | ----------------------------------------------------- |
| **Prime System**        | Different shipping rules, filters, seller eligibility |
| **Lightning Deals**     | Queued inventory slots, auto-start/stop               |
| **Currency & Locale**   | Prices, languages, units localized                    |
| **Multi-vendor Orders** | Split order across multiple sellers/warehouses        |
| **Retry Logic**         | Payment, email failures handled via retries           |
