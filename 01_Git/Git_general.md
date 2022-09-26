Repository:  
A repository contains all of your project's files and each file's revision history. You can discuss and manage your project's work within the repository  

Main:  
The default development branch. Whenever you create a Git repository, a branch named main is created, and becomes the active branch.  
In most cases, this contains the local development, though that is purely by convention and is not required.


Master:  
The default branch in many Git repositories.  
By default, when you create a new Git repository on the command line, a branch called master is created.  
Many tools now use an alternative name for the default branch.  
For example, when you create a new repository on GitHub, the default branch is called main.


Branch:  
A branch is a parallel version of a repository.  
It is contained within the repository, but does not affect the primary or main branch allowing you to work freely without disrupting the "live" version.  
When you've made the changes you want to make, you can merge your branch back into the main branch to publish your changes.

Commit:  
A commit, or "revision", is an individual change to a file (or set of files).  
When you make a commit to save your work,  
Git creates a unique ID (a.k.a. the "SHA" or "hash") that allows you to keep record of the specific changes committed along with who made them and when.  
Commits usually contain a commit message which is a brief description of what changes were made.  

Push:  
To push means to send your committed changes to a remote repository on GitHub.com. 
For instance, if you change something locally, you can push those changes so that others may access them

Pull:  
Pull refers to when you are fetching in changes and merging them.  
For instance, if someone has edited the remote file you're both working on,  
you'll want to pull in those changes to your local copy so that it's up to date. See also fetch.

Merge:  
Merging takes the changes from one branch (in the same repository or from a fork), and applies them into another.  
This often happens as a "pull request" (which can be thought of as a request to merge), or via the command line.  
A merge can be done through a pull request via the GitHub.com web interface if there are no conflicting changes, or can always be done via the command line

Fork:  
A fork is a personal copy of another user's repository that lives on your account.  
Forks allow you to freely make changes to a project without affecting the original upstream repository.  
You can also open a pull request in the upstream repository and keep your fork synced with the latest changes since both repositories are still connected.

Link used: https://docs.github.com/en/get-started/quickstart/github-glossary#branch 
