"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING

import praw.models

"""Provide the EditableMixin class."""
if TYPE_CHECKING:
    ...
class EditableMixin:
    """Interface for classes that can be edited and deleted."""
    def delete(self): # -> None:
        """Delete the object.

        Example usage:

        .. code-block:: python

            comment = reddit.comment("dkk4qjd")
            comment.delete()

            submission = reddit.submission("8dmv8z")
            submission.delete()

        """
        ...
    
    def edit(self, body: str) -> praw.models.Comment | praw.models.Submission:
        """Replace the body of the object with ``body``.

        :param body: The Markdown formatted content for the updated object.

        :returns: The current instance after updating its attributes.

        Example usage:

        .. code-block:: python

            comment = reddit.comment("dkk4qjd")

            # construct the text of an edited comment
            # by appending to the old body:
            edited_body = comment.body + "Edit: thanks for the gold!"
            comment.edit(edited_body)

        """
        ...
    

