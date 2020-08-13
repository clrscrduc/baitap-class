from datetime import *
from functools import reduce


class CanBo:
    thuc_linh = 0

    def __init__(self, ma_can_bo, name, gioi_tinh, nam_sinh, chuyen_mon, he_so_luong, phu_cap):
        if ma_can_bo[0:2] != 'BA' or len(ma_can_bo) != 6:
            raise Exception('nhap sai ma can bo')
        self.ma_can_bo = ma_can_bo
        self.name = name
        self.gioi_tinh = gioi_tinh
        self.nam_sinh = nam_sinh
        self.chuyen_mon = chuyen_mon
        self.he_so_luong = he_so_luong
        self.phu_cap = phu_cap
        self.thuc_linh = he_so_luong * 450000 + phu_cap


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


duc = CanBo('BA1234', 'Le minh Duc', True, date(1958, 1, 11), 'CNTT', 5.4, 570050)
minh = CanBo('BA2344', 'Pham quanh Minh', True, date(1968, 1, 11), 'AN', 6.4, 470000)
phong = CanBo('BA2234', 'vu Quoc Phong', False, date(1957, 1, 11), 'CNTT', 2.4, 470000)
dat = CanBo('BA5554', 'Nguyen quy Dat', True, date(1967, 1, 11), 'CNTT', 4.4, 574000)
hung = CanBo('BA3424', 'tran Duy Hung', True, date(1944, 1, 11), 'CNTT', 6.7, 570000)
vuong = CanBo('BA2344', 'Pham Vuong', False, date(1998, 1, 11), 'AN', 5.5, 570000)
manh = CanBo('BA2344', 'Doan Manh', True, date(1990, 1, 11), 'CNTT', 6.6, 570000)

tinh = Tinh(duc, minh, phong, dat, hung, vuong, manh)


for i in range(0, len(tinh.list_can_bo)):
    print(tinh.list_can_bo[i].name)
