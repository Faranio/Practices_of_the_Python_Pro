import warnings


class Author:
    def __init__(self, author_data):
        self.first_name = author_data['first_name']
        self.last_name = author_data['last_name']

    @property
    def for_display(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def for_citation(self):
        return f'{self.last_name}, {self.first_name[0]}'


class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.author_data = data['author']
        self.author = Author(self.author_data)

    @property
    def author_for_display(self):
        warnings.warn('Use book.author.for_display instead.', DeprecationWarning)
        return self.author.for_display

    @property
    def author_for_citation(self):
        warnings.warn('Use book.author.for_citation instead.', DeprecationWarning)
        return self.author.for_citation

    @property
    def display_title(self):
        if self.title and self.subtitle:
            return f'{self.title}: {self.subtitle}'
        elif self.title:
            return self.title
        else:
            return 'Untitled'
