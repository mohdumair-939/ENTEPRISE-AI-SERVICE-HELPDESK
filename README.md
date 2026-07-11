# Enterprise AI Service Desk

Academic Title:
Smart Help Desk Ticketing System for IT Services

## Overview

Enterprise AI-powered IT Service Desk using

- FastAPI
- React
- PostgreSQL
- Gemini
- LangChain
- ChromaDB
- Docker
- AWS
## Architecture
                           Employee
                               │
                               ▼
                     React + TypeScript Frontend
                               │
                        HTTPS / REST APIs
                               │
                               ▼
                     FastAPI Backend (Python)
                               │
       ┌──────────────┬────────┼────────────────────┬
        ▼             ▼        ▼                    ▼
PostgreSQL     Redis       AI Engine           Monitoring
(Database)     (Cache)     (LangChain)        (Prometheus)
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
      Gemini API           ChromaDB           ML Engine
      (LLM)             (Vector Database)   (Scikit-Learn)
          │                    │
          └───────────────────RAG────────────────┘
                               │
                        Multi-Agent System
                               │
          ┌─────────────┬─────────────┬─────────────┐
          ▼             ▼             ▼             ▼
      Network       Security      Database      Cloud
       Agent          Agent         Agent        Agent
                               │
                               ▼
                     Dashboard & Analytics


## Setup



## Contributors

Mohd Umair  
T. Meghana 
P.S.S.A Karthikeya 
