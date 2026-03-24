"""
Donnees sur les technologies de messagerie et de streaming d'evenements.
Chaque entree documente un systeme de messagerie avec son histoire, son architecture,
ses cas d'usage et ses caracteristiques techniques.
"""

TECHNOLOGIES = {
    "kafka": {
        "name": "Apache Kafka",
        "category": "messaging",
        "year_created": 2011,
        "creator": "LinkedIn / Apache",
        "paradigm": ["Event Streaming", "Pub/Sub", "Log distribue"],
        "typing": "Agnostique (clients multi-langages)",
        "sections": {
            "overview": (
                "Apache Kafka est une plateforme de streaming d'evenements distribuee,\n"
                "concue pour gerer des flux de donnees en temps reel a tres grande\n"
                "echelle. A la difference d'un message broker traditionnel, Kafka\n"
                "repose sur le concept fondamental du log distribue immutable : chaque\n"
                "message publie dans un topic est persiste sur disque de maniere\n"
                "sequentielle et conserve pendant une duree configurable, independamment\n"
                "de sa consommation par les abonnes.\n\n"
                "Cette architecture de log append-only confere a Kafka des proprietes\n"
                "uniques. Les consommateurs ne detruisent pas les messages apres lecture ;\n"
                "ils maintiennent un offset qui represente leur position dans le log.\n"
                "Plusieurs groupes de consommateurs peuvent ainsi lire le meme topic\n"
                "independamment, a des vitesses differentes, et meme rejouer l'historique\n"
                "complet des evenements depuis le debut du log.\n\n"
                "Kafka a ete concu pour garantir un debit extremement eleve, capable\n"
                "de traiter des millions de messages par seconde sur un cluster\n"
                "correctement dimensionne. Cette performance est obtenue grace a\n"
                "l'ecriture sequentielle sur disque (qui exploite le cache du systeme\n"
                "d'exploitation), au batching des messages cote producteur et\n"
                "consommateur, et au mecanisme zero-copy pour le transfert reseau.\n\n"
                "Kafka se positionne aujourd'hui comme l'epine dorsale de nombreuses\n"
                "architectures evenementielles (event-driven architecture), permettant\n"
                "le decouplage temporel et spatial entre producteurs et consommateurs,\n"
                "la construction de pipelines de donnees en temps reel, et la mise en\n"
                "oeuvre de patterns comme Event Sourcing et CQRS a l'echelle de\n"
                "l'entreprise."
            ),
            "history": (
                "Apache Kafka a ete cree en 2010-2011 au sein de LinkedIn par une\n"
                "equipe dirigee par Jay Kreps, Neha Narkhede et Jun Rao. LinkedIn\n"
                "faisait face a un defi majeur : unifier les flux de donnees entre\n"
                "ses nombreux systemes internes (recherche, recommandations, monitoring,\n"
                "analytics) qui generaient des volumes colossaux de donnees en temps\n"
                "reel. Les solutions de messagerie existantes (ActiveMQ, RabbitMQ)\n"
                "ne pouvaient pas supporter le debit requis.\n\n"
                "Le nom 'Kafka' a ete choisi par Jay Kreps en reference a l'ecrivain\n"
                "Franz Kafka, car le systeme est 'optimise pour l'ecriture' et Kreps\n"
                "appreciait les oeuvres de l'auteur. Le projet a ete open-source en\n"
                "janvier 2011 et a rejoint l'incubateur Apache la meme annee.\n\n"
                "En 2012, Kafka est devenu un projet top-level de la fondation Apache.\n"
                "Les versions 0.8 (2013) et 0.9 (2015) ont apporte la replication\n"
                "des partitions, les groupes de consommateurs, et le nouveau protocole\n"
                "client. La version 0.10 (2016) a introduit Kafka Streams, permettant\n"
                "le traitement de flux directement dans Kafka.\n\n"
                "En 2014, Jay Kreps, Neha Narkhede et Jun Rao ont fonde Confluent,\n"
                "l'entreprise commerciale derriere Kafka, qui propose une distribution\n"
                "enrichie (Confluent Platform) avec Schema Registry, ksqlDB, des\n"
                "connecteurs manages et Confluent Cloud.\n\n"
                "La version 2.8 (2021) a marque un tournant avec l'introduction du\n"
                "mode KRaft (Kafka Raft), eliminant progressivement la dependance a\n"
                "Apache ZooKeeper pour la gestion des metadonnees du cluster. Cette\n"
                "evolution simplifie considerablement le deploiement et l'exploitation.\n"
                "En 2023-2024, ZooKeeper a ete officiellement deprecie au profit de\n"
                "KRaft, rendant Kafka autonome pour la gestion de son consensus."
            ),
            "architecture": (
                "L'architecture de Kafka repose sur plusieurs concepts fondamentaux\n"
                "qui en font un systeme de streaming distribue extremement robuste :\n\n"
                "Topics et Partitions : Un topic est un flux logique de messages.\n"
                "Chaque topic est divise en partitions, qui sont des logs ordonnes\n"
                "et immutables. Les partitions sont la unite de parallelisme de Kafka :\n"
                "chaque partition est consommee par un seul consommateur au sein d'un\n"
                "groupe, permettant une scalabilite horizontale proportionnelle au\n"
                "nombre de partitions.\n\n"
                "Brokers et Cluster : Un cluster Kafka est compose de plusieurs\n"
                "brokers (serveurs). Chaque partition est repliquee sur plusieurs\n"
                "brokers selon le facteur de replication configure. Un broker est\n"
                "designe comme leader pour chaque partition et gere les lectures et\n"
                "ecritures, tandis que les followers repliquent les donnees de maniere\n"
                "synchrone ou asynchrone.\n\n"
                "ISR (In-Sync Replicas) : Kafka maintient un ensemble de replicas\n"
                "synchronisees pour chaque partition. Un message est considere comme\n"
                "commite uniquement quand toutes les replicas ISR l'ont recu (avec\n"
                "acks=all). Si un leader tombe en panne, un follower ISR est promu\n"
                "automatiquement.\n\n"
                "Groupes de consommateurs : Les consommateurs sont organises en\n"
                "groupes. Kafka assigne automatiquement les partitions aux membres\n"
                "du groupe (rebalancing). Chaque partition est consommee par exactement\n"
                "un membre du groupe, garantissant l'ordre de traitement par partition.\n"
                "Les offsets de chaque consommateur sont stockes dans un topic interne\n"
                "(__consumer_offsets).\n\n"
                "ZooKeeper vs KRaft : Historiquement, Kafka dependait d'Apache\n"
                "ZooKeeper pour la gestion des metadonnees (liste des brokers,\n"
                "election des leaders, configuration des topics). Depuis la version\n"
                "3.x, le mode KRaft (Kafka Raft Metadata) remplace ZooKeeper par un\n"
                "quorum de controleurs internes utilisant le protocole Raft pour le\n"
                "consensus, simplifiant l'architecture et ameliorant les performances\n"
                "de demarrage du cluster.\n\n"
                "Garanties de livraison : Kafka supporte trois niveaux de garantie.\n"
                "At-most-once : le producteur n'attend pas d'acquittement (risque de\n"
                "perte). At-least-once : le producteur reessaie en cas d'echec (risque\n"
                "de doublons). Exactly-once : via les transactions et l'idempotence du\n"
                "producteur (enable.idempotence=true, transactional.id), Kafka garantit\n"
                "un traitement exactement-une-fois de bout en bout."
            ),
            "pros_cons": {
                "pros": [
                    "Debit extraordinaire : des millions de messages par seconde grace au log sequentiel et au zero-copy",
                    "Persistance durable des messages sur disque avec retention configurable (heures, jours, illimitee)",
                    "Scalabilite horizontale quasi lineaire en ajoutant des partitions et des brokers",
                    "Garantie exactly-once via les transactions et les producteurs idempotents",
                    "Rejouabilite totale : les consommateurs peuvent relire l'historique complet depuis n'importe quel offset",
                    "Ecosysteme riche : Kafka Connect, Kafka Streams, ksqlDB, Schema Registry",
                    "Haute disponibilite avec replication automatique et failover transparent des partitions",
                    "Decouplage fort entre producteurs et consommateurs permettant des architectures evenementielles robustes"
                ],
                "cons": [
                    "Complexite operationnelle significative : le deploiement et le tuning d'un cluster requierent une expertise devops poussee",
                    "Latence plus elevee que les brokers traditionnels pour les messages individuels (optimise pour le debit en batch)",
                    "Consommation de ressources importante : necessite des disques rapides, de la memoire pour le page cache, et du reseau performant",
                    "La gestion des partitions est rigide : augmenter le nombre de partitions est possible mais les reduire ne l'est pas",
                    "Le rebalancing des groupes de consommateurs peut provoquer des pauses de traitement (ameliore avec les cooperative rebalancing)",
                    "La courbe d'apprentissage est abrupte : comprendre les offsets, les ISR, le partitionnement et le tuning demande du temps",
                    "Surdimensionne pour les cas d'usage simples : un message broker classique suffit souvent pour des volumes moderes"
                ]
            },
            "use_cases": (
                "Kafka excelle dans de nombreux scenarios a forte volumetrie :\n\n"
                "Streaming d'evenements en temps reel : collecte et traitement de\n"
                "clics utilisateurs, evenements IoT, logs applicatifs et metriques\n"
                "systeme. LinkedIn traite plus de 7 trillions de messages par jour\n"
                "via Kafka.\n\n"
                "Pipelines de donnees : Kafka sert de colonne vertebrale pour\n"
                "alimenter des entrepots de donnees, des lacs de donnees (data lakes),\n"
                "et des systemes analytiques en temps reel. Les connecteurs Kafka\n"
                "Connect permettent l'integration avec des dizaines de sources et\n"
                "destinations (bases de donnees, S3, Elasticsearch, etc.).\n\n"
                "Event Sourcing et CQRS : Kafka est ideal pour stocker l'historique\n"
                "complet des evenements d'un systeme, permettant la reconstruction\n"
                "de l'etat a n'importe quel point dans le temps.\n\n"
                "Communication inter-microservices : decouplage asynchrone entre\n"
                "services avec garanties de livraison et possibilite de rejouer\n"
                "les evenements en cas de defaillance d'un service.\n\n"
                "Detection de fraude et monitoring en temps reel : analyse de flux\n"
                "de transactions financieres ou de donnees de securite avec Kafka\n"
                "Streams ou ksqlDB pour detecter des anomalies instantanement."
            ),
            "ecosystem": (
                "L'ecosysteme Kafka est vaste et en constante expansion :\n\n"
                "Kafka Connect : framework d'integration qui permet de connecter\n"
                "Kafka a des systemes externes (bases de donnees, systemes de fichiers,\n"
                "services cloud) via des connecteurs source et sink. Des centaines\n"
                "de connecteurs sont disponibles (Debezium pour le CDC, connecteurs\n"
                "JDBC, S3, Elasticsearch, etc.).\n\n"
                "Kafka Streams : bibliotheque Java/Scala pour le traitement de flux\n"
                "en temps reel directement dans les applications. Elle offre des\n"
                "operations de type map, filter, join, aggregate, et windowing sans\n"
                "necesiter un cluster de traitement separe (contrairement a Spark ou\n"
                "Flink).\n\n"
                "ksqlDB : moteur de traitement de flux accessible via une syntaxe\n"
                "SQL. Permet de creer des requetes continues (materialized views)\n"
                "sur les topics Kafka sans ecrire de code Java.\n\n"
                "Schema Registry : service de gestion des schemas (Avro, Protobuf,\n"
                "JSON Schema) assurant la compatibilite des formats de donnees entre\n"
                "producteurs et consommateurs au fil des evolutions.\n\n"
                "Confluent Platform : distribution commerciale incluant Confluent\n"
                "Control Center (interface d'administration), des connecteurs\n"
                "manages, le support multi-datacenter (Cluster Linking), et\n"
                "Confluent Cloud (Kafka entierement manage).\n\n"
                "Autres outils : Kafdrop et AKHQ (interfaces web), Conduktor\n"
                "(outil de gestion), Strimzi (operateur Kubernetes), MirrorMaker 2\n"
                "(replication inter-clusters)."
            ),
            "companies": [
                "LinkedIn",
                "Netflix",
                "Uber",
                "Airbnb",
                "Spotify",
                "Twitter/X",
                "Goldman Sachs",
                "Adidas"
            ],
            "code_example": (
                "# --- Producteur Kafka (Python avec confluent-kafka) ---\n"
                "from confluent_kafka import Producer\n"
                "import json\n\n"
                "config_producteur = {\n"
                "    'bootstrap.servers': 'localhost:9092',\n"
                "    'acks': 'all',                # Attendre l'acquittement de toutes les replicas ISR\n"
                "    'enable.idempotence': True,    # Garantir l'idempotence (pas de doublons)\n"
                "    'retries': 5,\n"
                "    'linger.ms': 10,               # Regrouper les messages pendant 10ms pour du batching\n"
                "    'compression.type': 'snappy'   # Compresser les lots de messages\n"
                "}\n\n"
                "producteur = Producer(config_producteur)\n\n"
                "def rapport_livraison(err, msg):\n"
                "    if err is not None:\n"
                "        print(f'Echec de livraison : {err}')\n"
                "    else:\n"
                "        print(f'Message livre a {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}')\n\n"
                "# Publier des evenements de commande\n"
                "for i in range(100):\n"
                "    evenement = {\n"
                "        'commande_id': f'CMD-{i:04d}',\n"
                "        'produit': 'Clavier mecanique',\n"
                "        'montant': 89.99,\n"
                "        'statut': 'creee'\n"
                "    }\n"
                "    # La cle determine la partition (meme cle = meme partition = ordre garanti)\n"
                "    producteur.produce(\n"
                "        topic='commandes',\n"
                "        key=evenement['commande_id'],\n"
                "        value=json.dumps(evenement),\n"
                "        callback=rapport_livraison\n"
                "    )\n"
                "    producteur.poll(0)  # Traiter les callbacks en attente\n\n"
                "producteur.flush()  # S'assurer que tous les messages sont envoyes\n\n"
                "# --- Consommateur Kafka ---\n"
                "from confluent_kafka import Consumer\n\n"
                "config_consommateur = {\n"
                "    'bootstrap.servers': 'localhost:9092',\n"
                "    'group.id': 'service-traitement-commandes',\n"
                "    'auto.offset.reset': 'earliest',   # Lire depuis le debut si pas d'offset\n"
                "    'enable.auto.commit': False         # Commit manuel pour at-least-once\n"
                "}\n\n"
                "consommateur = Consumer(config_consommateur)\n"
                "consommateur.subscribe(['commandes'])\n\n"
                "try:\n"
                "    while True:\n"
                "        msg = consommateur.poll(timeout=1.0)\n"
                "        if msg is None:\n"
                "            continue\n"
                "        if msg.error():\n"
                "            print(f'Erreur : {msg.error()}')\n"
                "            continue\n"
                "        evenement = json.loads(msg.value().decode('utf-8'))\n"
                "        print(f'Traitement commande {evenement[\"commande_id\"]} '\n"
                "              f'- Partition {msg.partition()} - Offset {msg.offset()}')\n"
                "        # Traitement metier ici...\n"
                "        consommateur.commit(asynchronous=False)  # Commit apres traitement reussi\n"
                "finally:\n"
                "    consommateur.close()"
            ),
            "performance": {
                "startup_time": "Le demarrage d'un broker Kafka prend quelques secondes a quelques dizaines de secondes selon le nombre de partitions et la taille des logs. Avec KRaft, le temps de demarrage est significativement reduit par rapport a l'ancienne architecture ZooKeeper, car les metadonnees sont chargees localement.",
                "throughput": "Kafka est optimise pour un debit massif. Un seul broker peut gerer des centaines de milliers de messages par seconde. Un cluster bien configure peut atteindre des millions de messages par seconde. L'ecriture sequentielle sur disque, le batching et le zero-copy (sendfile) sont les cles de cette performance.",
                "memory": "Kafka s'appuie fortement sur le page cache du systeme d'exploitation plutot que sur la memoire JVM. Un broker typique fonctionne avec 4-8 Go de heap JVM, mais beneficie de dizaines de Go de page cache pour les lectures recentes. Les producteurs et consommateurs utilisent des buffers configurables pour le batching.",
                "concurrency_model": "Le parallelisme de Kafka repose sur le partitionnement. Chaque partition est un flux ordonne independant, traite par un seul thread consommateur au sein d'un groupe. Le nombre de partitions determine le degre maximum de parallelisme cote consommation. Cote broker, chaque partition est geree par un thread I/O dedie."
            },
            "learning_curve": (
                "La courbe d'apprentissage de Kafka est considerable. Les concepts\n"
                "de base (topics, partitions, offsets, groupes de consommateurs) sont\n"
                "accessibles en quelques jours, mais la maitrise operationnelle demande\n"
                "des semaines voire des mois d'experience. Il faut comprendre le\n"
                "partitionnement et son impact sur l'ordre des messages, le rebalancing\n"
                "des groupes de consommateurs, les strategies de retention, le tuning\n"
                "des parametres de performance (batch.size, linger.ms, acks, etc.),\n"
                "la gestion des replicas ISR, et la planification de la capacite.\n\n"
                "La mise en place d'un cluster de production requiert des competences\n"
                "d'administration systeme et de monitoring. La comprehension des\n"
                "garanties de livraison (at-most-once, at-least-once, exactly-once)\n"
                "et de leurs implications sur l'architecture applicative est\n"
                "essentielle pour eviter les pieges classiques comme la perte de\n"
                "messages ou les doublons. La documentation officielle d'Apache Kafka\n"
                "et les ressources de Confluent sont les meilleures sources\n"
                "d'apprentissage."
            ),
            "community_size": "Kafka possede l'une des communautes les plus actives de l'ecosysteme data. Plus de 27 000 etoiles sur GitHub, des milliers de contributeurs, et des conferences dediees (Kafka Summit, Current). La communaute Confluent, les forums Stack Overflow et les meetups locaux forment un reseau de support dense.",
            "job_market": "La demande pour les competences Kafka est tres elevee, particulierement dans les secteurs de la fintech, du e-commerce et de la data engineering. Kafka est mentionne dans une grande proportion des offres d'emploi data engineer et backend senior. La certification Confluent est un atout reconnu sur le marche."
        },
        "traits": {
            "performance": 9,
            "developer_speed": 4,
            "learning_curve": 7,
            "ecosystem_size": 8,
            "type_safety": 5,
            "concurrency": 9,
            "memory_safety": 7,
            "scalability": 10
        }
    },
    "rabbitmq": {
        "name": "RabbitMQ",
        "category": "messaging",
        "year_created": 2007,
        "creator": "Rabbit Technologies (Pivotal/VMware)",
        "paradigm": ["Message Broker", "AMQP", "Pub/Sub", "Point-a-Point"],
        "typing": "Agnostique (clients multi-langages)",
        "sections": {
            "overview": (
                "RabbitMQ est un message broker open source mature et polyvalent,\n"
                "implementant le protocole AMQP (Advanced Message Queuing Protocol)\n"
                "comme standard principal. Il fait office d'intermediaire intelligent\n"
                "entre les producteurs et les consommateurs de messages, offrant un\n"
                "routage flexible, des garanties de livraison fiables et une grande\n"
                "variete de patterns de messagerie.\n\n"
                "Contrairement a Kafka qui est un log distribue immutable, RabbitMQ\n"
                "est un broker traditionnel ou les messages sont destines a etre\n"
                "consommes puis supprimes de la file d'attente. Ce modele est ideal\n"
                "pour le decouplage de taches asynchrones, la distribution de travail\n"
                "entre workers, et la communication inter-services avec des garanties\n"
                "de livraison au niveau du message individuel.\n\n"
                "Le point fort de RabbitMQ est son systeme de routage extremement\n"
                "flexible base sur les exchanges et les bindings. Un exchange recoit\n"
                "les messages des producteurs et les route vers une ou plusieurs\n"
                "queues selon des regles de routage configurables (direct, topic,\n"
                "fanout, headers). Cette flexibilite permet de modeliser facilement\n"
                "des patterns complexes de messagerie.\n\n"
                "RabbitMQ est ecrit en Erlang/OTP, un langage et une plateforme\n"
                "specialement concus pour les systemes distribues, concurrents et\n"
                "tolerants aux pannes. Cette fondation lui confere une stabilite\n"
                "remarquable et une gestion native du clustering et de la haute\n"
                "disponibilite. Le broker supporte egalement les protocoles STOMP,\n"
                "MQTT et AMQP 1.0 via des plugins, en faisant un choix versatile\n"
                "pour les architectures heterogenes."
            ),
            "history": (
                "RabbitMQ a ete cree en 2007 par Rabbit Technologies Ltd, une\n"
                "startup fondee par Alexis Richardson et Matthias Radestock a\n"
                "Londres. L'objectif initial etait de creer une implementation\n"
                "open source robuste du protocole AMQP, qui venait d'etre\n"
                "standardise par un consortium incluant JPMorgan Chase, Red Hat\n"
                "et d'autres acteurs majeurs de l'industrie financiere.\n\n"
                "Le choix d'Erlang/OTP comme langage d'implementation etait\n"
                "delibere et strategique. Erlang avait ete concu par Ericsson dans\n"
                "les annees 1980 pour les systemes de telecomunications, avec des\n"
                "proprietes essentielles pour un message broker : concurrence massive\n"
                "par processus legers, tolerance aux pannes, remplacement de code\n"
                "a chaud, et distribution native.\n\n"
                "En 2010, Rabbit Technologies a ete acquise par SpringSource, une\n"
                "division de VMware. RabbitMQ est alors devenu partie integrante de\n"
                "l'ecosysteme Spring, ce qui a considerablement accelere son adoption\n"
                "dans le monde Java/enterprise. L'integration avec Spring AMQP et\n"
                "Spring Cloud Stream a facilite son utilisation dans les architectures\n"
                "microservices.\n\n"
                "En 2013, Pivotal Software a ete cree comme spin-off de VMware et\n"
                "EMC, reprenant RabbitMQ sous son aile. Pivotal a continue le\n"
                "developpement et a lance des offres commerciales (Pivotal RabbitMQ).\n"
                "En 2019, VMware a racquise Pivotal, et RabbitMQ est revenu dans le\n"
                "giron de VMware/Broadcom.\n\n"
                "Les versions recentes ont apporte des evolutions majeures :\n"
                "RabbitMQ 3.8 (2019) a introduit les quorum queues pour une\n"
                "replication plus fiable basee sur l'algorithme Raft. RabbitMQ 3.9\n"
                "(2021) a ajoute les streams, un nouveau type de queue persistent\n"
                "et rejouable inspire par le modele de Kafka. RabbitMQ 3.13 et 4.x\n"
                "(2024-2025) continuent de moderniser le broker avec des ameliorations\n"
                "de performance et de nouvelles fonctionnalites de clustering."
            ),
            "architecture": (
                "L'architecture de RabbitMQ est centree sur le modele AMQP avec\n"
                "des extensions qui en font un broker extremement flexible :\n\n"
                "Exchanges : Ce sont les points d'entree des messages. Le producteur\n"
                "publie un message a un exchange, jamais directement a une queue.\n"
                "Il existe quatre types d'exchanges : direct (routage par cle exacte),\n"
                "topic (routage par pattern avec wildcards * et #), fanout (diffusion\n"
                "a toutes les queues liees), et headers (routage par attributs d'en-tete).\n\n"
                "Queues : Les queues stockent les messages en attente de traitement.\n"
                "Elles sont liees aux exchanges par des bindings qui definissent les\n"
                "regles de routage. Plusieurs types de queues coexistent : classic\n"
                "queues (stockage en memoire avec optionnel flush disque), quorum\n"
                "queues (repliquees via le protocole Raft pour la haute disponibilite),\n"
                "et streams (log append-only persistent et rejouable).\n\n"
                "Bindings et Routing Keys : Les bindings lient les exchanges aux\n"
                "queues avec des criteres de routage. La routing key est un attribut\n"
                "du message utilise par les exchanges direct et topic pour determiner\n"
                "la queue de destination. Ce systeme permet un decouplage total entre\n"
                "la logique de publication et la logique de consommation.\n\n"
                "Acquittements et garanties : RabbitMQ supporte les acquittements\n"
                "manuels (consumer acknowledgements) qui permettent au consommateur\n"
                "de confirmer le traitement reussi d'un message. Si le consommateur\n"
                "echoue sans acquitter, le message est remis en queue (redelivery).\n"
                "Cote producteur, les publisher confirms permettent de s'assurer que\n"
                "le broker a bien recu et persiste le message. La combinaison des\n"
                "deux mecanismes offre une garantie at-least-once fiable.\n\n"
                "Clustering et haute disponibilite : Un cluster RabbitMQ partage\n"
                "les metadonnees (definitions d'exchanges, queues, bindings) entre\n"
                "tous les noeuds. Les quorum queues repliquent automatiquement les\n"
                "messages sur une majorite de noeuds via le protocole Raft, assurant\n"
                "la tolerance aux pannes. Le Federation plugin et le Shovel plugin\n"
                "permettent la communication entre clusters distants.\n\n"
                "Modele Erlang : Chaque connexion, canal et queue est gere par un\n"
                "processus Erlang leger (quelques Ko de memoire). Des milliers de\n"
                "ces processus s'executent en parallele, supervises par des arbres\n"
                "de supervision OTP qui redemarrent automatiquement les processus\n"
                "defaillants."
            ),
            "pros_cons": {
                "pros": [
                    "Routage extremement flexible avec les exchanges (direct, topic, fanout, headers)",
                    "Protocole AMQP standardise garantissant l'interoperabilite entre langages et plateformes",
                    "Acquittements fins au niveau du message individuel (consumer acks, publisher confirms)",
                    "Interface de gestion web integree avec monitoring, configuration et diagnostic",
                    "Support multi-protocoles via plugins : AMQP 0.9.1, AMQP 1.0, STOMP, MQTT",
                    "Quorum queues offrant une haute disponibilite robuste basee sur le consensus Raft",
                    "Ecosysteme de plugins riche : federation, shovel, delayed messages, priorites de queues",
                    "Stabilite eprouvee en production grace a la plateforme Erlang/OTP"
                ],
                "cons": [
                    "Debit inferieur a Kafka pour les charges a tres forte volumetrie (optimise pour la fiabilite du message individuel)",
                    "La memoire peut exploser si les consommateurs ne suivent pas le rythme des producteurs (backpressure limitee)",
                    "L'administration d'un cluster en production requiert une comprehension d'Erlang/OTP et de ses outils",
                    "Les classic mirrored queues (deprecees) pouvaient perdre des messages lors du failover",
                    "Pas de rejouabilite native des messages consommes (sauf avec les streams recents)",
                    "Les performances se degradent significativement quand les queues deviennent tres profondes (millions de messages en attente)",
                    "Le partitionnement reseau (split-brain) peut etre problematique sans une configuration adaptee"
                ]
            },
            "use_cases": (
                "RabbitMQ excelle dans les scenarios de messagerie traditionnelle :\n\n"
                "Traitement de taches asynchrones : delegation de taches longues\n"
                "(envoi d'emails, generation de rapports, traitement d'images) a\n"
                "des workers en arriere-plan. Le pattern Work Queue distribue la\n"
                "charge equitablement entre les workers avec acquittement.\n\n"
                "Communication inter-microservices : decouplage des services via\n"
                "des messages asynchrones avec routage intelligent. Les exchanges\n"
                "topic permettent un routage pub/sub granulaire (ex: commande.creee,\n"
                "commande.payee, commande.expediee).\n\n"
                "Integration de systemes heterogenes : grace au support multi-\n"
                "protocoles (AMQP, STOMP, MQTT), RabbitMQ peut servir de pont\n"
                "entre des systemes Java, Python, .NET, IoT et web en temps reel.\n\n"
                "RPC asynchrone : le pattern Request-Reply de RabbitMQ permet\n"
                "d'implementer des appels de procedure a distance asynchrones avec\n"
                "des queues de reponse temporaires.\n\n"
                "IoT et telemetrie : le plugin MQTT fait de RabbitMQ un broker\n"
                "viable pour les dispositifs IoT qui publient des donnees de\n"
                "capteurs. La flexibilite du routage permet de dispatcher les\n"
                "donnees vers differents systemes de traitement."
            ),
            "ecosystem": (
                "L'ecosysteme RabbitMQ est mature et bien integre au monde enterprise :\n\n"
                "Bibliotheques clientes officielles et communautaires : amqplib et\n"
                "pika (Python), amqp.node et amqplib (Node.js), Bunny (Ruby),\n"
                "RabbitMQ Java Client et Spring AMQP (Java), amqp (Go). Chaque\n"
                "langage majeur dispose d'au moins un client bien maintenu.\n\n"
                "Spring Integration : Spring AMQP et Spring Cloud Stream offrent\n"
                "une integration de premier ordre avec l'ecosysteme Spring Boot.\n"
                "Les annotations @RabbitListener et @RabbitHandler simplifient\n"
                "considerablement le code de consommation.\n\n"
                "Management Plugin : interface web integree permettant de visualiser\n"
                "les queues, exchanges, bindings, connexions et canaux en temps reel.\n"
                "Elle offre aussi une API REST complete pour l'automatisation.\n\n"
                "Plugins notables : rabbitmq-delayed-message-exchange (messages\n"
                "differes), rabbitmq-federation (communication inter-clusters),\n"
                "rabbitmq-shovel (transfert de messages entre brokers),\n"
                "rabbitmq-mqtt (support MQTT pour l'IoT).\n\n"
                "Operateurs Kubernetes : le RabbitMQ Cluster Operator et le\n"
                "Messaging Topology Operator facilitent le deploiement et la\n"
                "gestion de clusters RabbitMQ sur Kubernetes.\n\n"
                "Services manages : CloudAMQP (specialiste RabbitMQ), Amazon MQ,\n"
                "Azure Service Bus (compatible AMQP), VMware Tanzu RabbitMQ."
            ),
            "companies": [
                "Bloomberg",
                "Reddit",
                "Zalando",
                "Mozilla",
                "Trivago",
                "WeTransfer",
                "Runtastic/Adidas",
                "Instagram (historiquement)"
            ],
            "code_example": (
                "# --- Producteur RabbitMQ (Python avec pika) ---\n"
                "import pika\n"
                "import json\n\n"
                "# Connexion au broker\n"
                "connexion = pika.BlockingConnection(\n"
                "    pika.ConnectionParameters(\n"
                "        host='localhost',\n"
                "        credentials=pika.PlainCredentials('guest', 'guest')\n"
                "    )\n"
                ")\n"
                "canal = connexion.channel()\n\n"
                "# Declaration de l'exchange de type 'topic' pour un routage flexible\n"
                "canal.exchange_declare(\n"
                "    exchange='evenements_commandes',\n"
                "    exchange_type='topic',\n"
                "    durable=True     # Survit au redemarrage du broker\n"
                ")\n\n"
                "# Declaration d'une queue durable avec dead-letter exchange\n"
                "canal.queue_declare(\n"
                "    queue='traitement_commandes',\n"
                "    durable=True,\n"
                "    arguments={\n"
                "        'x-dead-letter-exchange': 'dlx_commandes',  # Messages echoues\n"
                "        'x-message-ttl': 86400000                    # TTL de 24h\n"
                "    }\n"
                ")\n\n"
                "# Binding : la queue recoit les messages dont la cle correspond au pattern\n"
                "canal.queue_bind(\n"
                "    exchange='evenements_commandes',\n"
                "    queue='traitement_commandes',\n"
                "    routing_key='commande.*'    # commande.creee, commande.payee, etc.\n"
                ")\n\n"
                "# Publication d'un message persistant\n"
                "message = {'commande_id': 'CMD-0042', 'produit': 'Ecran 4K', 'montant': 449.99}\n"
                "canal.basic_publish(\n"
                "    exchange='evenements_commandes',\n"
                "    routing_key='commande.creee',\n"
                "    body=json.dumps(message),\n"
                "    properties=pika.BasicProperties(\n"
                "        delivery_mode=2,          # Message persistant sur disque\n"
                "        content_type='application/json'\n"
                "    )\n"
                ")\n"
                "print(f'Message publie : {message}')\n"
                "connexion.close()\n\n"
                "# --- Consommateur RabbitMQ avec acquittement manuel ---\n"
                "import pika\n"
                "import json\n\n"
                "connexion = pika.BlockingConnection(\n"
                "    pika.ConnectionParameters(host='localhost')\n"
                ")\n"
                "canal = connexion.channel()\n\n"
                "def traiter_commande(canal, methode, proprietes, corps):\n"
                "    evenement = json.loads(corps)\n"
                "    print(f'Traitement : {evenement[\"commande_id\"]} - {methode.routing_key}')\n"
                "    try:\n"
                "        # Logique metier ici...\n"
                "        canal.basic_ack(delivery_tag=methode.delivery_tag)  # Acquittement OK\n"
                "    except Exception as e:\n"
                "        # Rejeter et renvoyer en queue (ou vers dead-letter)\n"
                "        canal.basic_nack(delivery_tag=methode.delivery_tag, requeue=False)\n\n"
                "# Prefetch : traiter un seul message a la fois par worker\n"
                "canal.basic_qos(prefetch_count=1)\n"
                "canal.basic_consume(queue='traitement_commandes', on_message_callback=traiter_commande)\n\n"
                "print('En attente de messages...')\n"
                "canal.start_consuming()"
            ),
            "performance": {
                "startup_time": "RabbitMQ demarre en quelques secondes grace a la machine virtuelle Erlang BEAM. Le temps de demarrage augmente legerement avec le nombre de queues et de bindings a charger. Le hot code reloading d'Erlang permet des mises a jour sans interruption complete.",
                "throughput": "RabbitMQ peut gerer des dizaines de milliers de messages par seconde sur un seul noeud. Les quorum queues offrent un debit legerement inferieur aux classic queues mais avec des garanties de durabilite superieures. Les performances dependent fortement de la taille des messages, de la persistance et du nombre de consommateurs.",
                "memory": "La consommation memoire depend du nombre de messages en attente dans les queues. RabbitMQ peut paginer les messages sur disque (page-out) quand la memoire atteint un seuil configurable (vm_memory_high_watermark). Les processus Erlang legers consomment peu de memoire unitairement mais peuvent s'accumuler.",
                "concurrency_model": "RabbitMQ herite du modele de concurrence d'Erlang : des millions de processus legers s'executent en parallele sur les coeurs disponibles, supervises par des arbres OTP. Chaque queue, connexion et canal est un processus independant. Le prefetch_count controle le parallelisme cote consommateur."
            },
            "learning_curve": (
                "La courbe d'apprentissage de RabbitMQ est moderee et progressive.\n"
                "Les concepts de base (queues, exchanges, bindings, routing keys)\n"
                "sont intuitifs et bien documentes, permettant de demarrer rapidement\n"
                "avec des patterns simples comme la work queue ou le pub/sub.\n\n"
                "L'interface de gestion web est un atout majeur pour l'apprentissage :\n"
                "elle permet de visualiser les flux de messages, de creer des exchanges\n"
                "et des queues, et de publier des messages de test sans ecrire de code.\n\n"
                "La complexite augmente avec les besoins : comprendre les nuances\n"
                "entre les types de queues (classic, quorum, stream), configurer\n"
                "correctement la persistance et les acquittements, gerer le clustering\n"
                "et le partitionnement reseau, et mettre en place des dead-letter\n"
                "exchanges pour la gestion des erreurs. La maitrise du tuning de\n"
                "performance et de la planification de capacite demande de l'experience.\n\n"
                "Le protocole AMQP est un standard bien documente, et les nombreux\n"
                "tutoriels officiels de RabbitMQ (les 'RabbitMQ Tutorials') sont\n"
                "excellents pour decouvrir les patterns de messagerie pas a pas."
            ),
            "community_size": "RabbitMQ a une communaute etablie et stable. Plus de 12 000 etoiles sur GitHub, une documentation officielle detaillee, des meetups et des conferences (RabbitMQ Summit). Le support commercial de VMware/Broadcom et les services manages comme CloudAMQP ajoutent une couche de support professionnel.",
            "job_market": "RabbitMQ est largement demande dans les offres d'emploi backend et devops, particulierement dans les environnements enterprise et les architectures microservices. Sa popularite est stable et son integration avec l'ecosysteme Spring/Java en fait un incontournable dans de nombreuses entreprises."
        },
        "traits": {
            "performance": 7,
            "developer_speed": 7,
            "learning_curve": 5,
            "ecosystem_size": 7,
            "type_safety": 5,
            "concurrency": 8,
            "memory_safety": 7,
            "scalability": 7
        }
    },
    "nats": {
        "name": "NATS",
        "category": "messaging",
        "year_created": 2010,
        "creator": "Derek Collison (Synadia)",
        "paradigm": ["Pub/Sub", "Request-Reply", "Queue Groups"],
        "typing": "Agnostique (clients multi-langages)",
        "sections": {
            "overview": (
                "NATS est un systeme de messagerie cloud-native ultra-performant,\n"
                "concu pour la simplicite, la securite et la haute performance.\n"
                "Son architecture minimaliste et son protocole texte leger en font\n"
                "l'un des systemes de messagerie les plus rapides disponibles,\n"
                "capable de gerer des millions de messages par seconde avec une\n"
                "latence de l'ordre de la microseconde.\n\n"
                "NATS se distingue des autres brokers par sa philosophie 'at most\n"
                "once' par defaut (core NATS) : les messages sont livres aux\n"
                "abonnes connectes au moment de la publication, sans persistance\n"
                "ni acquittement. Ce modele 'fire and forget' est ideal pour les\n"
                "scenarios ou la vitesse prime sur la garantie de livraison, comme\n"
                "la telemetrie, le monitoring et la decouverte de services.\n\n"
                "Pour les cas d'usage necessitant des garanties plus fortes, NATS\n"
                "JetStream (integre depuis NATS 2.2) ajoute une couche de persistance\n"
                "avec streaming, replay, exactement-une-fois et stockage distribue.\n"
                "JetStream transforme NATS en un systeme complet capable de rivaliser\n"
                "avec Kafka pour le streaming d'evenements tout en conservant la\n"
                "simplicite operationnelle qui fait la reputation de NATS.\n\n"
                "NATS est ecrit en Go, ce qui lui confere un binaire unique sans\n"
                "dependances, un deploiement trivial, et une empreinte memoire\n"
                "extremement reduite (quelques Mo de RAM). Un serveur NATS peut\n"
                "tourner sur un Raspberry Pi comme sur un cluster Kubernetes\n"
                "mondial, avec la meme simplicite de configuration.\n\n"
                "La philosophie de NATS est celle de la 'connectivite adaptative' :\n"
                "le systeme s'adapte automatiquement aux conditions du reseau et\n"
                "aux pannes, avec reconnexion automatique des clients, decouverte\n"
                "dynamique des serveurs, et routage intelligent des messages a\n"
                "travers les clusters et les super-clusters."
            ),
            "history": (
                "NATS a ete cree en 2010 par Derek Collison, un veteran de\n"
                "l'industrie des systemes de messagerie avec plus de 30 ans\n"
                "d'experience. Avant NATS, Collison avait travaille chez TIBCO\n"
                "(systemes de messagerie enterprise) et chez Google sur les\n"
                "systemes distribues internes.\n\n"
                "La premiere version de NATS (alors appelee 'gnatsd') a ete ecrite\n"
                "en Ruby pour le projet Cloud Foundry, la plateforme PaaS de VMware.\n"
                "NATS servait de systeme nerveux interne pour la communication entre\n"
                "les composants de Cloud Foundry. Face aux limitations de performance\n"
                "de l'implementation Ruby, Collison a reecrit NATS en Go en 2012,\n"
                "obtenant des gains de performance spectaculaires.\n\n"
                "En 2014, Derek Collison a fonde Apcera, une entreprise de\n"
                "plateforme cloud qui utilisait NATS comme couche de communication.\n"
                "NATS a ete open-source des le debut sous licence Apache 2.0.\n\n"
                "En 2018, NATS a rejoint la Cloud Native Computing Foundation\n"
                "(CNCF) comme projet incubateur, marquant sa reconnaissance comme\n"
                "technologie cloud-native de reference. La meme annee, Derek\n"
                "Collison a fonde Synadia Communications, dediee au developpement\n"
                "et a la commercialisation de NATS.\n\n"
                "NATS 2.0 (2019) a introduit un systeme de securite avance base\n"
                "sur des comptes et des utilisateurs avec authentification par\n"
                "JWT et NKeys (cles Ed25519). NATS 2.2 (2021) a ete une version\n"
                "majeure avec l'introduction de JetStream, le sous-systeme de\n"
                "persistance et de streaming integre, remplacant l'ancien NATS\n"
                "Streaming Server (STAN) qui etait un composant separe.\n\n"
                "En 2022, NATS est devenu un projet 'graduated' de la CNCF,\n"
                "rejoignant les rangs de Kubernetes, Prometheus et Envoy. Cette\n"
                "graduation temoigne de la maturite et de l'adoption croissante\n"
                "de NATS dans l'ecosysteme cloud-native."
            ),
            "architecture": (
                "L'architecture de NATS est deliberement minimaliste, privilegiant\n"
                "la simplicite et la performance a chaque niveau de conception :\n\n"
                "Protocole : NATS utilise un protocole texte simple base sur TCP.\n"
                "Les commandes sont des lignes de texte (PUB, SUB, MSG, CONNECT,\n"
                "PING/PONG) facilement lisibles et debuggables. Cette simplicite\n"
                "permet d'ecrire un client NATS en quelques centaines de lignes\n"
                "de code dans n'importe quel langage.\n\n"
                "Subjects : Les messages sont publies sur des sujets (subjects)\n"
                "hierarchiques separes par des points (ex: commandes.france.creee).\n"
                "Les abonnes peuvent utiliser des wildcards : '*' pour un token\n"
                "(commandes.*.creee) et '>' pour tous les tokens restants\n"
                "(commandes.france.>). Ce systeme permet un routage pub/sub\n"
                "extremement expressif sans configuration prealable.\n\n"
                "Queue Groups : Pour la distribution de charge, NATS offre les\n"
                "queue groups. Plusieurs consommateurs s'abonnent au meme sujet\n"
                "avec un nom de groupe partage. NATS distribue automatiquement\n"
                "chaque message a un seul membre du groupe (load balancing natif),\n"
                "sans configuration de queues ou de bindings.\n\n"
                "Request-Reply : NATS supporte nativement le pattern requete-reponse.\n"
                "Le client publie un message avec un sujet de reponse automatique\n"
                "(inbox) et attend la reponse. Ce mecanisme est la base pour\n"
                "construire des appels RPC legers entre microservices.\n\n"
                "Clustering : Les serveurs NATS forment des clusters en se\n"
                "connectant entre eux via des routes TCP. Les messages et les\n"
                "abonnements sont propages automatiquement a travers le cluster.\n"
                "NATS utilise un modele de routage par interet : un message n'est\n"
                "transmis a un serveur que si celui-ci a des abonnes interesses.\n\n"
                "Super-clusters et Leaf Nodes : Les gateways connectent des\n"
                "clusters NATS distants en super-clusters pour une couverture\n"
                "mondiale. Les leaf nodes permettent a des serveurs NATS locaux\n"
                "de se connecter a un cluster central, ideal pour l'edge computing\n"
                "et les architectures hub-and-spoke.\n\n"
                "JetStream (persistance) : JetStream ajoute la persistance a NATS\n"
                "via des streams (logs durables) et des consumers (abonnements\n"
                "durables avec suivi de position). Les streams sont repliques sur\n"
                "plusieurs serveurs via le protocole Raft. JetStream supporte les\n"
                "garanties at-least-once et exactly-once, le replay depuis n'importe\n"
                "quel point, le stockage par sujet ou par flux, et la deduplication\n"
                "des messages. Contrairement a Kafka, la persistance est une option\n"
                "ajoutee sur le meme systeme, pas un prerequis architectural."
            ),
            "pros_cons": {
                "pros": [
                    "Performance exceptionnelle : latence sub-milliseconde et millions de messages par seconde",
                    "Simplicite operationnelle : un seul binaire Go sans dependance, configuration minimale",
                    "Empreinte memoire minuscule : quelques Mo suffisent pour un serveur fonctionnel",
                    "JetStream offre persistance, streaming et exactly-once dans le meme systeme",
                    "Securite avancee integree avec comptes, utilisateurs, JWT et NKeys (Ed25519)",
                    "Topologie flexible : clustering, super-clusters et leaf nodes pour l'edge computing",
                    "Queue groups pour le load balancing natif sans configuration complexe",
                    "Protocole texte simple facilitant le debugging et l'ecriture de clients"
                ],
                "cons": [
                    "Ecosysteme plus restreint que Kafka ou RabbitMQ : moins d'outils et de connecteurs tiers",
                    "JetStream est relativement recent et moins eprouve en production que Kafka pour le streaming massif",
                    "Core NATS est at-most-once par defaut, ce qui peut surprendre les developpeurs habitues aux garanties at-least-once",
                    "Moins de ressources d'apprentissage et de tutoriels disponibles en francais",
                    "Le monitoring et l'observabilite necessitent des outils externes (pas d'interface web integree par defaut)",
                    "Le routage par interet dans les super-clusters peut generer du trafic de controle significatif avec de tres nombreux sujets"
                ]
            },
            "use_cases": (
                "NATS excelle dans les architectures cloud-native et les scenarios\n"
                "exigeant faible latence et simplicite :\n\n"
                "Communication inter-microservices : NATS est ideal comme couche\n"
                "de transport entre microservices, offrant pub/sub, request-reply\n"
                "et load balancing natif. Sa simplicite eliminite la complexite\n"
                "operationnelle des brokers traditionnels.\n\n"
                "IoT et edge computing : l'empreinte memoire minimale de NATS\n"
                "permet son deploiement sur des dispositifs contraints. Les leaf\n"
                "nodes connectent les capteurs et les passerelles edge au cloud\n"
                "central de maniere transparente.\n\n"
                "Telemetrie et monitoring en temps reel : le modele at-most-once\n"
                "de core NATS est parfait pour les metriques et les logs ou la\n"
                "perte occasionnelle d'un message est acceptable face au gain\n"
                "de performance.\n\n"
                "Service mesh et decouverte de services : NATS peut servir de\n"
                "couche de decouverte et de communication dans un service mesh,\n"
                "avec son routage par sujets et ses queue groups.\n\n"
                "Systemes de commande et controle : les patterns request-reply\n"
                "et pub/sub de NATS sont adaptes aux systemes de commande\n"
                "distribues (robotique, drones, vehicules autonomes) ou la\n"
                "latence minimale est critique.\n\n"
                "Streaming d'evenements avec JetStream : pour les cas necessitant\n"
                "persistance et replay, JetStream permet de construire des\n"
                "architectures event-driven completes avec un systeme unique."
            ),
            "ecosystem": (
                "L'ecosysteme NATS est centre sur la simplicite et le cloud-native :\n\n"
                "Clients officiels : NATS propose des clients officiels maintenus\n"
                "par Synadia pour Go, Rust, Python, Java, .NET, Node.js, C, Elixir,\n"
                "Deno et WebSocket. Chaque client supporte core NATS et JetStream.\n"
                "Les clients Go et Rust sont les plus performants.\n\n"
                "NATS CLI (nats) : outil en ligne de commande puissant pour\n"
                "publier, s'abonner, gerer les streams et consumers JetStream,\n"
                "surveiller le serveur et administrer les comptes. C'est l'outil\n"
                "principal d'interaction avec NATS.\n\n"
                "nsc (NATS Security Credentials) : outil pour gerer les comptes,\n"
                "les utilisateurs et les permissions via des tokens JWT. Permet\n"
                "une gestion decentralisee de la securite sans redemarrer les\n"
                "serveurs.\n\n"
                "NATS Surveyor : outil de monitoring qui expose des metriques\n"
                "Prometheus pour le suivi de la sante du cluster, des connexions,\n"
                "des messages et de JetStream.\n\n"
                "nats-top : outil de monitoring en temps reel pour le terminal,\n"
                "affichant les connexions actives, le debit et les abonnements.\n\n"
                "Integration Kubernetes : le NATS Helm chart et l'operateur\n"
                "nack permettent un deploiement simplifie sur Kubernetes avec\n"
                "auto-scaling et configuration declarative.\n\n"
                "Synadia Cloud : service NATS entierement manage par Synadia,\n"
                "le createur de NATS, offrant des clusters mondiaux avec\n"
                "super-clusters geographiquement distribues."
            ),
            "companies": [
                "Synadia",
                "Mastercard",
                "Netlify",
                "Ericsson",
                "Huawei",
                "Clarifai",
                "Choria (infrastructure automation)",
                "Platform9"
            ],
            "code_example": (
                "# --- Pub/Sub simple avec NATS (Python avec nats-py) ---\n"
                "import asyncio\n"
                "import nats\n"
                "import json\n\n"
                "async def exemple_pubsub():\n"
                "    # Connexion au serveur NATS\n"
                "    nc = await nats.connect('nats://localhost:4222')\n\n"
                "    # --- Abonnement avec wildcard ---\n"
                "    async def gestionnaire_commandes(msg):\n"
                "        sujet = msg.subject\n"
                "        donnees = json.loads(msg.data.decode())\n"
                "        print(f'Recu sur [{sujet}]: {donnees}')\n\n"
                "    # S'abonner a tous les evenements de commandes\n"
                "    await nc.subscribe('commandes.*', cb=gestionnaire_commandes)\n\n"
                "    # --- Queue Group pour load balancing ---\n"
                "    async def worker_traitement(msg):\n"
                "        donnees = json.loads(msg.data.decode())\n"
                "        print(f'Worker traite : {donnees[\"commande_id\"]}')\n\n"
                "    # 3 workers se partagent la charge automatiquement\n"
                "    for i in range(3):\n"
                "        await nc.subscribe(\n"
                "            'taches.traitement',\n"
                "            queue='workers',       # Nom du queue group\n"
                "            cb=worker_traitement\n"
                "        )\n\n"
                "    # --- Publication de messages ---\n"
                "    for i in range(10):\n"
                "        evenement = {'commande_id': f'CMD-{i:04d}', 'montant': 99.99}\n"
                "        await nc.publish(\n"
                "            f'commandes.creee',\n"
                "            json.dumps(evenement).encode()\n"
                "        )\n\n"
                "    # --- Request-Reply (RPC leger) ---\n"
                "    async def service_prix(msg):\n"
                "        requete = json.loads(msg.data.decode())\n"
                "        reponse = {'produit': requete['produit'], 'prix': 49.99}\n"
                "        await nc.publish(msg.reply, json.dumps(reponse).encode())\n\n"
                "    await nc.subscribe('services.prix', cb=service_prix)\n\n"
                "    # Appel RPC : envoyer une requete et attendre la reponse\n"
                "    reponse = await nc.request(\n"
                "        'services.prix',\n"
                "        json.dumps({'produit': 'Souris ergonomique'}).encode(),\n"
                "        timeout=2.0\n"
                "    )\n"
                "    print(f'Prix recu : {json.loads(reponse.data.decode())}')\n\n"
                "    await nc.drain()\n\n"
                "# --- JetStream : persistance et streaming ---\n"
                "async def exemple_jetstream():\n"
                "    nc = await nats.connect('nats://localhost:4222')\n"
                "    js = nc.jetstream()\n\n"
                "    # Creer un stream persistent\n"
                "    await js.add_stream(\n"
                "        name='COMMANDES',\n"
                "        subjects=['commandes.>'],   # Capturer tous les sujets commandes.*\n"
                "        retention='limits',           # Retention par taille/duree\n"
                "        max_msgs=100000,\n"
                "        storage='file'                # Persistance sur disque\n"
                "    )\n\n"
                "    # Publier avec acquittement (at-least-once)\n"
                "    ack = await js.publish(\n"
                "        'commandes.creee',\n"
                "        json.dumps({'commande_id': 'CMD-0001', 'montant': 129.99}).encode()\n"
                "    )\n"
                "    print(f'Message persiste : stream={ack.stream}, seq={ack.seq}')\n\n"
                "    # Consommateur durable (reprend ou il s'etait arrete)\n"
                "    sous = await js.pull_subscribe(\n"
                "        'commandes.>',\n"
                "        durable='processeur-commandes'\n"
                "    )\n"
                "    messages = await sous.fetch(batch=10, timeout=5)\n"
                "    for msg in messages:\n"
                "        print(f'JetStream : {json.loads(msg.data.decode())}')\n"
                "        await msg.ack()   # Acquittement explicite\n\n"
                "    await nc.drain()\n\n"
                "asyncio.run(exemple_pubsub())\n"
                "asyncio.run(exemple_jetstream())"
            ),
            "performance": {
                "startup_time": "NATS demarre quasi instantanement (quelques dizaines de millisecondes). Le binaire Go unique se lance sans aucune dependance externe. Meme avec JetStream active et des streams a charger, le demarrage reste de l'ordre de la seconde. C'est l'un des systemes de messagerie les plus rapides a demarrer.",
                "throughput": "Core NATS peut gerer plus de 10 millions de messages par seconde sur un seul serveur pour de petits messages. La latence est de l'ordre de quelques microsecondes. JetStream reduit le debit en raison de la persistance et de la replication, mais reste capable de millions de messages par seconde sur un cluster bien configure.",
                "memory": "L'empreinte memoire de NATS est remarquablement faible : un serveur NATS idle consomme environ 10-20 Mo de RAM. En charge moderee, la consommation reste de l'ordre de quelques centaines de Mo. JetStream utilise de la memoire supplementaire pour le cache des streams, mais reste bien plus leger que Kafka ou RabbitMQ.",
                "concurrency_model": "NATS exploite le modele de concurrence de Go : des goroutines legeres gerent les connexions clients et le routage des messages de maniere asynchrone. Le serveur utilise un event loop optimise avec multiplexage I/O. Les clients utilisent egalement des patterns asynchrones (async/await en Python, goroutines en Go) pour le traitement concurrent des messages."
            },
            "learning_curve": (
                "La courbe d'apprentissage de NATS est l'une des plus douces\n"
                "parmi les systemes de messagerie. Le protocole est simple, les\n"
                "concepts fondamentaux (subjects, publish, subscribe, queue groups,\n"
                "request-reply) sont intuitifs et maitrisables en quelques heures.\n"
                "Un developpeur peut etre productif avec core NATS en une journee.\n\n"
                "La simplicite du deploiement contribue a l'accessibilite : un seul\n"
                "binaire a telecharger, pas de dependance (pas de ZooKeeper, pas de\n"
                "JVM), et une configuration par defaut qui fonctionne immediatement.\n"
                "La CLI nats est un excellent outil d'exploration et d'apprentissage.\n\n"
                "JetStream ajoute une couche de complexite significative : comprendre\n"
                "les streams, les consumers (push vs pull), les politiques de retention,\n"
                "la replication et les garanties de livraison demande plus de temps.\n"
                "Cependant, cette complexite reste inferieure a celle de Kafka car\n"
                "JetStream est une extension optionnelle du meme systeme, pas un\n"
                "paradigme architectural different.\n\n"
                "La documentation officielle (docs.nats.io) est claire et bien\n"
                "structuree, avec des exemples concrets dans plusieurs langages.\n"
                "Les 'NATS by Example' fournissent des snippets prets a l'emploi\n"
                "pour chaque pattern de messagerie."
            ),
            "community_size": "NATS a une communaute en forte croissance depuis sa graduation a la CNCF. Plus de 16 000 etoiles sur GitHub, un Slack communautaire actif avec des milliers de membres, et des presentations regulieres dans les conferences cloud-native (KubeCon, CNCF events). La communaute est plus petite que celle de Kafka ou RabbitMQ mais tres engagee.",
            "job_market": "La demande pour NATS est en croissance, particulierement dans les environnements cloud-native et Kubernetes. Les offres mentionnant NATS sont moins nombreuses que celles citant Kafka ou RabbitMQ, mais la tendance est a la hausse. La maitrise de NATS est un atout differenciateur dans les equipes adoptant des architectures microservices modernes."
        },
        "traits": {
            "performance": 10,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 5,
            "type_safety": 4,
            "concurrency": 9,
            "memory_safety": 7,
            "scalability": 9
        }
    }
}
