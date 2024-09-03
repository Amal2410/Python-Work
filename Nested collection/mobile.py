mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},

    {"id":101,"title":"s23 ","brand":"samsung","price":54000,"network":"4g"},

    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},

    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},

    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},

    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},

]

mobile_names=[mob.get("title") for mob in mobiles]

print(mobile_names)

brand_names={brand.get("brand") for brand in mobiles}

print(brand_names)

samsung_mobile=[samsung.get("title") for samsung in mobiles if samsung.get("brand")==("samsung")]

print(samsung_mobile)

price_range=[mob_range.get("title") for mob_range in mobiles if mob_range.get("price")in range (23000,40001) ]

print(price_range)

max_price=0

for mob in mobiles:

    if mob.get("price")>max_price:

        max_price=mob.get("price")

costly_mobile=[mob.get ("title")for mob in mobiles if mob.get("price")==max_price]

print(costly_mobile)