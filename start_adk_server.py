#!/usr/bin/env python3
"""
Start Google ADK API Server for AgentOps Integration
This script starts the ADK server with proper configuration to work with the AgentOps web UI.
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

def start_adk_server():
    """Start the Google ADK API server with proper configuration"""
    
    # Load environment variables
    load_dotenv()
  
    print("🚀 Starting Google ADK API Server for AgentOps Integration")
    
    # Check if required environment variables are set
    required_env_vars = ["GOOGLE_API_KEY", "AGENTOPS_API_KEY"]
    missing_vars = []
    
    for var in required_env_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these in your .env file or environment.")
        return False
    

    # ADK server configuration
    server_config = {
        "host": "0.0.0.0",
        "port": "8000", 
        "allow_origins": "http://localhost:4200",
        "agents_dir": str("path/to/google-adk-RAG/"),  # Point to your adk rag agent
    }
    
    print(f"🔍 Agents Directory: {server_config['agents_dir']}")
    
    # Build the ADK server command - agents_dir is passed as positional argument
    cmd = [
        "adk", 
        "api_server",
        f"--host={server_config['host']}",
        f"--port={server_config['port']}",
        f"--allow_origins={server_config['allow_origins']}",
        server_config['agents_dir'],  # Positional argument for agents directory
    ]
    
    print(f"🔧 Server Configuration:")
    for key, value in server_config.items():
        print(f"   {key}: {value}")
    
    print(f"\n💻 Command: {' '.join(cmd)}")
    print("\n" + "="*60)
    print("🌐 ADK Server will be available at: http://localhost:8000")
    print("📊 Start the web UI with: npm run serve --backend=http://localhost:8000")
    print("="*60)
    
    try:
        # Start the server
        print("\n🎬 Starting server...")
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting ADK server: {e}")
        return False
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        return True
    except FileNotFoundError:
        print("❌ 'adk' command not found. Please ensure Google ADK is installed:")
        print("   pip install google-adk")
        return False

if __name__ == "__main__":
    success = start_adk_server()
    sys.exit(0 if success else 1)