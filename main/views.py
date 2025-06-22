from django.shortcuts import render


def home(request):
    brands = [
        {
            'name': 'Audi',
            'image': 'main/images/audi.webp',
            'url_name': 'audi'
        },
        {
            'name': 'Mercedes',
            'image': 'main/images/mercedes.jpeg',
            'url_name': 'mercedes'
        },
        {
            'name': 'Lada',
            'image': 'main/images/lada.jpg',
            'url_name': 'lada'
        },
        {
            'name': 'Haval',
            'image': 'main/images/haval.webp',
            'url_name': 'haval'
        }
    ]
    return render(request, 'main/index.html', {'brands': brands})


def car_detail(request, brand):
    cars = {
        'audi': {
            'brand': 'Audi',
            'model': 'Q7',
            'image': 'main/images/audi.webp',
            'description': 'Премиальный внедорожник',
            'specs': [
                {'label': 'Двигатель', 'value': '3.0 TDI'},
                {'label': 'Мощность', 'value': '249 л.с.'},
                {'label': 'Разгон', 'value': '6.9 сек до 100 км/ч'},
                {'label': 'Привод', 'value': 'Полный'},
            ],
            'price': '5 990 000'
        },
        'mercedes': {
            'brand': 'Mercedes-Benz',
            'model': 'GLE',
            'image': 'main/images/mercedes.jpeg',
            'description': 'Роскошный кроссовер',
            'specs': [
                {'label': 'Двигатель', 'value': '3.0 Diesel'},
                {'label': 'Мощность', 'value': '269 л.с.'},
                {'label': 'Разгон', 'value': '6.1 сек до 100 км/ч'},
                {'label': 'Привод', 'value': '4MATIC'},
            ],
            'price': '6 500 000'
        },
        'lada': {
            'brand': 'Lada',
            'model': 'Vesta',
            'image': 'main/images/lada.jpg',
            'description': 'Надежный седан',
            'specs': [
                {'label': 'Двигатель', 'value': '1.6 L'},
                {'label': 'Мощность', 'value': '106 л.с.'},
                {'label': 'Разгон', 'value': '11.8 сек до 100 км/ч'},
                {'label': 'Привод', 'value': 'Передний'},
            ],
            'price': '1 200 000'
        },
        'haval': {
            'brand': 'Haval',
            'model': 'F7',
            'image': 'main/images/haval.webp',
            'description': 'Современный кроссовер',
            'specs': [
                {'label': 'Двигатель', 'value': '2.0 Turbo'},
                {'label': 'Мощность', 'value': '190 л.с.'},
                {'label': 'Разгон', 'value': '9.6 сек до 100 км/ч'},
                {'label': 'Привод', 'value': 'Полный'},
            ],
            'price': '2 300 000'
        }
    }

    car_data = cars.get(brand.lower())
    if not car_data:
        # Обработка несуществующей марки
        return render(request, 'main/404.html', status=404)

    return render(request, 'main/car_detail.html', car_data)