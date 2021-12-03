import random
from hashlib import md5
from concurrent.futures import ProcessPoolExecutor


def generate_coin(seed):
    random.seed(seed)
    while True:
        s = "".join([random.choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            break


def main(max_workers, stop_after):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for i in range(stop_after):
            executor.submit(generate_coin, i >> 12345 * 678 + 910)


if __name__ == '__main__':
    main(10, 4)