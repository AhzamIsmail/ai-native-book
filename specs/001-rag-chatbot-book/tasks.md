# Tasks: Integrated RAG Chatbot for AI-Native Book

**Feature**: Integrated RAG Chatbot for AI-Native Book  
**Spec**: [Link to spec.md](../specs/001-rag-chatbot-book/spec.md)  
**Plan**: [Link to plan.md](../specs/001-rag-chatbot-book/plan.md)  
**Created**: December 13, 2025

## Implementation Strategy

The implementation will follow a phased approach, starting with the most critical user story (Query Full Book Content - P1) which serves as the core functionality. This will establish the foundational components (Cohere integration, Qdrant vector store, basic UI), which can then be extended to support the other user stories (Query User-Specific Text - P2 and PDF Ingestion - P3). Each user story will be implemented with its dependent components and independently testable.

## Dependencies

- User Story 1 (P1) - Query Full Book Content: Foundation for all other stories
- User Story 2 (P2) - Query User-Specific Text: Depends on P1 (shared RAG infrastructure)
- User Story 3 (P3) - PDF Ingestion: Can be developed in parallel with P1/P2 but needed before full functionality

## Parallel Execution Examples

- Cohere client development can run in parallel with Qdrant setup
- API endpoint development can parallel with Frontend development
- PDF ingestion script can be developed in parallel with RAG service

---

## Phase 1: Setup

- [X] T001 Create project structure with backend directory
- [X] T002 Setup Python virtual environment with Python 3.11
- [X] T003 Create requirements.txt with dependencies (FastAPI, Streamlit, Cohere, Qdrant, Neon, LangChain)
- [X] T004 Create .env.example file with required environment variables
- [X] T005 Create project README.md with setup instructions

## Phase 1.5: Vercel Deployment Preparation

- [X] T014 Create api/main.py in root by moving FastAPI app code from backend/api/main.py
- [X] T015 Ensure all imports in api/main.py are correct for Vercel deployment
- [X] T016 Create vercel.json in root with appropriate build configuration
- [X] T017 Move requirements.txt to root and add mangum dependency

## Phase 2: Vercel Serverless Configuration

- [X] T047 Add Mangum handler to api/main.py for serverless compatibility
- [X] T048 Add CORS middleware configuration to api/main.py
- [X] T049 Ensure uvicorn-specific code is properly isolated for local development

## Phase 3: Vercel Environment Configuration

- [X] T050 Configure COHERE_API_KEY environment variable on Vercel dashboard
- [X] T051 Configure QDRANT_URL environment variable on Vercel dashboard
- [X] T052 Configure QDRANT_API_KEY environment variable on Vercel dashboard
- [X] T053 Configure NEON_DB_URL environment variable on Vercel dashboard
- [X] T054 Confirm all environment variables are correctly set on Vercel

## Phase 4: Foundational Components

- [X] T006 [P] Setup Cohere API client with command-r-plus and embed-multilingual-v3 models
- [X] T007 [P] Setup Qdrant client and create "ai_native_book" collection (1024-dim, Cosine)
- [X] T008 [P] Setup Neon Postgres connection for metadata storage
- [X] T009 [P] Create configuration module with pydantic-settings for .env loading
- [X] T010 [P] Create base data models for Book Content, User Query, User Response, and PDF Document entities

## Phase 5: User Story 1 - Query Full Book Content (Priority: P1)

**Goal**: End-users can ask questions about the book content and receive accurate answers based on the full book text.

**Independent Test**: Users can enter a question about general book content and receive an accurate response that references the correct sections of the book within 5 seconds.

- [X] T011 [US1] Implement vector store module with full search capability
- [X] T012 [US1] Implement RAG service to retrieve, prompt, generate, and extract sources
- [X] T013 [US1] Create FastAPI endpoint POST /api/v1/chat for full-book RAG (top-k=5)
- [X] T014 [US1] Implement response formatting with sources (page number and text)
- [X] T015 [US1] Create Streamlit UI with chat interface for full-book queries
- [X] T016 [US1] Connect Streamlit UI to backend API for full-book queries
- [ ] T017 [US1] Test response time optimization to ensure <5s average
- [ ] T018 [US1] Verify 90%+ accuracy in blind evaluation queries

## Phase 6: User Story 2 - Query User-Specific Text (Priority: P2)

**Goal**: End-users can select specific text within the book interface and ask questions about only that selected text without getting responses influenced by the full book content.

**Independent Test**: Users can select text in the book, ask questions about it, and receive responses based solely on the selected text without irrelevant information from other parts of the book.

- [ ] T019 [US2] Extend vector store module to support filtered search by chunk_ids/pages
- [X] T020 [US2] Update RAG service to support isolated context queries
- [X] T021 [US2] Create FastAPI endpoint POST /api/v1/chat-selected for isolated RAG
- [X] T022 [US2] Implement context isolation to prevent full-book leakage
- [X] T023 [US2] Update Streamlit UI with text selection and isolated query functionality
- [X] T024 [US2] Connect Streamlit UI to backend API for selected-text queries
- [ ] T025 [US2] Verify no context contamination from full-book content during selected-text queries

## Phase 7: User Story 3 - PDF Ingestion and Processing (Priority: P3)

**Goal**: Developers can import new book PDFs into the system so that the RAG functionality works with updated or different book content.

**Independent Test**: Developers can upload a book PDF file and confirm that it has been processed and indexed correctly in the system.

- [X] T026 [US3] Create PDF ingestion script using PyPDF or similar library to load book content
- [X] T027 [US3] Implement text splitting using LangChain RecursiveCharacterTextSplitter (chunk_size=1000, overlap=200)
- [X] T028 [US3] Generate embeddings using Cohere embed-multilingual-v3 for each chunk
- [X] T029 [US3] Store embeddings in Qdrant collection "ai_native_book" with metadata
- [X] T030 [US3] Store metadata in Neon "chunks" table with page numbers and source info
- [ ] T031 [US3] Implement idempotent processing to avoid duplicate ingestion
- [ ] T032 [US3] Test ingestion with various PDF formats and handle malformed PDFs
- [ ] T033 [US3] Create API endpoint for PDF upload and processing trigger

## Phase 8: Testing and Validation

- [ ] T034 Create unit tests for Cohere client module
- [ ] T035 Create unit tests for vector store module
- [X] T036 Create unit tests for RAG service
- [X] T037 Create integration tests for API endpoints
- [ ] T038 Implement 20+ test queries for both full-book and selected-text modes
- [ ] T039 Verify context isolation with comprehensive test cases
- [ ] T040 Performance testing to ensure <5s response time

## Phase 9: Polish & Cross-Cutting Concerns

- [X] T041 Implement proper error handling and user-friendly messages
- [X] T042 Add logging throughout the application for observability
- [ ] T043 Implement embeddable UI that works seamlessly in book format (iframe)
- [X] T044 Update README.md with complete setup, ingestion, and run instructions
- [ ] T045 Code cleanup and documentation
- [ ] T046 Final testing of embeddable functionality