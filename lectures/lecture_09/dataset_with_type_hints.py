from typing import TypeVar

# A type variable represents an unspecified type that becomes concrete when a function or class is used.
T = TypeVar("T")


class Dataset:
    """A container class for managing a sequence of data records.

    Provides standard sequence behaviors including length inspection, indexing,
    slicing, membership testing, and iteration.
    """

    def __init__(self, records: list[T]) -> None:
        """Initializes the dataset with a list of records.

        Args:
            records: A list containing the dataset elements.
        """
        self._records: list[T] = records

    def __len__(self) -> int:
        """Returns the total number of records in the dataset.

        Returns:
            The total count of records.
        """
        return len(self._records)

    def __getitem__(self, index: int | slice) -> T | list[T]:
        """Retrieves a single record or a slice of records.

        Enables indexing (`dataset[0]`), slicing (`dataset[1:3]`), and
        automatic iteration (`for record in dataset:`).

        Args:
            index: An integer index or a slice object.

        Returns:
            A single element if accessed by integer index, or a list of elements
            if accessed by slice.
        """
        return self._records[index]

    def __contains__(self, item: object) -> bool:
        """Checks whether an item is present in the dataset.

        Enables membership testing using the `in` operator (`item in dataset`).

        Args:
            item: The element to check for presence.

        Returns:
            True if the item exists in the dataset, False otherwise.
        """
        return item in self._records
