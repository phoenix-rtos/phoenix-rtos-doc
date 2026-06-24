from docutils import nodes
from docutils.parsers.rst import Directive


class ShellTranscript(Directive):
    has_content = True
    shell_classes = ["root", "user", "psh"]

    def run(self):
        container = nodes.container(classes=["shell-transcript"])

        for line in self.content:
            line = line.rstrip()

            css_class = "plain"
            text = line

            for shell_class in self.shell_classes:
                prefix = f"[{shell_class}] "
                if line.startswith(prefix):
                    css_class = shell_class
                    text = line[len(prefix):]
                    break

            node = nodes.container(classes=["shell-line", css_class])
            node += nodes.inline(text, text)
            container += node

        return [container]
