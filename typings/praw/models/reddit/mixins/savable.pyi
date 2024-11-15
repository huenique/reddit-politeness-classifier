"""
This type stub file was generated by pyright.
"""

from ....util import _deprecate_args

"""Provide the SavableMixin class."""
class SavableMixin:
    """Interface for :class:`.RedditBase` classes that can be saved."""
    @_deprecate_args("category")
    def save(self, *, category: str | None = ...): # -> None:
        """Save the object.

        :param category: The category to save to. If the authenticated user does not
            have Reddit Premium this value is ignored by Reddit (default: ``None``).

        Example usage:

        .. code-block:: python

            submission = reddit.submission("5or86n")
            submission.save(category="view later")

            comment = reddit.comment("dxolpyc")
            comment.save()

        .. seealso::

            :meth:`.unsave`

        """
        ...
    
    def unsave(self): # -> None:
        """Unsave the object.

        Example usage:

        .. code-block:: python

            submission = reddit.submission("5or86n")
            submission.unsave()

            comment = reddit.comment("dxolpyc")
            comment.unsave()

        .. seealso::

            :meth:`.save`

        """
        ...
    

