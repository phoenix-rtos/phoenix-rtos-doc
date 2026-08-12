#
# Custom Sphinx directives
#
# Copyright 2026 Phoenix Systems
# Author: Adam Greloch
#
# SPDX-License-Identifier: BSD-3-Clause
#

import html

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.docutils import SphinxDirective


class ShellTranscript(SphinxDirective):
    """
    Example:

    ```{shell-transcript}
    [user] rm -rf /
    rm: it is dangerous to operate recursively on '/'
    rm: use --no-preserve-root to override this failsafe
    [root] rm -rf /
    rm: congratulations, you won
    ```

    Sphinx will transform this block so that the [user]/[root]/[psh]
    placeholders get replaced with non-selectable "user $"/"root #"/"(psh)%"
    prompts. This also works for multi-line commands, as long as each line
    except the last one ends with a backslash.

    Additionally, passing the `:hide-output:` to the block:

    ```{shell-transcript}
    :hide-output:
    [user] cat /dev/urandom
    42
    ```

    Will cause the outputs to be hidden (via HTML checkboxes) under "[show
    output]" in the HTML code block. Useful for long output examples. In
    case of multiple commands, each command will get its own corresponding
    button.

    In HTML, the block gets a copy button that copies only the commands,
    without prompts and outputs.
    """

    has_content = True
    shell_prompts = {
        "root": "root # ",
        "user": "user $ ",
        "psh": "(psh)% ",
    }

    option_spec = {
        "hide-output": directives.flag,
    }

    def run(self):
        wrapper = nodes.container(classes=["shell-transcript-wrapper"])
        container = nodes.container(classes=["shell-transcript"])
        # Keep "--" and quotes intact
        container["support_smartquotes"] = False
        hide_output = "hide-output" in self.options

        current_output_group = None
        commands = []
        in_continuation = False

        for line in self.content:
            line = line.rstrip()

            css_class = "continuation" if in_continuation else "plain"
            text = line

            for shell_class in self.shell_prompts:
                prefix = f"[{shell_class}] "
                if line.startswith(prefix):
                    css_class = shell_class
                    text = line[len(prefix) :]
                    break

            node = nodes.container(classes=["shell-line", css_class])
            if css_class in self.shell_prompts:
                prompt = self.shell_prompts[css_class]
                node += nodes.inline(prompt, prompt, classes=["prompt"])
            node += nodes.inline(text, text)

            if css_class != "plain":
                commands.append(text)
                in_continuation = text.endswith("\\")

                if current_output_group is not None:
                    container += current_output_group
                    current_output_group = None

                container += node
            else:
                if hide_output:
                    if current_output_group is None:
                        current_output_group = nodes.container(
                            classes=["shell-output-group"]
                        )

                        toggle_id = f"shell-toggle-{self.env.new_serialno('shell-toggle')}"

                        toggle_html = f"""
                        <input type="checkbox" id="{toggle_id}" class="shell-toggle-checkbox" autocomplete="off" />
                        <label for="{toggle_id}" class="shell-toggle-label"></label>
                        """
                        current_output_group += nodes.raw("", toggle_html, format="html")

                    current_output_group += node
                else:
                    container += node

        if current_output_group is not None:
            container += current_output_group

        # Hidden plain-text copy of the commands for sphinx-copybutton
        copy_text = html.escape("\n".join(commands))
        copy_html = f'<pre class="shell-transcript-copy" hidden>{copy_text}</pre>'
        wrapper += nodes.raw("", copy_html, format="html")
        wrapper += container

        return [wrapper]


class ShellTranscriptToLiteral(SphinxPostTransform):
    """
    Replaces shell-transcript wrappers with plain literal blocks in LaTeX
    builds. The container-based layout relies on CSS, so without it the lines
    would get merged into a single paragraph with collapsed whitespace.
    """

    default_priority = 200
    builders = ("latex",)

    def run(self, **kwargs):
        for container in list(self.document.findall(nodes.container)):
            if "shell-transcript-wrapper" not in container["classes"]:
                continue

            lines = [
                "".join(child.astext() for child in line.children)
                for line in container.findall(nodes.container)
                if "shell-line" in line["classes"]
            ]
            text = "\n".join(lines)

            literal = nodes.literal_block(text, text)
            literal["language"] = "text"
            literal.source, literal.line = container.source, container.line
            container.replace_self(literal)
