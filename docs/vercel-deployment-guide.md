# Vercel Deployment Process for RAG Chatbot

## Overview
This document outlines the process for deploying the RAG Chatbot for AI-Native Book to Vercel.

## Prerequisites
- A Vercel account
- Git repository with all required files committed
- Environment variables configured in Vercel dashboard:
  - COHERE_API_KEY
  - QDRANT_URL
  - QDRANT_API_KEY
  - NEON_DB_URL

## Deployment Steps

1. **Import Project to Vercel**
   - Go to https://vercel.com/dashboard
   - Click "Add New Project" → "Import Git Repository"
   - Select your repository containing the RAG Chatbot code

2. **Configure Project Settings**
   - Project name: (your-project-name)
   - Framework: Other (since it's a Python FastAPI app)
   - Root directory: Select the root of your repository

3. **Build Settings** (these are handled automatically by vercel.json)
   - Build Command: `npm run build` (or leave empty for Python projects)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

4. **Environment Variables**
   - Make sure the following are set under Settings → Environment Variables:
     - COHERE_API_KEY
     - QDRANT_URL
     - QDRANT_API_KEY
     - NEON_DB_URL

5. **Deploy**
   - Click "Deploy" button
   - Vercel will automatically detect the Python project and use the settings from vercel.json
   - Monitor the deployment logs for any errors

## Post-Deployment Verification

1. **Check the Live URL**
   - Visit `https://your-project-name.vercel.app` (or the provided Vercel URL)
   - Verify the API is accessible

2. **Test Endpoints**
   - Visit `https://your-project-name.vercel.app/docs` for Swagger UI
   - Test the `/api/v1/chat` endpoint with sample queries
   - Verify the root endpoint `/` returns "RAG Chatbot API"

3. **Verify Serverless Function**
   - The Mangum handler ensures FastAPI compatibility with Vercel's serverless functions
   - Endpoints should respond within expected timeframes

## Troubleshooting

- If deployment fails, check the build logs for dependency installation issues
- Ensure all required environment variables are correctly set
- Verify vercel.json configuration matches the project structure
- Check that the requirements.txt file contains all necessary dependencies