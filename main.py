from dataclasses import dataclass, field
from typing import Optional
import random


@dataclass
class File:
    file_id: int
    file_size: int
    folder_id: Optional[int] = None  # связь 1→М


@dataclass
class Folder:
    folder_id: int
    name: str
    files: list[File] = field(default_factory=list)  # 1→М


@dataclass
class FolderFileLink:
    folder_id: int
    file_id: int


def generate_data(num_folders: int = 5, files_per_folder: int = 5):
    folders: list[Folder] = []
    files: dict[int, File] = {}
    links: list[FolderFileLink] = []

    file_counter = 1

    for i in range(1, num_folders + 1):
        folder = Folder(folder_id=i, name=f"Folder_{i}")
        for j in range(1, files_per_folder + 1):
            f = File(file_id=file_counter, file_size=random.randint(100, 10_000), folder_id=i)
            folder.files.append(f)
            files[file_counter] = f
            file_counter += 1
        folders.append(folder)

    for _ in range(10):
        folder = random.choice(folders)
        file = random.choice(list(files.values()))
        link = FolderFileLink(folder_id=folder.folder_id, file_id=file.file_id)
        if link not in links:
            links.append(link)

    return folders, files, links


def query_all_folders_and_files(folders: list[Folder]):
    print("=== Запрос А1  ===\n")
    for folder in sorted(folders, key=lambda f: f.name):
        print(f"{folder.name}")
        for f in folder.files:
            print(f"File {f.file_id} (size={f.file_size})")
        print()


def query_folders_by_total_size(folders: list[Folder]):
    print("=== Запрос А2 ===\n")
    totals = [(folder, sum(f.file_size for f in folder.files)) for folder in folders]
    totals.sort(key=lambda x: x[1], reverse=True)
    for folder, total in totals:
        print(f"{folder.name}: total size = {total}")
    print()


def query_even_folders_mn(folders: list[Folder], files: dict[int, File], links: list[FolderFileLink]):
    print("=== Запрос А3 ===\n")
    even_folders = [
        f for f in folders
        if any(ch.isdigit() and int(ch) % 2 == 0 for ch in f.name)
    ]

    for folder in even_folders:
        linked_file_ids = [link.file_id for link in links if link.folder_id == folder.folder_id]
        linked_files = [files[fid] for fid in linked_file_ids]

        print(f"{folder.name}")
        if linked_files:
            for f in linked_files:
                print(f"Linked File {f.file_id} (size={f.file_size})")
        else:
            print("Нет связанных файлов")
        print()


if __name__ == "__main__":
    folders, files, links = generate_data()

    query_all_folders_and_files(folders)
    query_folders_by_total_size(folders)
    query_even_folders_mn(folders, files, links)
