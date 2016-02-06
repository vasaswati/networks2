# networks2
Public repository for Networks 2 coursework

# Instructions to set-up ubuntu
Go to http://www.ubuntu.com/download/desktop 

Download Ubuntu 14.04.3 LTS image ; Select flavour as 64-bit (recommended) and click download !

Go to http://www.v3.co.uk/v3-uk/download-review/1957177/vmware-player-600

Download VMware Player 7.1.1 and install.

Start VMPlayer by clicking on shortcut it creates on desktop.

Once VMPlayer launches, click on 'Create a New Virtual Machine'. A pop-up comes up !

Select 'Installer disc image file (iso)' and browse for the ubuntu image 14.04.3 that you downloaded earlier.

Click next and enter your information - full name, username, password, confirm password. Click next again !

Give your ubuntu vm a name (default: Ubuntu 64-bit, let it be the same!).

Click next and select 'Split virtual disk into multiple files'. Click next again !

Finally, Click Finish.

Select 'Ubuntu 64-bit' on the left section. Click 'Play Virtual Machine'. That's it ! Your VM is up and running. Give some time to boot up VM. Generally takes about a minute or 2.

Login using the username and password that you created above !

# Instructions to install python 3 on ubuntu 
Click search, type terminal and click on 'Terminal'. Type the following commands -

sudo apt-get install python3 

sudo apt-get install idle-python3.4

alias python=python3 

// This should show the version of python just installed

python -V 

# Instructions to install git on ubuntu 

https://help.github.com/articles/set-up-git/#platform-linux

Basically, what the above link to set-up git, says is ->

You can install git in ubuntu using following commands -

sudo apt-get install git

Then, Go to https://github.com/join?source=header-home
and Sign up for creating your GitHub account online (It's free, don't worry !).

Again, in the terminal, type the following commands -

//"YOUR NAME" is the username you created during sign up, and "YOUR EMAIL ADDRESS" is the email address

git config --global user.name "YOUR NAME"

git config --global user.email "YOUR EMAIL ADDRESS"

# Instructions to fork an existing repo on GitHub

Go to https://github.com/jugg3rn4u7/networks2 

On the top right corner, you'll find a 'Fork' button. Click it !

# Instructions to clone your repo

Once an existing repo is forked onto your account, you need to clone it to your local repository (local environment, your computer !)

Type the following command in your Terminal -

git clone https://github.com/YOUR-USERNAME/networks2

# Instructions to check remote configurations in GitHub

Type the following command in your Terminal -

git remote -v

# Syncing your local with your UPSTREAM (I'll explain to you what's UPSTREAM :). But for now, just follow the instructions !)

git remote add upstream https://github.com/YOUR-USERNAME/networks2.git

//Check your remote configurations again - (What do you see ?? :O :D)

git remote -v

# Branching (I'll explain !)

https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/

# Pull Requests (I'll explain !)

https://help.github.com/articles/creating-a-pull-request/

# Git Documentation

https://git-scm.com/doc

There are a lot of details in git-scm about github commands. But its better to learn on the fly ! Reading the entire document will take a loooooooooooooooootttt of time. Better to learn by doing than reading first !  






