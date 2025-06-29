"""Module for reading data from files."""
import csv
import json
from copy import deepcopy
from pathlib import Path


def read_data(file_path: Path) -> list:
    """Read data from file."""
    if not Path.exists(file_path):
        msg = f"File {file_path} not found."
        raise FileNotFoundError(msg)

    file_extension = Path(file_path).suffix
    file_extension = file_extension.lower().lstrip(".")
    reader_by_type = {
        "csv": reader_csv,
        "json": reader_json,
    }.get(file_extension)

    if reader_by_type is None:
        message = """Unknow extension for reader. Check reader's extensions."""
        raise ValueError(message)

    return reader_by_type(file_path)


def reader_json(file_path: Path) -> list:
    """Read data from file with json format."""
    with Path(file_path).open() as json_file:
        return json.load(json_file)


def reader_csv(file_path: Path) -> list:
    """Read data from file with csv format."""
    with Path(file_path).open() as csv_file:
        return list(csv.DictReader(csv_file))

def format_data(data: dict, required_fields: dict[str, type]) -> dict:
    """Format data by required fields."""
    result_data = {}
    for field_name, field_type_converter in required_fields.items():
        value = field_type_converter(data[field_name])
        result_data[field_name.lower()] = value
    return result_data

def write_data(file_path: str, data: list) -> None:
    """Write json data to file."""
    with Path(file_path).open("w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":

    _users = read_data(Path("users.json"))
    _books = read_data(Path("books.csv"))

    if not _users:
        msg = "No users found."
        raise ValueError(msg)
    if not _books:
        msg = "No books found."
        raise ValueError(msg)

    users = deepcopy(_users)
    books = deepcopy(_books)
    result = []
    user_required_fields = {
        "name": str,
        "gender": str,
        "address": str,
        "age": int,
    }
    book_required_fields = {
        "Title": str,
        "Author": str,
        "Pages": int,
        "Genre": str,
    }

    books_min_count = len(books) // len(users)


    for user_idx, user in enumerate(users):
        min_idx = user_idx * books_min_count
        max_idx = min_idx + books_min_count

        result_user = format_data(user, user_required_fields)
        result_user["books"] = [
            format_data(book, book_required_fields)
            for book in books[min_idx:max_idx]
        ]
        result.append(result_user)

    if len(books) > max_idx:
        for idx, book in enumerate(books[max_idx:-1]):
            result[idx]["books"].append(
                format_data(book, book_required_fields),
            )


    write_data("results.json", result)
