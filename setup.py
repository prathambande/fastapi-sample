from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fastapi-sample",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple FastAPI application with hello world and calculator endpoints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fastapi-sample",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "fastapi>=0.104.0,<0.116.0",
        "uvicorn[standard]>=0.24.0,<0.33.0",
        "pydantic>=2.5.0,<2.10.0",
    ],
)
