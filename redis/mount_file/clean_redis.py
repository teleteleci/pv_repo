import redis
import os

myHostname = os.environ['REDIS_HOST_NAME']
myPassword = os.environ['REDIS_KEY']
port = 6380

r = redis.StrictRedis(
    host=myHostname,
    port=port,
    password=myPassword,
    ssl=True)

result = r.ping()
print("Ping to redis : " + str(result))
r.flushall()
print('... flush is successful')
