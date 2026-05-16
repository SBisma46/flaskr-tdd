FROM python:3.12-slim
RUN apt-get update && apt-get install -y chromium chromium-driver && rm -rf /var/lib/apt/lists/*
WORKDIR /tests
COPY test_selenium.py /tests/
RUN pip install --no-cache-dir selenium pytest
CMD ["pytest", "test_selenium.py", "-v", "--tb=short"]