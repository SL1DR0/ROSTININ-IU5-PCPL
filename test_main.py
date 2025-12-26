import pytest
from main import File, Folder, FolderFileLink, \
    get_sorted_folders_with_files, \
    get_folders_total_size, \
    get_linked_files_for_even_folders


def test_sorting_folders_by_name():
    f1 = Folder(1, "Gamma")
    f2 = Folder(2, "Alpha")
    f3 = Folder(3, "Beta")

    result = get_sorted_folders_with_files([f1, f2, f3])

    assert result[0].name == "Alpha"
    assert result[1].name == "Beta"
    assert result[2].name == "Gamma"


def test_total_size_calculation():
    folder1 = Folder(1, "Small", files=[File(1, 100)])
    folder2 = Folder(2, "Big", files=[File(2, 200), File(3, 300)])

    result = get_folders_total_size([folder1, folder2])

    assert result[0] == ("Big", 500)
    assert result[1] == ("Small", 100)


def test_even_folders_links():
    f_even = Folder(2, "Folder_2")
    f_odd = Folder(1, "Folder_1")

    file_linked = File(10, 500)
    files_map = {10: file_linked}

    links = [FolderFileLink(folder_id=2, file_id=10)]

    result = get_linked_files_for_even_folders([f_even, f_odd], files_map, links)

    assert "Folder_2" in result
    assert "Folder_1" not in result
    assert result["Folder_2"][0].file_id == 10
