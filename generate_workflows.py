import os

repos = {
    "back/apiGateway-back-corvus": "api-gateway",
    "back/authentication-back-corvus": "auth-service",
    "back/notifications-back-corvus": "notifications-service",
    "back/integratorProjectClustering-back-corvus": "clustering-integrator-service",
    "back/llm-back-corvus": "llm-service",
    "front/administration-front-corvus": "admin-frontend",
    "back/studentsGroupsClustering-corvus": "students-groups-clustering-service",
    "back/studentsInformationClustering-back-corvus": "students-information-clustering-service",
    "back/subjectMatterClustering-back-corvus": "subject-matter-clustering-service"
}

dev_template = """name: Deploy to Staging (Dev)

on:
  push:
    branches:
      - dev

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Server
        uses: appleboy/ssh-action@v0.1.10
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USERNAME }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            cd /home/corvus-pruebas/${{ github.event.repository.name }}
            git fetch --all
            git checkout dev
            git pull origin dev
            cd /home/corvus-pruebas/orquestador-pruebas
            docker compose up -d --build {service}
"""

main_template = """name: Deploy to Production (Main)

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Server
        uses: appleboy/ssh-action@v0.1.10
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USERNAME }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            cd /home/corvus/${{ github.event.repository.name }}
            git fetch --all
            git checkout main
            git pull origin main
            cd /home/corvus/orchestration-back-corvus
            docker compose up -d --build {service}
"""

for repo, service in repos.items():
    if not os.path.exists(repo):
        print(f"Skipping {repo} because it doesn't exist.")
        continue
    
    wf_dir = os.path.join(repo, ".github", "workflows")
    os.makedirs(wf_dir, exist_ok=True)
    
    with open(os.path.join(wf_dir, "deploy-dev.yml"), "w") as f:
        f.write(dev_template.format(service=service))
        
    with open(os.path.join(wf_dir, "deploy-main.yml"), "w") as f:
        f.write(main_template.format(service=service))
    
    print(f"Generated workflows for {repo}")

