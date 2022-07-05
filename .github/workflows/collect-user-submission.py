import json
import os
import typing

import frontmatter
import pydantic
from markdown_it import MarkdownIt


class Submission(pydantic.BaseModel):
    repo: str


@pydantic.dataclasses.dataclass
class IssueInfo:
    gh_event_path: pydantic.FilePath
    submission: Submission = pydantic.Field(default=None)

    def __post_init_post_parse__(self):
        with open(self.gh_event_path) as f:
            self.data = json.load(f)

    def create_submission(self):
        self._get_inputs()
        self._create_submission_input()
        return self

    def _get_inputs(self):
        self.repo = self.data['repo-root-name']

    def _create_submission_input(self):
        md = MarkdownIt()
        inputs = None
        for token in md.parse(self.body):
            if token.tag == 'code':
                inputs = frontmatter.loads(token.content).metadata
                break
        repo = inputs.get('repo-root-name')
        self.submission = Submission(repo=repo)


if __name__ == '__main__':

    issue = IssueInfo(gh_event_path=os.environ['GITHUB_EVENT_PATH']).create_submission()
    inputs = issue.submission.dict()
    with open('gallery-submission-input.json', 'w') as f:
        json.dump(inputs, f)