ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Optional: Uncomment if you want a non-root user
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

COPY . .

# Optional: Uncomment if you switch to non-root
# USER appuser

# EXPOSE 7999  # Uncomment if your app uses a specific port

CMD ["python3", "app.py"]
