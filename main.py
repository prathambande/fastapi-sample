from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import platform
import os
import psutil
from datetime import datetime
import socket

app = FastAPI(title="Welcome to Linux App Service")

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def welcome(request: Request):
    """Main welcome page"""
    return templates.TemplateResponse("welcome.html", {"request": request})

@app.get("/api/system-info")
async def system_info():
    """Return system information - great for showcasing the Linux environment"""
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            "platform": {
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "hostname": socket.gethostname(),
                "python_version": platform.python_version()
            },
            "resources": {
                "cpu_percent": cpu_percent,
                "cpu_count": psutil.cpu_count(),
                "memory": {
                    "total_gb": round(memory.total / (1024**3), 2),
                    "available_gb": round(memory.available / (1024**3), 2),
                    "percent_used": memory.percent
                },
                "disk": {
                    "total_gb": round(disk.total / (1024**3), 2),
                    "used_gb": round(disk.used / (1024**3), 2),
                    "free_gb": round(disk.free / (1024**3), 2),
                    "percent_used": disk.percent
                }
            },
            "environment": {
                "app_service": os.getenv("WEBSITE_SITE_NAME", "Not running in App Service"),
                "region": os.getenv("REGION_NAME", "Unknown"),
                "instance_id": os.getenv("WEBSITE_INSTANCE_ID", "Unknown")
            },
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "FastAPI on Linux App Service"
    }

@app.get("/api/uptime")
async def uptime():
    """Show system uptime"""
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_duration = datetime.now() - boot_time
    
    return {
        "boot_time": boot_time.isoformat(),
        "uptime_days": uptime_duration.days,
        "uptime_hours": uptime_duration.seconds // 3600,
        "uptime_minutes": (uptime_duration.seconds % 3600) // 60
    }

@app.get("/api/environment")
async def environment_vars():
    """Show relevant environment variables"""
    interesting_vars = [
        "WEBSITE_SITE_NAME", "WEBSITE_INSTANCE_ID", "REGION_NAME",
        "WEBSITE_RESOURCE_GROUP", "WEBSITE_OWNER_NAME", "WEBSITE_SKU",
        "PYTHON_VERSION", "PORT", "HOME", "HOSTNAME"
    ]
    
    env_vars = {}
    for var in interesting_vars:
        value = os.getenv(var)
        if value:
            env_vars[var] = value
    
    return env_vars

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
