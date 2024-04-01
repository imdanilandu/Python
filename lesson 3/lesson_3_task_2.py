from smartphone import Smartphone

catalog = [Smartphone('iPhone', 'SE', '89001234567'),
Smartphone('Samsung', 'Galaxy S10', '89998765432'),
Smartphone('Huawei', 'P30', '89934561234'),
Smartphone('Xiaomi', 'Mi11', '89007654321'),
Smartphone('Honor', '50', '89996784523')]

for i in range(0, 5):
    catalog[i].sayPhone()