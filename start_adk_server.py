#!/usr/bin/env python3
"""
Start Google ADK API Server for AgentOps Integration
This script starts the ADK server with proper configuration to work with the AgentOps web UI.
"""

import os
import sys
import subprocess
import socket
from pathlib import Path
from dotenv import load_dotenv

def _find_open_port(start_port: int, max_tries: int = 20) -> int:
    """Find an available TCP port starting at start_port."""
    port = start_port
    for _ in range(max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("127.0.0.1", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No open port found in range {start_port}-{start_port + max_tries}")


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
    

    # Determine agents directory (default to project root, allow override via env)
    default_agents_dir = str(Path(__file__).parent.resolve())

    # Determine port (allow override through env and find open port if needed)
    desired_port = int(os.getenv("ADK_PORT", "8000"))
    try:
        open_port = _find_open_port(desired_port)
    except RuntimeError:
        print(f"❌ Could not find an open port starting at {desired_port}.")
        return False

    # ADK server configuration
    server_config = {
        "host": "0.0.0.0",
        "port": str(open_port), 
        "allow_origins": "http://localhost:4200",
        # Set to absolute project path by default; override with ADK_AGENTS_DIR if provided
        "agents_dir": os.getenv("ADK_AGENTS_DIR", default_agents_dir),
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
    print(f"🌐 ADK Server will be available at: http://localhost:{server_config['port']}")
    print(f"📊 Start the web UI with: npm run serve --backend=http://localhost:{server_config['port']}")
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