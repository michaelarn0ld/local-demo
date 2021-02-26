## Getting an existing repository from github to local machine

git clone (url) ---------------> this clones an existing remote repo down to my local machine

## Creating a repository locally and then adding a remote to push/pull from

git init -----------> initalize git in the working directory
git remote add origin (url) -------------> url is from a blank repository created on github

## Adding and committing files to the github repository

git add [. or filename.extension] -----------> adds all files or a specific file to the commit
git commit -m "some message" -------> prepares the file(s) to be committed and adds a descriptive message of changes made
git push -u origin master ---------> pushes files to origin (github repo) on the master branch
git push -------------> once we have set the upstream with -u then future pushes dont need 'origin master'

## Creating a new branch for features and updates to the master branch

git checkout -b feature -------------> creates a new branch in the repo and sets you to it
git push origin feature -------------> once you are ready, you can push the branch to a new branch in github

<!-- Now we will make a pull request from github to review the feature, comment on it, and merge to the master branch -->

## Update your local repository so that it is consistent with the github repository

git checkout master -------------> ensure that you are on the master branch locally
git pull -------------> this updates the master branch locally to any changes that are on the github repo

## Delete feature branches from the local repository and remote repository after merging

git branch -d feature -------------> deletes the branch locally
git push origin --delete feature -------------> deletes the branch on the remote repo
