# Vertex AI RAG Agent with ADK

This repository contains a Google Agent Development Kit (ADK) implementation of a Retrieval Augmented Generation (RAG) agent using Google Cloud Vertex AI.

## Overview

The Vertex AI RAG Agent allows you to:

- Query document corpora with natural language questions
- List available document corpora
- Create new document corpora
- Add new documents to existing corpora
- Get detailed information about specific corpora
- Delete corpora when they're no longer needed

## Prerequisites

- A Google Cloud account with billing enabled
- A Google Cloud project with the Vertex AI API enabled
- Appropriate access to create and manage Vertex AI resources
- Python 3.9+ environment
- Node.js and npm (for web UI)

## Setting Up Google Cloud Authentication

Before running the agent, you need to set up authentication with Google Cloud:

1. **Install Google Cloud CLI**:
   - Visit [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) for installation instructions for your OS

2. **Initialize the Google Cloud CLI**:
   ```bash
   gcloud init
   ```
   This will guide you through logging in and selecting your project.

3. **Set up Application Default Credentials**:
   ```bash
   gcloud auth application-default login
   ```
   This will open a browser window for authentication and store credentials in:
   `~/.config/gcloud/application_default_credentials.json`

4. **Verify Authentication**:
   ```bash
   gcloud auth list
   gcloud config list
   ```

5. **Enable Required APIs** (if not already enabled):
   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```

## Installation

1. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setting Up the Web UI

The Google ADK web UI provides a user-friendly interface for interacting with your RAG agent.

### 1. Clone the ADK Web Repository

```bash
# Clone the Google ADK web UI repository
git clone https://github.com/google/adk-web

# Install web UI dependencies
npm install
```

### 2. Configure Environment Variables

Create a `.env` file in the google-adk-rag directory with your API keys:

```bash
# In google-adk-RAG/.env
GOOGLE_API_KEY=your_google_api_key_here
AGENTOPS_API_KEY=your_agentops_api_key_here
```

### 3. Update the Server Configuration

**Important**: Update the `agents_dir` variable in `start_adk_server.py` to point to your actual project path:

```python
# In start_adk_server.py, line 47
"agents_dir": str("/path/to/google-adk-RAG/"),  # Update this path
```

Replace `/path/to/` with your actual file system path where the `google-adk-RAG` directory is located.

## Running the Application

You'll need to run both the ADK server and the web UI simultaneously.

### 1. Start the ADK Server

In your first terminal, navigate to the project root and start the server:

```bash
cd /path/to/google-adk-RAG
python start_adk_server.py
```

The server will start on `http://localhost:8000`.

### 2. Start the Web UI

In your second terminal, navigate to the web UI directory and start it:

```bash
npm run serve --backend=http://localhost:8000
```

The web UI will be available at `http://localhost:4200`.

### 3. Access the Application

- Open your browser and go to `http://localhost:4200`
- The web UI will automatically connect to the ADK server running on port 8000
- You can now interact with your RAG agent through the web interface

## Using the Agent

The agent provides the following functionality through its tools:

### 1. Query Documents
Allows you to ask questions and get answers from your document corpus:
- Automatically retrieves relevant information from the specified corpus
- Generates informative responses based on the retrieved content

### 2. List Corpora
Shows all available document corpora in your project:
- Displays corpus names and basic information
- Helps you understand what data collections are available

### 3. Create Corpus
Create a new empty document corpus:
- Specify a custom name for your corpus
- Sets up the corpus with recommended embedding model configuration
- Prepares the corpus for document ingestion

### 4. Add New Data
Add documents to existing corpora or create new ones:
- Supports Google Drive URLs and GCS (Google Cloud Storage) paths
- Automatically creates new corpora if they don't exist

### 5. Get Corpus Information
Provides detailed information about a specific corpus:
- Shows document count, file metadata, and creation time
- Useful for understanding corpus contents and structure

### 6. Delete Corpus
Removes corpora that are no longer needed:
- Requires confirmation to prevent accidental deletion
- Permanently removes the corpus and all associated files

## Troubleshooting

If you encounter issues:

- **Authentication Problems**:
  - Run `gcloud auth application-default login` again
  - Check if your service account has the necessary permissions

- **API Errors**:
  - Ensure the Vertex AI API is enabled: `gcloud services enable aiplatform.googleapis.com`
  - Verify your project has billing enabled

- **Quota Issues**:
  - Check your Google Cloud Console for any quota limitations
  - Request quota increases if needed

- **Missing Dependencies**:
  - Ensure all requirements are installed: `pip install -r requirements.txt`

- **Web UI Connection Issues**:
  - Verify the ADK server is running on port 8000
  - Check that the web UI is pointing to the correct backend URL
  - Ensure both terminals are running the correct commands

## Additional Resources

- [Vertex AI RAG Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview)
- [Google Agent Development Kit (ADK) Documentation](https://github.com/google/agents-framework)
- [Google Cloud Authentication Guide](https://cloud.google.com/docs/authentication)
