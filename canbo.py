class CanBo:
    thuc_linh = 0

    def __init__(self, ma_can_bo, name, gioi_tinh, nam_sinh, chuyen_mon, he_so_luong, phu_cap):
        if ma_can_bo[0:2] != 'BA' or len(ma_can_bo) != 5:
            raise Exception('nhap sai ma can bo')
        self.ma_can_bo = ma_can_bo
        self.name = name
        self.gioi_tinh = gioi_tinh
        self.nam_sinh = nam_sinh
        self.chuyen_mon = chuyen_mon
        self.he_so_luong = he_so_luong
        self.phu_cap = phu_cap
        self.thuc_linh = he_so_luong * 450000 + phu_cap
