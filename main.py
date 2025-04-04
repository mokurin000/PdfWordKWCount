import os
from pathlib import Path
from multiprocessing import Pool

from pdftotext import PDF


INPUT_DIR = "./input"


def process_report(filename: str | Path):
    filename = Path(filename)
    txt_path = filename.with_suffix(".txt")

    with open(filename, "rb") as f:
        pdf = PDF(f)
        text = "\n".join(pdf)
    with open(txt_path, encoding="utf-8", mode="w") as out:
        out.write(text)


def main():
    with Pool() as pool:
        pool.map(
            process_report,
            filter(
                lambda fn: fn.endswith(".pdf"),
                map(lambda s: os.path.join(INPUT_DIR, s), os.listdir(INPUT_DIR)),
            ),
        )


if __name__ == "__main__":
    main()
