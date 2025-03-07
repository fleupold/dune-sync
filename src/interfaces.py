"""
Interface definitions for the dune-sync package.
"""

from abc import ABC, abstractmethod
from typing import Any
from typing import TypeVar, Generic

from pandas import DataFrame

TypedDataFrame = tuple[DataFrame, dict[str, Any]]

# This will represent your data type (DataFrame, dict, etc.)
T = TypeVar("T")


class Validate(ABC):
    """Enforces validation on inheriting classes"""

    def __init__(self) -> None:
        if not self.validate():
            raise ValueError(f"Config for {self.__class__.__name__} is invalid")

    @abstractmethod
    def validate(self) -> bool:
        """Validate the configuration"""


class Source(Validate, Generic[T]):
    """Abstract base class for data sources"""

    @abstractmethod
    async def fetch(self) -> T:
        """Fetch data from the source"""

    @abstractmethod
    def is_empty(self, data: T) -> bool:
        """Return True if the fetched data is empty"""


class Destination(Validate, Generic[T]):
    """Abstract base class for data destinations"""

    @abstractmethod
    def save(self, data: T) -> None:
        """Save data to the destination"""
