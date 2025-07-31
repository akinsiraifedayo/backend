# create ssh for github actions
create ssh key for github actions and copy the repo key into the env secrets, alon with username and ip address


# then on the server
git clone repo into server

ssh-keygen -t ed25519 -f ~/.ssh/github_deploy_key -N ""

copy ~/.ssh/github_deploy_key into repo deploy key

add github into server config
cat > ~/.ssh/config <<EOF
Host github.comcat repo
  HostName github.com
  User git
  IdentityFile ~/.ssh/github_deploy_key
  IdentitiesOnly yes
EOF
chmod 600 ~/.ssh/config

# Personal GitHub
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal
  IdentitiesOnly yes

# you connect with git clone git@github-personal:akinsiraifedayo/frontend

# install docker
# 1. Update packages
sudo apt-get update

# 2. Install prerequisites
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 3. Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. Set up the repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# login dockerhub
docker login

visit docker url and use their code to authenticate


# 1. Add your user to the docker group
sudo usermod -aG docker $USER

# 2. Apply changes without logout
newgrp docker

# 3. Verify
docker ps  # Should work without sudo


# NEXT STEPS
configure nginx 
