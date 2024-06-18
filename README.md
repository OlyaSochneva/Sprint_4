### Предусловие: 
setup - фикстура, находится в файле conftest.py, для каждого теста создаёт экземпляр класса и добавляет в словарь books_genre книгу «Дюна» (без жанра)

### Тест 1
#### test_add_new_book_book_added_without_genre_has_empty_value
Тестируемый метод: add_new_book

Проверка: у книги, добавленной без жанра, действительно не будет жанра

ТД:

name = 'Дюна'


ОР: `setup.get_book_genre('Дюна') == ''`
### Тест 2
#### test_add_new_book_incorrect_named_book_is_not_added
Тестируемый метод: add_new_book

Проверка: книга с некорректным названием (0 или более 40 символов) не добавится

ТД:

name = 'Дюна', ' ', 'Книга с очень очень очень длинным названием'


ОР: `len(setup.get_books_genre()) == 1`
### Тест 3
#### test_get_books_genre_with_one_added_book_returns_correct
Тестируемый метод: get_books_genre

Проверка: если добавить в словарь books_genre одну книгу, возвращается словарь с одной этой книгой

ТД:

name = 'Дюна'

ОР: `setup.get_books_genre() == {'Дюна': ''}`
### Тест 4
#### test_set_book_genre_genre_out_of_list_is_not_set
Тестируемый метод: set_book_genre

Проверка: нельзя присвоить книге свой жанр (не из списка)

ТД:

name = 'Дюна'

genre = 'Научная фантастика'

ОР: `setup.get_book_genre('Дюна') == ''`
### Тест 5
#### test_get_book_genre_genre_got_by_name_is_correct
Тестируемый метод: get_book_genre

Проверка: жанр книги, полученный по имени, соответсвует установленному

ТД:

name = 'Дюна'

genre = 'Фантастика'

ОР: `setup.get_book_genre('Дюна') == 'Фантастика'`
### Тест 6
#### test_get_books_with_specific_genre_returned_list_for_each_genre_is_correct
Тестируемый метод: get_books_with_specific_genre

Проверка: при добавлении одной книги каждого жанра возвращается список с одной этой книгой

ТД:

name = 'Тестовая книга'

genre = 'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'

ОР: `len(setup.get_books_with_specific_genre(genre)) == 1`
### Тест 7
#### test_get_books_for_children_books_without_genre_not_append
Тестируемый метод: get_books_for_children

Проверка: книги без присвоенного жанра не попадают в список для детей

ТД:

name = 'Дюна'

genre = ' '

ОР: `len(setup.get_books_for_children()) == 0`
### Тест 8
#### test_get_books_for_children_books_with_age_rating_not_append
Тестируемый метод: get_books_for_children

Проверка: книги с жанром ужасы и детективы не попадают в список для детей

ТД:

name = 'Сияние', 'Немезида'

genre = 'Ужасы', 'Детективы'

ОР: `len(setup.get_books_for_children()) == 0`
### Тест 9
#### test_add_book_in_favorites_same_book_not_added_twice
Тестируемый метод: add_book_in_favorites

Проверка: нельзя дважды добавить в избранное одну и ту же книгу

ТД:

name = 'Дюна', 'Дюна'

ОР: `len(setup.get_list_of_favorites_books()) == 1`
### Тест 10
#### test_delete_book_from_favorites_book_removed_successfully
Тестируемый метод: delete_book_from_favorites

Проверка: книга успешно удалилась из избранного

ТД:

name = 'Дюна'

ОР: `'Дюна' not in setup.get_list_of_favorites_books()`
### Тест 11
#### test_get_list_of_favorites_books_with_one_added_book_returns_correct
Тестируемый метод: get_list_of_favorites_books

Проверка: если добавить в избранное одну книгу, возвращается список с одной этой книгой

ТД:

name = 'Дюна'

ОР: `setup.get_list_of_favorites_books() == ['Дюна']`