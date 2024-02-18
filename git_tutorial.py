print("hello this is a tutorial on git commands")

#BASIC COMMANDS TO CHANGE THE FILE STATUS
#git init --> to make any repo a git repo
#git status  --> to check which files are staged or not
#git add .  --> to push all files in the staged area
#git commit -m "some meaningful message"  --> to commit all files in the staged area
#git commit -a -m "some meaningful message"  --> to commit all files directly from working area 
#rm -rf .git   --> to delete the git repository

#IGNORING FILES
#.gitignore  -->inside this file you can add any files/folders which you want to ignore while staging
# if you want to ignore a file already being tracked by Git, you need to untrack it using:
#git rm --cached <file_name>

#COMPARING FILES IN DIFFERENT AREAS
#git diff  -> compares files from working tree to the staging area
#git diff --staged  -> compares working tree to the last commit

#VIEWING AND CHANGING COMMITS 
#git log --stat   --> shows the changes in all commits a/c to change in lines
#git log -p       --> shows the change in all commits with diff
#git log --pretty=oneline --> shows the change in commits in a single line

#UNSTAGING AND UNMODIFYING FILES 
#git restore --staged <file_name>  --> to remove any file from the staged area
#git checkout <file_name>  --> to restore a file from the last commit
#git checkout -f  --> to restore all files from the last commit


#WORKING WITH REMOTE REPOS
#After making a repo in github run the following command
#git remote add origin_1 https://github.com/aayushsynth/My_Second_Repository.git  -->to link your git repo with your local directory through origin_1
#Here the name origin_1 and the url may change a/c to the project
#git push -u origin_1 master  --> to push the branch "master" from local repo to github (origin_1)


#BRANCHING IN GIT
#git branch <brach_name>  --> to create a branch
#git checkout <branch_name>  --> to navigate to the branch
#git checkout -b <branch_name>  --> to create a branch and move into it
#git branch -v  --> shows the commit id and last commit message of all branches
#git branch --merged  --> shows all the branches that are merged already
#git branch --no-merged  --> shows all the branches that are not merged already
#git branch -d <branch_name>  --> to delete a branch
#git push -d origin <branch_name>  --> to delete <branch_name> from github

#MERGING TWO BRANCHES
#git merge <branch_name>  --> to merge <branch_name> in the current branch you are in
