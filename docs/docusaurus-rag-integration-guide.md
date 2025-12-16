# Docusaurus Book with Embedded RAG Chatbot - Deployment Guide

## Overview

This document explains how to integrate the RAG chatbot into your Docusaurus book and deploy the entire application to Vercel.

## Prerequisites

- Your RAG backend service must be deployed and accessible via a URL (e.g., `https://your-backend.vercel.app`)
- Your Docusaurus book codebase
- A Vercel account

## Component Integration

The RAG chatbot component (`RAGChatbot.js`) has been created with the following features:

1. **Full Book Queries**: Users can ask questions about the entire book content
2. **Selected Text Queries**: Users can select text on the page and ask questions specifically about that text
3. **Source Attribution**: Responses include citations to the relevant pages/sections of the book
4. **Responsive Design**: Works well in both light and dark modes

## Embedding in Book Pages

The component has been embedded in:
- `docs/intro.mdx` (main introduction page)
- `docs/module-1-ros2/chapter-1-introduction/introduction.mdx` (first chapter)

To embed the component in additional pages, add these two lines to any MDX file:

```md
import RAGChatbot from '@site/src/components/RAGChatbot';

<RAGChatbot backendUrl="https://your-deployed-backend.vercel.app" />
```

Replace `https://your-deployed-backend.vercel.app` with your actual deployed backend URL.

## Environment Configuration

The component accepts a `backendUrl` prop that should point to your deployed backend service.

## Deployment to Vercel

1. **Before deploying your Docusaurus book**, ensure your backend service is already deployed and accessible
2. Push your updated Docusaurus code (with the embedded RAGChatbot component) to your GitHub repository
3. Go to https://vercel.com and create a new project
4. Import your Docusaurus repository
5. Configure the project with these settings:
   - Framework Preset: `Docusaurus`
   - Build Command: `npm run build`
   - Output Directory: `build`
   - Root Directory: Project root
6. Vercel will automatically deploy your book with the embedded chatbot
7. The chatbot will connect to your deployed backend service to provide RAG functionality

## Testing the Integration

After deployment:

1. Navigate to your deployed Docusaurus book
2. Find the embedded chatbot on the integrated pages
3. Test with general questions about the book content
4. Test the selected text feature by highlighting text on the page and checking the "Use selected text" option
5. Verify that responses include proper source citations

## Troubleshooting

- If the chatbot doesn't appear, verify the component import path is correct
- If API calls fail, check that the backend URL is correctly configured and accessible
- Ensure CORS is properly configured on your backend to allow requests from your book's domain
- Check browser developer tools for any error messages

## Architecture

- **Frontend**: Docusaurus React application with embedded RAGChatbot component
- **Backend**: FastAPI application deployed on Vercel with Cohere, Qdrant, and Neon integration
- **Communication**: REST API calls from the frontend component to the backend endpoints
- **Data Flow**: Book content → Qdrant vector store → RAG service → responses to the frontend