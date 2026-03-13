import os
import re
from pathlib import Path


def get_required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def update_file(file_path, pattern, replacement):
    temp_path = file_path.with_suffix(".tmp")

    with open(file_path, "r") as fin, open(temp_path, "w") as fout:
        for line in fin:
            fout.write(re.sub(pattern, replacement, line))

    os.replace(temp_path, file_path)


def main():
    build_num = get_required_env("BuildNum")
    source_path = Path(get_required_env("SourcePath"))

    src_dir = source_path / "develop" / "global" / "src"

    sconstruct = src_dir / "SConstruct"
    version = src_dir / "VERSION"

    update_file(
        sconstruct,
        r"point=\d+",
        f"point={build_num}"
    )

    update_file(
        version,
        r"ADLMSDK_VERSION_POINT=\d+",
        f"ADLMSDK_VERSION_POINT={build_num}"
    )


if __name__ == "__main__":
    main()
