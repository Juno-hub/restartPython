import theater_module

theater_module.price(3)
theater_module.price_mornig(4)
theater_module.price_soldier(5)

import theater_module as mv

mv.price(3)
mv.price_mornig(4)
mv.price_soldier(5)

from theater_module import *

price(3)
price_mornig(4)
price_soldier(5)

from theater_module import price, price_mornig

price(5)
price_mornig(6)

from theater_module import price_soldier as price

price(5)