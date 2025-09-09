from pathlib import Path


def main() -> None:
    fortunes_path = Path('fortunes.txt')
    with fortunes_path.open('r') as src, Path('one_liners.py').open('w') as dst:
        dst.write('one_liners = [\n')
        for line in src:
            dst.write(f"r'''{line.strip()}''',\n")
        dst.write(']\n')


if __name__ == '__main__':
    main()

