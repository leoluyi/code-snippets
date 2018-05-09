# [Python] How to manage your Python projects with Pipenv

- https://github.com/pypa/pipenv
- http://pipenv-ja.readthedocs.io/ja/latest/index.html
- https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv
- https://medium.com/@jllorencetti/my-somewhat-pragmatic-approach-towards-pipenv-62bd5396ffdd
- https://medium.com/@dboyliao/python-相依管理-f7d89dfe917b
- https://www.youtube.com/watch?v=tRmmjlVHzno&t=301s

### Get Started

Install Pipenv

```
$ pip install pipenv
```

> For MacOS, use `.bashrc` to let `pipenv shell` use your custom bash settings
> in a nonlogin interactive shell:
> 
> ```
> $ cp ${HOME}/.bash_profile ${HOME}/.bashrc
> ```

Then change directory to the folder containing your Python project and initiate Pipenv, 

```
$ cd my_project
$ pipenv install
```

This will create two new files, `Pipfile` and `Pipfile.lock`, in your project directory, and a new virtual environment for your project if it doesn’t exist already.

To install a Python package for your project use the install keyword. For example,

```
$ pipenv install beautifulsoup4
```

Unsinstall packages

```
$ pipenv uninstall beautifulsoup4
```

The package name, together with its version and a list of its own dependencies, can be frozen by updating the `Pipfile.lock`.

```
$ pipenv lock
```

Now suppose we decide that its time to update our dependencies to their latest version. You just need to `pipenv lock` the dependencies again.

It’s worth adding the `Pipfiles` to your Git repository, so that if another user were to clone the repository, all they would have to do is install Pipenv on their system and then type `pipenv install`.

### Managing your development environment

There are usually some Python packages that are only required in your development environment and not in your production environment, such as `unit testing` packages. Pipenv will let you keep the two environments separate using the `--dev` flag. For example,

```
$ pipenv install --dev pytest
Installing pytest...
...
Adding pytest to Pipfile's [dev-packages]...
```

will install `pytest`, but will also associate it as a package that is only required in your development environment. The `pytest` package won’t be installed by default using `pipenv install`.

If another developer were to clone your project into their own development environment, they could use the --dev flag,

```
$ pipenv install --dev
```

### Running your code

In order to activate the virtual environment associated with your Python project you can simply use the shell keyword,

```
$ pipenv shell
```

You can also invoke shell commands in your virtual environment, without explicitly activating it first, by using the run keyword. For example,

```
$ pipenv run which python
```

will run the which python command in your virtual environment. This feature is a neat way of running your own Python code in the virtual environment,

```
$ pipenv run python my_project.py
```

If you shudder at having to type so much every time you want to run Python, you can always set up an alias in your shell, such as,

```
$ alias prp="pipenv run python"
```

### Misc

Locate the project:

```
$ pipenv --where
/Users/kennethreitz/Library/Mobile Documents/com~apple~CloudDocs/repos/kr/pipenv/test
```

Locate the virtualenv:

```
$ pipenv --venv
/Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre
```

Locate the Python interpreter:

```
$ pipenv --py
/Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre/bin/python
```


### Python integration

If you have `pyenv` installed, `pipenv` integrates with it and can install the required version described in the `Pipfile`

https://github.com/pypa/pipenv/issues/1549

Pyenv global:

- `Anaconda`: pipenv does not work for anaconda virtualenv
- Use `3.6.5` instead


### Pipfile and Pipfile.lock, our “requirements.txt 2.0”.

- `Pipfile`: is where you declare the required Python version, the packages used in your production and development environment and their source, e.g. PyPI, PackageCloud, etc.
- `Pipfile.lock`: where all of all packages versions are pinned, along with a bunch of other information, like the hashes of each package.

