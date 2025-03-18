print "Hello World"
print "How are you ?"



''' 
    Basic Git Commands



        1. git --version - Check installed Git version
        2. git config --global user.name "Your Name" - Set global username
        3. git config --global user.email "[your-email@example.com]" - Set global email
        4. git config --global --list - View global Git configurations
        5. git init - Initialize a new Git repository
        6. git status - Check the status of files in the repository
        7. git add  - Stage a specific file
        8. git add . - Stage all changes
        9. git commit -m "Your commit message" - Commit staged changes
        10. git log - View commit history



Branching & Merging



        11\. git branch - List all branches
        
        12\. git branch  - Create a new branch
        
        13\. git checkout  - Switch to another branch
        
        14\. git checkout -b  - Create and switch to a new branch
        
        15\. git merge  - Merge a branch into the current branch
        
        16\. git branch -d  - Delete a branch
        


Remote Repositories (GitHub)



        17\. git remote -v - View linked remote repositories
        
        18\. git remote add origin  - Link a local repository to GitHub
        
        19\. git push -u origin main - Push the local branch to GitHub
        
        20\. git pull origin main - Fetch and merge changes from GitHub
        
        21\. git clone  - Clone a remote repository locally
        
        22\. git remote set-url origin  - Change the remote repository URL



SSH Configuration for GitHub



            26\. ls -al \~/.ssh - Check if SSH keys exist
            
            27\. ssh-keygen -t rsa -b 4096 -C "[your-email@example.com]" - Generate a new SSH key
            
            28\. eval "\$(ssh-agent -s)" - Start the SSH agent
            
            29\. ssh-add \~/.ssh/id\_rsa - Add SSH key to the SSH agent
            
            30\. cat \~/.ssh/id\_rsa.pub - Display SSH public key
            
            31\. ssh -T [git@github.com] - Test SSH connection with GitHub




'''