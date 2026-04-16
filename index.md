# Code-Memo

#### Personal Notes

make a big collection:
1. software engineering concepts
2. system design
3. python + django + drf (+ some libraries)
4. dsa + leetcodes

### To Learn (Quick Notes)

CI/CD (all questions about it, theoretically)
SQL
caching & Queues (Redis, Celery/RQ)
testing (Pytest, unittest)
distributed systems
database: optimization, indexing, and sharding
auth flows
code review
mentoring juniors
architecture discussion
performance optimization (py, dj)
failure tolerance
debugging
discuss trade offs (ALL (sql vs nosql, db choices))
microservices vs. monoliths + other architectures
event-driven architecture, pub/sub systems
service mesh, API gateways
message queues (Kafka, RabbitMQ)
learn in more details Docker, Kubernetes (how to's + questions)
Data modeling and indexing
Data consistency and migration (how to)
caching and message brokers (Redis, Memcached, RabbitMQ)
background tasks (Redis, Celery)
how a system fails safely (no unhandeled exceptioned,  logging,.. add to docs and tests)
django and API security
prepare tech theoretical questions like: when do you consider refactoring
prepare 6–8 solid stories: include challenges, leadership, conflict, failure, success, growth
why would you use ....... (reverse proxy)
master slave in distributed system
microservice: does ONE job, a single business unit
load balancer: top algo + some jobs like monitoring and logging
how do you actually do horz and vert scaling??? (aws)
how to actually do a loadbalancer??? (aws ec2)
usages of api gateway?
when to horiz vs vert scaling???? discuss tradeoffs
actually learn MQ: RabbitMQ, kafka etc (AND similar services)
WHY monolith vs microservice?? (+ other designs)
-> prolly mononith is faster cause no comm, but microservices doesn't crash all. microservices are harder to design but way easier to scale
stackoverflow: mono, facebook: micro
learn tradeoffs of all decisions
DB sharding
how would you query: optimize the query, indexing, sharding
horizontal portioning...
how to ACTUALLY cache (redis and other tools) + algos
fan out (events)
event driven system
publisher subscriber model
write ahead logs HOW TO DO
indexing a db in details??
deepening info: image saved as file vs blob? discuss tradeoffs
weird questions like: can you use cdn on ssr
when to use nosql db?
data replication
context managers in programming
prepare interview questions for all like Django and DRF
prepare SE and SYS DES questions like What’s the bottleneck at 10M QPS?
Why Redis over Memcached? TRADEOFFS (online status: redis (mem) or db?)
microserv inside microserv?? socials has chat
we always have api gateway, can we use that as load balancer?
try grpc (and try microservices in fastapi)
list of all Sys des questions ("How would you allow image uploads in a scalable way?")
performance and reliability trade-offs
db design: sql (syntax) and modeling techniques (norms)
devops things
debugging and testing tips
some frontend knowledge
git and managing conflicts
advanced topics like : LRU cache, Trie, Custom decorators, generators
writing clean docs (and comments)
cicd (nginx, jenkins, github actions)
STAR method for behaviorals
how to Justify choices in system design

### Soft Skills

Team Work
Branding
Public Speaking
Think Creatively in Business
Lead Teams to Success
Set Goals & Manage Time Effectively
Project Management
Personal Productivity
Emotional Intelligence
Digital Transformation
Business Strategy
Conflict Management
Leadership
Sales Negotiation
Financial Literacy + Accounting
Budgeting + Forecasting
Marketing
Project Management
Product Management
Business Strategy + Analysis
Management Skills
Communication Skills
Presentation Skills
Public Speaking
Writing
Business Communication
Business Writing
Email Writing and Etiquette
SQL
Microsoft Power BI
Data Analysis
Business Analysis
Tableau
Data Visualization
Data Modeling
-prepare all sorta questions about DAF-
also about contributing to cpython


#### Code Memo

Welcome to my [Code Memo](https://mmasri1.github.io/Code-Memo/)! I forget a lot! So I created this simple project, which is a collection of my notes on various programming topics, including Python, Django, Django REST Framework (DRF), algorithms and data structures (maybe some leetcode problems), and Linux. This serves as my personal reference to help me recall concepts quickly. I hope you find it useful as well.

## Table of Contents

1. [Python](/python.md)
2. [Data Structures and Algorithms](/dsa.md)
3. [Django and Django REST Framework (DRF)](/django.md)
4. [Software Engineering Principles](/sep.md)
5. [System Design and Architecture](/system-design.md)
6. API Design ⏳
7. [Misc](/misc.md)
8. [Mentorship Notes](/mentorship-notes.md)
9. [Today I Learned - DAF 🔥](/daf-today-i-learned.md)

<p>
  <a href="#" onclick="randomPage();" style="text-decoration:none;">
    <button style="padding:10px 15px; font-size:14px; color:white; background-color:#007BFF; border:none; border-radius:5px; cursor:pointer;">
      Take Me to a Random Page &nbsp; 🎲
    </button>
  </a>
</p>

<script>
  async function randomPage() {
    try {
      const response = await fetch('pages.json');
      const data = await response.json();
      
      if (data.pages.length > 0) {
        let randomPage = data.pages[Math.floor(Math.random() * data.pages.length)];
        
        randomPage = randomPage.replace(/\.md$/, '');

        window.location.href = randomPage;
      } else {
        console.error("No pages found");
      }
    } catch (error) {
      console.error("Error fetching pages:", error);
    }
  }
</script>

<br>

Note: This project is a bunch of personal notes. While you may find them useful, it's intended more as a quick reference rather than a learning resource, ideal for a brief review 5 minutes before your next interview :D

Feel free to explore each section and make use of the information as needed. If you have any suggestions or contributions, please don't hesitate to create a pull request or open an issue.

And don't forget to take notes! ❤️

Version: 3.2.2