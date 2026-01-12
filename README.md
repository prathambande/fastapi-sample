# Sample Python Welcome App for Linux App Service

A simple, interactive web application built with **FastAPI** and **Uvicorn** to showcase Azure Linux App Service capabilities.

## Features

- 🚀 Built with FastAPI for high performance
- 📊 Real-time system resource monitoring (CPU, Memory, Disk)
- 🐧 Linux environment information display
- ☁️ Azure App Service metadata integration
- 🎨 Modern, responsive UI with interactive features
- 🔍 RESTful API endpoints for system information
- ✅ Health check endpoint for monitoring

## What This App Does

This welcome application demonstrates:

1. **System Information**: View real-time CPU, memory, and disk usage
2. **Platform Details**: Display Linux system information, Python version, and hostname
3. **App Service Metadata**: Show Azure-specific environment variables
4. **Uptime Tracking**: Monitor how long the system has been running
5. **Environment Variables**: Display relevant configuration settings

## API Endpoints

- `GET /` - Main welcome page with interactive UI
- `GET /api/system-info` - Detailed system and platform information
- `GET /api/health` - Health check endpoint
- `GET /api/uptime` - System uptime information

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -e .
   ```
   Or if you prefer using the legacy requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```
   Or use Uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Access the application**:
   Open your browser to `http://localhost:8000`

## Deploy to Azure Linux App Service

### Option 1: Using Azure CLI

```bash
# Create a resource group
az group create --name myResourceGroup --location eastus

# Create an App Service plan (Linux)
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --is-linux --sku B1

# Create the web app
az webapp create --name myUniqueAppName --resource-group myResourceGroup --plan myAppServicePlan --runtime "PYTHON:3.11"

# Configure startup command
az webapp config set --name myUniqueAppName --resource-group myResourceGroup --startup-file "startup.sh"

# Deploy the code
az webapp up --name myUniqueAppName --resource-group myResourceGroup
```

### Option 2: Using VS Code Azure Extension

1. Install the Azure App Service extension
2. Right-click on the folder and select "Deploy to Web App"
3. Follow the prompts to create/select your App Service

### Startup Command

For Azure App Service, configure the startup command:
```bash
bash startup.sh
```

Or directly:
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

## Requirements

- Python 3.9+
- Dependencies managed via `pyproject.toml`
  - FastAPI
  - Uvicorn
  - Jinja2
  - psutil

## Project Structure

```
.
├── main.py              # FastAPI application
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Legacy requirements (optional)
├── startup.sh          # Startup script for App Service
├── templates/
│   └── welcome.html    # HTML template
└── README.md           # This file
```

## Environment Variables

The app automatically detects Azure App Service environment variables:
- `WEBSITE_SITE_NAME` - Your app name
- `WEBSITE_INSTANCE_ID` - Instance identifier
- `REGION_NAME` - Azure region
- `PORT` - Port to bind to (default: 8000)

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: Lightning-fast ASGI server
- **Jinja2**: Template engine for HTML rendering
- **psutil**: System and process utilities

## License

MIT License - Feel free to use this as a template for your own projects!
