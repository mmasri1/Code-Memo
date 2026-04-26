# Django

Hi Djangonauts! And welcome to my Django notes, all about the web framework for **perfectionists** with **deadlines** 🤌

Django's philosophy is centered on the principles of rapid development, clean and pragmatic design, and the "don't repeat yourself" (DRY) principle.

When building a large database-driven application, I would honestly pay to use Django.

Django follows the "**Batteries included**" philosophy and provides almost everything developers might want to do "**out of the box**". Because everything you need is part of the one "product", it all works seamlessly together, follows consistent design principles, and has extensive and up-to-date documentation.

With around [10](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset) [lines](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer) of code I get `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` API endpoints for any DB table normalised into clean consistent formats, with proper status codes, proper exceptions, throttling, permissions (per user, per object, e.t.c), are browsable, easy to document, and all the other good stuff that proper APIs should have. 🙌 🔥

## Quick Docs 📗

## Introduction

1. [Setting Up a Django Project](django/project-sample)
2. [Apps and Project Structure](django/apps-and-project-structure)
3. [Django Admin Interface](django/admin-interface)
4. [URL Routing and Configuration](django/url-routing-and-configuration)

### Models

1. [Defining Models](django/defining-models)
2. [Model Fields](django/model-fields)
3. [Model Methods](django/model-methods)
4. [Model Meta Options](django/model-meta-options)
5. [Model Inheritance](django/model-inheritance)
6. [Model Migrations](django/model-migrations)
7. [Relationships (OneToOne, ManyToMany, ForeignKey)](django/relationships)

### Queries

1. [Creating Queries](django/creating-queries)
2. [QuerySets](django/querysets)
3. [Field Lookups](django/field-lookups)
4. [Query Expressions](django/query-expressions)
5. [Complex Lookups](django/complex-lookups)
6. [Aggregation and Annotation](django/aggregation-annotation)

### Views

1. [Function-Based Views (FBVs)](django/fbvs)
2. [Class-Based Views (CBVs)](django/cbvs)
3. [Generic Views](django/generic-views)
4. [Mixins](django/mixins)
5. [Handling Requests and Responses](django/requests-responses)

### Authentication

1. [User Authentication and Authorization](django/user-authentication-and-authorization)
2. [Password Management](django/password-management)
5. [User Registration](django/user-registration)
6. [Permissions and Groups](django/permissions-and-groups)

### Middleware

1. [Understanding Middleware](django/understanding-middleware)
2. [Built-in Middleware](django/built-in-middleware)
3. [Custom Middleware](django/custom-middleware)

### Advanced Topics

1. [Signals](django/signals)
2. [Caching](django/caching)
3. [Sessions](django/sessions)
4. [Environment Variables and Secret Keys](django/environment-variables-and-secret-keys)
5. [Internationalization and Localization](django/internationalization-and-localization)
6. [Management Commands](django/management-commands)
7. [Asynchronous Views](django/asynchronous-views)
8. [Working with Databases (Other than SQLite)](django/working-with-databases)
9. [Custom User Models](django/custom-user-models)
10. [Security Best Practices](django/security-best-practices)

### Testing

1. [Writing and Running Tests](django/writing-and-running-tests)
2. [Testing Tools and Libraries](django/testing-tools-and-libraries)
3. [Testing Models, Views, and Forms](django/testing-models-views-forms)
4. [Using the Django Test Client](django/using-django-test-client)

### Deployment

1. [Deployment Checklist](django/deployment-checklist)
2. [Deploying with WSGI](django/deploying-with-wsgi)
3. [Deploying to AWS (Elastic Beanstalk, EC2)](django/deploying-to-aws)
4. [Using Docker with Django](django/docker-with-django)
5. [Setting Up CI/CD](django/setting-up-cicd)

### Performance Optimization

1. [N+1 Query Problem](django/n+1-query-problem)
2. [Query Optimization](django/query-optimization)
3. [Using Django Debug Toolbar](django/using-django-debug-toolbar)
4. [Database Indexing](django/database-indexing)
5. [Profiling and Monitoring](django/profiling-and-monitoring)

### Best Practices

1. Project Structure and Organization
2. Code Quality and Style Guides
3. Documentation Practices
4. Security Best Practices
5. Maintaining Django Projects

# Django Rest Framework (DRF)

[Why DRF ?? 💡](django/why-drf)

#### DRF Basics

1. [Creating a Simple API](django/creating-a-aimple-api)
2. [Requests](django/requests)
3. [Responses](django/responses)

#### Views

1. Function-Based Views (FBVs) in DRF
2. Class-Based Views (CBVs) in DRF
3. ViewSets and Routers
4. [API Views](django/apiview)
5. [Generic Views](django/generic-view)
6. Mixins

#### Serializers

1. Understanding Serializers
2. ModelSerializers
3. Serializer Fields
4. Validations and Validators
5. Custom Serializers
6. Nested Serializers

#### Routers

1. SimpleRouter
2. DefaultRouter
3. Custom Routers

#### Authentication and Permissions

1. Authentication in DRF
2. Token Authentication
3. Session Authentication
4. OAuth2 with Django OAuth Toolkit
5. Custom Authentication
6. Permission Classes
7. Object-Level Permissions
8. [Custom Permissions and Roles](django/custom-permissions-and-roles)

#### Throttling

1. Understanding Throttling
2. Built-in Throttling Classes
3. Custom Throttling

#### Pagination

1. Pagination in DRF
2. Built-in Pagination Classes
3. Custom Pagination

#### Filtering, Searching, and Ordering

1. Filtering in DRF
2. DjangoFilterBackend
3. SearchFilter
4. OrderingFilter
5. Custom Filters

#### Versioning

1. Understanding API Versioning
2. URL Path Versioning
3. Host Name Versioning
4. Query Parameter Versioning
5. Accept Header Versioning

#### Content Negotiation

1. Understanding Content Negotiation
2. Media Types
3. Custom Content Negotiation

#### Testing

1. Testing DRF APIs
2. Using DRF's APIClient
3. Testing Serializers
4. Testing Views and ViewSets

#### Advanced Topics

1. Hyperlinked APIs
2. API Documentation with DRF (Swagger)
3. Rate Limiting
4. Asynchronous Views with Django Channels
5. Using WebSockets with DRF

#### Misc

1. [Uploading Images](drf/uploading-images)

#### Best Practices

1. Structuring DRF Projects
2. Writing Clean and Maintainable Code
3. Security Best Practices for DRF
4. Documentation Practices for APIs
5. Maintaining DRF Projects

<br>

# Django Auditlog

<i>Nothing to see here yet</i>

<br>

# DRF Spectacular

<i>Nothing to see here yet</i>

<br>

# Channels and WebSockets

<i>Nothing to see here yet</i>

<br>

# Graphene (GraphQL)

<i>Nothing to see here yet</i>
<br>

# Django-Ninja

<i>Nothing to see here yet</i>
