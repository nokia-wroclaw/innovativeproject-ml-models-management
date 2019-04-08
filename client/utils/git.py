import git


class GitProvider:
    """Provides an interface for interacting with git repositories.
    
    :param path: path to the repository. If not given, GitPython will
    traverse the parent directories in search for a match.
    """

    def __init__(self, path: str = None):
        self._specified_path = path
        self._repo = None

    @property
    def repository(self) -> object:
        """Returns the GitPython object of a selected repository."""

        if not self._repo:
            if self._specified_path:
                repo = git.Repo(self._specified_path)
            else:
                repo = git.Repo(search_parent_directories=True)

            # assert not repo.bare
            self._repo = repo
        return self._repo

    @property
    def active_branch(self) -> str:
        """Returns the name of the active branch."""

        return self.repository.active_branch.name

    @property
    def latest_commit(self) -> str:
        """Returns the hash of a latest commit in the active branch."""

        return self.repository.head.object.hexsha

    @property
    def is_dirty(self) -> bool:
        """Checks whether there are uncommited changes in the repository."""

        return self.repository.is_dirty()

    def remotes(self, include_name=True, include_url=True) -> list:
        """Retrieves a list of remotes defined in the repository.
        
        :param include_name: whether to include the names of remotes
        :param include_url: whether to include the urls of remotes
        :returns: a list of remotes in a requested schema"""

        if not include_name and not include_url:
            raise Exception

        output = []
        remotes = self.repository.remotes
        for remote in remotes:
            entry = []
            if include_name:
                entry.append(remote.name)
            if include_url:
                entry.append(remote.url)

            output.append(entry)

        return output
