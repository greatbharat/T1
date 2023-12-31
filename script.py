import git
import os
# import datetime
from datetime import timezone, datetime
from dateutil.parser import parse  # For flexible date parsing

def commit_with_custom_date(repo_path, file_path, commit_message, commit_date):
    """
    Commits a file to a Git repository with a specified commit date.

    Args:
        repo_path (str): Path to the Git repository.
        file_path (str): Path to the file to be committed.
        commit_message (str): The commit message.
        commit_date (str or datetime): The desired commit date. 
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
    if not isinstance(commit_date, datetime):
        raise TypeError(f"commit_date must be a string or datetime object")

    # Stage the file
    repo.index.add([file_path])

    # Get the current author info (adjust if needed)
    author = "bg"
    email = "one@gmail.com"

    # Commit with custom date using environment variables
    # Commit with custom date using environment variables
    committer = git.Actor(author, email)  # Create a committer object
    repo.index.commit(
        commit_message,
        author_date=commit_date,  # Use 'author_date'
        commit_date=commit_date,  # Use 'committer_date'
        committer=committer  # Pass the committer object
    )
# commit_with_custom_date("/workspaces/T1", "a.py", "testing", commit_date=datetime.datetime(2023, 12, 31, 20, 30) )

commit_with_custom_date(
    repo_path="/workspaces/T1",
    file_path="b.txt",
    commit_message="Implemented new feature X",
     commit_date = datetime(2023, 12, 31, 20, 30, tzinfo=timezone.utc)
)