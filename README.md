# Repo Agent

A Python project for processing GitHub repositories and applying various text chunking strategies for document analysis and Q&A systems.

## Features

### Document Processing
- **GitHub Repository Reader**: Download and process markdown files from GitHub repositories
- **Frontmatter Support**: Extract metadata from markdown files with frontmatter parsing
- **Multiple File Format Support**: Process `.md` and `.mdx` files

### Text Chunking Strategies
- **Sliding Window Chunking**: Process text using overlapping windows with configurable size and step
- **Markdown Level Splitting**: Split documents by specific header levels (e.g., `## headers`)
- **Intelligent Chunking**: AI-powered semantic chunking using OpenAI models for optimal section division

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Repo_Agent
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync
```

3. Set up environment variables:
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Project Structure

```
project/
├── src/
│   ├── chunking.py         # Text chunking strategies and AI integration
│   └── read_repo.py        # GitHub repository processing
├── main.py                 # Example usage and entry point
├── pyproject.toml          # Project configuration and dependencies
├── README.md               # This file
└── .env                    # Environment variables (create this)
```

## Requirements

- Python >= 3.13
- OpenAI API key (for intelligent chunking)
