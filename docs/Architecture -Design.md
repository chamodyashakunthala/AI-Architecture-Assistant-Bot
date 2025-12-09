Project: AI Architecture Assistant — Chatbot for Software Architecture Guidance

Overview

This document describes the system architecture for the AI Architecture Assistant — a rule-based, lightweight-NLP chatbot that helps users design software architecture by recommending patterns, generating diagrams, identifying actors and use-cases, and producing exportable documentation.

1. Chosen Architecture Style

Hybrid: Modular + Layered architecture (default)

Rationale:

A layered design separates concerns (Presentation, Application/Domain, Rules/Inference, Persistence). This simplifies development and testing.

A modular approach groups related functionality (NLP, Rule Engine, Diagram Generator, Exporter) into replaceable modules.

This hybrid gives clear separation of responsibilities while keeping the system lightweight and easy to extend (no full microservices complexity required at first). If scale requires, modules can later be split into microservices.

2. System Components (Definitions & Responsibilities)

User Interface (UI)

Web-based front-end where users type project descriptions, see recommendations, view and export diagrams and docs.

Responsibilities: accept natural language input, show results, allow refinements, present export options.

API Layer / Controller

Thin layer receiving UI requests and routing them to internal modules; handles validation and orchestration.

NLP Parser

Lightweight NLP that tokenizes user input, extracts keywords, intents, entities (system type, domain terms, constraints), and maps those to internal canonical forms.

Uses rule-driven patterns and simple ML (optional) for intent classification.

Project Classifier

Determines project type (web, mobile, embedded, enterprise, data-intensive) and recommended quality priorities (e.g., performance vs. consistency).

Rule-Based Inference Engine (Architecture Recommendation Engine)

Core of the system. Contains predefined rule-sets mapping project characteristics to architecture patterns, components, and quality attribute suggestions.

Supports rule editing via Admin Panel.

Component/Model Generator

Based on inference results, suggests actors, use cases, classes, entities, and relationships.

Produces structured outputs (JSON) representing diagrams.

Diagram Generator

Converts structured outputs to human-readable diagrams (Mermaid and/or PlantUML text). Keeps diagrams simple so rendering is optional.

Types: Use Case Diagram, High-level System Diagram, Context Diagram, Class Diagram, ERD, Sequence/Flow Diagrams.

Exporter

Produces downloadable artifacts: Markdown, PDF, DOCX, and raw diagram text (Mermaid/PlantUML).

Knowledge Base (Rule Store + Ontology)

Stores the rules, templates, and mapping tables used by the inference engine and NLP parser.

Versioned so admins can rollback and update.

Storage & Logging

Stores user sessions, logs, and anonymized analytics to improve rule coverage. Must avoid storing sensitive personal data.

Admin Panel

Allows architects to edit rule-sets, update templates, review logs, and manage exports.

Optional Integrations

External diagram rendering services, authentication provider (OAuth), cloud file storage (S3), and VCS (Git) to export artifacts into a repo.

3. High-level Module Interaction

UI → API Controller → NLP Parser → Project Classifier → Inference Engine → Component Generator → Diagram Generator → Exporter

Admin operations (edit rules) happen via Admin Panel → Knowledge Base → Inference Engine

Logging/Storage records each step for audit and improvement.
