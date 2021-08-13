from pathlib import Path

import pipeline


def test_collect_files(tmp_path: Path, monkeypatch):
    # given
    data_dir = tmp_path / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    file = data_dir / "file1.txt"
    file.touch(exist_ok=True)

    monkeypatch.setattr(pipeline, "DATA_DIR", data_dir)
    expect = 1

    # when
    files = pipeline.collect_files("*.txt")
    actual = len(files)

    # then
    assert actual == expect
