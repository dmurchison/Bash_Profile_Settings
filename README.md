# Properly install WSL, RBENV, PYENV, Node.JS

* This folder is meant to be open daily and kept open throughout the day, it allows me to open new codespaces and work throughout the day knowing every instance of VS Code will be open in my WSL.
* Working on a more streamlined way to open VS Code every time using WSL without using the terminal.

## Setup

1. Install the WSL app from the Microsoft Store.
    * From the internet:
        * Install Google Chrome
        * Install VS Code
2. Open the powershell as an admin and run the CMD `wsl --install` to install the WSL.
    * After the installation is complete, restart your computer.
3. Now open the Ubuntu terminal and run the following CMD's:
    * `sudo apt update`
    * `sudo apt upgrade`

## RBENV Installation and Configuration

1. Run the following CMD's:
    * `sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev`
    * `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`
    * `echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc`
    * `echo 'eval "$(rbenv init -)"' >> ~/.bashrc`
    * `echo export EDITOR="code --wait" >> ~/.bashrc`
    * `source ~/.bashrc`

## Ruby Installation

* Run the following CMD's:
  * `rbenv install 3.2.2`
  * `rbenv global 3.2.2`
  * `ruby -v`
  * `rbenv rehash`
  * `gem install bundler pry byebug`
  * `gem install rails -v 7.1.0`
  * `rbenv rehash`

## PSQL and SQLite Installation

* Run the following CMD's:
  * `sudo apt-get inatall postgresql libpq-dev`
  * `sudo service postgresql start`
  * `source ~/.bashrc`
  * `sudo apt install sqlite3 libsqlite3-dev`
  * PSQL
    * `sudo -u postgres psql`
    * `CREATE USER your_username WITH SUPERUSER CREATEROLE CREATEDB REPLICATION;`
    * `ALTER USER your_username WITH BYPASSRLS;`
    * `CREATE DATABASE your_username;`
    * `psql`
    * `\q`
  * SQLite
    * `sudo apt-get install sqlite3 libsqlite3-dev`

## NodeJS Installation

* Run the following CMD's:
  * `curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh -o install_nvm.sh`
  * `bash install_nvm.sh`
  * `source ~/.bashrc`
  * `nvm install 16`
  * `nvm use 16`
  * `source ~/.bashrc`
