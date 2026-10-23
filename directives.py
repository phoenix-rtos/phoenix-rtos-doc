#
# Custom Sphinx directives
#
# Copyright 2026 Phoenix Systems
# Author: Adam Greloch
#
# SPDX-License-Identifier: BSD-3-Clause
#

import uuid
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class ShellTranscript(Directive):
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
    prompts. This also works for multi-line commands.

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
    """

    has_content = True
    shell_classes = ["root", "user", "psh"]

    option_spec = {
        "hide-output": directives.flag,
    }

    def run(self):
        container = nodes.container(classes=["shell-transcript"])
        hide_output = "hide-output" in self.options

        current_output_group = None

        for line in self.content:
            line = line.rstrip()

            css_class = "plain"
            text = line

            for shell_class in self.shell_classes:
                prefix = f"[{shell_class}] "
                if line.startswith(prefix):
                    css_class = shell_class
                    text = line[len(prefix) :]
                    break

            node = nodes.container(classes=["shell-line", css_class])
            node += nodes.inline(text, text)

            if css_class != "plain":
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

                        toggle_id = f"shell-toggle-{uuid.uuid4().hex[:8]}"

                        html = f"""
                        <input type="checkbox" id="{toggle_id}" class="shell-toggle-checkbox" autocomplete="off" />
                        <label for="{toggle_id}" class="shell-toggle-label"></label>
                        """
                        current_output_group += nodes.raw("", html, format="html")

                    current_output_group += node
                else:
                    container += node

        if current_output_group is not None:
            container += current_output_group

        return [container]
