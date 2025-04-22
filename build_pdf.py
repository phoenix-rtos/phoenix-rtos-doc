import os
import sys
import shutil
import subprocess
from pathlib import Path
import argparse

TEMP_DIR = Path("_build/_pdf")
LATEX_BUILD = TEMP_DIR / "latex"


def find_markdown_files(directories, exclude=None):
    exclude_path = Path(exclude).resolve() if exclude else None
    return sorted(
        [
            path
            for directory in directories
            for path in Path(directory).rglob("*.md")
            if not exclude_path or path.resolve() != exclude_path
        ]
    )


def create_index_md(md_files, output_dir):
    index_path = output_dir / "index.md"
    content = [
        "# PDF Documentation",
        "",
        "```{toctree}",
        ":maxdepth: 3",
    ]

    for path in md_files:
        try:
            rel_path = path.relative_to(Path.cwd()).with_suffix("")
        except ValueError:
            rel_path = path.with_suffix("")
        content.append(str(rel_path))

    content.append("```")
    index_path.write_text("\n".join(content), encoding="utf-8")
    return index_path


def prepare_pdf_source(md_files, custom_index=None, base_dirs=None):
    if TEMP_DIR.exists():
        try:
            shutil.rmtree(TEMP_DIR)
            print(f"[INFO] Removed existing {TEMP_DIR}")
        except Exception as e:
            sys.exit(f"[ERROR] Failed to remove {TEMP_DIR}: {e}")

    TEMP_DIR.mkdir(parents=True)
    for src in md_files:
        matched = False
        for base in base_dirs or []:
            base_path = Path(base).resolve()
            try:
                rel_path = src.resolve().relative_to(base_path.parent)
                dest_path = TEMP_DIR / rel_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(src, dest_path)
                matched = True
                break
            except ValueError:
                continue
        if not matched:
            shutil.copy(src, TEMP_DIR / src.name)

    if custom_index:
        shutil.copy(custom_index, TEMP_DIR / "index.md")
    else:
        create_index_md(md_files, TEMP_DIR)

    for file in ["conf.py", "version_management.py"]:
        src = Path(file)
        if src.exists():
            shutil.copy(src, TEMP_DIR)

    for folder in ["_static", "_templates"]:
        src = Path(folder)
        if src.exists():
            shutil.copytree(src, TEMP_DIR / folder)


def insert_authors(authors):
    maketitle_path = TEMP_DIR / "_static/latex/maketitle.tex"
    if not maketitle_path.exists():
        print("[WARN] maketitle.tex not found — skipping LaTeX title modification.")
        return

    content = maketitle_path.read_text(encoding="utf-8")

    insert_block = rf"""
\vspace{{1cm}}

\begin{{flushright}}
    {{\setmainfont{{Liberation Sans}}
    \textcolor{{ps-darkblue}}{{%
        \fontsize{{12}}{{14}}\selectfont Authors: {authors}
    }} }}
\end{{flushright}}
"""

    marker = r"""% Orange line below bottom blocks
\begin{center}
    \color{ps-orange}\rule{\textwidth}{2pt}
\end{center}"""

    if marker not in content:
        print("[WARN] Marker for orange line not found in maketitle.tex — cannot insert author block.")
        return

    updated_content = content.replace(marker, insert_block + "\n" + marker)

    maketitle_path.write_text(updated_content, encoding="utf-8")
    print(f"[INFO] Inserted authors into maketitle.tex: {authors}")


def insert_title(title):
    maketitle_path = TEMP_DIR / "_static/latex/maketitle.tex"
    if not maketitle_path.exists():
        print("[WARN] maketitle.tex not found — skipping title modification.")
        return

    content = maketitle_path.read_text(encoding="utf-8")

    marker_start = r"\textcolor{ps-darkblue}{%"
    marker_match = r"{\fontsize{28}{36}\selectfont \textbf{Phoenix-RTOS Documentation}}"

    if marker_match not in content:
        print("[WARN] Default title line not found — skipping title replacement.")
        return

    new_title_block = rf"{{\fontsize{{28}}{{36}}\selectfont \textbf{{{title}}}}}"

    updated_content = content.replace(marker_match, new_title_block)
    maketitle_path.write_text(updated_content, encoding="utf-8")

    print(f"[INFO] Replaced title in maketitle.tex with: {title}")


def run_cmd(cmd, cwd=None, verbose=False):
    try:
        subprocess.run(
            cmd,
            cwd=cwd,
            check=True,
            stdout=None if verbose else subprocess.DEVNULL,
            stderr=None if verbose else subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        sys.exit(f"[ERROR] Command failed: {' '.join(cmd)}\n{e}")


def build_latex_pdf(output_pdf_name, verbose=False):
    run_cmd(["sphinx-build", "-b", "latex", str(TEMP_DIR), str(LATEX_BUILD)], verbose=verbose)
    run_cmd(["make", "all-pdf"], cwd=LATEX_BUILD, verbose=verbose)

    default_pdf = LATEX_BUILD / "phoenix-rtos.pdf"
    final_pdf = LATEX_BUILD / output_pdf_name
    if default_pdf.exists():
        default_pdf.rename(final_pdf)
        print(f"[INFO] Renamed output to {output_pdf_name}")
    else:
        print("[WARN] Default PDF not found — build may have failed.")
    return final_pdf


def main():
    parser = argparse.ArgumentParser(description="Build Phoenix-RTOS PDF from Markdown sources.")
    parser.add_argument("input_dirs", nargs="+", help="Folders containing .md files")
    parser.add_argument("-i", "--index", help="Path to custom index.md (with toctree)")
    parser.add_argument("-o", "--output", help="Output PDF file name", default="phoenix-rtos.pdf")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show LaTeX output")
    parser.add_argument("-a", "--authors", help="Author(s) to appear on the title page")
    parser.add_argument("-t", "--title", help="Custom title to appear on the title page")

    args = parser.parse_args()

    md_files = find_markdown_files(args.input_dirs, exclude=args.index)
    if not md_files and not args.index:
        sys.exit("[ERROR] No markdown files found.")

    print(f"[INFO] Found {len(md_files)} markdown files:")
    for f in md_files:
        print(" -", f)

    if args.index:
        print(f"[INFO] Using custom index: {args.index}")
    print(f"[INFO] Output PDF will be named: {args.output}")

    prepare_pdf_source(md_files, args.index, base_dirs=args.input_dirs)

    if args.authors:
        insert_authors(args.authors)
    if args.title:
        insert_title(args.title)

    final_pdf = build_latex_pdf(args.output, args.verbose)

    print(f"\n[✔] Done! PDF generated at: {final_pdf}")


if __name__ == "__main__":
    main()
