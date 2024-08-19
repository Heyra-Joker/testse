# -*- encoding: utf-8 -*-
import hashlib
import sys
from typing import AnyStr


class Sign:

    @staticmethod
    def equal(t, e):
        return t == e

    @staticmethod
    def mod(t, e):
        return t % e

    @staticmethod
    def and_(t, e):
        return t & e

    @staticmethod
    def xor(t, e):
        return t ^ e

    @staticmethod
    def or_(t, e):
        return t | e

    @staticmethod
    def multiply(t, e):
        return t * e

    @staticmethod
    def add(t, e):
        return t + e

    def run(self, url: AnyStr) -> AnyStr:
        print(url)
        res = list(url.encode())
        print(res)

        res_1 = []
        for r, t in enumerate(res):
            if self.equal(self.mod(r, 3), 0):
                t1 = self.and_(self.xor(t, 123), 255)
            else:
                if self.equal(self.mod(r, 3), 1):
                    t1 = self.and_(self.or_(t, 177), 255)
                else:
                    t1 = self.xor(self.and_(t, 203), 89)
            res_1.append(t1)

        print(res_1)

        res_2 = []
        for r, t in enumerate(res_1):
            t2 = self.and_(self.add(self.add(t, self.multiply(r, 17)), 3), 255)
            res_2.append(t2)

        print(res_2)
        # res_2 = [87, 5, 62, 72, 6, 115, 179, 57, 164, 226]
        f = bytes(res_2).decode("utf-8", errors='replace')
        print(f)
        print(list(f.encode()))
        md5 = hashlib.md5(f.encode()).hexdigest()
        print(md5)
        print(u'\uFFFD', list(u'\uFFFD'.encode()))
        return hashlib.md5(md5.encode()).hexdigest()


if __name__ == '__main__':
    s = Sign()
    print(s.run("/api/v1?t=1719123903&url=https%3A%2F%2Fhaijiao.com%2Fpost%2Fdetails%3Fpid%3D1379359"))
