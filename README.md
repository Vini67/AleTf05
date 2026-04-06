# TF05 - Sistema de Monitoramento e Automação

## Aluno

* **Nome:** Paulo Vinicius Bernardes  
* **RA:** 6324010 
* **Curso:** Análise e Desenvolvimento de Sistemas - 5° semestre

---

## 📌 Descrição do Projeto

Este projeto implementa um sistema completo de monitoramento de aplicações com healthchecks inteligentes, coleta de métricas, automação de deploy e scripts de manutenção.

O sistema é composto por:

* Backend em Flask (API de monitoramento)
* Banco de dados MySQL (armazenamento de métricas)
* Redis (simulado para cache)
* Dashboard web para visualização
* Scripts de automação e manutenção
* Ambiente containerizado com Docker

---

## 🚀 Funcionalidades

### ✔ Healthchecks Inteligentes

* Verificação HTTP, TCP e Database
* Endpoint `/health`
* Endpoint `/health/status`
* Endpoint `/health/all`
* Endpoint `/health/report`

### ✔ Métricas de Performance

* Tempo de resposta (response time)
* Uptime simulado
* Armazenamento no banco de dados

### ✔ Sistema de Alertas

* Alertas automáticos via console (simulado)
* Detecção de falhas em serviços (TCP e Database)

### ✔ Dashboard

* Exibição de métricas em tempo real
* Atualização automática via JavaScript
* Status dos serviços

### ✔ Automação

* Build automatizado
* Deploy com Docker
* Scripts de manutenção
* Backup e limpeza

---

## 🐳 Tecnologias Utilizadas

* Python (Flask)
* MySQL
* Redis
* Docker / Docker Compose
* JavaScript (Frontend)
* Bash (scripts)

---

## 📂 Estrutura do Projeto
TF05/
├── README.md
├── docker-compose.yml
├── dashboard/
│ ├── Dockerfile
│ ├── index.html
│ ├── js/
│ │ ├── dashboard.js
│ │ └── charts.js
│ └── css/
│ └── dashboard.css
├── api/
│ ├── Dockerfile
│ ├── app.py
│ ├── models/
│ │ ├── metrics.py
│ │ └── alerts.py
│ └── healthchecks/
│ ├── http_check.py
│ ├── db_check.py
│ └── custom_check.py
├── database/
│ ├── init.sql
│ └── migrations/
├── scripts/
│ ├── build.sh
│ ├── deploy.sh
│ ├── rollback.sh
│ ├── backup.sh
│ ├── cleanup.sh
│ └── health-monitor.sh
├── config/
│ ├── healthchecks.yml
│ ├── alerts.yml
│ └── thresholds.yml
└── docs/
├── automation.md
├── healthchecks.md
└── maintenance.md

🌐 Acessos
Dashboard: http://localhost:3000
API: http://localhost:5000

🔍 Testes de Healthcheck
curl http://localhost:5000/health
curl http://localhost:5000/health/status
curl http://localhost:5000/health/all
curl http://localhost:5000/metrics

 Scripts Disponíveis

 Build
./scripts/build.sh

 Deploy
./scripts/deploy.sh

 Rollback
./scripts/rollback.sh

 Backup
./scripts/backup.sh

 Limpeza
./scripts/cleanup.sh

 Monitoramento manual
./scripts/health-monitor.sh


Monitoramento
Verificar status em tempo real
./scripts/health-monitor.sh

Testar endpoints
curl http://localhost:5000/health/status