FROM python:3.10-slim

WORKDIR /mcp

COPY pyproject.toml ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /mcp

CMD ["python", "mcp.py"]