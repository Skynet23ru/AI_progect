#!/bin/bash
# Watchdog script for AI_progect services

PROJECT_DIR="/home/skynet/AI_progect"
cd "$PROJECT_DIR" || exit 1

# Check if containers are running
# We look for 'running' state in docker ps output
RUNNING_SERVICES=$(docker compose ps --format json | jq -r '.services[] | select(.State == "running") | .Service')

REQUIRED_SERVICES=("db" "backend" "frontend")
RESTART_NEEDED=false

for service in "${REQUIRED_SERVICES[@]}"; do
    if [[ ! "$RUNNING_SERVICES" =~ "$service" ]]; then
        echo "$(date): Service $service is DOWN! Attempting restart..." >> "$PROJECT_DIR/docker/watchdog.log"
        RESTART_NEEDED=true
    fi
done

if [ "$RESTART_NEEDED" = true ]; then
    docker compose up -d
    echo "$(date): Restart command executed." >> "$PROJECT_DIR/docker/watchdog.log"
else
    # Optional: log health
    echo "$(date): All services are healthy." >> "$PROJECT_DIR/docker/watchdog.log"
fi
