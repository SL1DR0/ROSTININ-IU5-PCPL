from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple
import random


@dataclass
class File:
    file_id: int
    file_size: int
    folder_id: Optional[int] = None


@dataclass
class Folder:
    folder_id: int
    name: str
    files: List[File] = field(default_factory=list)


@dataclass
class FolderFileLink:
    folder_id: int
    file_id: int


def get_sorted_folders_with_files(folders: List[Folder]) -> List[Folder]:
    return sorted(folders, key=lambda f: f.name)


def get_folders_total_size(folders: List[Folder]) -> List[Tuple[str, int]]:
    totals = [(folder.name, sum(f.file_size for f in folder.files)) for folder in folders]
    return sorted(totals, key=lambda x: x[1], reverse=True)


def get_linked_files_for_even_folders(folders: List[Folder], files: Dict[int, File], links: List[FolderFileLink]) -> \
Dict[str, List[File]]:
    res = {}
    even_folders = [
        f for f in folders
        if any(ch.isdigit() and int(ch) % 2 == 0 for ch in f.name)
    ]
    for folder in even_folders:
        linked_file_ids = [link.file_id for link in links if link.folder_id == folder.folder_id]
        res[folder.name] = [files[fid] for fid in linked_file_ids]
    return res


def generate_data(num_folders: int = 5, files_per_folder: int = 5):
    folders: List[Folder] = []
    files: Dict[int, File] = {}
    links: List[FolderFileLink] = []
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
        if link not in links: links.append(link)
    return folders, files, links


if __name__ == "__main__":
    f, fls, l = generate_data()
    print("Данные успешно сгенерированы и обработаны.")
