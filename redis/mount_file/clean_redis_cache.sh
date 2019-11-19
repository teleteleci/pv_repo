#!/usr/bin/env ash

cd /app

if [ -z "$REDIS_HOST_NAME" ] || [ -z "$REDIS_HOST_NAME" ]; then
    echo "Variable REDIS_HOST_NAME and REDIS_KEY is mandatory"
    exit 1
fi

# Install requirements
pip3 install -r requirements.txt

# echo "x Makummbaaaaa...$REDIS_HOST_NAME and $REDIS_KEY"

# Call flush python script
python3 clean_redis.py
