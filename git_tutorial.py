print("hello this is a tutorial on git commands")

#BASIC COMMANDS TO CHANGE THE FILE STATUS
#git init --> to make any repo a git repo
#git status  --> to check which files are staged or not
#git add .  --> to push all files in the staged area
#git commit -m "some meaningful message"  --> to commit all files in the staged area
#git commit -a -m "some meaningful message"  --> to commit all files directly from working area 

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
#git log --pretty=short --> shows the change in commits in a single line

#git branch <brach_name>  --> to create a branch
#git checkout <branch_name>  --> to navigate to the branch
#git checkout -b <branch_name>  --> to create a branch and move into it
# #sgs