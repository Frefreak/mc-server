import os
import json
import argparse
from pathlib import Path

import nbtlib


class RelaxedParser(nbtlib.Parser):
    def collect_tokens_until(self, token_type):
        while True:
            try:
                yield from super().collect_tokens_until(token_type)
                return
            except nbtlib.InvalidLiteral as exc:
                if exc.args[1].startswith("Expected comma"):
                    yield self.current_token


texts = {}


def extract(file_path, input_folder):
    with open(file_path) as f:
        snbt = f.read()
        obj = RelaxedParser(nbtlib.tokenize(snbt)).parse()

    def ext_(o, prefix):
        if not isinstance(o, dict):
            return
        key = prefix
        for field in ["title", "command", "Name", "text"]:
            if field in o:
                p = key + f".{field}"
                if p in texts:
                    raise Exception(f"key exists: {p}")
                texts[p] = o[field]
                o[field] = "{" + p + "}"
        if "subtitle" in o:
            p = key + ".subtitle"
            if isinstance(o["subtitle"], str):
                if p in texts:
                    raise Exception(f"key exists: {p}")
                texts[p] = o["subtitle"]
                o["subtitle"] = "{" + p + "}"
            elif isinstance(o["subtitle"], list):
                for i, subt in enumerate(o["subtitle"]):
                    if not isinstance(subt, str):
                        raise Exception("unexpected type for subtitle list")
                    pp = p + f".{str(i)}"
                    if pp in texts:
                        raise Exception(f"key exists: {pp}")
                    texts[pp] = subt
                    o["subtitle"][i] = "{" + pp + "}"
            else:
                raise Exception("unexpected type for subtitle")
        for field in ["quests", "tasks", "rewards", "chapter_groups"]:
            if field in o:
                for i, q in enumerate(o[field]):
                    ext_(q, key + f".{field}.{i}")
        if "description" in o:
            for i, line in enumerate(o["description"]):
                if line != "":
                    k = key + ".desc." + str(i)
                    if k in texts:
                        raise Exception(f"key exists: {k}")
                    texts[k] = line
                    o["description"][i] = "{" + k + "}"
        for k, v in o.items():
            if isinstance(v, dict):
                ext_(v, key + f".{k}")

    uniq = os.path.relpath(file_path, input_folder)
    cat = rel_path_to_key(uniq)
    ext_(obj, f"quest.{cat}")
    ooo = output_dict(obj)
    return ooo


def rel_path_to_key(rel_path):
    path_without_ext = os.path.splitext(rel_path)[0]
    path_parts = os.path.normpath(path_without_ext).split(os.sep)
    key = ".".join(path_parts)
    return key


parser = argparse.ArgumentParser(
    description="This program will read files in original ftbquests folder and output "
    "a new folder with text value replaced by key. It will also create a en_us.json "
    "file under the current folder that should be put in kubejs/assets/kubejs/lang folder"
)
parser.add_argument("input_folder", help="Specify original ftbquests folder")
parser.add_argument(
    "output_folder",
    help="Specify output folder that can substitute the original folder later",
)
parser.add_argument(
    "--lang-file",
    default="en_us.json",
    help="Specify lang output file",
)


def output_dict(data):
    tab = "\t"

    def print_(s, end="\n"):
        return s + end

    def print_value(value, indent=0):
        ss = ""
        if isinstance(value, dict):
            ss += print_(f"{{")
            for k, v in value.items():
                ss += print_(
                    f"{tab * (indent+1)}{json.dumps(k, ensure_ascii=False)}: ", end=""
                )
                ss += print_value(v, indent + 1)
            ss += print_(f"{tab * indent}}}")
        elif isinstance(value, list):
            ss += print_("[")
            for item in value:
                ss += print_(f"{tab * (indent+1)}", end="")
                ss += print_value(item, indent + 1)
            ss += print_(f"{tab * (indent)}]")
        elif isinstance(value, str):
            ss += print_(f"{json.dumps(value, ensure_ascii=False)}")
        elif isinstance(value, float):
            ss += print_(f"{float(value)}d")
        elif isinstance(value, nbtlib.Byte):
            ss += print_(f"{int(value)}b")
        elif isinstance(value, int):
            v = int(value)
            if v <= 2**31:
                ss += print_(f"{int(value)}")
            else:
                ss += print_(f"{int(value)}L")
        else:
            ss += print_(f"{value}")
        return ss

    return print_value(data)


def main():
    args = parser.parse_args()
    input_folder = args.input_folder
    output_folder = args.output_folder
    lang_file = args.lang_file
    print(f"{input_folder=}")
    print(f"{output_folder=}")
    print(f"{lang_file=}")

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".snbt"):
                input_file_path = Path(root, file)
                output_file_path = output_folder / input_file_path.relative_to(
                    input_folder
                )
                output_file_path.parent.mkdir(parents=True, exist_ok=True)

                new_content = extract(input_file_path, input_folder)

                with output_file_path.open("w") as output_file:
                    output_file.write(new_content)

    with open(lang_file, "w") as f:
        json.dump(texts, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
