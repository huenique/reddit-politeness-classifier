"""
This type stub file was generated by pyright.
"""

from .base import PRAWBase

"""Provide the ModNote class."""
class ModNote(PRAWBase):
    """Represent a moderator note.

    .. include:: ../../typical_attributes.rst

    =============== ====================================================================
    Attribute       Description
    =============== ====================================================================
    ``action``      If this note represents a moderator action, this field indicates the
                    type of action. For example, ``"banuser"`` if the action was banning
                    a user.
    ``created_at``  Time the moderator note was created, represented in `Unix Time`_.
    ``description`` If this note represents a moderator action, this field indicates the
                    description of the action. For example, if the action was banning
                    the user, this is the ban reason.
    ``details``     If this note represents a moderator action, this field indicates the
                    details of the action. For example, if the action was banning the
                    user, this is the duration of the ban.
    ``id``          The ID of the moderator note.
    ``label``       The label applied to the note, currently one of:
                    ``"ABUSE_WARNING"``, ``"BAN"``, ``"BOT_BAN"``, ``"HELPFUL_USER"``,
                    ``"PERMA_BAN"``, ``"SOLID_CONTRIBUTOR"``, ``"SPAM_WARNING"``,
                    ``"SPAM_WATCH"``, or ``None``.
    ``moderator``   The moderator who created the note.
    ``note``        The text of the note.
    ``reddit_id``   The fullname of the object this note is attributed to, or ``None``
                    if not set. If this note represents a moderators action, this is the
                    fullname of the object the action was performed on.
    ``subreddit``   The subreddit this note belongs to.
    ``type``        The type of note, currently one of: ``"APPROVAL"``, ``"BAN"``,
                    ``"CONTENT_CHANGE"``, ``"INVITE"``, ``"MUTE"``, ``"NOTE"``,
                    ``"REMOVAL"``, or ``"SPAM"``.
    ``user``        The redditor the note is for.
    =============== ====================================================================

    .. _unix time: https://en.wikipedia.org/wiki/Unix_time

    """
    def __eq__(self, other: ModNote) -> bool:
        """Return whether the other instance equals the current."""
        ...
    
    def delete(self): # -> None:
        """Delete this note.

        For example, to delete the last note for u/spez from r/test, try:

        .. code-block:: python

            for note in reddit.subreddit("test").mod.notes("spez"):
                note.delete()

        """
        ...
    

