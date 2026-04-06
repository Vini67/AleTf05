#!/bin/bash

echo "Rollback..."
docker-compose down
docker-compose up -d