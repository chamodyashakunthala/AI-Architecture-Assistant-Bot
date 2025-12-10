1. Introduction

The AI Architecture Assistant Tool is designed to help students, junior developers, and architects generate system architectures, diagrams, and design decisions using a rule-based chatbot engine.

This document describes the system’s architecture, components, and data flow.

2. Goals

Generate high-level software architectures (3-tier, microservices, monolith, etc.)

Generate ASCII-style diagrams (class, sequence, architecture sketches)

Recommend design patterns

Propose basic database designs

Provide an interactive chat UI

3. System Overview

The system consists of:

Chatbot NLP Engine – Detects intents from the user message

Architecture Engine – Generates architectures, diagrams, patterns, and ER designs

Backend API – FastAPI/Flask service exposing /chat

Frontend UI – Web interface that interacts with the chatbot

Integration Layer – Frontend → Backend → Architecture Engine

4. High-Level Architecture
   +-----------------+        +---------------------+        +--------------------------+
|     Frontend    | -----> |      Backend API    | -----> |   Architecture Engine    |
|  (React UI)     |        |    (FastAPI/Flask)  |        |  (Python modules)        |
+-----------------+        +---------------------+        +--------------------------+
                                          |
                                          v
                                 +------------------+
                                 |  NLP Engine      |
                                 +------------------+
5. Module Breakdown
5.1 Chatbot NLP Engine

Cleans text

Detects keywords

Classifies intents

Routes to correct handler

Files:
  chatbot/
   nlp_engine.py
   chatbot_core.py
   intents/

 5.2 Architecture Engine

Handles all domain logic:
   architecture_engine/core/
   architecture_generator.py
   diagram_generator.py
   pattern_advisor.py
   database_designer.py

5.3 Backend API

/chat endpoint

Calls Chatbot Core

Returns JSON

Stateless

5.4 Frontend UI

Chat bubble interface

Sends text → backend

Displays response

6. Design Decisions

Rule-based NLP (simple, explainable)

Modular architecture (separation of concerns)

Lightweight ASCII diagrams (no heavy visualization libraries)

Simple REST API for communication

7. Limitations

No machine learning model

Diagrams are text-based

Only supports predefined intents

8. Future Improvements

Add LLM-based NLP

Add UML diagram image generation

Add pattern visualization

Allow exporting architecture documents automatically
