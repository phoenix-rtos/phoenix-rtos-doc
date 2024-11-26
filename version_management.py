import subprocess
import re
from packaging import version
from typing import List, Tuple


class VersionManager:
    def __init__(self, min_version: str, max_versions: int = 3):
        self.min_version = min_version
        self.max_versions = max_versions
        # Pattern to match versioning (with or without 'v' prefix)
        self.version_pattern = re.compile(r"^v?\d+\.\d+\.\d+$")

    def get_git_tags(self) -> List[str]:
        """Get all git tags from the repository."""
        try:
            result = subprocess.run(
                ["git", "tag"], capture_output=True, text=True, check=True
            )
            return result.stdout.strip().split("\n")
        except subprocess.CalledProcessError:
            return []

    def is_valid_version(self, tag: str) -> bool:
        """
        Check if the tag matches versioning pattern.
        """
        return bool(self.version_pattern.match(tag))

    def filter_and_sort_versions(self, tags: List[str]) -> List[str]:
        """
        Filter versions >= min_version and sort them in descending order.
        Removes 'v' prefix if present and ignores non-semantic versioning tags.
        """
        valid_versions = []

        for tag in tags:
            if not self.is_valid_version(tag):
                continue

            clean_version = tag.lstrip("v")

            try:
                if version.parse(clean_version) >= version.parse(self.min_version):
                    valid_versions.append(clean_version)
            except version.InvalidVersion:
                continue

        return sorted(valid_versions, key=version.parse, reverse=True)

    def generate_version_tuples(self, versions: List[str]) -> List[Tuple[str, str]]:
        """
        Generate version tuples for html_context in Sphinx configuration.
        Always includes 'latest' and up to max_versions recent versions.
        """
        result = [("latest", "/")]

        for ver in versions[: self.max_versions]:
            result.append((ver, f"/{ver}/"))

        return result

    def get_version_context(self) -> tuple:
        """
        Generate the version context for Sphinx configuration.
        """
        tags = self.get_git_tags()
        filtered_versions = self.filter_and_sort_versions(tags)
        version_tuples = self.generate_version_tuples(filtered_versions)
        return tuple(version_tuples)


def get_version_context(min_version: str = "3.3.0", max_versions: int = 3) -> tuple:
    manager = VersionManager(min_version, max_versions)
    return manager.get_version_context()
