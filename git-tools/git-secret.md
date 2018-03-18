# git-secret: A bash-tool to store your private data inside a git repository

- https://github.com/sobolevn/git-secret
- http://git-secret.io/
- https://help.github.com/articles/generating-a-new-gpg-key/

1. Before starting, make sure you have created gpg RSA key-pair: public and secret key identified by your email address. `LANG=en gpg --full-generate-key`
2. Initialize `git-secret` repository by running `git secret init` command. `.gitsecret/` folder will be created, note that `.gitsecret/` folder should not be ignored.
3. Add first user to the system by running `git secret tell your@gpg.email`.
4. Now it’s time to add files you wish to encrypt inside the git-secret repository. It can be done by running `git secret add <filenames...>` command. Make sure these files are ignored, otherwise git-secret won’t allow you to add them, as these files will be stored unencrypted.
5. When done, run `git secret hide` all files, which you have added by `git secret add` command will be encrypted with added public-keys by the `git secret tell` command. Now it is safe to commit your changes. **But**. It’s recommended to add `git secret hide` command to your `pre-commit` hook, so you won’t miss any changes.
6. Now decrypt files with `git secret reveal` command. It will ask you for your password. And you’re done!

```sh
$ git init
$ git secret init
$ git secret tell -m   # Add person who knows the secret
                       # `-m` takes your current `git config user.email` as an 
                       # identifier for the key.
$ echo "key.txt" .gitignore  # Ignore original secret file
$ git secret add "key.txt"
$ git secret hide
$ rm "key.txt"  # Remove secret file
$ git add "key.txt" "key.txt.secret" && git commit -m "Encrypt secret file"
```

## Setting git pre-commit hooks

https://www.atlassian.com/git/tutorials/git-hooks

```
$ cd .git/hooks
```

## GPG 的雷

#### Key generation failed: Timeout

```
gpg: agent_genkey failed: Timeout
Key generation failed: Timeout
```

Solution:

```
rm -rf ~/.gnupg
```

