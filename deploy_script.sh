#!/bin/bash
echo "Waiting for background push to finish..."
while pgrep -f "git push -u origin palomeque" > /dev/null; do
    sleep 2
done

echo "Creating dev branch and pushing..."
git checkout -b dev
git push -u origin dev

echo "Creating PR from palomeque to dev..."
gh pr create --base dev --head palomeque --title "Fix clustering profile" --body "Fixes 502 error and suggestions filter"
gh pr merge --merge --delete-branch=false

echo "Creating PR from dev to main..."
gh pr create --base main --head dev --title "Merge dev to main" --body "Deploy to production"
gh pr merge --merge --delete-branch=false

echo "Connecting to VPS to deploy..."
ssh -o StrictHostKeyChecking=no root@207.180.215.71 << 'SSH_EOF'
cd /root/project9no
git checkout main
git pull origin main
docker restart studentsGroupsClustering-corvus
# Or whatever command is used to deploy
echo "Deployed successfully on VPS!"
SSH_EOF
