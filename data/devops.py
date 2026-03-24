"""
Donnees sur les outils DevOps et d'infrastructure.
Chaque entree documente un outil avec son histoire, son architecture,
ses cas d'usage et ses caracteristiques techniques.
"""

TECHNOLOGIES = {
    "docker": {
        "name": "Docker",
        "category": "devops",
        "year_created": 2013,
        "creator": "Docker Inc",
        "paradigm": ["conteneurisation", "immutable infrastructure", "declaratif", "microservices"],
        "typing": "declaratif (Dockerfile, Compose YAML)",
        "sections": {
            "overview": (
                "Docker est une plateforme de conteneurisation qui permet d'empaqueter\n"
                "une application et toutes ses dependances dans un conteneur leger,\n"
                "portable et reproductible. Un conteneur Docker isole l'application\n"
                "du systeme hote tout en partageant le noyau Linux, offrant une\n"
                "alternative bien plus legere aux machines virtuelles.\n\n"
                "Le principe fondamental de Docker est la reproductibilite : une\n"
                "image Docker construite sur le poste d'un developpeur fonctionnera\n"
                "de maniere identique en production. Cela elimine le tristement\n"
                "celebre probleme 'ca marche sur ma machine' qui a hante le\n"
                "developpement logiciel pendant des decennies.\n\n"
                "Docker utilise un systeme de couches (layers) pour les images :\n"
                "chaque instruction du Dockerfile cree une nouvelle couche, et\n"
                "les couches sont mises en cache et partagees entre les images.\n"
                "Ce systeme minimise l'espace disque et accelere les builds.\n\n"
                "Docker Compose permet de definir et d'orchestrer des applications\n"
                "multi-conteneurs via un fichier YAML declaratif. C'est l'outil\n"
                "standard pour le developpement local d'applications composees\n"
                "de plusieurs services (API, base de donnees, cache, etc.).\n\n"
                "Docker a fondamentalement transforme la facon dont les logiciels\n"
                "sont developpes, testes et deployes. Il est devenu la brique\n"
                "de base de l'infrastructure moderne, sous-tendant des\n"
                "technologies comme Kubernetes, les architectures microservices\n"
                "et les pipelines CI/CD."
            ),
            "history": (
                "Docker a ete cree par Solomon Hykes au sein de dotCloud, une\n"
                "plateforme PaaS (Platform as a Service). Le projet a debute\n"
                "comme un outil interne utilisant les cgroups et les namespaces\n"
                "Linux pour isoler les applications des clients de la plateforme.\n\n"
                "Docker a ete presente pour la premiere fois lors de la conference\n"
                "PyCon en mars 2013, dans un lightning talk de 5 minutes qui est\n"
                "devenu legendaire. La demonstration a immediatement enflamme la\n"
                "communaute developpeur : en quelques semaines, le projet GitHub\n"
                "a accumule des milliers d'etoiles.\n\n"
                "L'adoption a ete si rapide que dotCloud a pivote entierement\n"
                "vers Docker, se renommant Docker Inc en 2013. La societe a\n"
                "leve plus de 200 millions de dollars en capital-risque.\n\n"
                "Docker 1.0 est sorti en juin 2014, marquant la stabilite\n"
                "pour la production. Docker Compose (initialement Fig) et\n"
                "Docker Machine ont complete l'ecosysteme.\n\n"
                "En 2015, Docker a cree l'Open Container Initiative (OCI)\n"
                "avec d'autres acteurs de l'industrie, standardisant les\n"
                "formats de conteneurs et les runtimes. Cette ouverture\n"
                "a permis l'emergence d'alternatives compatibles.\n\n"
                "Docker Swarm, l'orchestrateur natif de Docker, a ete\n"
                "lance en 2016 mais a rapidement ete eclipse par Kubernetes.\n"
                "Docker Inc a connu des difficultes financieres et a ete\n"
                "rachete partiellement par Mirantis en 2019.\n\n"
                "Docker Desktop, la version pour developpeurs sur macOS et\n"
                "Windows, est devenue payante pour les grandes entreprises\n"
                "en 2021, suscitant la recherche d'alternatives (Podman,\n"
                "Rancher Desktop, Colima). Malgre ces turbulences, Docker\n"
                "reste le standard de facto de la conteneurisation."
            ),
            "architecture": (
                "L'architecture de Docker repose sur un modele client-serveur\n"
                "utilisant les fonctionnalites d'isolation du noyau Linux :\n\n"
                "Docker Engine : Le daemon dockerd gere les objets Docker\n"
                "(images, conteneurs, reseaux, volumes). Le CLI docker\n"
                "communique avec le daemon via l'API REST.\n\n"
                "Conteneur : Un conteneur est un processus isole utilisant\n"
                "les namespaces Linux (PID, NET, MNT, UTS, IPC, USER) pour\n"
                "l'isolation et les cgroups pour la limitation des ressources\n"
                "(CPU, memoire, I/O). Le conteneur partage le noyau hote.\n\n"
                "Image : Une image est un template en lecture seule compose\n"
                "de couches empilees (Union Filesystem, generalement OverlayFS).\n"
                "Chaque instruction du Dockerfile cree une couche. Les couches\n"
                "sont immutables et partagees entre les images.\n\n"
                "Dockerfile : Le fichier declaratif definissant comment\n"
                "construire une image. Les instructions (FROM, RUN, COPY,\n"
                "CMD, ENTRYPOINT, ENV, EXPOSE, etc.) sont executees\n"
                "sequentiellement, chaque etape produisant une couche.\n\n"
                "Registry : Docker Hub est le registre public par defaut\n"
                "hebergeant des millions d'images. Les registres prives\n"
                "(Harbor, GitHub Container Registry, AWS ECR, etc.) stockent\n"
                "les images d'entreprise.\n\n"
                "Reseau : Docker fournit plusieurs drivers reseau : bridge\n"
                "(par defaut, reseau isole), host (partage le reseau hote),\n"
                "overlay (multi-hote pour Swarm/Kubernetes), et macvlan.\n\n"
                "Volumes : Les volumes Docker persistent les donnees au-dela\n"
                "du cycle de vie des conteneurs. Ils sont geres par Docker\n"
                "et peuvent utiliser differents drivers de stockage."
            ),
            "pros_cons": {
                "pros": [
                    "Reproductibilite parfaite : 'build once, run anywhere' sans probleme d'environnement",
                    "Legerete : les conteneurs demarrent en secondes et partagent le noyau hote",
                    "Systeme de couches minimisant l'espace disque et accelerant les builds",
                    "Docker Compose simplifie l'orchestration locale multi-services",
                    "Ecosysteme massif : des millions d'images disponibles sur Docker Hub",
                    "Standard de l'industrie avec OCI, compatible avec tout l'ecosysteme cloud",
                    "Isole les dependances, permettant de faire cohabiter differentes versions",
                    "Facilite enormement les pipelines CI/CD et le deploiement"
                ],
                "cons": [
                    "Overhead de performance par rapport a une execution native (minimal mais present)",
                    "La securite des conteneurs necessite une attention particuliere (images de base, secrets)",
                    "Docker Desktop est payant pour les grandes entreprises",
                    "La gestion des volumes et de la persistance est plus complexe qu'en natif",
                    "Les images mal optimisees peuvent etre tres volumineuses",
                    "Le debugging dans les conteneurs est moins intuitif que sur la machine hote",
                    "La complexite augmente rapidement avec les architectures microservices"
                ]
            },
            "use_cases": (
                "Docker est utilise dans quasiment tous les contextes de\n"
                "developpement moderne : environnements de developpement\n"
                "reproductibles, pipelines CI/CD, deploiement de microservices,\n"
                "applications cloud-native, tests d'integration, reproductibilite\n"
                "scientifique, empaquetage d'applications, et distribution de\n"
                "logiciels. Docker Compose est l'outil standard pour le\n"
                "developpement local d'applications multi-services."
            ),
            "ecosystem_size": (
                "L'ecosysteme Docker est immense. Docker Hub heberge des millions\n"
                "d'images. Docker Compose gere les applications multi-conteneurs.\n"
                "Docker Scout analyse la securite des images. Docker Build Cloud\n"
                "accelere les builds dans le cloud. BuildKit est le nouveau\n"
                "moteur de build avec support du cache avance et des builds\n"
                "multi-plateformes (buildx). Alternatives compatibles :\n"
                "Podman (rootless, daemonless), containerd (runtime),\n"
                "nerdctl (CLI compatible Docker pour containerd)."
            ),
            "companies": [
                "Pratiquement toutes les entreprises tech modernes",
                "Google",
                "Microsoft",
                "Amazon",
                "Netflix",
                "Spotify",
                "PayPal",
                "Goldman Sachs"
            ],
            "code_example": (
                "# Dockerfile multi-stage pour une application Python\n"
                "FROM python:3.12-slim AS base\n"
                "WORKDIR /app\n\n"
                "# Etape de build avec les dependances de developpement\n"
                "FROM base AS builder\n"
                "COPY requirements.txt .\n"
                "RUN pip install --no-cache-dir --prefix=/install -r requirements.txt\n\n"
                "# Image finale legere\n"
                "FROM base AS production\n"
                "COPY --from=builder /install /usr/local\n"
                "COPY src/ ./src/\n\n"
                "# Utilisateur non-root pour la securite\n"
                "RUN useradd --create-home appuser\n"
                "USER appuser\n\n"
                "EXPOSE 8000\n"
                "CMD [\"python\", \"-m\", \"uvicorn\", \"src.main:app\", \"--host\", \"0.0.0.0\"]\n\n"
                "# ---\n"
                "# docker-compose.yml\n"
                "services:\n"
                "  api:\n"
                "    build: .\n"
                "    ports:\n"
                "      - \"8000:8000\"\n"
                "    environment:\n"
                "      - DATABASE_URL=postgresql://user:pass@db:5432/app\n"
                "    depends_on:\n"
                "      db:\n"
                "        condition: service_healthy\n\n"
                "  db:\n"
                "    image: postgres:16-alpine\n"
                "    environment:\n"
                "      POSTGRES_USER: user\n"
                "      POSTGRES_PASSWORD: pass\n"
                "      POSTGRES_DB: app\n"
                "    volumes:\n"
                "      - donnees_pg:/var/lib/postgresql/data\n"
                "    healthcheck:\n"
                "      test: [\"CMD-SHELL\", \"pg_isready -U user\"]\n"
                "      interval: 5s\n\n"
                "  redis:\n"
                "    image: redis:7-alpine\n"
                "    ports:\n"
                "      - \"6379:6379\"\n\n"
                "volumes:\n"
                "  donnees_pg:"
            ),
            "performance": {
                "startup_time": "Demarrage en secondes (vs minutes pour une VM). Les conteneurs demarrent presque instantanement car ils partagent le noyau hote.",
                "throughput": "Overhead minimal par rapport a l'execution native (<5% dans la plupart des cas). Les namespaces et cgroups ajoutent un cout negligeable.",
                "memory": "Consommation memoire proche du natif. L'overhead est principalement lie au systeme de fichiers Union (OverlayFS). Les images Alpine minimisent l'empreinte de base.",
                "concurrency_model": "Chaque conteneur est un processus (ou groupe de processus) isole. L'orchestration de multiples conteneurs est geree par Docker Compose ou Kubernetes."
            },
            "learning_curve": (
                "La courbe d'apprentissage de Docker est progressive. Les bases\n"
                "(docker run, docker build, Dockerfile) sont accessibles en\n"
                "quelques heures. Docker Compose s'apprend en une journee.\n"
                "La complexite augmente avec l'optimisation des images\n"
                "(multi-stage builds, caching), la securite (images de base,\n"
                "utilisateur non-root, secrets), les reseaux, et les volumes\n"
                "en production."
            ),
            "community_size": "Docker Hub heberge des millions d'images. Communaute massive et omnipresente. Docker est le standard de facto mentionne dans pratiquement toutes les documentations modernes.",
            "job_market": "Docker est un prerequis quasi universel pour les postes DevOps, backend et cloud. Sa maitrise est souvent consideree comme acquise dans les offres d'emploi modernes."
        },
        "traits": {
            "performance": 7,
            "developer_speed": 8,
            "learning_curve": 4,
            "ecosystem_size": 9,
            "type_safety": 5,
            "concurrency": 7,
            "memory_safety": 7,
            "scalability": 8
        }
    },

    "kubernetes": {
        "name": "Kubernetes",
        "category": "devops",
        "year_created": 2014,
        "creator": "Google",
        "paradigm": ["orchestration", "declaratif", "distribue", "auto-reparation"],
        "typing": "declaratif (manifestes YAML/JSON)",
        "sections": {
            "overview": (
                "Kubernetes (souvent abrege K8s) est une plateforme open source\n"
                "d'orchestration de conteneurs qui automatise le deploiement,\n"
                "la mise a l'echelle et la gestion des applications conteneurisees.\n"
                "Cree par Google et base sur plus de 15 ans d'experience interne\n"
                "avec les systemes Borg et Omega, Kubernetes est devenu le\n"
                "standard de facto pour l'orchestration de conteneurs.\n\n"
                "Kubernetes adopte une approche declarative : l'utilisateur decrit\n"
                "l'etat desire du systeme (combien de repliques, quelle image,\n"
                "quelles ressources), et Kubernetes converge continuellement\n"
                "l'etat reel vers l'etat desire via des boucles de reconciliation.\n"
                "Ce modele declaratif est la cle de la robustesse de Kubernetes.\n\n"
                "Les fonctionnalites principales incluent : le deploiement\n"
                "automatise avec rollback, la mise a l'echelle automatique\n"
                "(Horizontal Pod Autoscaler), la decouverte de services et\n"
                "l'equilibrage de charge, la gestion des secrets et de la\n"
                "configuration, le stockage persistant, et l'auto-reparation\n"
                "(redemarrage des conteneurs defaillants).\n\n"
                "Kubernetes est extensible par conception : les Custom Resource\n"
                "Definitions (CRD) permettent de definir de nouveaux types de\n"
                "ressources, et les operateurs encodent la logique operationnelle\n"
                "specifique a un domaine. Cet ecosysteme d'extensions est\n"
                "l'une des forces majeures de la plateforme."
            ),
            "history": (
                "L'histoire de Kubernetes commence chez Google dans les annees\n"
                "2000. Google utilisait en interne deux systemes d'orchestration\n"
                "de conteneurs : Borg (depuis 2003) et son successeur Omega.\n"
                "Ces systemes geraient des millions de conteneurs quotidiennement\n"
                "dans les datacenters de Google.\n\n"
                "En 2014, trois ingenieurs de Google - Joe Beda, Brendan Burns\n"
                "et Craig McLuckie - ont lance le projet Kubernetes, s'inspirant\n"
                "de l'architecture de Borg tout en creant un systeme open source\n"
                "accessible a tous. Le nom 'Kubernetes' vient du grec et signifie\n"
                "'timonier' ou 'pilote', ce qui explique le logo en forme de\n"
                "gouvernail.\n\n"
                "La premiere version, Kubernetes 1.0, est sortie en juillet 2015.\n"
                "Google a simultanement cree la Cloud Native Computing Foundation\n"
                "(CNCF), une branche de la Linux Foundation, et lui a fait don\n"
                "de Kubernetes comme premier projet.\n\n"
                "L'adoption a ete fulgurante. En 2017, Kubernetes avait deja\n"
                "gagne la 'guerre des orchestrateurs' contre Docker Swarm et\n"
                "Apache Mesos. Les trois principaux fournisseurs cloud ont\n"
                "lance des services manages : GKE (Google, 2015), EKS (Amazon,\n"
                "2018) et AKS (Microsoft, 2018).\n\n"
                "La maturite de l'ecosysteme s'est acceleree avec le projet\n"
                "Helm (gestionnaire de packages), Istio (service mesh), et\n"
                "des centaines d'operateurs et d'outils complementaires.\n\n"
                "En 2025, Kubernetes est deploye dans la grande majorite des\n"
                "entreprises tech et une part croissante des entreprises\n"
                "traditionnelles. Il est devenu le 'systeme d'exploitation\n"
                "du cloud'."
            ),
            "architecture": (
                "L'architecture de Kubernetes suit un modele maitre-worker\n"
                "(control plane + data plane) :\n\n"
                "Control Plane (Plan de controle) :\n"
                "- kube-apiserver : Le point d'entree de toute communication.\n"
                "  Expose l'API REST de Kubernetes et valide les requetes.\n"
                "- etcd : La base de donnees distribuee (cle-valeur) stockant\n"
                "  l'etat complet du cluster de maniere fiable.\n"
                "- kube-scheduler : Decide sur quel noeud placer chaque Pod\n"
                "  en fonction des contraintes de ressources et d'affinite.\n"
                "- kube-controller-manager : Execute les boucles de\n"
                "  reconciliation (ReplicaSet, Deployment, StatefulSet, etc.).\n\n"
                "Data Plane (Noeuds workers) :\n"
                "- kubelet : L'agent sur chaque noeud qui s'assure que les\n"
                "  conteneurs des Pods sont en cours d'execution.\n"
                "- kube-proxy : Gere les regles reseau pour le routage du\n"
                "  trafic vers les Pods.\n"
                "- Container Runtime : Le moteur d'execution des conteneurs\n"
                "  (containerd, CRI-O) gerant le cycle de vie des conteneurs.\n\n"
                "Objets fondamentaux :\n"
                "- Pod : L'unite de deploiement minimale, un ou plusieurs\n"
                "  conteneurs partageant reseau et stockage.\n"
                "- Service : Abstraction reseau fournissant une IP stable et\n"
                "  l'equilibrage de charge vers un ensemble de Pods.\n"
                "- Deployment : Gere le deploiement declaratif et les mises a\n"
                "  jour progressives (rolling updates) des Pods.\n"
                "- ConfigMap/Secret : Gestion externalisee de la configuration\n"
                "  et des donnees sensibles.\n\n"
                "Le modele de reconciliation : chaque controller observe l'etat\n"
                "actuel, le compare a l'etat desire, et effectue les actions\n"
                "necessaires pour les aligner. Ce pattern est la cle de\n"
                "l'auto-reparation de Kubernetes."
            ),
            "pros_cons": {
                "pros": [
                    "Orchestration automatisee : deploiement, scaling, rolling updates et rollback",
                    "Auto-reparation : redemarrage automatique des conteneurs defaillants",
                    "Mise a l'echelle automatique horizontale basee sur les metriques (HPA, VPA, KEDA)",
                    "Modele declaratif garantissant la convergence vers l'etat desire",
                    "Extensibilite via les CRD et les operateurs pour tout type d'application",
                    "Standard de l'industrie supporte par tous les fournisseurs cloud (GKE, EKS, AKS)",
                    "Ecosysteme CNCF extremement riche (Prometheus, Istio, Argo, Flux, etc.)",
                    "Multi-cloud et hybride : evite le vendor lock-in"
                ],
                "cons": [
                    "Complexite operationnelle elevee : la courbe d'apprentissage est raide",
                    "Suringenierie pour les petites applications (overhead disproportionne)",
                    "La securite necessite une expertise dediee (RBAC, NetworkPolicies, PodSecurity)",
                    "Les manifestes YAML sont verbeux et sujets aux erreurs",
                    "Le debugging distribue est complexe (logs, traces, metriques)",
                    "Le cout d'infrastructure est significatif (control plane + overhead par noeud)",
                    "Les mises a jour de cluster sont delicates et necessitent une planification",
                    "Risque de 'YAML engineering' excessif sans les bons outils (Helm, Kustomize)"
                ]
            },
            "use_cases": (
                "Kubernetes excelle pour les architectures microservices, les\n"
                "applications cloud-native, le deploiement continu (CD), les\n"
                "charges de travail a scalabilite variable, le traitement par\n"
                "lots (jobs, CronJobs), les applications stateful (StatefulSets\n"
                "pour les bases de donnees), le machine learning (Kubeflow),\n"
                "et les plateformes internes de developpement (Platform Engineering).\n"
                "Il est surdimensionne pour les monolithes simples ou les\n"
                "petites equipes."
            ),
            "ecosystem_size": (
                "L'ecosysteme Kubernetes est le plus riche de l'infrastructure\n"
                "moderne. Helm gere les packages (charts). Kustomize personalise\n"
                "les manifestes sans templates. ArgoCD et Flux implementent le\n"
                "GitOps. Prometheus et Grafana pour le monitoring. Istio et\n"
                "Linkerd pour le service mesh. cert-manager pour les certificats\n"
                "TLS. External DNS pour le DNS automatique. KEDA pour l'auto-\n"
                "scaling base sur les evenements. Tekton et ArgoWorkflows\n"
                "pour les pipelines CI/CD cloud-native."
            ),
            "companies": [
                "Google",
                "Spotify",
                "Airbnb",
                "The New York Times",
                "Adidas",
                "ING Bank",
                "CERN",
                "Goldman Sachs"
            ],
            "code_example": (
                "# deployment.yaml - Deploiement d'une application web\n"
                "apiVersion: apps/v1\n"
                "kind: Deployment\n"
                "metadata:\n"
                "  name: api-web\n"
                "  labels:\n"
                "    app: api-web\n"
                "spec:\n"
                "  replicas: 3\n"
                "  selector:\n"
                "    matchLabels:\n"
                "      app: api-web\n"
                "  strategy:\n"
                "    type: RollingUpdate\n"
                "    rollingUpdate:\n"
                "      maxSurge: 1\n"
                "      maxUnavailable: 0\n"
                "  template:\n"
                "    metadata:\n"
                "      labels:\n"
                "        app: api-web\n"
                "    spec:\n"
                "      containers:\n"
                "      - name: api\n"
                "        image: mon-registre/api-web:v1.2.0\n"
                "        ports:\n"
                "        - containerPort: 8000\n"
                "        resources:\n"
                "          requests:\n"
                "            cpu: 100m\n"
                "            memory: 128Mi\n"
                "          limits:\n"
                "            cpu: 500m\n"
                "            memory: 256Mi\n"
                "        livenessProbe:\n"
                "          httpGet:\n"
                "            path: /sante\n"
                "            port: 8000\n"
                "          initialDelaySeconds: 10\n"
                "        readinessProbe:\n"
                "          httpGet:\n"
                "            path: /pret\n"
                "            port: 8000\n"
                "---\n"
                "# service.yaml - Exposition du service\n"
                "apiVersion: v1\n"
                "kind: Service\n"
                "metadata:\n"
                "  name: api-web\n"
                "spec:\n"
                "  selector:\n"
                "    app: api-web\n"
                "  ports:\n"
                "  - port: 80\n"
                "    targetPort: 8000\n"
                "  type: ClusterIP\n"
                "---\n"
                "# hpa.yaml - Auto-scaling horizontal\n"
                "apiVersion: autoscaling/v2\n"
                "kind: HorizontalPodAutoscaler\n"
                "metadata:\n"
                "  name: api-web\n"
                "spec:\n"
                "  scaleTargetRef:\n"
                "    apiVersion: apps/v1\n"
                "    kind: Deployment\n"
                "    name: api-web\n"
                "  minReplicas: 3\n"
                "  maxReplicas: 20\n"
                "  metrics:\n"
                "  - type: Resource\n"
                "    resource:\n"
                "      name: cpu\n"
                "      target:\n"
                "        type: Utilization\n"
                "        averageUtilization: 70"
            ),
            "performance": {
                "startup_time": "Le deploiement d'un Pod prend generalement 5-30 secondes (scheduling + pull image + demarrage conteneur). Le control plane demarre en quelques minutes.",
                "throughput": "Kubernetes lui-meme n'impacte pas le throughput applicatif. L'overhead reseau (kube-proxy, service mesh) ajoute une latence minime (< 1ms). L'API server gere des milliers de requetes/seconde.",
                "memory": "L'overhead par noeud est significatif : kubelet, kube-proxy et le runtime consomment 500 Mo - 1 Go. Le control plane (etcd, apiserver, etc.) necessite des ressources dediees.",
                "concurrency_model": "Modele declaratif avec boucles de reconciliation asynchrones. Chaque controller s'execute independamment. La concurrence est geree au niveau des Pods (multiples repliques) et des noeuds (scheduling distribue)."
            },
            "learning_curve": (
                "La courbe d'apprentissage de Kubernetes est l'une des plus raides\n"
                "de l'ecosysteme DevOps. Les concepts fondamentaux (Pods, Services,\n"
                "Deployments) sont accessibles, mais la maitrise operationnelle\n"
                "(RBAC, NetworkPolicies, resource quotas, operators, CRD, service\n"
                "mesh, observabilite) necessite des mois voire des annees\n"
                "d'experience. Les certifications CKA/CKAD attestent de cette\n"
                "expertise."
            ),
            "community_size": "Le plus grand projet open source au monde apres Linux. Plus de 110 000 etoiles GitHub. Des milliers de contributeurs. KubeCon attire plus de 10 000 participants.",
            "job_market": "Kubernetes est la competence DevOps la plus demandee et la mieux remuneree. Les postes d'ingenieur Kubernetes/Platform offrent des salaires parmi les plus eleves du secteur."
        },
        "traits": {
            "performance": 7,
            "developer_speed": 4,
            "learning_curve": 8,
            "ecosystem_size": 9,
            "type_safety": 6,
            "concurrency": 9,
            "memory_safety": 7,
            "scalability": 10
        }
    },

    "terraform": {
        "name": "Terraform",
        "category": "devops",
        "year_created": 2014,
        "creator": "HashiCorp",
        "paradigm": ["infrastructure as code", "declaratif", "immutable", "plan-apply"],
        "typing": "declaratif (HCL - HashiCorp Configuration Language)",
        "sections": {
            "overview": (
                "Terraform est un outil d'Infrastructure as Code (IaC) open source\n"
                "qui permet de definir, provisionner et gerer l'infrastructure\n"
                "cloud et on-premise de maniere declarative. Plutot que de\n"
                "configurer l'infrastructure manuellement via des consoles web\n"
                "ou des scripts imperatifs, Terraform permet de decrire l'etat\n"
                "desire de l'infrastructure dans des fichiers de configuration.\n\n"
                "Terraform utilise HCL (HashiCorp Configuration Language), un\n"
                "langage declaratif concu pour etre lisible par les humains\n"
                "tout en etant machine-parseable. HCL combine la lisibilite\n"
                "du YAML avec les capacites programmatiques necessaires pour\n"
                "decrire des infrastructures complexes.\n\n"
                "Le workflow de Terraform suit trois etapes : Write (ecrire la\n"
                "configuration), Plan (previsualiser les changements) et Apply\n"
                "(appliquer les changements). La commande 'terraform plan'\n"
                "affiche un diff detaille des changements prevus avant toute\n"
                "modification, offrant une securite precieuse.\n\n"
                "La force majeure de Terraform est son ecosysteme de providers :\n"
                "des plugins qui permettent de gerer des ressources chez plus de\n"
                "3000 fournisseurs (AWS, Azure, Google Cloud, Kubernetes, GitHub,\n"
                "Datadog, PagerDuty, etc.). Cette universalite fait de Terraform\n"
                "un point d'entree unique pour gerer toute l'infrastructure.\n\n"
                "Le fichier d'etat (state) de Terraform est un concept central :\n"
                "il maintient la correspondance entre la configuration declaree\n"
                "et les ressources reelles, permettant a Terraform de calculer\n"
                "les changements incrementaux necessaires."
            ),
            "history": (
                "Terraform a ete cree par Mitchell Hashimoto et Armon Dadgar,\n"
                "cofondateurs de HashiCorp, en 2014. HashiCorp avait deja cree\n"
                "Vagrant (pour les environnements de developpement) et Packer\n"
                "(pour les images machine). Terraform completait cette vision\n"
                "en adressant le provisionnement de l'infrastructure cloud.\n\n"
                "La premiere version publique (0.1) est sortie en juillet 2014.\n"
                "L'approche de Terraform etait novatrice : un outil multi-cloud\n"
                "unique utilisant un langage declaratif et un systeme d'etat\n"
                "pour gerer l'infrastructure de maniere incrementale.\n\n"
                "L'adoption a ete progressive mais constante. AWS CloudFormation\n"
                "existait deja mais etait limite a AWS et utilisant un JSON\n"
                "verbeux. Terraform offrait la portabilite multi-cloud et\n"
                "un langage plus agreable.\n\n"
                "Terraform 0.12 (2019) a ete une refonte majeure de HCL,\n"
                "ajoutant les expressions riches, les boucles (for_each),\n"
                "les conditions, et un typage ameliore. Cette version a\n"
                "considerablement reduit la frustration des utilisateurs.\n\n"
                "Terraform 1.0 (juin 2021) a marque la garantie de stabilite\n"
                "de l'API et du langage. Les versions suivantes ont ameliore\n"
                "les performances, les tests (terraform test), et l'import\n"
                "de ressources existantes.\n\n"
                "En aout 2023, HashiCorp a change la licence de Terraform de\n"
                "MPL 2.0 a BSL (Business Source License), une decision\n"
                "controversee qui a provoque la creation du fork OpenTofu,\n"
                "soutenu par la Linux Foundation. Ce schisme a divise la\n"
                "communaute mais les deux projets continuent d'evoluer.\n\n"
                "En 2024, IBM a rachete HashiCorp pour 6,4 milliards de dollars,\n"
                "ajoutant une nouvelle incertitude sur le futur de Terraform."
            ),
            "architecture": (
                "L'architecture de Terraform repose sur trois composants\n"
                "principaux et un workflow plan/apply :\n\n"
                "Core Terraform : Le moteur central qui parse les fichiers HCL,\n"
                "construit le graphe de dependances des ressources, calcule le\n"
                "plan de changements, et orchestre l'execution du plan via\n"
                "les providers.\n\n"
                "Providers : Les plugins qui implementent la logique d'interaction\n"
                "avec les API externes. Chaque provider (aws, azurerm, google,\n"
                "kubernetes, etc.) definit des types de ressources et de data\n"
                "sources. Les providers sont distribues independamment via le\n"
                "Terraform Registry.\n\n"
                "State (Etat) : Le fichier d'etat (terraform.tfstate) est une\n"
                "representation JSON de l'infrastructure geree. Il fait le lien\n"
                "entre les identifiants logiques (dans le code HCL) et les\n"
                "identifiants physiques (dans le cloud). Le state backend\n"
                "stocke cet etat (localement, S3, Azure Blob, GCS, Terraform\n"
                "Cloud, etc.).\n\n"
                "Graphe de dependances : Terraform construit automatiquement\n"
                "un DAG (Directed Acyclic Graph) des ressources basees sur\n"
                "leurs references mutuelles. Les ressources independantes\n"
                "sont creees en parallele, les dependantes sequentiellement.\n\n"
                "Workflow Plan/Apply :\n"
                "- terraform init : Telecharge les providers et initialise\n"
                "  le backend d'etat.\n"
                "- terraform plan : Compare l'etat desire (config) avec\n"
                "  l'etat actuel (state/API) et produit un plan de changements.\n"
                "- terraform apply : Execute le plan apres confirmation.\n"
                "- terraform destroy : Supprime toutes les ressources gerees.\n\n"
                "Modules : Les modules sont des blocs de configuration\n"
                "reutilisables, equivalents aux fonctions en programmation.\n"
                "Le Terraform Registry heberge des milliers de modules\n"
                "communautaires."
            ),
            "pros_cons": {
                "pros": [
                    "Multi-cloud veritable avec plus de 3000 providers disponibles",
                    "Le workflow plan/apply offre une previsualisation securisee des changements",
                    "HCL est lisible, expressif et concu pour l'Infrastructure as Code",
                    "Le graphe de dependances gere automatiquement l'ordre de creation",
                    "Les modules permettent la reutilisation et la standardisation",
                    "Ecosysteme mature avec Terraform Cloud, Atlantis, Spacelift, env0",
                    "Versionnable dans Git : revue de code, historique, collaboration",
                    "Import de ressources existantes pour adopter Terraform progressivement"
                ],
                "cons": [
                    "La gestion de l'etat (state) est complexe et source d'erreurs en equipe",
                    "Le changement de licence BSL a fragmente la communaute (fork OpenTofu)",
                    "Les changements destructifs (recreate) peuvent etre surprenants et dangereux",
                    "Le debugging des erreurs de providers est parfois opaque",
                    "HCL a des limitations programmatiques (pas de vraie logique conditionnelle complexe)",
                    "Le drift (ecart entre l'etat declare et l'etat reel) necessite une gestion attentive",
                    "Les modules complexes peuvent devenir difficiles a maintenir et a comprendre"
                ]
            },
            "use_cases": (
                "Terraform est utilise pour provisionner et gerer toute\n"
                "infrastructure cloud : reseaux (VPC, sous-reseaux, load\n"
                "balancers), compute (instances, clusters Kubernetes, serverless),\n"
                "stockage (S3, bases de donnees), securite (IAM, certificats),\n"
                "et services annexes (DNS, monitoring, alerting). Il est\n"
                "egalement utilise pour gerer des services SaaS (GitHub repos,\n"
                "Datadog dashboards, PagerDuty policies) via leurs providers."
            ),
            "ecosystem_size": (
                "L'ecosysteme Terraform est riche. Terraform Cloud/Enterprise\n"
                "fournit la gestion d'etat, les plans en equipe et la gouvernance.\n"
                "Atlantis permet le plan/apply via les pull requests. Spacelift,\n"
                "env0 et Scalr sont des alternatives cloud. Terragrunt (Gruntwork)\n"
                "facilite la gestion de configurations complexes. Checkov,\n"
                "tfsec et Trivy analysent la securite des configurations.\n"
                "Terraform CDK (CDKTF) permet d'ecrire du Terraform en\n"
                "TypeScript, Python, Java ou C#. OpenTofu est le fork\n"
                "communautaire sous licence MPL."
            ),
            "companies": [
                "Pratiquement toutes les entreprises utilisant le cloud",
                "Stripe",
                "Uber",
                "Shopify",
                "Slack",
                "Twitch",
                "DoorDash",
                "Databricks"
            ],
            "code_example": (
                "# main.tf - Infrastructure AWS avec Terraform\n"
                "terraform {\n"
                "  required_providers {\n"
                "    aws = {\n"
                "      source  = \"hashicorp/aws\"\n"
                "      version = \"~> 5.0\"\n"
                "    }\n"
                "  }\n"
                "  backend \"s3\" {\n"
                "    bucket = \"mon-terraform-state\"\n"
                "    key    = \"prod/infrastructure.tfstate\"\n"
                "    region = \"eu-west-3\"  # Paris\n"
                "  }\n"
                "}\n\n"
                "provider \"aws\" {\n"
                "  region = var.region\n"
                "}\n\n"
                "# Reseau VPC\n"
                "resource \"aws_vpc\" \"principal\" {\n"
                "  cidr_block           = \"10.0.0.0/16\"\n"
                "  enable_dns_hostnames = true\n"
                "  tags = {\n"
                "    Nom         = \"vpc-production\"\n"
                "    Environnement = \"production\"\n"
                "  }\n"
                "}\n\n"
                "# Sous-reseaux dans plusieurs zones de disponibilite\n"
                "resource \"aws_subnet\" \"publics\" {\n"
                "  for_each = toset([\"eu-west-3a\", \"eu-west-3b\"])\n\n"
                "  vpc_id            = aws_vpc.principal.id\n"
                "  cidr_block        = cidrsubnet(aws_vpc.principal.cidr_block, 8, index(tolist(toset([\"eu-west-3a\", \"eu-west-3b\"])), each.value))\n"
                "  availability_zone = each.value\n"
                "}\n\n"
                "# variables.tf\n"
                "variable \"region\" {\n"
                "  description = \"Region AWS de deploiement\"\n"
                "  type        = string\n"
                "  default     = \"eu-west-3\"\n"
                "}\n\n"
                "# outputs.tf\n"
                "output \"vpc_id\" {\n"
                "  description = \"Identifiant du VPC principal\"\n"
                "  value       = aws_vpc.principal.id\n"
                "}"
            ),
            "performance": {
                "startup_time": "L'initialisation (terraform init) prend quelques secondes pour telecharger les providers. Le plan peut prendre de secondes a minutes selon le nombre de ressources.",
                "throughput": "Terraform cree les ressources independantes en parallele (configurable via -parallelism). Le throughput depend principalement de la vitesse des API cloud.",
                "memory": "Consommation memoire moderee pour les petites configurations. Les grands etats (milliers de ressources) peuvent consommer plusieurs Go de RAM pendant le plan.",
                "concurrency_model": "Parallelisme base sur le graphe de dependances. Les ressources sans dependances mutuelles sont provisionnees simultanement. Le verrouillage de l'etat empeche les modifications concurrentes."
            },
            "learning_curve": (
                "La courbe d'apprentissage est moderee. Les bases de HCL sont\n"
                "accessibles en quelques heures. La comprehension du state, des\n"
                "modules, des workspaces et du workflow en equipe prend plus\n"
                "de temps. La vraie complexite reside dans la connaissance\n"
                "des services cloud sous-jacents (AWS, Azure, GCP) et les\n"
                "patterns d'IaC a grande echelle (organisation des modules,\n"
                "gestion de l'etat multi-environnement)."
            ),
            "community_size": "Plus de 42 000 etoiles sur GitHub. Enorme communaute. Le Terraform Registry heberge des milliers de providers et modules. OpenTofu poursuit en parallele avec une communaute croissante.",
            "job_market": "Terraform est la competence IaC la plus demandee. Mentionne dans la majorite des offres DevOps et SRE. Sa maitrise est un critere quasi obligatoire pour les postes infrastructure cloud."
        },
        "traits": {
            "performance": 5,
            "developer_speed": 6,
            "learning_curve": 5,
            "ecosystem_size": 8,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 9
        }
    },

    "github_actions": {
        "name": "GitHub Actions",
        "category": "devops",
        "year_created": 2019,
        "creator": "GitHub/Microsoft",
        "paradigm": ["CI/CD", "evenementiel", "declaratif", "workflow automation"],
        "typing": "declaratif (YAML)",
        "sections": {
            "overview": (
                "GitHub Actions est une plateforme d'integration continue (CI)\n"
                "et de deploiement continu (CD) integree directement dans GitHub.\n"
                "Elle permet d'automatiser les workflows de developpement en\n"
                "reponse a des evenements sur le depot : push, pull request,\n"
                "publication de release, creation d'issue, ou meme un planning\n"
                "cron.\n\n"
                "La force de GitHub Actions reside dans son integration native\n"
                "avec GitHub. Il n'y a pas de service externe a configurer,\n"
                "pas d'authentification complexe entre le CI et le depot.\n"
                "Les workflows sont definis dans des fichiers YAML places dans\n"
                "le dossier .github/workflows/ du depot.\n\n"
                "Le Marketplace GitHub Actions heberge plus de 20 000 actions\n"
                "communautaires reutilisables, allant du linting au deploiement\n"
                "cloud en passant par les notifications. Les actions sont\n"
                "versionees et peuvent etre ecrites en JavaScript/TypeScript,\n"
                "en Docker, ou comme composite actions.\n\n"
                "GitHub Actions offre des runners heberges (Ubuntu, Windows, macOS)\n"
                "et la possibilite d'utiliser des runners auto-heberges pour\n"
                "des besoins specifiques (GPU, materiel particulier, reseau\n"
                "prive). Les runners heberges sont gratuits pour les depots\n"
                "publics avec des quotas genereux.\n\n"
                "Le systeme de matrice de build permet de tester une application\n"
                "sur de multiples combinaisons d'OS, versions de langage et\n"
                "configurations en parallele, simplifiant les tests de\n"
                "compatibilite."
            ),
            "history": (
                "GitHub Actions a ete annonce pour la premiere fois lors de\n"
                "GitHub Universe en octobre 2018, un an apres le rachat de\n"
                "GitHub par Microsoft pour 7,5 milliards de dollars. La version\n"
                "initiale utilisait un format HCL (comme Terraform), mais a\n"
                "rapidement pivote vers YAML avant la sortie publique.\n\n"
                "La version beta a debute en 2018, accessible sur invitation.\n"
                "Le format de configuration a evolue significativement pendant\n"
                "cette phase, passant du HCL a un format YAML qui est devenu\n"
                "le standard.\n\n"
                "GitHub Actions est sorti en disponibilite generale en\n"
                "novembre 2019. L'adoption a ete explosive : la commodite\n"
                "de l'integration native avec GitHub, la generosite du plan\n"
                "gratuit pour les depots publics, et le Marketplace d'actions\n"
                "ont seduit instantanement la communaute.\n\n"
                "En quelques mois, GitHub Actions est devenu une menace\n"
                "serieuse pour Jenkins, Travis CI et CircleCI. Travis CI,\n"
                "qui etait le standard de facto pour les projets open source,\n"
                "a vu ses utilisateurs migrer massivement vers GitHub Actions.\n\n"
                "Les evolutions subsequentes ont apporte les environments\n"
                "de deploiement avec protection, les secrets d'organisation,\n"
                "les runners ephemeres, les caches ameliores, les reusable\n"
                "workflows, les composite actions, et les larger runners\n"
                "(machines plus puissantes).\n\n"
                "En 2023-2024, GitHub a introduit les Attestations pour la\n"
                "securite de la chaine d'approvisionnement logicielle (SLSA),\n"
                "les Actions Immer pour les actions JavaScript rapides, et\n"
                "des ameliorations continues du cache et des performances.\n\n"
                "En 2025, GitHub Actions est le service CI/CD le plus utilise\n"
                "au monde pour les projets open source et gagne rapidement\n"
                "des parts de marche en entreprise."
            ),
            "architecture": (
                "L'architecture de GitHub Actions repose sur un systeme\n"
                "evenementiel et des runners d'execution :\n\n"
                "Workflows : Definis en YAML dans .github/workflows/. Un\n"
                "workflow est declenche par un ou plusieurs evenements et\n"
                "contient un ou plusieurs jobs. Les workflows sont versionnes\n"
                "avec le code source.\n\n"
                "Events (Evenements) : Les declencheurs de workflows. Les\n"
                "evenements incluent : push, pull_request, release, schedule\n"
                "(cron), workflow_dispatch (declenchement manuel), issue\n"
                "events, et des webhooks personnalises.\n\n"
                "Jobs : Chaque job s'execute sur un runner independant.\n"
                "Les jobs peuvent s'executer en parallele ou avoir des\n"
                "dependances (needs:). Chaque job contient une sequence\n"
                "d'etapes (steps).\n\n"
                "Steps (Etapes) : Chaque etape est soit une commande shell\n"
                "(run:) soit une action reutilisable (uses:). Les etapes\n"
                "s'executent sequentiellement dans le meme runner.\n\n"
                "Actions : Des unites de travail reutilisables. Types :\n"
                "JavaScript/TypeScript (executees directement), Docker\n"
                "(executees dans un conteneur), Composite (assemblage\n"
                "d'autres actions). Les actions sont distribuees via\n"
                "des depots Git et versionnees.\n\n"
                "Runners : Les machines executant les jobs. GitHub fournit\n"
                "des runners heberges (Ubuntu, Windows, macOS) avec des\n"
                "images pre-configurees. Les runners auto-heberges\n"
                "permettent des configurations personnalisees.\n\n"
                "Artefacts et cache : Les artefacts sont des fichiers\n"
                "produits pendant un job et partages entre jobs ou\n"
                "telecharges. Le cache (actions/cache) persiste les\n"
                "dependances entre les executions pour accelerer les builds."
            ),
            "pros_cons": {
                "pros": [
                    "Integration native avec GitHub : aucun service externe a configurer",
                    "Gratuit et genereux pour les depots publics open source",
                    "Marketplace de plus de 20 000 actions communautaires reutilisables",
                    "Matrice de build pour tester sur plusieurs OS/versions en parallele",
                    "YAML lisible et versionne avec le code source",
                    "Runners heberges (Ubuntu, Windows, macOS) sans infrastructure a gerer",
                    "Reusable workflows pour partager des pipelines entre depots",
                    "Securite integree : secrets chiffres, OIDC pour le cloud, attestations SLSA"
                ],
                "cons": [
                    "Verrouillage dans l'ecosysteme GitHub (migration couteuse vers d'autres plateformes)",
                    "Le debugging des workflows est fastidieux (pas d'execution locale native)",
                    "Les temps d'execution des runners heberges peuvent etre lents aux heures de pointe",
                    "La syntaxe YAML est source d'erreurs de formatage et difficile a valider",
                    "Les couts peuvent augmenter rapidement pour les depots prives en entreprise",
                    "Le systeme de cache a des limites (7 jours de retention, taille limitee)",
                    "La securite des actions tierces necessite une vigilance (supply chain attacks)",
                    "L'absence d'execution locale rend le cycle de developpement de workflows long"
                ]
            },
            "use_cases": (
                "GitHub Actions couvre tous les cas d'usage CI/CD : tests\n"
                "automatiques sur les pull requests, builds et packaging,\n"
                "deploiement continu vers le cloud (AWS, Azure, GCP),\n"
                "publication de packages (npm, PyPI, Docker Hub),\n"
                "automatisation de la gestion de depot (labels automatiques,\n"
                "stale issue management), generation de documentation,\n"
                "scans de securite, et tout workflow automatisable\n"
                "lie au cycle de vie du code."
            ),
            "ecosystem_size": (
                "L'ecosysteme GitHub Actions est centre sur le Marketplace.\n"
                "Actions officielles majeures : actions/checkout, actions/setup-node,\n"
                "actions/cache, actions/upload-artifact. Actions cloud :\n"
                "aws-actions/configure-aws-credentials, azure/login,\n"
                "google-github-actions/auth. Securite : github/codeql-action,\n"
                "aquasecurity/trivy-action. Deploiement : peaceiris/actions-gh-pages.\n"
                "Outils de developpement local : act (execution locale des\n"
                "workflows), actionlint (linting YAML). Integration avec\n"
                "GitHub Packages, GitHub Pages, Dependabot et GitHub\n"
                "Advanced Security."
            ),
            "companies": [
                "Microsoft (tous les projets .NET, VS Code, TypeScript)",
                "Google (certains projets open source)",
                "Meta (React, React Native)",
                "Vercel (Next.js)",
                "Rust Foundation (compilateur Rust)",
                "La majorite des projets open source sur GitHub",
                "Shopify",
                "Stripe"
            ],
            "code_example": (
                "# .github/workflows/ci.yml\n"
                "name: Integration Continue\n\n"
                "on:\n"
                "  push:\n"
                "    branches: [main]\n"
                "  pull_request:\n"
                "    branches: [main]\n\n"
                "jobs:\n"
                "  tests:\n"
                "    name: Tests (${{ matrix.os }}, Python ${{ matrix.python }})\n"
                "    runs-on: ${{ matrix.os }}\n"
                "    strategy:\n"
                "      matrix:\n"
                "        os: [ubuntu-latest, macos-latest]\n"
                "        python: ['3.11', '3.12']\n\n"
                "    steps:\n"
                "    - name: Recuperer le code\n"
                "      uses: actions/checkout@v4\n\n"
                "    - name: Configurer Python ${{ matrix.python }}\n"
                "      uses: actions/setup-python@v5\n"
                "      with:\n"
                "        python-version: ${{ matrix.python }}\n\n"
                "    - name: Mettre en cache les dependances\n"
                "      uses: actions/cache@v4\n"
                "      with:\n"
                "        path: ~/.cache/pip\n"
                "        key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}\n\n"
                "    - name: Installer les dependances\n"
                "      run: |\n"
                "        python -m pip install --upgrade pip\n"
                "        pip install -r requirements.txt\n\n"
                "    - name: Verifier le formatage\n"
                "      run: ruff check --select I .\n\n"
                "    - name: Executer les tests\n"
                "      run: pytest --cov=src --cov-report=xml tests/\n\n"
                "    - name: Publier la couverture\n"
                "      if: matrix.os == 'ubuntu-latest' && matrix.python == '3.12'\n"
                "      uses: codecov/codecov-action@v4\n"
                "      with:\n"
                "        files: coverage.xml\n\n"
                "  deploiement:\n"
                "    name: Deployer en production\n"
                "    needs: tests\n"
                "    if: github.ref == 'refs/heads/main' && github.event_name == 'push'\n"
                "    runs-on: ubuntu-latest\n"
                "    environment: production\n"
                "    steps:\n"
                "    - uses: actions/checkout@v4\n"
                "    - name: Deployer\n"
                "      run: echo \"Deploiement en production...\""
            ),
            "performance": {
                "startup_time": "Les jobs demarrent en 10-60 secondes sur les runners heberges (temps de provisionnement du runner + checkout). Les runners auto-heberges demarrent plus rapidement.",
                "throughput": "Parallelisme excellent : les jobs independants s'executent en parallele sur des runners separes. Les matrices de build permettent de tester de nombreuses combinaisons simultanement.",
                "memory": "Les runners heberges offrent 7 Go de RAM (standard) ou plus (larger runners). Les runners auto-heberges offrent les ressources de la machine sous-jacente.",
                "concurrency_model": "Chaque job s'execute dans un runner independant (VM ou conteneur). Les etapes d'un job sont sequentielles. Les jobs sans dependances mutuelles s'executent en parallele. Le controle de concurrence limite les executions simultanees."
            },
            "learning_curve": (
                "La courbe d'apprentissage est douce pour les cas simples.\n"
                "Un workflow de test basique peut etre ecrit en 15 minutes.\n"
                "La complexite augmente avec les matrices de build, les\n"
                "reusable workflows, les environnements de deploiement, la\n"
                "securite (OIDC, secrets), et la creation d'actions\n"
                "personnalisees. Le debugging sans execution locale est\n"
                "la principale source de friction."
            ),
            "community_size": "La plus grande communaute CI/CD au monde, adossee a la communaute GitHub. Le Marketplace heberge plus de 20 000 actions. Des milliers de tutoriels et d'exemples disponibles.",
            "job_market": "GitHub Actions est mentionne dans un nombre croissant d'offres DevOps. Sa connaissance est un atout pour tout poste impliquant du CI/CD. Souvent combine avec Terraform et Kubernetes dans les offres."
        },
        "traits": {
            "performance": 5,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 8,
            "type_safety": 4,
            "concurrency": 6,
            "memory_safety": 5,
            "scalability": 7
        }
    }
}
