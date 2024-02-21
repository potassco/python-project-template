## Deployment

To release this project on (test.)pypi.org please follow these instructions:

Long version:
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
TL;DR
 - create a github environmnent (Github->Your Project->Settings->Environments) with the safety regulations you prefer, e.g. restriction
   to a fixed set of branches like "test_release" or manual confirmation
   This step is important to prevent other people from releasing new versions on accident
 - create a [test.]pypi.org account (enable 2fa)
 - create a project with the same name
 - add the formerly created github environment
 - run the respective CI scripts either manually (test.pypi.org) or by tagging a release version (pypi.org)

[nox]: https://nox.thea.codes/en/stable/index.html
[pipx]: https://pypa.github.io/pipx/
[pre]: https://pre-commit.com/
[editable]: https://setuptools.pypa.io/en/latest/userguide/development_mode.html


