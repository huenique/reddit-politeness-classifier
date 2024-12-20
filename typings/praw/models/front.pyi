"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING, Iterator

import praw.models

from .listing.mixins import SubredditListingMixin

"""Provide the Front class."""
if TYPE_CHECKING:
    ...
class Front(SubredditListingMixin):
    """Front is a Listing class that represents the front page."""
    def __init__(self, reddit: praw.Reddit) -> None:
        """Initialize a :class:`.Front` instance."""
        ...
    
    def best(self, **generator_kwargs: str | int) -> Iterator[praw.models.Submission]:
        """Return a :class:`.ListingGenerator` for best items.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        """
        ...
    


