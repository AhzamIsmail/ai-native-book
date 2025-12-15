# Feature Specification: Integrated RAG Chatbot for AI-Native Book

**Feature Branch**: `001-rag-chatbot-book`
**Created**: December 12, 2025
**Status**: Draft
**Input**: User description: "Integrated RAG Chatbot for AI-Native Book Target audience: End-users reading the published book, developers maintaining the chatbot Focus: Accurate RAG-based querying on full book content or user-selected text, using Cohere for generation, Qdrant for vector search, and Neon for metadata storage Success criteria: - Chatbot answers 90%+ of test queries correctly based on book content in blind evaluation - Supports isolated context for user-selected text without full-book leakage - Ingests book PDF into Qdrant/Neon without errors - FastAPI endpoints return responses in under 5 seconds average - Full code reproducibility with provided credentials and structure - Embeddable UI (Streamlit) works seamlessly in book format (e.g., iframe) Constraints: - LLM strictly Cohere (no OpenAI); use command-r-plus model - Vector DB: Qdrant Cloud Free Tier only - DB: Neon Serverless Postgres - Backend: FastAPI with Python 3.11+ - Frontend: Streamlit for chat interface - Embeddings: Cohere embed-multilingual-v3 - Text splitting: LangChain RecursiveCharacterTextSplitter (chunk_size=1000, overlap=200) - Exact credentials (hardcode only in .env, never in code): COHERE_API_KEY=e0Gew92LjzbtwIxWf3bubqOBLA75UBmBsKNjNO4o QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.RKcZaFRDwuBaOsVXQn3yvqZkNAADpTaAMD5q3dQwXnk QDRANT_URL=https://b4cce397-6df9-4163-b478-0117fb9c8f72.europe-west3-0.gcp.cloud.qdrant.io QDRANT_CLUSTER_ID=b4cce397-6df9-4163-b478-0117fb9c8f72 NEON_DB_URL=postgresql://neondb_owner:npg_ETDM14inCGvs@ep-weathered-scene-ahzw3wnz-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require - Timeline: Prototype complete by 25 Dec 2025 - Deployment: Local-first, optional cloud (no extra cost) - Code quality: PEP8, type hints, pydantic schemas, unit tests for services Not building: - Full-scale production deployment (e.g., no Kubernetes or paid tiers) - Multi-user authentication or session management - Advanced features like voice input or multi-modal (images/tables in book) - Integration with Qwen CLI unless explicitly added later - Any UI beyond basic Streamlit for embedding"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Query Full Book Content (Priority: P1)

End-users reading the published book need to ask questions about the book content and receive accurate answers based on the full book text. The system should provide responses that accurately reflect information from the entire book.

**Why this priority**: This is the primary function of the RAG chatbot - allowing users to ask questions about the book content and receive relevant answers based on the entire book.

**Independent Test**: Users can enter a question about general book content and receive an accurate response that references the correct sections of the book within 5 seconds.

**Acceptance Scenarios**:

1. **Given** a user has access to the book chatbot interface, **When** they enter a question about the book content, **Then** they receive an accurate response based on the book content within 5 seconds.
2. **Given** a user enters a complex question requiring information from multiple book sections, **When** they submit the query, **Then** the system provides a comprehensive answer synthesizing information from relevant parts of the book.

---

### User Story 2 - Query User-Specific Text (Priority: P2)

End-users need to select specific text within the book interface and ask questions about only that selected text without getting responses influenced by the full book content.

**Why this priority**: Advanced users need contextual queries on specific sections without interference from other book content, providing isolated analysis of selected text.

**Independent Test**: Users can select text in the book, ask questions about it, and receive responses based solely on the selected text without irrelevant information from other parts of the book.

**Acceptance Scenarios**:

1. **Given** a user has selected specific text in the book, **When** they ask a question related to only that text, **Then** the response is contextual to the selected text without content from other parts of the book.

---

### User Story 3 - PDF Ingestion and Processing (Priority: P3)

Developers maintaining the chatbot need to be able to import new book PDFs into the system so that the RAG functionality works with updated or different book content.

**Why this priority**: For the system to be useful, it must support ingesting new book content, which is typically provided in PDF format.

**Independent Test**: Developers can upload a book PDF file and confirm that it has been processed and indexed correctly in the system.

**Acceptance Scenarios**:

1. **Given** a developer has a book in PDF format, **When** they upload it to the system, **Then** the PDF is processed and becomes available for querying without errors.

---

### Edge Cases

- What happens when the user asks a question that is not answered by the book content?
- How does system handle malformed PDF files during ingestion?
- What occurs when the system encounters a query during peak load periods?
- How does the system handle very long user queries or selected text?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow end-users to input questions about book content through a chat interface
- **FR-002**: System MUST provide accurate responses to questions based on the book content with 90%+ accuracy in blind evaluation
- **FR-003**: System MUST support isolated context queries on user-selected text without contamination from full-book content
- **FR-004**: System MUST ingest PDF files containing book content without errors
- **FR-005**: System MUST return responses to user queries in under 5 seconds average response time
- **FR-006**: System MUST provide an embeddable UI that works seamlessly in book format (e.g., iframe)
- **FR-007**: System MUST maintain full code reproducibility with provided credentials and structure
- **FR-008**: System MUST store metadata about book content for retrieval purposes

### Key Entities *(include if feature involves data)*

- **Book Content**: Represents the text content of the book, including pages, sections, and paragraphs that will be stored for retrieval
- **User Query**: Represents the questions submitted by users with metadata about when asked and context used
- **PDF Document**: Represents the source book files that need to be processed and ingested into the system

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Chatbot answers 90%+ of test queries correctly based on book content in blind evaluation
- **SC-002**: System supports isolated context for user-selected text without full-book leakage during contextual queries
- **SC-003**: Book PDF ingestion completes without errors and all content is available for querying
- **SC-004**: System returns responses to user queries in under 5 seconds average
- **SC-005**: Embeddable UI works seamlessly in book format (e.g., iframe) without performance issues
- **SC-006**: System demonstrates full code reproducibility with provided credentials and structure