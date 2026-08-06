# PDF Template

Paste your main MD file here and place all the needed attachments in this directory.

<!--
1. For the structure with all .md files in the directory (without nesting),
 markdowns above the index.md should be listed as follows:
```{toctree}
:maxdepth: n
file1.md
file2.md
file3.md
```
The maxdepth parameter determines how many levels in the hierarchy 
will be shown in the table of contents.

2. For the nested structure, all the internal directories 
should include index.md that have to be listed as follows:
```{toctree}
:maxdepth: n
dir1/index.md
dir2/index.md
dir3/index.md
```

3. When some files are not intended to be visible in the PDF document 
they just should not be placed in {toctree}. 
When the whole directory is not intended be included in PDF, 
it can be added to exclude_patterns in conf.py

4. Icons such as ✅ ❌ ⚠️ 🔴 🟡 🟢 🔶 ⏭ can be used directly in the text,
docsresources draws them with the glyphs of the fonts it declares, so that they
stay characters of the PDF. See icons.py of that package for the whole supported
set. An icon which is missing there has to be mapped in conf.py, otherwise it is
dropped from the PDF, for example:
```python
from phoenixsystems.docsresources.icons import Icon

latexpdf_icons = {"🔒": Icon(color="ps-darkblue")}
```

5. The cells of a table are aligned to the left and to the top, which is what
the tables holding descriptions need. A table of short values looks better
with its cells centered both ways, which the \psC column type of docsresources
does. It takes the width of the column as a fraction of the width of the table
and is passed by the {tabularcolumns} directive, applying to the table that
follows it and replacing the :widths: option of that table:

    ```{tabularcolumns} |\psC{18}{100}|\psC{24}{100}|\psC{29}{100}|\psC{29}{100}|
    ```

6. For more information visit the Sphinx Documentation (https://www.sphinx-doc.org/en/master/)
-->
