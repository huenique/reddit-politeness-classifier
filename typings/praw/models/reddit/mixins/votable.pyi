"""
This type stub file was generated by pyright.
"""

"""Provide the VotableMixin class."""
class VotableMixin:
    """Interface for :class:`.RedditBase` classes that can be voted on."""
    def clear_vote(self): # -> None:
        """Clear the authenticated user's vote on the object.

        .. note::

            Votes must be cast by humans. That is, API clients proxying a human's action
            one-for-one are OK, but bots deciding how to vote on content or amplifying a
            human's vote are not. See the reddit rules for more details on what
            constitutes vote manipulation. [`Ref
            <https://www.reddit.com/dev/api#POST_api_vote>`_]

        Example usage:

        .. code-block:: python

            submission = reddit.submission("5or86n")
            submission.clear_vote()

            comment = reddit.comment("dxolpyc")
            comment.clear_vote()

        """
        ...
    
    def downvote(self): # -> None:
        """Downvote the object.

        .. note::

            Votes must be cast by humans. That is, API clients proxying a human's action
            one-for-one are OK, but bots deciding how to vote on content or amplifying a
            human's vote are not. See the reddit rules for more details on what
            constitutes vote manipulation. [`Ref
            <https://www.reddit.com/dev/api#POST_api_vote>`_]

        Example usage:

        .. code-block:: python

            submission = reddit.submission("5or86n")
            submission.downvote()

            comment = reddit.comment("dxolpyc")
            comment.downvote()

        .. seealso::

            :meth:`.upvote`

        """
        ...
    
    def upvote(self): # -> None:
        """Upvote the object.

        .. note::

            Votes must be cast by humans. That is, API clients proxying a human's action
            one-for-one are OK, but bots deciding how to vote on content or amplifying a
            human's vote are not. See the reddit rules for more details on what
            constitutes vote manipulation. [`Ref
            <https://www.reddit.com/dev/api#POST_api_vote>`_]

        Example usage:

        .. code-block:: python

            submission = reddit.submission("5or86n")
            submission.upvote()

            comment = reddit.comment("dxolpyc")
            comment.upvote()

        .. seealso::

            :meth:`.downvote`

        """
        ...
    

