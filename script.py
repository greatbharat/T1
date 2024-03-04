import git
import os
import datetime
from dateutil.parser import parse  # For flexible date parsing

def commit_with_custom_date(repo_path, file_path, commit_message, commit_date):
    """
    Commits a file to a Git repository with a specified commit date.

    Args:
        repo_path (str): Path to the Git repository.
        file_path (str): Path to the file to be committed.
        commit_message (str): The commit message.
        commit_date (str or datetime.datetime): The desired commit date. 
                                             Can be a string (e.g., '2023-12-25 10:00')
                                             or a datetime object.
    """

    repo = git.Repo(repo_path)

    # Input validation
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if isinstance(commit_date, str):
        try:
            commit_date = parse(commit_date)  # Try to parse from string
        except ValueError:
            raise ValueError(f"Invalid commit date format: {commit_date}")

    # Ensure commit_date is a datetime object
    if not isinstance(commit_date, datetime.datetime):
        raise TypeError(f"commit_date must be a string or datetime.datetime object")

    # Stage the file
    repo.index.add([file_path])

    # Get the current author info (adjust if needed)
    author = repo.config_reader().get_value('user', 'name')
    email = repo.config_reader().get_value('user', 'email')

    # Commit with custom date using environment variables
    repo.index.commit(
        commit_message,
        author=author,
        email=email,
        env={
            "GIT_AUTHOR_DATE": commit_date.isoformat(),
            "GIT_COMMITTER_DATE": commit_date.isoformat()
        }
    )

commit_with_custom_date()