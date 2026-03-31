# EN

#  AI Log Analyzer & Security Insights

A real-time log monitoring system powered by a **Local LLM (Llama 3.2)**. This project automatically detects security threats and system errors, providing instant AI-generated technical solutions.

##  Key Features
* **Real-time Monitoring**: Automatically tracks log files for `ERROR` and `WARNING` states.
* **Local LLM Integration**: Uses **Ollama** and **Llama 3.2 (3B)** to analyze data locally (ensuring 100% data privacy).
* **Interactive Dashboard**: Modern UI built with **React** and **Tailwind CSS**.
* **Containerized Architecture**: Full microservices structure based on **Docker Compose**.
* **Automated Insights**: Generates professional technical advice for every detected incident.

##  System Architecture
The system consists of 4 main components working together:
1. **Logger (Python)**: Simulates realistic system logs and attack attempts (SQL Injection, Brute-force).
2. **Analyzer (Python + Ollama)**: The "brain" of the system—it catches errors and sends them to the LLM via Ollama's API.
3. **Backend (FastAPI)**: Serves analyzed data through a REST API and manages the SQLite database.
4. **Frontend (React)**: A dynamic dashboard with live updates and database management capabilities.

##  Tech Stack
* **Frontend**: React.js, Tailwind CSS, Axios, Vite.
* **Backend**: FastAPI, SQLite.
* **AI/ML**: Ollama, Llama 3.2 (3B).
* **DevOps**: Docker, Docker Compose.

##  How to run the project?

### Prerequisites
* **Docker Desktop** installed.
* **Ollama** installed on the host operating system.
* Downloaded model: `ollama run llama3.2:3b`.

### Quick Start
1. Start the containers: `docker-compose up --build`
2. Access the Dashboard: `http://localhost:5173`

###  A Note on Networking (The "Fun" Part)
Getting this project to run "out of the box" can be a bit of a challenge due to the **Docker <-> Host (Ollama)** communication. By default, Ollama binds to `localhost`, which prevents Docker containers from accessing it.

To make it work, you need to get your hands a bit dirty:
1. You must force Ollama to listen on all interfaces by setting `OLLAMA_HOST=0.0.0.0`.
2. You need to allow traffic on port `11434` through your system Firewall.
3. I've used `host.docker.internal` in the code, which solves most issues, but the rest of the "technical gymnastics" with port forwarding and the Docker Network Bridge is left for the ambitious ones who want to feel the true pain and joy of container networking. ;)

---
*This project was created for portfolio purposes to demonstrate the integration of local LLMs with modern microservices architecture.*

# PL

#  AI Log Analyzer & Security Insights

System monitorowania logów w czasie rzeczywistym wspierany przez lokalny model AI (Llama 3.2). Projekt automatycznie wykrywa zagrożenia bezpieczeństwa oraz błędy systemowe, dostarczając natychmiastowe rozwiązania generowane przez sztuczną inteligencję.

##  Główne Funkcje
* **Monitoring Real-time**: Automatyczne śledzenie plików logów pod kątem statusów ERROR oraz WARNING.
* **Integracja z Lokalnym LLM**: Wykorzystanie Ollama i modelu Llama 3.2 (3B) do analizy danych lokalnie (pełna prywatność).
* **Interaktywny Dashboard**: Nowoczesny UI zbudowany w React i Tailwind CSS.
* **Architektura Kontenerowa**: Pełna mikroserwisowa struktura oparta na Docker Compose.

##  Architektura Systemu
System składa się z 4 głównych komponentów:
1. **Logger (Python)**: Symuluje realistyczne logi systemowe i próby ataków.
2. **Analyzer (Python + Ollama)**: Serce systemu, przesyła błędy do LLM.
3. **Backend (FastAPI)**: Serwuje przeanalizowane dane przez REST API.
4. **Frontend (React)**: Dynamiczny dashboard z odświeżaniem na żywo.

##  Tech Stack
* **Frontend**: React.js, Tailwind CSS, Axios, Vite.
* **Backend**: FastAPI, SQLite.
* **AI/ML**: Ollama, Llama 3.2 (3B).
* **DevOps**: Docker, Docker Compose.

##  Jak uruchomić projekt?

### Wymagania (Prerequisites)
* Zainstalowany **Docker Desktop**.
* Zainstalowana **Ollama** na systemie operacyjnym.
* Pobrany model: `ollama run llama3.2:3b`.

### Szybki Start
1. Uruchom kontenery: `docker-compose up --build`
2. Dostęp do Dashboardu: `http://localhost:5173`

###  Uwaga dot. konfiguracji (Networking)
Uruchomienie tego projektu "z palca" może być wyzwaniem ze względu na komunikację na linii Docker <-> Host (Ollama). Domyślnie Ollama izoluje się na localhost, co blokuje dostęp kontenerom. 

Aby to działało, trzeba się trochę "pobawić":
1. Trzeba wymusić na Ollamie słuchanie na wszystkich interfejsach (`OLLAMA_HOST=0.0.0.0`).
2. Należy ogarnąć przepuszczanie ruchu na porcie 11434 w zaporze Windows (Firewall).
3. W kodzie użyłem `host.docker.internal`, co rozwiązuje większość problemów, ale resztę technicznej gimnastyki z portami i Docker Network Bridge zostawiam dla ambitnych, którzy chcą poczuć prawdziwy ból i radość konfigurowania sieci kontenerowej. ;)

---
Projekt stworzony do portfolio jako demonstracja integracji lokalnych LLM z architekturą mikroserwisową.