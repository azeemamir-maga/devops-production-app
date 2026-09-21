# ==============================
# Stage 1: Builder
# ==============================

FROM python:3.11-slim AS builder

WORKDIR /app

# Create virtual environment
RUN python -m venv /opt/venv

# Make virtual environment the default Python environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# ==============================
# Stage 2: Production
# ==============================

FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Make virtual environment the default
ENV PATH="/opt/venv/bin:$PATH"

# Copy application
COPY . .

# Create non-root user
RUN useradd --create-home appuser

# Run application as non-root user
USER appuser

EXPOSE 5000

CMD ["flask", "--app", "app:create_app", "run", "--host=0.0.0.0", "--port=5000"]
