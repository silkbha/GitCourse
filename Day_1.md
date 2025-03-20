# Collaborative Document Day 1

2025-03-18-ds-cr-TU-Delft

Welcome to The Workshop Collaborative Document.

This Document is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents.

----------------------------------------------------------------------------


This is the Document for today: https://edu.nl/qfvt9

Collaborative Document day 1: https://edu.nl/qfvt9

Collaborative Document day 2: https://edu.nl/gw98c


##  🫱🏽‍🫲🏻 Code of Conduct

Participants are expected to follow these guidelines:
* Use welcoming and inclusive language.
* Be respectful of different viewpoints and experiences.
* Gracefully accept constructive criticism.
* Focus on what is best for the community.
* Show courtesy and respect towards other community members.

 If you feel that the code of conduct is breached, please talk to one of the instructors (if the complaint is for one of the participants) or send an email to training@esciencecenter.nl (if the complaint is for one of the instructors).
 
## ⚖️ License

All content is publicly available under the Creative Commons Attribution License: [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/).

## 🙋Getting help

To ask a question, just raise your hand.

If you need help from a helper, place a pink post-it note on your laptop lid. A helper will come to assist you as soon as possible.

## 🖥 Workshop website

[link](https://esciencecenter-digital-skills.github.io/2025-03-18-ds-cr-TU-Delft)

🛠 Setup

[Day 1](https://carpentries-incubator.github.io/collaborative-git-and-github-lesson/#software-setup)
[Day 2](https://carpentries-incubator.github.io/good-practices-lesson/#software-setup)


## 👩‍🏫👩‍💻🎓 Instructors

Lucas Esclapez, Olga Lyashevska

## 🧑‍🙋 Helpers

Heather Andrews, Carlos Utrilla Guerrero, Leila Inigo de la Cruz, Yasel Quintero, Selin Kubilay


## 🗓️ Agenda
| Topic                             |  Time |
|:--------------------------------- | -----:|
|                                   |       |
| Welcome and icebreaker            | 09:30 |
| Workshop Introduction             | 09:45 |
| Version control with Git          | 10:00 |
| Coffee break                      | 10:30 |
| Version control with Git          | 10:45 |
| Coffee break                      | 11:30 |
| Version control with Git          | 11:45 |
| Lunch Break                       | 12:30 |
| Collaboration with Git and GitHub | 13:30 |
| Coffee break                      | 14:15 |
| Collaboration with Git and GitHub | 14:30 |
| Coffee break                      | 15:15 |
| Collaboration with Git and GitHub | 15:30 |
| Wrap-up                           | 16:15 |
| END                               | 16:30 |

## 🏢 Location logistics
Ask Paula

## 🎓 Certificate of attendance
If you attend the full workshop you can request a certificate of attendance by emailing to training@esciencecenter.nl.
Please request your certificate within 8 months after the workshop, as we will delete all personal identifyable information after this period.


## 🔧 Exercises

**Exercise 1**: Commiting Multiple Files (10 min)

**Exercise 2**: Understanding Workflow and History

https://swcarpentry.github.io/git-novice/05-history.html

The answer is: `I like tomatoes, therefore I like ketchup`.

The changes to the file from the second echo command are only applied to the working copy, not the version in the staging area. The command git add ketchup.md places the current version of ketchup.md into the staging area.

So, when git commit -m "My opinions about the red sauce" is executed, the version of ketchup.md committed to the repository is the one from the staging area and has only one line.

At this time, the working copy still has the second line (and git status will show that the file is modified). However, git restore ketchup.md replaces the working copy with the most recently committed version of ketchup.md. So, cat ketchup.md will output

Collaborative development:

    PERSON A: Create an issue in the repository
    PERSON B: Clone this repository to your system
    PERSON B: Create a new branch, using git switch -c new_feature
    PERSON B: Make the changes requested in the issue
    PERSON B: Push the changes to the remote repository on GitHub using git push origin new_feature
    PERSON B: Submit a Pull Request, refer to the issue (e.g. “Closes #1”)
    PERSON A: Review the Pull Request
    PERSON B: Address the comments
    PERSON A: Approve the Pull Request
    PERSON B: Merge the Pull Request

External collaborative development:


    PERSON A: Create an issue in Person B’s repository
    PERSON A: Fork the repository to their own (= Person A’s) account
    PERSON A: Clone the repository, make changes, push them back to the fork
    PERSON A: Submit a Pull Request from the fork to the original repository
    PERSON B: Make a change in the original repository in the same place as person A’s proposed changes
    PERSON A: Solve the merge conflict in the Pull Request
    PERSON B: Review/Approve the Pull Request
    PERSON B: merge the Pull Request


## 🧠 Collaborative Notes

### Day 1:

### Programming vs Software Engineering
- "Software engineering is programming integrated over time"
- Software engineering focuses on sustainability, avoiding "code debt"
    - This takes a bit longer in the beginning, but pays off in the future
    - Investments like version control, code reviews, testing, etc.
- Projects are getting exponentially more complex to manage the more people are involved
- When is the "investment" in best-practices worth it? Rule of thumb:
    
    | lifetime  | use                             |
    | --------- | ------------------------------- |
    | 1-shot    | 🚫                              |
    | week+     | git github                      |
    | 3 months+ | testing                         |
    | 6 months+ | documentation, automate testing |

    | users          | use                              |
    | -------------- | -------------------------------- |
    | 1              | push to main                     |
    | 2+             | branches, merging                |
    | 2+ (+students) | code review                      |
    | 2+ (+external) | release branch & everything else |

- Following best practices saves time in the long-run by
    - Efficiency
    - Reproducibility
    - Reusability
    - Faster debugging
    - Robustness
    - Fewer headaches!

### Version Control
- Documents are a collection of changes
- Collaboration means that there are independent changes (just like in this collaborative doc!) that can be merged
- Version Control tracks changes, gives you unlimited undo (yeah!), and enables work in parallel
- The Holy Realms of Git
    - workspace: your filesystem 📂
    - index: a.k.a. "staging area", files to be committed 🕓
    - local repository: contains branches, commits, history, etc. 🗂️
- Staging area can hold many files and folder
- What's a good commit message?
    - Short, descriptive, imperative
- Common commands
    - `git status` show the state of the repository, you will use this _all the time_
    - `git add` put files in the "index"/"staging area"
    - `git commit` saves the staged content as a new commit to the local repository
- Commit style
    - "atomic", a change (or a set of changes) that cover one specific aspect, like "fixed bug A", or "implement feature B"

### Saying hi to `git`

```
git --version
```

Should return something like:

```output
git version 2.39.3
git version 2.47.1.windows.2
```

### Configuring `git`

#### Mandatory Settings
These two settings are the only ones that are mandatory:

```bash
git config --global user.name "Sam Anonymous"
git config --global user.email "sam@example.com"
```

#### Optional settings

```bash
git config --global core.editor "nano"  # vim, emacs nano ...
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "subl -n -w"  # Sublime Text
```

Good practice:
```bash
git config --global init.defaultBranch main
```

Editing your config directly:
```bash
git config --global --edit
```

Listing your config:
```bash
git config --list
```

If you have global _and_ local settings, you get more info where which settings is defined with:
```bash
git config --list --show-origin
```

Getting help:
```bash
# general help
git --help

# Pattern for specific commands: git [COMMAND] --help
git config --help
git add --help
git commit --help
```

### Hands-On!

#### Create Content
Use whichever editor you are comfortable with. For the examples I use `nano`.

Create a folder for our project `mkdir recipes` and go into the folder `cd recipes`. From there hit `git init`:
(it could be that your branch is named `master` instead of `main` - that is all OK)

Creating `dessert` within `recipes` and hit `git init`
Remove a directory: `rm -rf .git/`
Creating a .md file with nano `guacamole.md` and checking file in the terminal with `cat guacamole.md`

*----------------- break -------------------*
#### Getting an Overview
```bash
git log  # Shows commits and commit messages of the current branch
```
N.B.: The commit "hash" (a sort of fingerprint) is very long. If you need to use it somewhere in a command, copying the first few (6+) characters is sufficient.

Using `git status` shows the newly created `guacamole.md` file in red, indicating that this file is not tracked by git.

add the file:`git add guacamole`
commit the changes with message: `git commit -m "create initial structure ..."`
Using `git status` again, we see that git reports a clean working tree, i.e. all the files and changes to tracked files are commited to the repository
Check the git log (history of commits) using `git log`

Adding more changes on `guacamole.md` and check new changes on your terminal with `cat`.

## 🗺️ Exploring `diff`
```bash
git diff guacamole.md  # show only differences of the `guacamole.md` file
git diff HEAD guacamole.md   # show diff between HEAD (last commit) and local file
git diff HEAD~1 guacamole.md   # show diff between _previous commit_ and local file
```

Checking deltas and differences with `git diff` showing the version *before* versus *after* changes.
Now we commit these changes with `git commit` BUT you need first to ADD the new changes, and then COMMIT these new changes:
`git add guacamole.md`
`git commit -m "adding ingredients to the file"`
`git log`
 
 
comparing file versions:
`git diff HEAD guacamole.md`
`git log --oneline`
`git diff HEAD~3 guacamole.md`
`git show HEAD~2 guacamole.md`
`git restore guacamole.md` restore to no instruction versions
`git restore -s YOURVERSIONNUMBER guacamole.md` to restore back with instruction version
`git restore guacamole.md` restore to the last commit
:::info
💡
`git` only tracks files, not folders! Files within folders are fine, but empty folders are ignored. If you want to track an "empty" folder, you can put a hidden file inside, e.g. `.gitkeep` and track that one instead. Its parent folder is now tracked as part of the `.gitkeep` file.
::: 

Updating an ingredient on the `.md` file and using `git add` to place the file in the staging area. If we use `git diff`, nothing is printed because by default `git diff` compares the commited repository with the working directory. To check the differences between the repository and the staged area use `git diff --staged`.

...creating new directoty with a new file: `mkdir cakes`

`touch cakes/brownie.md cakes/lemon_drizzle.md`

...adding the changes and git status
`git add .`
`git status`

...and then commiting the new changes and new file
`git commit -m "add some initial cakes"`

create a image files in the folder
`❯ touch a.png b.png c.png receipts/a.jpg receipts/b.jpg


## 🙈 Ignoring Files

create a .gitignore file -- `nano .gitignore`
and add files extension to ignore or entire folders, e.g.:
```
*.png
receipts/
```


adding gitignore file: `git add .gitignore`

------break---------

editing the file for instructions
`nano guacamole.md` and add new instructions



creating branches `git branch YOURNAME` and switch to that branch. In the new branch:
- modify guacamole
- switch to main `git swich main` (or master)
- come back to the new branch and add the changes with `git add guacamole.md`
- commit the changes in the new branch: `git commit -m "added more ingredients"`

Rename branches (for those that has `master` instead of `main`): `git branch -M main`


**Collaborate with Git:**
...setting ssh with `ssh -T git@github.com`

Learn more on **remote**, from remote to local:
- create a new repository via github web
- clone a repository with ssh!! git clone `git clone REPO.ssh`
- list the files with `ls`
- check remotes with `git remote -v`

From local to remote:
- create empty directory
- type `remote add origin git@github.com:yourusernameandrepo`


Now, modify the readme file, add and commit it:
- `vim readme.md`
- `git add readme.md`
- `git commit -m "added file"`
- `git push` new command to sync local and remote

Now, the readme file has been edited via Github web remotely:
- `git pull` in order to get the new edited readme file in your local machine

## Connecting to the Outside World
Create a new repository called "awesome project" on github.com, then copy the URL (make sure to copy the SSH address!) and come back to the terminal.
```bash
# git remote add ALIAS URL
git remote add origin git@github.com/YOUR_USERNAME/awesome-project.git
```

::: info
💡
`origin` is the standard alias for a remote repository.
:::

```bash
git remote -v  # checking if the remote is indeed added

# pushing all your committed changes to the remote repo
git push  # Fails! Oh no! But git tells us how to proceed.
git push --set-upstream origin main  # we only need to do this the first time
```


---- LUNCH BREAK ----

### Collaborating on code with Github

#### Workflow for this section:
- Create a new repository (or use the one that you made yesterday)
    - Make sure it has a unique name (e.g. python-sum)
    - Add README & .gitignore files
    - Choose a licence: Apache 2.0
- Go to your new repository and add a new collaborator
    - Go to the settings tab and click on collaborators on the left hand side
    - Add collaborator and type in the name of the person you want to add
    - The person can then accept the invite

- Creating an issue: 
    - In the issues tab, create a new issue.
    - This is a way to track things that you want to implement or fix in your project.
    - In issues, you can link to people (e.g. @username), PRs (e.g. #1) and links etc. You can also assign people to take care of an issue. 

- Clone the repo you are collaborating on:
    - Copy SSH link: `git clone [ssh-link]`
    - Create a new branch: `git switch -c 1-add-python-sum`
    - Make the change you want to make: `vim sum-two-numbers.py` (or use the editor you prefer), add the code and save the file. 
    - Commit and push your changes to GH
    - This will open a pull request on GH.

- Creating a pull request:
    - After pushing your changes, the option to create a pull request (PR) automatically appears in GH.
    - You can add a title and description of the changes the pull request addresses:
        - Best practice is to list what the PR addresses and which issue(s) it addresses (you can link issues with e.g #1)
    - Choose a reviewer for the PR

- Code review:
    - When you open the pull request you can open the "files changes" to look at the files that have changed
    - You can leave comments on specific parts of the code (hover over the bit of code and click +)
    - When you "start a review" the comments are in draft mode until you click "finish your review".
    - Leave a general comment and either: 
        - "Approve" - branch can be merged, 
        - "Comment" - just leaving comments, the person can choose what the want to do 
        - "Request changes" -  changes should be made before merging
    
- Addressing comments: 
    - `git pull`
    - Make sure you are on the correct branch then make your changes. 
    - Commit and push your changes. 
    - Respond to the comments on the PR
        - Say you addressed them, or how you did or if there were any problems with the suggestion. 
    - Re-request a review

- Suggesting a change: 
    - In GH, click + where you want to add your suggestion. This will open a comment, on the top bar (on the right or preview) you can click on "add a suggestion" and you can adjust the code. 
    - Your collaborator can then accept the suggestion and commit it within GH without needing to pull. 

Once everyone is happy, you can merge the PR into main! 

- Creating a fork:
    - A fork is cloning a repository serverside (in this case GH). You can then make changes and commit them to your own fork without affecting the original project.
    - You do this when you want to make changes to a project that you do not have write access to. This is often the case with big projects (e.g. [Pandas](https://github.com/pandas-dev/pandas), [Xarray](https://github.com/pydata/xarray) etc), but smaller ones too. 
    - If you make a change that you want to contribute to the original project, you can make a pull request from your fork. 

#### General notes:
- Choosing a licence is important, as in principle if you do not choose one no one is allowed to use your code. [Apache licence 2.0](https://choosealicense.com/licenses/apache-2.0/) is a permissive open source licence.
- If someone does not use GitHub, you can still invite them by using their e-mail address: it will send an invite to join GitHub.
- To accept an invite, you can either do it through the notifications in GH or through email. (You can also go directly to the repository and accept there.)
- When creating a new branch, you can name it what you want but try to be descriptive of what the branch will do. If using issues, you can add the number of the issue.
- When you create a new local branch to work on, it is not seen by GH. So when pushing your local branch to GH for the first time you will be prompted to create this branch on GH too (set upstream branch). 
    - `git push -u origin [branch]` 

#### Linking a pull request to an issue
To link a pull request to an issue to show that a fix is in progress and to automatically close the issue when someone merges the pull request, type one of the following keywords followed by a reference to the issue. For example, Closes #10 or Fixes octo-org/octo-repo#100.

*close
closes
closed
fix
fixes
fixed
resolve
resolves
resolved*

## 📚 Resources
- Choosing a licence: https://choosealicense.com/licenses/
- Tracking issues: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
- Using keywords in GH: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests
- Code reviews: https://dev.to/akdevcraft/how-to-review-code-2gam
- Git guide: https://github.com/git-guides
- git cheatsheet: https://education.github.com/git-cheat-sheet-education.pdf
- forking: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
- Resolving merge conflicts in GitHub: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github
- Resolving merge conflicts in the command line: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line
- Duplicating repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository

## ❓ Questions?
Jing ask:
"create a image files in the folder
`❯ touch a.png b.png c.png receipts/a.jpg receipts/b.jpb"
really receipts/b.jpb? not .jpg? it was a mistake, its .jpg!! :) 


Jing ask: error occur when:
$ touch a.png b.png c.png receipts/a.jpg receipts/b.jpg
touch: cannot touch 'receipts/a.jpg': No such file or directory
touch: cannot touch 'receipts/b.jpg': No such file or directory -- **Answer**: you should first create a receipts folder -- first write `mkdir receipts` and then `touch a.png b.png c.png receipts/a.jpg receipts/b.jpg`




## 📢 Feedback (Morning)
### What went well?
good pace, interactive
All is good, nice pace; the introduction slides with the common mistakes really capture my mistakes too, so it's nice to know that I will eventually improve on them :)
very good!
All clear for now!
Very nice to get help whenever you need assistance.
I like the collaborative notes, it is a good way to keep track of what we have done and to follow the process if you are lost
Nice, all clear!
Nice and clear!
Very interesting and clear!
### What could be improved?
It'd be better the instructor does not clear the terminal so that we can see the previous commands on the screen.
Yes, clearing less often would be nice, so that if you are a bit behind you do not get lost completely.
Two coffee break in one hour break my focus, it would be nice to have one somewhere in between (i.e. 11:00)
I get errors and then I get lost because the live coding doesn't
stop
maybe good to provide command lines, to make the process faster
use simple words, like book insteade of Guacamole :)    --Jing agree！
Currently relatively basic
Always show history codes on the screen would be better, in case we are lost in some steps, and cannot catch the following.
Not typing with the whole group in the same document at the same time. (Or perhaps already insert the names, such that everyone has a predetermined place where to type for intorduction.) 
Automatic taken notes instead of human

## 📢 Feedback (Afternoon)
### What went well?
Great! But also tired in the afternoon.
Collaborative examples were nicely addressed, working with two people and showing both screens. 
It was really good to have several helpers who we could address with specific questions at anytime during the course
Really nice!
Helpful having interactive examples that are collaborative. Good pace
The extra material at the end was very helpful!
Really helpful!


### What could be improved?
More collaboration? Because we can practice coding ourselves, but cannot practice collaboration part by one person.

The first part after lunch was a bit complex (not because of the difficulty) but maybe the explanation was too long, or too much time passed between the explanation and the start of the practical part 

Lecture bit after lunch could was a bit hard to keep paying attention 

Some basic concepts(e.g. HEAD branch) are not introduced which makes it difficult to understand the branch management.

The conflict part was really interesting, but it would be better to have it more in deep. We couldn't create a conflict and test the solcing process.
## 📚 Resources

If you want to know about the features and how to use the TU Delft GitLab instance, you can use this resource: https://tu-delft-dcc.github.io/docs/infrastructure/gitlab/gitlab_intro.html
