from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_book_added_without_genre_has_empty_value(self, setup):
        assert setup.get_book_genre('Дюна') == ''

    incorrect_book_names = ['', 'Книга с очень очень очень длинным названием']
    @pytest.mark.parametrize('book_name', incorrect_book_names)
    def test_add_new_book_incorrect_named_book_is_not_added(self, setup, book_name):
        setup.add_new_book(book_name)
        assert len(setup.get_books_genre()) == 1

    def test_get_books_genre_with_one_added_book_returns_correct(self, setup):
        assert setup.get_books_genre() == {'Дюна': ''}

    def test_set_book_genre_genre_out_of_list_is_not_set(self, setup):
        setup.set_book_genre('Дюна', 'Научная фантастика')
        assert setup.get_book_genre('Дюна') == ''

    def test_get_book_genre_genre_got_by_name_is_correct(self, setup):
        setup.set_book_genre('Дюна', 'Фантастика')
        assert setup.get_book_genre('Дюна') == 'Фантастика'


    genre_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    @pytest.mark.parametrize('genre', genre_list)
    def test_get_books_with_specific_genre_returned_list_for_each_genre_is_correct(self, setup, genre):
        setup.add_new_book('тестовая книга')
        setup.set_book_genre('тестовая книга', genre)
        assert len(setup.get_books_with_specific_genre(genre)) == 1

    def test_get_books_for_children_books_without_genre_not_append(self, setup):
        assert len(setup.get_books_for_children()) == 0


    name_genre_list = [['Сияние', 'Ужасы'], ['Немезида', 'Детективы']]
    @pytest.mark.parametrize('name, genre', name_genre_list)
    def test_get_books_for_children_books_with_age_rating_not_append(self, setup, name, genre):
        setup.add_new_book(name)
        setup.set_book_genre(name, genre)
        assert len(setup.get_books_for_children()) == 0

    def test_add_book_in_favorites_same_book_not_added_twice(self, setup):
        setup.add_book_in_favorites('Дюна')
        setup.add_book_in_favorites('Дюна')
        assert len(setup.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_removed_successfully(self, setup):
        setup.add_book_in_favorites('Дюна')
        setup.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in setup.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_with_one_added_book_returns_correct(self, setup):
        setup.add_book_in_favorites('Дюна')
        assert setup.get_list_of_favorites_books() == ['Дюна']

