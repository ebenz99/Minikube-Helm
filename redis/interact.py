import redis
#r = redis.Redis(host='35.196.124.142', port=6379, db=0)

r = redis.Redis(host='34.73.169.5', port=6379, db=0, password='helloworld')
#r = redis.StrictRedis(host='34.73.169.5', port=6379, db=0, password='helloworld')
#r = redis.StrictRedis(host='10.108.34.156', port=30012, db=0, password='helloworld')
#r = redis.StrictRedis(host='35.227.109.179', port=6379, db=0, password='helloworld')
r.set("key", "value")
print(r.get('key'))
