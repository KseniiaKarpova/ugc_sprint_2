import sys
from typing import Sequence, Type, TypeVar

from beanie import Document
from models.review import ReviewMark, FilmReview

# All database models must be imported here to be able to
# initialize them on startup.

DocType = TypeVar('DocType', bound=Document)


def gather_documents() -> Sequence[Type[DocType]]:
    from inspect import getmembers, isclass

    return [
        doc
        for _, doc in getmembers(sys.modules[__name__], isclass)
        if issubclass(doc, Document) and doc.__name__ != 'Document'
    ]
