from datetime import *
from functools import reduce
# from canbo import CanBo


class Tinh:
    def __init__(self, *args):
        self.list_can_bo = list(args)

    def tong_luong(self):
        li = [x.thuc_linh for x in self.list_can_bo]
        return reduce(lambda u, y: u + y, li)

    def liet_ke_chuyen_mon(self):
        return list(filter(lambda x: x.chuyen_mon == 'CNTT', self.list_can_bo))

    def liet_ke_huu(self):
        kq = []
        for x in self.list_can_bo:
            sex = x.gioi_tinh
            tuoi = date.today().year - x.nam_sinh.year
            if sex:
                if tuoi >= 55:
                    kq.append(x)
            else:
                if tuoi >= 50:
                    kq.append(x)
        return kq

    def sort_by_id(self):
        def my_key(e):
            return e.ma_can_bo

        return sorted(self.list_can_bo, key=my_key)

    def delete_by_id(self, _id):
        self.list_can_bo = [x for x in self.list_can_bo if x.ma_can_bo != _id]

    def insert(self, x):
        self.list_can_bo.append(x)
