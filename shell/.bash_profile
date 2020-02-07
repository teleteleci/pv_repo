# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

# added by Anaconda3 5.1.0 installer
# export PATH="/Users/pav/anaconda3/bin:$PATH"

# bash-completion
if [ -f /opt/local/etc/profile.d/bash_completion.sh ]; then
  . /opt/local/etc/profile.d/bash_completion.sh
fi

# Git branch in prompt.
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# kubectl autocomplete
if [ -f $(brew --prefix)/etc/bash_completion ]; then
. $(brew --prefix)/etc/bash_completion
fi


export PS1="\u@\h \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "

# git autocomplete
if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi


# functions
chck (){
    git checkout $1
}

# conTestReadProdApp (){
#     echo "Prod App $1"
#     DB_USER=$1
#     MSDB_NAME="abx-de-sqlserver-db-app"
#     MSDB_URL="abx-de-mssql-prod.database.windows.net"
#     AZURE_KEYVAULT="abx-de-vault"
#
#     DB_LOGIN=$(az keyvault secret show --vault-name $AZURE_KEYVAULT --name "tmp-db-user-"$DB_USER"-name" --query value -o tsv)
#     DB_PWD=$(az keyvault secret show --vault-name $AZURE_KEYVAULT --name "tmp-db-user-"$DB_USER"-pwd" --query value -o tsv)
#     echo $DB_LOGIN $MSDB_NAME"/"$MSDB_URL
#     echo "------------------------------"
#     sqlcmd -S $MSDB_URL -d $MSDB_NAME -U $DB_LOGIN -P $DB_PWD
# }

# alias
alias ll='ls -la'
alias gr='git pull --rebase'
alias gt='git status'

# export PATH="/usr/local/opt/ruby/bin:$PATH"
