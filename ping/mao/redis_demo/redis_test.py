import redis
import random
r = redis.Redis(host='localhost',
                port=6379,
                decode_responses=True,
                password="123456")

def gen_score():
    for i in range(1000000):
        r.zadd("Z_1", "key_%d" % i, random.random())
        r.zadd("Z_2", "key_%d" % i, random.random())
        r.zadd("Z_3", "key_%d" % i, random.random())


def update_score(space, key, value):
    r.zadd(space, key, value)

def get_count(space):
    return r.zcard(space)

def select_score(key, start, end):
    return r.zrange(key, start, end, desc=True, withscores=True)

if __name__ == '__main__':
    # 产生数据
    # gen_score()

    # 查看总数
    print(get_count("Z_1"))

    # 查看数据
    print(select_score("Z_1", 88, 99))

    # 合并排序

