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

4. For more information visit the Sphinx Documentation (https://www.sphinx-doc.org/en/master/)
-->
