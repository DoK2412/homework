films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня'] # список фильмов
favorite_movies = [] # список под любимые фильмы

number_of_movies = int(input('Сколько фильмов вы бы хотели добавить в избранные: ')) #запрос на ввод

for _ in range(number_of_movies): #цикл ввода фильмов
    film = input('Введите фильм: ')
    for i in films: # проверка принадлежности ввода к списку
        if i in film:
            favorite_movies.append(film)
    else:
        print('Такого фильма нет в списках')

print('Любимые фильмы: ', favorite_movies)


