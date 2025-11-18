"""
Library shelf component for the library scenes.

Creates reusable library shelf visualizations with books.
"""

from manim import *
import numpy as np
import random
from components.colors import BTREE_AMBER_START, HASH_CYAN, ACCENT_PURPLE, GRAY, WHITE


class LibraryShelf(VGroup):
    """
    A library shelf with books of varying heights and colors.

    Used to create the infinite library visualization in the opening scenes.
    """

    def __init__(self, num_books=20, **kwargs):
        """
        Initialize a library shelf with books.

        Args:
            num_books: Number of books to place on the shelf
            **kwargs: Additional arguments passed to VGroup
        """
        super().__init__(**kwargs)

        # Create shelf base
        shelf_width = 10
        shelf = Rectangle(
            width=shelf_width,
            height=0.1,
            fill_color=GRAY,
            fill_opacity=0.3,
            stroke_width=0
        )

        # Create books with varying heights and colors
        books = VGroup()
        for i in range(num_books):
            book = Rectangle(
                width=shelf_width / num_books * 0.8,
                height=np.random.uniform(1.5, 2.5),
                fill_color=random.choice([
                    BTREE_AMBER_START,
                    HASH_CYAN,
                    ACCENT_PURPLE
                ]),
                fill_opacity=0.6,
                stroke_color=WHITE,
                stroke_width=1
            )
            # Position book on shelf
            book.next_to(shelf, UP, buff=0)
            book.shift(RIGHT * (i - num_books/2) * shelf_width/num_books)
            books.add(book)

        self.shelf = shelf
        self.books = books
        self.add(shelf, books)

    def get_book(self, index):
        """
        Get a specific book by index.

        Args:
            index: Index of the book to retrieve

        Returns:
            VMobject: The book at the specified index
        """
        return self.books[index]

    def highlight_book(self, index, color="#FFD700"):
        """
        Create animation to highlight a specific book.

        Args:
            index: Index of the book to highlight
            color: Color for the highlight

        Returns:
            Animation: The highlight animation
        """
        book = self.get_book(index)
        glow = book.copy().scale(1.3).set_stroke(
            color=color,
            width=10,
            opacity=0.3
        )
        return AnimationGroup(
            FadeIn(glow),
            book.animate.set_fill(opacity=0.9),
            run_time=0.8
        )
