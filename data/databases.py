"""
Donnees sur les systemes de gestion de bases de donnees.
Chaque entree documente une base de donnees avec son histoire, son architecture,
ses cas d'usage et ses caracteristiques techniques.
"""

TECHNOLOGIES = {
    "postgresql": {
        "name": "PostgreSQL",
        "category": "database",
        "year_created": 1996,
        "creator": "UC Berkeley",
        "paradigm": ["relationnel", "objet-relationnel", "extensible", "ACID"],
        "typing": "statique (schema strict avec types riches)",
        "sections": {
            "overview": (
                "PostgreSQL est un systeme de gestion de base de donnees\n"
                "objet-relationnel (ORDBMS) open source, souvent considere comme\n"
                "la base de donnees open source la plus avancee au monde. Il combine\n"
                "la fiabilite et la conformite aux standards SQL d'une base relationnelle\n"
                "traditionnelle avec des fonctionnalites avancees comme les types\n"
                "personnalises, l'heritage de tables, et le support natif de JSON/JSONB.\n\n"
                "PostgreSQL se distingue par son extensibilite remarquable. Les\n"
                "developpeurs peuvent definir leurs propres types de donnees, fonctions,\n"
                "operateurs, fonctions d'agregation et meme des methodes d'indexation.\n"
                "Cette extensibilite a permis la creation d'extensions puissantes comme\n"
                "PostGIS (donnees geospatiales), TimescaleDB (series temporelles),\n"
                "et pgvector (recherche vectorielle pour l'IA).\n\n"
                "Le systeme de concurrence de PostgreSQL est base sur MVCC\n"
                "(Multi-Version Concurrency Control), permettant a plusieurs\n"
                "transactions de s'executer simultanement sans blocage, chaque\n"
                "transaction voyant un snapshot coherent des donnees.\n\n"
                "PostgreSQL offre des garanties ACID completes, un systeme de\n"
                "replication robuste (streaming replication, replication logique),\n"
                "des index avances (B-tree, Hash, GiST, SP-GiST, GIN, BRIN),\n"
                "le partitionnement de tables, la recherche plein texte native,\n"
                "et un optimiseur de requetes extremement sophistique.\n\n"
                "Depuis les versions recentes, PostgreSQL supporte le parallelisme\n"
                "des requetes, le JIT (compilation Just-in-Time) via LLVM, et\n"
                "des ameliorations continues des performances."
            ),
            "history": (
                "L'histoire de PostgreSQL remonte a 1986, quand le professeur\n"
                "Michael Stonebraker de l'Universite de Californie a Berkeley\n"
                "a lance le projet POSTGRES (POST inGRES), successeur de la base\n"
                "de donnees Ingres qu'il avait precedemment creee. L'objectif\n"
                "etait d'explorer des concepts avances comme les types de donnees\n"
                "personnalises et l'heritage de tables.\n\n"
                "POSTGRES a ete finance par DARPA, l'ARO (Army Research Office)\n"
                "et la NSF. Les premieres versions utilisaient un langage de\n"
                "requete proprietaire appele POSTQUEL.\n\n"
                "En 1994, deux etudiants diplomes de Berkeley, Andrew Yu et\n"
                "Jolly Chen, ont ajoute un interpreteur SQL a POSTGRES, creant\n"
                "Postgres95. Ce fork open source a rapidement gagne en popularite.\n\n"
                "En 1996, le projet a ete renomme PostgreSQL pour refleter son\n"
                "support SQL, et la version 6.0 a marque le debut du systeme\n"
                "de numerotation moderne. Une communaute mondiale de developpeurs\n"
                "benevoles s'est formee autour du projet.\n\n"
                "Les annees 2000-2010 ont vu PostgreSQL murer avec l'ajout de\n"
                "MVCC, le WAL (Write-Ahead Logging), la replication, les CTE\n"
                "(Common Table Expressions), et les fonctions window.\n\n"
                "PostgreSQL 9.x (2010-2016) a introduit la replication streaming,\n"
                "la replication logique, le support JSON, et les index GIN\n"
                "ameliores. PostgreSQL 10+ (2017-present) a apporte le\n"
                "partitionnement declaratif, le parallelisme des requetes,\n"
                "le JIT, et des ameliorations de performances majeures.\n\n"
                "En 2025, PostgreSQL est la base de donnees la plus admiree\n"
                "et la plus recherchee selon les enquetes Stack Overflow,\n"
                "et son adoption continue de croitre dans tous les secteurs."
            ),
            "architecture": (
                "L'architecture de PostgreSQL est basee sur un modele processus\n"
                "client-serveur avec une gestion memoire sophistiquee :\n\n"
                "Modele processus : PostgreSQL utilise un processus par connexion\n"
                "(fork). Le processus Postmaster ecoute les connexions entrantes\n"
                "et fork un processus backend pour chaque client. Des processus\n"
                "auxiliaires gerent le WAL writer, le checkpointer, l'autovacuum,\n"
                "le stats collector et le background writer.\n\n"
                "Gestion memoire : La memoire partagee (shared buffers) est un\n"
                "cache de pages disque en memoire. Le WAL (Write-Ahead Logging)\n"
                "garantit la durabilite des transactions en ecrivant les modifications\n"
                "dans un journal avant de les appliquer aux fichiers de donnees.\n\n"
                "MVCC : Chaque ligne possede des champs systeme (xmin, xmax) qui\n"
                "definissent sa visibilite transactionnelle. Les transactions\n"
                "concurrentes voient des versions differentes de la meme ligne,\n"
                "eliminant les verrous de lecture.\n\n"
                "Optimiseur de requetes : L'optimiseur base sur les couts utilise\n"
                "des statistiques collectees par ANALYZE pour choisir le meilleur\n"
                "plan d'execution. Il considere les jointures (nested loop, hash\n"
                "join, merge join), les scans (sequential, index, bitmap) et\n"
                "le parallelisme.\n\n"
                "Stockage : Les donnees sont organisees en tablespaces, bases de\n"
                "donnees, schemas et tables. Chaque table est stockee comme un\n"
                "ensemble de pages de 8 Ko. TOAST (The Oversized-Attribute\n"
                "Storage Technique) gere les valeurs volumineuses.\n\n"
                "Extensibilite : Le systeme de catalogue est lui-meme stocke\n"
                "dans des tables, rendant le SGBD intrinsecablement extensible.\n"
                "Les extensions sont chargees dynamiquement via CREATE EXTENSION."
            ),
            "pros_cons": {
                "pros": [
                    "Conformite stricte aux standards SQL avec des extensions puissantes",
                    "Extensibilite exceptionnelle : types, operateurs, index, langages proceduraux",
                    "MVCC offrant une excellente concurrence sans verrous de lecture",
                    "Support natif de JSON/JSONB combinant relationnel et NoSQL",
                    "Ecosysteme d'extensions riche (PostGIS, TimescaleDB, pgvector, Citus)",
                    "Optimiseur de requetes sophistique avec support du parallelisme",
                    "Replication robuste (streaming, logique) et haute disponibilite",
                    "Communaute open source active et perenne depuis plus de 25 ans"
                ],
                "cons": [
                    "Consommation memoire elevee due au modele processus par connexion",
                    "Configuration initiale complexe pour des performances optimales",
                    "Le VACUUM peut etre problematique sur les tables a fort trafic d'ecriture",
                    "La replication multi-maitre native est absente (necessite des extensions)",
                    "Performances en ecriture inferieures a certaines bases NoSQL pour les charges massives",
                    "La montee en charge horizontale necessite des extensions tierces comme Citus",
                    "La mise a jour des versions majeures requiert pg_upgrade ou un dump/restore"
                ]
            },
            "use_cases": (
                "PostgreSQL convient a pratiquement tous les cas d'usage :\n"
                "applications web et mobiles, systemes financiers necessitant\n"
                "des transactions ACID, entrepots de donnees, applications\n"
                "geospatiales (avec PostGIS), series temporelles (TimescaleDB),\n"
                "recherche vectorielle pour l'IA (pgvector), et systemes\n"
                "analytiques. Il est le choix par defaut pour les nouvelles\n"
                "applications necessitant une base relationnelle fiable."
            ),
            "ecosystem_size": (
                "L'ecosysteme PostgreSQL est extremement riche. Extensions majeures :\n"
                "PostGIS (geospatial), TimescaleDB (series temporelles), pgvector\n"
                "(IA/embeddings), Citus (distribution horizontale), pg_partman\n"
                "(partitionnement). Outils d'administration : pgAdmin, DBeaver.\n"
                "Pooling de connexions : PgBouncer, Pgpool-II. Sauvegarde :\n"
                "pg_dump, pgBackRest, Barman. Monitoring : pg_stat_statements,\n"
                "pgwatch2. Services manages : AWS RDS/Aurora, Google Cloud SQL,\n"
                "Azure Database, Supabase, Neon."
            ),
            "companies": [
                "Apple",
                "Instagram/Meta",
                "Spotify",
                "Reddit",
                "Twitch",
                "Goldman Sachs",
                "Skype/Microsoft",
                "The Guardian"
            ],
            "code_example": (
                "-- Creation d'une table avec contraintes et index\n"
                "CREATE TABLE utilisateurs (\n"
                "    id          SERIAL PRIMARY KEY,\n"
                "    nom         VARCHAR(100) NOT NULL,\n"
                "    email       VARCHAR(255) UNIQUE NOT NULL,\n"
                "    profil      JSONB DEFAULT '{}',\n"
                "    cree_le     TIMESTAMPTZ DEFAULT NOW(),\n"
                "    actif       BOOLEAN DEFAULT TRUE\n"
                ");\n\n"
                "-- Index GIN sur le champ JSONB pour des recherches rapides\n"
                "CREATE INDEX idx_profil ON utilisateurs USING GIN (profil);\n\n"
                "-- Insertion avec des donnees JSON\n"
                "INSERT INTO utilisateurs (nom, email, profil)\n"
                "VALUES ('Marie Dupont', 'marie@exemple.fr',\n"
                "        '{\"ville\": \"Paris\", \"competences\": [\"Python\", \"SQL\"]}');\n\n"
                "-- Requete combinant SQL relationnel et operateurs JSON\n"
                "SELECT nom, email, profil->>'ville' AS ville\n"
                "FROM utilisateurs\n"
                "WHERE profil @> '{\"competences\": [\"Python\"]}'\n"
                "  AND actif = TRUE\n"
                "ORDER BY cree_le DESC;"
            ),
            "performance": {
                "startup_time": "Demarrage en quelques secondes. Le temps de chauffe depende de la taille des shared_buffers et du cache disque a remplir.",
                "throughput": "Excellent pour les lectures concurrentes grace a MVCC. Des dizaines de milliers de transactions par seconde sur du materiel moderne. Le parallelisme ameliore les requetes analytiques.",
                "memory": "Configurable via shared_buffers (generalement 25% de la RAM), work_mem, maintenance_work_mem. Le modele processus consomme plus de memoire que les modeles threads.",
                "concurrency_model": "MVCC sans verrous de lecture. Les ecritures concurrentes sont gerees par des verrous au niveau des lignes. Le parallelisme des requetes distribue le travail sur plusieurs coeurs."
            },
            "learning_curve": (
                "La courbe d'apprentissage de PostgreSQL est progressive. Le SQL\n"
                "de base est accessible, mais la maitrise complete du tuning\n"
                "(work_mem, shared_buffers, effective_cache_size), de EXPLAIN\n"
                "ANALYZE, des index avances et de la replication demande une\n"
                "expertise significative. La documentation officielle est\n"
                "exceptionnellement complete et sert de reference."
            ),
            "community_size": "Communaute mondiale massive. Conferences annuelles (PGConf, PGDay). La mailing list pgsql-general est extremement active. Documentation officielle de reference.",
            "job_market": "PostgreSQL est la base de donnees la plus demandee en 2025. Presente dans pratiquement toutes les offres d'emploi backend. Sa maitrise est un atout quasi universel."
        },
        "traits": {
            "performance": 8,
            "developer_speed": 6,
            "learning_curve": 5,
            "ecosystem_size": 8,
            "type_safety": 8,
            "concurrency": 8,
            "memory_safety": 7,
            "scalability": 8
        }
    },

    "mysql": {
        "name": "MySQL",
        "category": "database",
        "year_created": 1995,
        "creator": "MySQL AB",
        "paradigm": ["relationnel", "ACID", "transactionnel"],
        "typing": "statique (schema strict)",
        "sections": {
            "overview": (
                "MySQL est le systeme de gestion de base de donnees relationnelle\n"
                "open source le plus populaire au monde, au coeur de la pile LAMP\n"
                "(Linux, Apache, MySQL, PHP) qui a propulse le web pendant deux\n"
                "decennies. Detenu par Oracle Corporation depuis le rachat de Sun\n"
                "Microsystems en 2010, MySQL reste le choix par defaut de millions\n"
                "de sites web et d'applications.\n\n"
                "MySQL se distingue par sa simplicite d'installation, sa rapidite\n"
                "pour les charges de lecture, et sa facilite d'utilisation. Le\n"
                "moteur de stockage InnoDB, devenu le moteur par defaut, offre\n"
                "des transactions ACID completes, le verrouillage au niveau des\n"
                "lignes et les cles etrangeres.\n\n"
                "L'architecture pluggable de MySQL permet de choisir differents\n"
                "moteurs de stockage selon les besoins : InnoDB pour les\n"
                "transactions, MyISAM pour la lecture rapide (historique),\n"
                "MEMORY pour les tables en memoire, et NDB pour le clustering.\n\n"
                "MySQL 8.0 a apporte des ameliorations majeures : les CTE\n"
                "(Common Table Expressions), les fonctions window, le support\n"
                "JSON natif, les index invisibles, les roles de securite, le\n"
                "dictionnaire de donnees atomique, et des ameliorations\n"
                "significatives du query optimizer.\n\n"
                "MySQL reste un pilier de l'infrastructure web mondiale, utilise\n"
                "par des geants comme Facebook, YouTube, Twitter et Wikipedia."
            ),
            "history": (
                "MySQL a ete cree en 1995 par Michael 'Monty' Widenius et David\n"
                "Axmark en Suede, au sein de la societe MySQL AB. Le nom 'My'\n"
                "vient du prenom de la fille de Monty. L'objectif etait de creer\n"
                "une base de donnees rapide, fiable et facile a utiliser.\n\n"
                "MySQL a connu une adoption massive avec l'essor du web dans les\n"
                "annees 2000, devenant le 'M' de la pile LAMP. Sa gratuite, sa\n"
                "rapidite et sa simplicite en faisaient le choix ideal pour les\n"
                "hebergeurs web et les startups.\n\n"
                "En 2008, Sun Microsystems a rachete MySQL AB pour un milliard de\n"
                "dollars. En 2010, Oracle a rachete Sun, suscitant des inquietudes\n"
                "dans la communaute open source. Monty Widenius a alors fork MySQL\n"
                "pour creer MariaDB, un fork compatible visant a rester purement\n"
                "communautaire.\n\n"
                "Sous la direction d'Oracle, MySQL a neanmoins continue d'evoluer.\n"
                "MySQL 5.6 (2013) a ameliore les performances d'InnoDB. MySQL 5.7\n"
                "(2015) a ajoute le support JSON natif et ameliore le replicateur.\n\n"
                "MySQL 8.0 (2018) a ete une mise a jour majeure avec les CTE, les\n"
                "fonctions window, un dictionnaire de donnees atomique, et des\n"
                "ameliorations de securite. MySQL 8.0 a rattrape une partie de\n"
                "l'ecart avec PostgreSQL en termes de fonctionnalites SQL avancees.\n\n"
                "MySQL HeatWave, lance par Oracle en 2020, apporte le traitement\n"
                "analytique in-memory directement dans MySQL, fusionnant OLTP et\n"
                "OLAP dans un seul systeme."
            ),
            "architecture": (
                "L'architecture de MySQL est organisee en couches distinctes\n"
                "offrant flexibilite et modularite :\n\n"
                "Couche connexion : Gere l'authentification, les connexions\n"
                "clients, le pool de threads et le cache de threads. MySQL\n"
                "utilise un modele de threads (un thread par connexion) plutot\n"
                "que le modele processus de PostgreSQL.\n\n"
                "Couche SQL : Comprend le parser, l'optimiseur de requetes, le\n"
                "cache de requetes (supprime en 8.0), et l'executeur. L'optimiseur\n"
                "transforme les requetes SQL en plans d'execution optimises.\n\n"
                "Couche moteur de stockage : L'architecture pluggable permet\n"
                "de brancher differents moteurs. InnoDB est le moteur par defaut\n"
                "et fournit : transactions ACID, MVCC, verrouillage au niveau\n"
                "des lignes, cles etrangeres, et recuperation apres crash.\n\n"
                "InnoDB en detail : Les donnees sont stockees dans un tablespace\n"
                "organise en pages de 16 Ko. L'arbre B+ est la structure d'index\n"
                "principale. Le buffer pool cache les pages en memoire. Le redo\n"
                "log (WAL equivalent) garantit la durabilite. L'undo log permet\n"
                "le rollback et le MVCC.\n\n"
                "Replication : MySQL supporte la replication asynchrone\n"
                "maitre-replique, la replication semi-synchrone, et le Group\n"
                "Replication pour la haute disponibilite. Le binlog (binary log)\n"
                "enregistre toutes les modifications pour la replication.\n\n"
                "InnoDB Cluster : Solution de haute disponibilite integree\n"
                "combinant Group Replication, MySQL Shell et MySQL Router pour\n"
                "un failover automatique et un routage transparent."
            ),
            "pros_cons": {
                "pros": [
                    "Extreme popularite garantissant une abondance de ressources et de support",
                    "Simplicite d'installation et de configuration pour les debutants",
                    "Excellentes performances en lecture pour les charges web classiques",
                    "Moteur InnoDB mature offrant des transactions ACID fiables",
                    "Replication flexible avec plusieurs topologies possibles",
                    "Ecosysteme d'outils matures : phpMyAdmin, MySQL Workbench, Percona Toolkit",
                    "Compatible avec pratiquement tous les langages et frameworks",
                    "Services manages disponibles chez tous les fournisseurs cloud"
                ],
                "cons": [
                    "Fonctionnalites SQL avancees en retard par rapport a PostgreSQL",
                    "Gouvernance Oracle suscitant des preoccupations pour le futur open source",
                    "Le mode SQL par defaut est permissif, acceptant des donnees invalides",
                    "Pas de types avances personnalises comme dans PostgreSQL",
                    "Le systeme de partitionnement est moins flexible que celui de PostgreSQL",
                    "La recherche plein texte est basique comparee a des solutions specialisees",
                    "Les sous-requetes etaient historiquement mal optimisees (ameliore en 8.0)"
                ]
            },
            "use_cases": (
                "MySQL excelle pour les applications web a forte charge de lecture :\n"
                "CMS (WordPress, Drupal), e-commerce (Magento, PrestaShop),\n"
                "applications SaaS, sites a fort trafic, et applications legacy.\n"
                "Il est particulierement adapte quand la simplicite de deploiement\n"
                "et la compatibilite avec l'ecosysteme PHP/web sont prioritaires.\n"
                "MySQL HeatWave etend son utilite aux charges analytiques."
            ),
            "ecosystem_size": (
                "L'ecosysteme MySQL est le plus large du monde des bases de donnees.\n"
                "Outils d'administration : MySQL Workbench, phpMyAdmin, DBeaver.\n"
                "Haute disponibilite : InnoDB Cluster, Percona XtraDB Cluster,\n"
                "Galera Cluster. Proxy : ProxySQL, MySQL Router. Sauvegarde :\n"
                "mysqldump, Percona XtraBackup. Monitoring : Percona Monitoring\n"
                "and Management (PMM), MySQL Enterprise Monitor. ORM : Sequelize,\n"
                "SQLAlchemy, Hibernate, Prisma, TypeORM. Services cloud : AWS\n"
                "RDS/Aurora, Google Cloud SQL, Azure Database for MySQL."
            ),
            "companies": [
                "Facebook/Meta",
                "YouTube/Google",
                "Twitter/X",
                "Netflix",
                "Uber",
                "Booking.com",
                "GitHub",
                "Wikipedia/Wikimedia"
            ],
            "code_example": (
                "-- Creation d'une table avec le moteur InnoDB\n"
                "CREATE TABLE articles (\n"
                "    id          INT AUTO_INCREMENT PRIMARY KEY,\n"
                "    titre       VARCHAR(200) NOT NULL,\n"
                "    contenu     TEXT NOT NULL,\n"
                "    auteur_id   INT NOT NULL,\n"
                "    tags        JSON,\n"
                "    publie_le   DATETIME DEFAULT CURRENT_TIMESTAMP,\n"
                "    INDEX idx_auteur (auteur_id),\n"
                "    FULLTEXT INDEX idx_recherche (titre, contenu),\n"
                "    FOREIGN KEY (auteur_id) REFERENCES utilisateurs(id)\n"
                ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n"
                "-- Insertion avec des donnees JSON\n"
                "INSERT INTO articles (titre, contenu, auteur_id, tags)\n"
                "VALUES ('Apprendre MySQL', 'MySQL est une base...', 1,\n"
                "        JSON_ARRAY('sql', 'base de donnees', 'tutoriel'));\n\n"
                "-- Requete avec fonction JSON et recherche plein texte\n"
                "SELECT titre, auteur_id,\n"
                "       JSON_EXTRACT(tags, '$[0]') AS premier_tag\n"
                "FROM articles\n"
                "WHERE MATCH(titre, contenu) AGAINST('MySQL' IN BOOLEAN MODE)\n"
                "ORDER BY publie_le DESC\n"
                "LIMIT 10;"
            ),
            "performance": {
                "startup_time": "Demarrage rapide, generalement en quelques secondes. Le temps de chauffe du buffer pool InnoDB peut prendre plus de temps pour les grandes bases.",
                "throughput": "Excellentes performances en lecture. Plusieurs centaines de milliers de requetes simples par seconde. Les benchmarks TPC-C montrent des performances competitives pour les charges OLTP.",
                "memory": "Le buffer pool InnoDB est le parametre critique (generalement 70-80% de la RAM). Le modele thread est plus econome en memoire que le modele processus de PostgreSQL.",
                "concurrency_model": "Modele thread-based avec un thread par connexion. InnoDB utilise MVCC pour la concurrence en lecture. Verrouillage au niveau des lignes pour les ecritures. Thread pool disponible en Enterprise."
            },
            "learning_curve": (
                "La courbe d'apprentissage de MySQL est l'une des plus douces\n"
                "parmi les bases de donnees relationnelles. L'installation est\n"
                "simple, le SQL de base est rapidement maitrise, et l'abondance\n"
                "de tutoriels facilite l'apprentissage. La complexite augmente\n"
                "avec le tuning de performance, la replication et la haute\n"
                "disponibilite."
            ),
            "community_size": "La plus grande communaute de bases de donnees au monde. Des millions de deployments actifs. Enormement de documentation, tutoriels et ressources disponibles.",
            "job_market": "MySQL est mentionne dans un tres grand nombre d'offres d'emploi. Sa maitrise est souvent consideree comme acquise pour les developpeurs backend."
        },
        "traits": {
            "performance": 7,
            "developer_speed": 7,
            "learning_curve": 4,
            "ecosystem_size": 8,
            "type_safety": 7,
            "concurrency": 7,
            "memory_safety": 7,
            "scalability": 7
        }
    },

    "mongodb": {
        "name": "MongoDB",
        "category": "database",
        "year_created": 2009,
        "creator": "MongoDB Inc",
        "paradigm": ["document", "NoSQL", "schema-flexible", "distribue"],
        "typing": "dynamique (schema flexible, validation optionnelle)",
        "sections": {
            "overview": (
                "MongoDB est une base de donnees NoSQL orientee documents, stockant\n"
                "les donnees sous forme de documents BSON (Binary JSON). Contrairement\n"
                "aux bases relationnelles qui imposent un schema rigide, MongoDB\n"
                "permet de stocker des documents avec des structures differentes\n"
                "dans la meme collection, offrant une flexibilite remarquable.\n\n"
                "Le modele de donnees document de MongoDB s'aligne naturellement\n"
                "avec les objets utilises dans le code applicatif, eliminant le\n"
                "mismatch objet-relationnel qui complique le developpement avec\n"
                "les bases SQL. Un document MongoDB peut contenir des sous-documents\n"
                "imbriques, des tableaux et des types riches (dates, binaires, etc.).\n\n"
                "MongoDB a ete concu des le depart pour la scalabilite horizontale.\n"
                "Le sharding natif distribue les donnees sur plusieurs serveurs\n"
                "de maniere transparente. Les replica sets assurent la haute\n"
                "disponibilite avec basculement automatique.\n\n"
                "Depuis MongoDB 4.0, le support des transactions multi-documents\n"
                "ACID est disponible, comblant une lacune historique majeure.\n"
                "MongoDB 5.0+ a introduit les time series collections, le\n"
                "versioned API, et le chiffrement queryable (Queryable Encryption).\n\n"
                "MongoDB Atlas, le service cloud manage, est devenu la facon\n"
                "la plus populaire de deployer MongoDB, offrant des fonctionnalites\n"
                "avancees comme Atlas Search (recherche plein texte basee sur\n"
                "Lucene), Atlas Vector Search pour l'IA, et les Data Federation."
            ),
            "history": (
                "MongoDB a ete cree en 2007 par Dwight Merriman, Eliot Horowitz et\n"
                "Kevin Ryan, fondateurs de la societe 10gen (renommee MongoDB Inc\n"
                "en 2013). Le projet est ne de leur experience chez DoubleClick,\n"
                "une regie publicitaire en ligne ou ils ont rencontre les limites\n"
                "des bases relationnelles pour gerer de gros volumes de donnees.\n\n"
                "La premiere version publique a ete lancee en 2009. Le nom 'MongoDB'\n"
                "vient de 'humongous' (enorme), refletant l'ambition de gerer des\n"
                "volumes massifs de donnees.\n\n"
                "L'adoption a ete extremement rapide, portee par le mouvement NoSQL\n"
                "et la promesse de simplicite. MongoDB est devenu le poster child\n"
                "du mouvement NoSQL, mais aussi sa cible favorite pour les critiques\n"
                "concernant la perte de donnees et l'absence de transactions.\n\n"
                "MongoDB 3.0 (2015) a introduit le moteur de stockage WiredTiger,\n"
                "ameliorant drastiquement les performances et la compression.\n"
                "MongoDB 3.6 a ajoute les change streams et le retryable writes.\n\n"
                "MongoDB 4.0 (2018) a ete un tournant avec le support des\n"
                "transactions multi-documents ACID, repondant a l'une des\n"
                "critiques les plus persistantes. MongoDB 4.4 a apporte les\n"
                "hedged reads et le compound wildcard indexes.\n\n"
                "L'introduction en bourse de MongoDB Inc en 2017 et le succes\n"
                "d'Atlas ont transforme l'entreprise en acteur majeur du cloud.\n"
                "En 2019, MongoDB a change sa licence pour SSPL (Server Side\n"
                "Public License), une decision controversee visant a empecher\n"
                "les cloud providers d'offrir MongoDB as a Service sans contribuer."
            ),
            "architecture": (
                "L'architecture de MongoDB est concue pour la distribution et\n"
                "la haute disponibilite :\n\n"
                "Modele de donnees : Les donnees sont organisees en bases de\n"
                "donnees, collections et documents. Chaque document est un\n"
                "objet BSON avec un identifiant unique _id. Les documents\n"
                "peuvent avoir des structures heterogenes dans la meme collection.\n\n"
                "Moteur de stockage WiredTiger : Le moteur par defaut utilise\n"
                "le controle de concurrence par document avec des verrous au\n"
                "niveau du document. Il offre la compression des donnees\n"
                "(snappy, zlib, zstd) et le journaling pour la durabilite.\n\n"
                "Replica Sets : Un ensemble de repliques comprend un noeud\n"
                "primaire (acceptant les ecritures) et des noeuds secondaires\n"
                "(copiant les donnees via l'oplog). Le basculement automatique\n"
                "elit un nouveau primaire en cas de defaillance en quelques\n"
                "secondes.\n\n"
                "Sharding : Le sharding distribue les donnees sur plusieurs\n"
                "shards (chacun etant un replica set). Le routeur mongos dirige\n"
                "les requetes vers les shards concernes. La cle de sharding\n"
                "determine la distribution des documents.\n\n"
                "Aggregation Pipeline : Le framework d'agregation permet des\n"
                "transformations de donnees complexes via un pipeline d'etapes\n"
                "(match, group, project, lookup, unwind, etc.), equivalent\n"
                "aux GROUP BY/JOIN du SQL mais plus flexible.\n\n"
                "Index : MongoDB supporte les index B-tree, texte, geospatiaux\n"
                "(2d, 2dsphere), hashes, compound, multikey (sur les tableaux),\n"
                "wildcard, et les index partiels/sparse."
            ),
            "pros_cons": {
                "pros": [
                    "Schema flexible permettant une evolution rapide du modele de donnees",
                    "Scalabilite horizontale native via le sharding transparent",
                    "Modele document s'alignant naturellement avec les objets applicatifs",
                    "Aggregation Pipeline puissant pour les transformations de donnees",
                    "Atlas offre un service cloud manage complet avec recherche et IA",
                    "Transactions ACID multi-documents depuis la version 4.0",
                    "Change Streams pour les applications reactives en temps reel",
                    "Excellentes performances en lecture/ecriture pour les charges web"
                ],
                "cons": [
                    "L'absence de schema peut mener a des donnees incoherentes si non discipline",
                    "Les jointures (lookup) sont moins performantes que dans les bases relationnelles",
                    "La consommation memoire peut etre elevee (WiredTiger cache + index en RAM)",
                    "Le choix de la cle de sharding est critique et difficile a modifier",
                    "La licence SSPL est controversee et non reconnue comme open source par l'OSI",
                    "Les transactions multi-documents ajoutent de la latence et de la complexite",
                    "Le manque de schema strict peut rendre la maintenance a long terme difficile"
                ]
            },
            "use_cases": (
                "MongoDB excelle pour les applications necessitant un schema\n"
                "flexible et evolutif : catalogues de produits e-commerce,\n"
                "gestion de contenu (CMS), applications IoT, applications\n"
                "mobiles avec synchronisation (Realm), gaming, applications\n"
                "temps reel, et prototypage rapide. Il est particulierement\n"
                "adapte quand le modele de donnees est hierarchique ou semi-\n"
                "structure, et quand la scalabilite horizontale est requise."
            ),
            "ecosystem_size": (
                "L'ecosysteme MongoDB est mature et complet. Atlas fournit un\n"
                "service cloud manage avec Atlas Search, Vector Search, Charts,\n"
                "et Data Federation. Realm (maintenant Atlas Device SDK) offre\n"
                "la synchronisation mobile. Compass est l'outil GUI officiel.\n"
                "Mongoose (Node.js), Motor (Python async), et Spring Data\n"
                "MongoDB (Java) sont les ODM/drivers populaires. MongoDB\n"
                "Connector for Spark permet l'integration Big Data."
            ),
            "companies": [
                "Forbes",
                "Toyota",
                "Adobe",
                "SAP",
                "eBay",
                "Cisco",
                "Bosch",
                "SEGA"
            ],
            "code_example": (
                "// Insertion d'un document avec sous-document et tableau\n"
                "db.produits.insertOne({\n"
                "  nom: 'Ordinateur Portable',\n"
                "  prix: 1299.99,\n"
                "  categorie: 'informatique',\n"
                "  specs: {\n"
                "    processeur: 'Apple M3',\n"
                "    ram: '16 Go',\n"
                "    stockage: '512 Go SSD'\n"
                "  },\n"
                "  tags: ['portable', 'apple', 'professionnel'],\n"
                "  avis: [\n"
                "    { utilisateur: 'Jean', note: 5, commentaire: 'Excellent !' },\n"
                "    { utilisateur: 'Marie', note: 4, commentaire: 'Tres bon produit' }\n"
                "  ]\n"
                "});\n\n"
                "// Pipeline d'agregation : note moyenne par categorie\n"
                "db.produits.aggregate([\n"
                "  { $unwind: '$avis' },\n"
                "  { $group: {\n"
                "      _id: '$categorie',\n"
                "      note_moyenne: { $avg: '$avis.note' },\n"
                "      nombre_avis: { $sum: 1 }\n"
                "    }\n"
                "  },\n"
                "  { $sort: { note_moyenne: -1 } }\n"
                "]);"
            ),
            "performance": {
                "startup_time": "Demarrage en quelques secondes. Le temps de chauffe depend de la taille du cache WiredTiger et des index a charger en memoire.",
                "throughput": "Excellentes performances pour les lectures et ecritures de documents individuels. Le sharding permet de scaler lineairement. Les agregations complexes peuvent etre plus lentes qu'en SQL.",
                "memory": "Le cache WiredTiger utilise par defaut 50% de la RAM. Les index doivent idealement tenir en memoire pour des performances optimales.",
                "concurrency_model": "Concurrence au niveau du document avec WiredTiger. Les lectures ne bloquent pas les ecritures et vice versa. Les transactions multi-documents utilisent un verrouillage plus large."
            },
            "learning_curve": (
                "La courbe d'apprentissage est douce pour les cas simples :\n"
                "l'insertion et la requete de documents JSON sont intuitives.\n"
                "La complexite augmente avec l'aggregation pipeline, le sharding,\n"
                "la modelisation de donnees (quand imbriquer vs referencer ?),\n"
                "et l'optimisation des index. Les developpeurs SQL doivent\n"
                "reapprendre a penser en termes de documents."
            ),
            "community_size": "Enorme communaute mondiale. MongoDB University offre des cours gratuits. Plus de 25 000 etoiles sur GitHub. Conferences MongoDB World et meetups reguliers.",
            "job_market": "Tres demande dans les entreprises modernes. MongoDB est souvent cite dans les offres d'emploi fullstack et backend, particulierement dans les startups et le e-commerce."
        },
        "traits": {
            "performance": 7,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 7,
            "type_safety": 3,
            "concurrency": 7,
            "memory_safety": 5,
            "scalability": 8
        }
    },

    "redis": {
        "name": "Redis",
        "category": "database",
        "year_created": 2009,
        "creator": "Salvatore Sanfilippo",
        "paradigm": ["cle-valeur", "in-memory", "structures de donnees", "NoSQL"],
        "typing": "dynamique (sans schema, structures de donnees typees)",
        "sections": {
            "overview": (
                "Redis (Remote Dictionary Server) est un magasin de structures de\n"
                "donnees en memoire, open source, utilise comme base de donnees,\n"
                "cache, courtier de messages et file d'attente. Sa particularite\n"
                "est de stocker l'integralite des donnees en RAM, offrant des\n"
                "latences de l'ordre de la microseconde.\n\n"
                "Contrairement a un simple cache cle-valeur, Redis supporte des\n"
                "structures de donnees riches : chaines, listes, ensembles,\n"
                "ensembles tries (sorted sets), hachages, bitmaps, HyperLogLog,\n"
                "flux (streams), et types geospatiaux. Chaque structure dispose\n"
                "d'operations atomiques optimisees.\n\n"
                "Redis est mono-thread pour les operations de donnees (bien que\n"
                "les operations d'I/O soient multithread depuis Redis 6), ce qui\n"
                "elimine les problemes de concurrence et garantit l'atomicite\n"
                "de chaque commande. Cette simplicite architecturale est la cle\n"
                "de ses performances extraordinaires.\n\n"
                "La persistance est optionnelle et configurable via RDB (snapshots\n"
                "periodiques) et/ou AOF (Append Only File, journal de toutes les\n"
                "ecritures). Redis peut ainsi servir a la fois de cache volatile\n"
                "et de base de donnees persistante.\n\n"
                "Redis Cluster permet le partitionnement automatique des donnees\n"
                "sur plusieurs noeuds avec replication et basculement automatique.\n"
                "Redis Sentinel fournit la haute disponibilite pour les deployments\n"
                "non clusteres."
            ),
            "history": (
                "Redis a ete cree en 2009 par Salvatore Sanfilippo (antirez), un\n"
                "developpeur italien. Il cherchait a ameliorer les performances\n"
                "de LLOOGG, un outil d'analyse de logs en temps reel qu'il\n"
                "developpait. Les bases de donnees existantes etaient trop lentes\n"
                "pour ses besoins de compteurs en temps reel.\n\n"
                "Sanfilippo a alors cree un prototype de magasin cle-valeur en\n"
                "memoire avec persistance, qu'il a publie en open source. Le\n"
                "projet a immediatement attire l'attention de la communaute\n"
                "developpeur par sa simplicite et ses performances.\n\n"
                "En 2010, VMware a sponsorise le developpement de Redis. En 2013,\n"
                "Pivotal (filiale de VMware/Dell) a pris le relais. En 2015,\n"
                "Redis Labs (renommee Redis Ltd en 2021) est devenue la societe\n"
                "principale derriere le developpement commercial de Redis.\n\n"
                "Redis 3.0 (2015) a introduit Redis Cluster, permettant le\n"
                "partitionnement automatique. Redis 5.0 (2018) a ajoute les\n"
                "Streams, une structure de donnees de type journal. Redis 6.0\n"
                "(2020) a apporte les ACL (listes de controle d'acces), le TLS\n"
                "et le multithreading des I/O.\n\n"
                "En 2020, Salvatore Sanfilippo a passe le relais de la maintenance\n"
                "a l'equipe Redis. En 2024, Redis Ltd a change la licence de Redis\n"
                "de BSD a une double licence RSALv2/SSPL, provoquant la creation\n"
                "de forks comme Valkey (soutenu par la Linux Foundation) et\n"
                "Redict. Cette decision a suscite un vif debat dans la communaute\n"
                "open source."
            ),
            "architecture": (
                "L'architecture de Redis est volontairement simple, optimisee\n"
                "pour les performances en memoire :\n\n"
                "Modele mono-thread : Le coeur de Redis est mono-thread pour\n"
                "les operations de donnees. Chaque commande est executee\n"
                "atomiquement sans possibilite d'interleaving. Cela simplifie\n"
                "enormement la logique interne et elimine les couts de\n"
                "synchronisation.\n\n"
                "Boucle d'evenements : Redis utilise une boucle d'evenements\n"
                "basee sur epoll (Linux) / kqueue (macOS) pour gerer des\n"
                "milliers de connexions simultanees avec un seul thread.\n"
                "Depuis Redis 6, les operations d'I/O reseau sont multithread.\n\n"
                "Structures de donnees : Chaque type de donnees est implemente\n"
                "avec des structures optimisees. Par exemple, les petites listes\n"
                "utilisent des ziplist (compacts), les grandes des linked lists\n"
                "ou listpacks. Les sorted sets combinent un skip list et une\n"
                "hash table.\n\n"
                "Persistance RDB : Redis fork le processus principal pour creer\n"
                "un snapshot binaire compact des donnees. Le copy-on-write du\n"
                "systeme d'exploitation minimise l'impact memoire du fork.\n\n"
                "Persistance AOF : Chaque commande d'ecriture est ajoutee a un\n"
                "fichier journal. L'AOF peut etre rewrite periodiquement pour\n"
                "reduire sa taille. Depuis Redis 7.0, le format AOF est\n"
                "multi-parties (manifeste + fichiers).\n\n"
                "Redis Cluster : Les donnees sont partitionnees en 16 384 hash\n"
                "slots distribues sur les noeuds. Chaque noeud connait la\n"
                "topologie complete du cluster. La redirection MOVED/ASK\n"
                "guide les clients vers le bon noeud."
            ),
            "pros_cons": {
                "pros": [
                    "Performances exceptionnelles : latences sous la milliseconde, millions d'operations/seconde",
                    "Structures de donnees riches (listes, sets, sorted sets, streams, etc.)",
                    "Simplicite d'utilisation avec un protocole texte lisible et des commandes intuitives",
                    "Polyvalent : cache, base de donnees, pub/sub, file d'attente, leaderboards",
                    "Atomicite de chaque commande sans gestion de concurrence cote client",
                    "Redis Cluster pour la scalabilite horizontale avec replication automatique",
                    "Lua scripting et Redis Functions pour la logique serveur atomique",
                    "Modules extensibles : RediSearch, RedisJSON, RedisTimeSeries, RedisGraph"
                ],
                "cons": [
                    "Toutes les donnees doivent tenir en RAM, cout eleve pour de gros volumes",
                    "Persistance non instantanee : risque de perte de donnees en cas de crash",
                    "Les transactions Redis (MULTI/EXEC) sont limitees comparees au SQL",
                    "Le modele mono-thread limite le throughput a un seul coeur CPU pour les operations",
                    "La gestion memoire necessite une surveillance attentive (fragmentation, eviction)",
                    "Le changement de licence (RSAL/SSPL) cree de l'incertitude sur le futur open source",
                    "Redis Cluster ne supporte pas les transactions multi-cles cross-slot"
                ]
            },
            "use_cases": (
                "Redis est incontournable pour : le caching applicatif (cache de\n"
                "sessions, de requetes, d'API), les leaderboards et classements\n"
                "en temps reel (sorted sets), les files d'attente de taches\n"
                "(lists, streams), le rate limiting, le comptage en temps reel\n"
                "(HyperLogLog), la messagerie pub/sub, les verrous distribues,\n"
                "et le stockage de sessions utilisateur. Il est souvent utilise\n"
                "en complement d'une base de donnees principale."
            ),
            "ecosystem_size": (
                "L'ecosysteme Redis inclut de nombreux modules officiels :\n"
                "RediSearch (recherche plein texte), RedisJSON (manipulation\n"
                "JSON native), RedisTimeSeries (series temporelles),\n"
                "RedisBloom (structures probabilistes). Redis Stack combine\n"
                "ces modules. Clients disponibles dans tous les langages :\n"
                "redis-py, ioredis, Jedis, go-redis, etc. Redis Insight est\n"
                "l'outil GUI officiel. Services manages : Redis Cloud, AWS\n"
                "ElastiCache, Azure Cache for Redis, Google Memorystore."
            ),
            "companies": [
                "Twitter/X",
                "GitHub",
                "Stack Overflow",
                "Pinterest",
                "Snapchat",
                "Craigslist",
                "The New York Times",
                "Airbnb"
            ],
            "code_example": (
                "import redis\n\n"
                "# Connexion a Redis\n"
                "r = redis.Redis(host='localhost', port=6379, decode_responses=True)\n\n"
                "# Caching simple avec expiration\n"
                "r.setex('session:utilisateur:42', 3600, 'donnees_session')\n\n"
                "# Classement en temps reel avec sorted set\n"
                "r.zadd('classement:jeu', {\n"
                "    'Alice': 2500,\n"
                "    'Bob': 1800,\n"
                "    'Charlie': 3200,\n"
                "    'Diana': 2900\n"
                "})\n\n"
                "# Top 3 des joueurs\n"
                "top3 = r.zrevrange('classement:jeu', 0, 2, withscores=True)\n"
                "for joueur, score in top3:\n"
                "    print(f'{joueur}: {int(score)} points')\n\n"
                "# File d'attente avec liste\n"
                "r.lpush('file:taches', 'envoyer_email')\n"
                "r.lpush('file:taches', 'generer_rapport')\n"
                "tache = r.rpop('file:taches')  # 'envoyer_email'\n\n"
                "# Pub/Sub pour la messagerie\n"
                "r.publish('notifications', 'Nouvelle commande recue !')"
            ),
            "performance": {
                "startup_time": "Demarrage quasi instantane (millisecondes) sans donnees. Le chargement d'un fichier RDB volumineux peut prendre plusieurs secondes.",
                "throughput": "Performances exceptionnelles : 100 000 a 1 000 000+ operations par seconde sur une seule instance selon la complexite des commandes et la taille des donnees.",
                "memory": "Toutes les donnees resident en RAM. La fragmentation memoire peut augmenter la consommation reelle. Les encodages compacts (ziplist, listpack) optimisent les petits objets.",
                "concurrency_model": "Mono-thread pour les operations de donnees, garantissant l'atomicite. Multithread pour les I/O reseau (Redis 6+). La concurrence est geree par la boucle d'evenements non bloquante."
            },
            "learning_curve": (
                "La courbe d'apprentissage de Redis est l'une des plus douces.\n"
                "Les commandes sont simples et intuitives (GET, SET, LPUSH, ZADD).\n"
                "La documentation officielle est excellente. La complexite apparait\n"
                "avec les patterns avances : verrous distribues (Redlock),\n"
                "caching strategies (cache-aside, write-through), et\n"
                "l'administration de Redis Cluster en production."
            ),
            "community_size": "Plus de 65 000 etoiles sur GitHub. Communaute massive. Le fork Valkey gagne aussi en popularite suite au changement de licence.",
            "job_market": "Redis est un prerequis quasi universel pour les postes backend. Sa maitrise est souvent mentionnee dans les offres, en complement d'une base de donnees principale."
        },
        "traits": {
            "performance": 10,
            "developer_speed": 7,
            "learning_curve": 3,
            "ecosystem_size": 7,
            "type_safety": 3,
            "concurrency": 8,
            "memory_safety": 5,
            "scalability": 7
        }
    },

    "sqlite": {
        "name": "SQLite",
        "category": "database",
        "year_created": 2000,
        "creator": "D. Richard Hipp",
        "paradigm": ["relationnel", "embarque", "ACID", "serverless"],
        "typing": "dynamique (type affinity system)",
        "sections": {
            "overview": (
                "SQLite est un moteur de base de donnees relationnelle embarque,\n"
                "c'est-a-dire qu'il fonctionne directement dans le processus de\n"
                "l'application sans serveur separe. C'est la base de donnees la\n"
                "plus deployee au monde, presente dans chaque smartphone (Android\n"
                "et iOS), chaque navigateur web, et d'innombrables applications.\n\n"
                "Contrairement a PostgreSQL ou MySQL qui fonctionnent en mode\n"
                "client-serveur, SQLite stocke l'integralite de la base de donnees\n"
                "dans un seul fichier disque. Ce fichier est portable entre les\n"
                "systemes d'exploitation et les architectures, faisant de SQLite\n"
                "un excellent format de transfert de donnees.\n\n"
                "SQLite offre des transactions ACID completes, un support SQL\n"
                "riche (CTE, fonctions window, JSON, FTS5 pour la recherche\n"
                "plein texte), et des performances remarquables pour les charges\n"
                "de travail en lecture et les volumes de donnees moderees.\n\n"
                "Le code source de SQLite est dans le domaine public (pas de\n"
                "licence, pas de restrictions). Il est extremement bien teste\n"
                "avec un ratio de 590 lignes de tests pour chaque ligne de code.\n"
                "Cette fiabilite en fait le choix par defaut pour les applications\n"
                "embarquees, mobiles et de bureau.\n\n"
                "SQLite n'est pas concu pour remplacer les bases de donnees\n"
                "client-serveur : il est concu pour remplacer les fichiers de\n"
                "donnees (CSV, XML, JSON) et les petites bases de donnees."
            ),
            "history": (
                "SQLite a ete cree en 2000 par D. Richard Hipp alors qu'il travaillait\n"
                "pour la societe Hwaci sur un projet pour la marine americaine (USS\n"
                "Oscar Austin). Le systeme existant necessitait un serveur de base de\n"
                "donnees Informix, ce qui etait problematique pour un deploiement\n"
                "embarque. Hipp a decide de creer une base de donnees qui ne\n"
                "necessite aucune configuration ni administration.\n\n"
                "La premiere version publique de SQLite est sortie en aout 2000.\n"
                "Le design etait radical pour l'epoque : pas de serveur, pas de\n"
                "configuration, un seul fichier, zero administration.\n\n"
                "En 2003, SQLite 3.0 a ete publie avec un nouveau format de fichier\n"
                "qui est reste compatible en avant et en arriere depuis lors, un\n"
                "exploit de stabilite remarquable.\n\n"
                "L'adoption massive est venue avec les smartphones : Apple a integre\n"
                "SQLite dans iOS comme base de donnees embarquee par defaut, et\n"
                "Google a fait de meme pour Android. Chaque application mobile\n"
                "utilisant Core Data (iOS) ou Room (Android) stocke ses donnees\n"
                "dans SQLite.\n\n"
                "Les navigateurs web utilisent SQLite pour le stockage local\n"
                "(Web SQL, bien que deprecie), les cookies, et l'historique.\n"
                "SQLite est ainsi present sur litteralement des milliards\n"
                "d'appareils.\n\n"
                "Le developpement de SQLite continue activement. Les versions\n"
                "recentes ont ajoute le support JSON, les fonctions window, le\n"
                "FTS5 (Full-Text Search 5), et des ameliorations de performances\n"
                "continues. Le projet Litestream permet la replication de SQLite\n"
                "vers le cloud."
            ),
            "architecture": (
                "L'architecture de SQLite est radicalement differente des bases\n"
                "de donnees client-serveur :\n\n"
                "Bibliotheque embarquee : SQLite est une bibliotheque C d'environ\n"
                "150 000 lignes de code, compilee directement dans l'application.\n"
                "Il n'y a pas de processus serveur, pas de communication reseau,\n"
                "pas de configuration.\n\n"
                "Format de fichier : La base de donnees entiere est stockee dans\n"
                "un seul fichier, organise en pages (par defaut 4096 octets).\n"
                "L'arbre B est la structure de donnees principale pour les tables\n"
                "et les index.\n\n"
                "Machine virtuelle : SQLite compile les requetes SQL en bytecode\n"
                "execute par une machine virtuelle (VDBE - Virtual DataBase\n"
                "Engine). La commande EXPLAIN montre ce bytecode.\n\n"
                "Gestion des transactions : SQLite utilise des verrous au niveau\n"
                "du fichier. En mode journal classique, un seul ecrivain est\n"
                "autorise a la fois. Le mode WAL (Write-Ahead Logging) permet\n"
                "des lectures concurrentes avec un ecrivain simultane.\n\n"
                "Mode WAL : Le WAL est le mode recommande pour les applications\n"
                "concurrentes. Les ecritures vont dans un fichier WAL separe,\n"
                "les lectures consultent a la fois le fichier principal et le\n"
                "WAL. Les checkpoints mergent periodiquement le WAL dans le\n"
                "fichier principal.\n\n"
                "VFS (Virtual File System) : SQLite abstrait les operations\n"
                "systeme de fichiers via une couche VFS, permettant d'adapter\n"
                "SQLite a differents environnements (memoire, HTTP, chiffre, etc.)."
            ),
            "pros_cons": {
                "pros": [
                    "Zero configuration et zero administration : aucun serveur a installer ou maintenir",
                    "Un seul fichier contenant l'integralite de la base de donnees, facilement portable",
                    "Performances exceptionnelles pour les lectures et les petits volumes de donnees",
                    "Fiabilite extreme : 590 lignes de tests par ligne de code, couverture 100% du branching",
                    "Empreinte memoire et disque minimales, ideal pour l'embarque et le mobile",
                    "Domaine public, aucune restriction de licence",
                    "Support SQL riche : CTE, fonctions window, JSON, FTS5, R-Tree",
                    "Transactions ACID completes avec support du mode WAL"
                ],
                "cons": [
                    "Un seul ecrivain a la fois (meme en mode WAL), limitant la concurrence d'ecriture",
                    "Pas de gestion d'acces multi-utilisateurs (pas d'authentification)",
                    "Non adapte aux volumes de donnees depassant quelques centaines de Go",
                    "Pas de replication native (solutions tierces comme Litestream existent)",
                    "Le systeme de types est flexible (type affinity) plutot que strict",
                    "Pas de support natif du reseau (pas d'acces distant sans proxy)",
                    "La scalabilite horizontale est impossible par conception"
                ]
            },
            "use_cases": (
                "SQLite est ideal pour : les applications mobiles (iOS, Android),\n"
                "les applications de bureau, les tests et prototypage, le\n"
                "stockage de configuration, les systemes embarques (IoT), les\n"
                "sites web a faible/moyen trafic, le format de transfert de\n"
                "donnees (remplacement de CSV/JSON), et les applications\n"
                "mono-utilisateur. Des projets comme Litestream et Turso\n"
                "etendent ses cas d'usage au cloud."
            ),
            "ecosystem_size": (
                "L'ecosysteme SQLite est ubiquitaire. Chaque langage de\n"
                "programmation offre un binding SQLite natif : sqlite3 (Python),\n"
                "better-sqlite3 (Node.js), rusqlite (Rust), etc. Frameworks\n"
                "ORM : Room (Android), Core Data (iOS), SQLAlchemy, Prisma.\n"
                "Outils GUI : DB Browser for SQLite, SQLiteStudio. Extensions\n"
                "modernes : Litestream (replication), Turso/libSQL (distribue),\n"
                "sql.js (SQLite compile en WebAssembly). FTS5 pour la recherche\n"
                "plein texte, R-Tree pour les donnees spatiales."
            ),
            "companies": [
                "Apple (iOS, macOS - chaque iPhone contient SQLite)",
                "Google (Android, Chrome)",
                "Mozilla (Firefox)",
                "Microsoft (Edge, Windows)",
                "Adobe",
                "Airbus (systemes embarques)",
                "Bloomberg",
                "Dropbox"
            ],
            "code_example": (
                "import sqlite3\n\n"
                "# Connexion (cree le fichier si inexistant)\n"
                "conn = sqlite3.connect('ma_base.db')\n"
                "conn.execute('PRAGMA journal_mode=WAL')  # Mode WAL recommande\n\n"
                "# Creation de la table\n"
                "conn.execute('''\n"
                "    CREATE TABLE IF NOT EXISTS taches (\n"
                "        id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                "        titre TEXT NOT NULL,\n"
                "        description TEXT,\n"
                "        priorite INTEGER DEFAULT 0,\n"
                "        terminee BOOLEAN DEFAULT FALSE,\n"
                "        creee_le DATETIME DEFAULT CURRENT_TIMESTAMP\n"
                "    )\n"
                "''')\n\n"
                "# Insertion securisee avec parametres\n"
                "conn.execute(\n"
                "    'INSERT INTO taches (titre, description, priorite) VALUES (?, ?, ?)',\n"
                "    ('Apprendre SQLite', 'Etudier le mode WAL et les index', 2)\n"
                ")\n"
                "conn.commit()\n\n"
                "# Requete avec CTE (Common Table Expression)\n"
                "resultats = conn.execute('''\n"
                "    WITH taches_prioritaires AS (\n"
                "        SELECT * FROM taches WHERE priorite >= 2 AND NOT terminee\n"
                "    )\n"
                "    SELECT titre, priorite FROM taches_prioritaires\n"
                "    ORDER BY priorite DESC\n"
                "''').fetchall()\n\n"
                "for titre, priorite in resultats:\n"
                "    print(f'[P{priorite}] {titre}')\n\n"
                "conn.close()"
            ),
            "performance": {
                "startup_time": "Demarrage instantane : SQLite est une bibliotheque chargee dans le processus, aucun serveur a demarrer.",
                "throughput": "Extremement rapide pour les lectures : des dizaines de milliers de requetes SELECT par seconde. Les ecritures sont limitees par le verrou exclusif (une seule ecriture a la fois).",
                "memory": "Empreinte memoire minimale : quelques centaines de Ko a quelques Mo selon le cache configure. Ideal pour les appareils contraints.",
                "concurrency_model": "Un seul ecrivain a la fois. En mode WAL : lectures concurrentes illimitees avec un ecrivain simultane. Pas de concurrence multi-processus pour les ecritures."
            },
            "learning_curve": (
                "La courbe d'apprentissage est la plus basse de toutes les bases\n"
                "de donnees relationnelles. Aucune installation de serveur,\n"
                "aucune configuration. Le SQL standard fonctionne directement.\n"
                "La maitrise avancee implique la comprehension du mode WAL,\n"
                "de EXPLAIN QUERY PLAN, des PRAGMA et de l'optimisation\n"
                "des requetes."
            ),
            "community_size": "Communaute distribuee. Pas de GitHub classique (le code est sur Fossil). Forum officiel actif. Documentation de reference exceptionnelle.",
            "job_market": "Rarement demande comme competence principale, mais sa connaissance est un atout pour le developpement mobile et embarque. Omnipresent dans les stacks techniques."
        },
        "traits": {
            "performance": 8,
            "developer_speed": 9,
            "learning_curve": 2,
            "ecosystem_size": 6,
            "type_safety": 6,
            "concurrency": 3,
            "memory_safety": 7,
            "scalability": 2
        }
    },

    "cassandra": {
        "name": "Apache Cassandra",
        "category": "database",
        "year_created": 2008,
        "creator": "Facebook/Apache",
        "paradigm": ["colonnes larges", "distribue", "NoSQL", "eventually consistent"],
        "typing": "statique (schema defini via CQL)",
        "sections": {
            "overview": (
                "Apache Cassandra est une base de donnees NoSQL distribuee concue\n"
                "pour gerer de grandes quantites de donnees reparties sur de\n"
                "nombreux serveurs sans point unique de defaillance. C'est la\n"
                "base de donnees de reference quand la scalabilite horizontale\n"
                "et la haute disponibilite sont les priorites absolues.\n\n"
                "Cassandra utilise un modele de donnees en colonnes larges (wide\n"
                "column), ou les donnees sont organisees en keyspaces, tables,\n"
                "partitions et lignes. Chaque ligne peut avoir un nombre different\n"
                "de colonnes, offrant une certaine flexibilite tout en conservant\n"
                "une structure definie par CQL (Cassandra Query Language).\n\n"
                "L'architecture de Cassandra est pair-a-pair (peer-to-peer) : il\n"
                "n'y a pas de noeud maitre ni de noeud special. Chaque noeud est\n"
                "identique et peut accepter des lectures et ecritures. Cette\n"
                "architecture elimine les points uniques de defaillance et\n"
                "simplifie les operations.\n\n"
                "Cassandra offre une consistance configurable (tunable consistency)\n"
                "permettant de choisir, pour chaque requete, le compromis entre\n"
                "la consistance et la disponibilite selon le theoreme CAP.\n"
                "On peut demander ONE (rapide, eventuellement inconsistant),\n"
                "QUORUM (equilibre), ou ALL (consistant, plus lent).\n\n"
                "Cassandra est optimisee pour les ecritures massives : les\n"
                "ecritures sont toujours sequentielles (append-only) via le\n"
                "commit log et les memtables, puis compactees en SSTables\n"
                "sur disque."
            ),
            "history": (
                "Cassandra a ete concue chez Facebook par Avinash Lakshman\n"
                "(co-createur de Dynamo chez Amazon) et Prashant Malik pour\n"
                "resoudre le probleme de la recherche dans la boite de reception\n"
                "Facebook, necessitant des lectures et ecritures rapides sur\n"
                "des milliards de messages distribues globalement.\n\n"
                "Facebook a publie Cassandra en open source en juillet 2008.\n"
                "Le projet combinait le modele de distribution de Dynamo (Amazon)\n"
                "avec le modele de donnees de Bigtable (Google), prenant le\n"
                "meilleur des deux approches.\n\n"
                "En 2009, Cassandra est devenue un projet Apache Incubator,\n"
                "puis un projet top-level en 2010. L'adoption a ete rapide\n"
                "parmi les entreprises gerant de gros volumes de donnees.\n\n"
                "DataStax, fondee en 2010 par Jonathan Ellis (un contributeur\n"
                "majeur de Cassandra), est devenue la societe commerciale\n"
                "principale offrant du support et des outils autour de Cassandra.\n\n"
                "Cassandra 2.0 (2013) a introduit les lightweight transactions\n"
                "(compare-and-set) et les triggers. Cassandra 3.0 (2015) a\n"
                "apporte la materialised views et un nouveau format de stockage.\n\n"
                "Cassandra 4.0 (2021) a ete une version axee sur la stabilite\n"
                "et la fiabilite, avec un processus de test exhaustif.\n"
                "Cassandra 5.0 (2023) a introduit les Storage Attached Indexes\n"
                "(SAI), les tries memtables, et des ameliorations significatives\n"
                "de performances.\n\n"
                "Aujourd'hui, Cassandra est utilisee par certaines des plus\n"
                "grandes installations de donnees au monde, avec des clusters\n"
                "depassant des petaoctets de donnees."
            ),
            "architecture": (
                "L'architecture de Cassandra est fondamentalement distribuee,\n"
                "sans maitre ni point unique de defaillance :\n\n"
                "Topologie en anneau : Les noeuds sont organises logiquement en\n"
                "anneau. Chaque noeud est responsable d'une plage de tokens\n"
                "(partitions) determinee par le partitioner (generalement\n"
                "Murmur3Partitioner).\n\n"
                "Protocole Gossip : Les noeuds communiquent via le protocole\n"
                "gossip pour partager les informations d'etat (disponibilite,\n"
                "charge, schema). Chaque noeud echange periodiquement des\n"
                "informations avec quelques voisins, propageant l'information\n"
                "a tout le cluster.\n\n"
                "Replication : Les donnees sont repliquees sur plusieurs noeuds\n"
                "selon la strategie de replication (SimpleStrategy pour un seul\n"
                "datacenter, NetworkTopologyStrategy pour le multi-datacenter).\n"
                "Le facteur de replication definit le nombre de copies.\n\n"
                "Chemin d'ecriture : Les ecritures passent par le commit log\n"
                "(pour la durabilite), puis la memtable (en memoire). Quand la\n"
                "memtable est pleine, elle est flushee en SSTable (Sorted String\n"
                "Table) sur disque. La compaction fusionne periodiquement les\n"
                "SSTables.\n\n"
                "Chemin de lecture : Les lectures consultent la memtable et les\n"
                "SSTables (via les Bloom filters pour eviter les lectures inutiles,\n"
                "puis les index et les blocs de donnees). La fusion des resultats\n"
                "utilise les timestamps pour resoudre les conflits.\n\n"
                "Consistance configurable : Pour chaque requete, le client\n"
                "specifie le niveau de consistance (ONE, QUORUM, LOCAL_QUORUM,\n"
                "ALL, etc.), equilibrant performance et coherence."
            ),
            "pros_cons": {
                "pros": [
                    "Scalabilite horizontale lineaire : ajoutez des noeuds pour augmenter la capacite",
                    "Haute disponibilite sans point unique de defaillance (architecture pair-a-pair)",
                    "Performances d'ecriture exceptionnelles grace a l'approche append-only",
                    "Support natif du multi-datacenter pour la distribution geographique",
                    "Consistance configurable permettant d'adapter le compromis CAP par requete",
                    "Gestion de volumes massifs de donnees (petaoctets) sur des milliers de noeuds",
                    "CQL offre une syntaxe familiere pour les developpeurs SQL",
                    "Compaction en arriere-plan sans impact sur les operations en cours"
                ],
                "cons": [
                    "Modelisation des donnees complexe : le schema doit etre concu autour des requetes",
                    "Pas de jointures, pas de sous-requetes : le modele est fondamentalement different du SQL",
                    "L'administration et le tuning d'un cluster en production sont complexes",
                    "Les lectures sont plus lentes que les ecritures, surtout avec de nombreuses SSTables",
                    "La consistance eventuelle peut etre deroutante pour les developpeurs habitues a ACID",
                    "Les lightweight transactions (LWT) sont lentes et a utiliser avec parcimonie",
                    "Necessite un minimum de 3 noeuds pour la replication, cout d'infrastructure eleve"
                ]
            },
            "use_cases": (
                "Cassandra excelle pour les cas d'usage necessitant une ecriture\n"
                "massive et une disponibilite totale : donnees de series temporelles\n"
                "(IoT, metriques, logs), messagerie a grande echelle, donnees\n"
                "d'evenements et d'activite utilisateur, catalogues de produits\n"
                "distribues globalement, systemes de recommandation, et toute\n"
                "application necessitant une scalabilite horizontale lineaire\n"
                "sans temps d'arret."
            ),
            "ecosystem_size": (
                "L'ecosysteme Cassandra comprend DataStax Enterprise (version\n"
                "commerciale), DataStax Astra (service cloud manage), cqlsh\n"
                "(client en ligne de commande), et les drivers officiels pour\n"
                "Java, Python, Node.js, Go, C++ et C#. Apache Spark s'integre\n"
                "nativement avec Cassandra via le Spark Cassandra Connector.\n"
                "Les outils incluent Apache Cassandra Reaper (reparation),\n"
                "Medusa (sauvegarde), et Cassandra Stress (benchmarking).\n"
                "ScyllaDB est une reimplementation compatible en C++ offrant\n"
                "des performances superieures."
            ),
            "companies": [
                "Apple (plus de 150 000 noeuds Cassandra)",
                "Netflix",
                "Instagram/Meta",
                "Spotify",
                "Uber",
                "eBay",
                "ING Bank",
                "Intuit"
            ],
            "code_example": (
                "-- Creation d'un keyspace avec replication multi-datacenter\n"
                "CREATE KEYSPACE IF NOT EXISTS commerce\n"
                "WITH REPLICATION = {\n"
                "    'class': 'NetworkTopologyStrategy',\n"
                "    'dc_paris': 3,\n"
                "    'dc_london': 3\n"
                "};\n\n"
                "USE commerce;\n\n"
                "-- Table modelisee autour de la requete principale\n"
                "CREATE TABLE commandes_par_client (\n"
                "    client_id UUID,\n"
                "    date_commande TIMESTAMP,\n"
                "    commande_id UUID,\n"
                "    montant DECIMAL,\n"
                "    statut TEXT,\n"
                "    articles LIST<FROZEN<MAP<TEXT, TEXT>>>,\n"
                "    PRIMARY KEY (client_id, date_commande)\n"
                ") WITH CLUSTERING ORDER BY (date_commande DESC);\n\n"
                "-- Insertion d'une commande\n"
                "INSERT INTO commandes_par_client\n"
                "    (client_id, date_commande, commande_id, montant, statut, articles)\n"
                "VALUES (\n"
                "    uuid(), toTimestamp(now()), uuid(), 149.99, 'en_cours',\n"
                "    [{'nom': 'Livre SQL', 'quantite': '1', 'prix': '39.99'},\n"
                "     {'nom': 'Clavier mecanique', 'quantite': '1', 'prix': '110.00'}]\n"
                ");\n\n"
                "-- Requete optimisee : commandes recentes d'un client\n"
                "SELECT * FROM commandes_par_client\n"
                "WHERE client_id = ? LIMIT 10;"
            ),
            "performance": {
                "startup_time": "Le demarrage d'un noeud prend 30 secondes a plusieurs minutes selon la taille des donnees et le nombre de SSTables. Le bootstrapping d'un nouveau noeud peut prendre des heures.",
                "throughput": "Ecritures exceptionnelles : des centaines de milliers par seconde par noeud. Scalabilite lineaire : doublez les noeuds, doublez le throughput. Les lectures sont plus variables.",
                "memory": "Consommation memoire significative : memtables, bloom filters, caches de lignes et cles en memoire. JVM heap typiquement configure entre 8 et 32 Go.",
                "concurrency_model": "Architecture thread-per-core avec SEDA (Staged Event-Driven Architecture). Les operations sont decomposees en etapes traitees par des pools de threads specialises."
            },
            "learning_curve": (
                "La courbe d'apprentissage de Cassandra est raide. CQL ressemble\n"
                "a SQL mais la modelisation des donnees est fondamentalement\n"
                "differente : il faut penser aux requetes avant de designer le\n"
                "schema. Les concepts de partition key, clustering key,\n"
                "consistance configurable et compaction necessitent une\n"
                "comprehension approfondie. L'administration d'un cluster\n"
                "de production est un metier en soi."
            ),
            "community_size": "Communaute Apache active. Conferences annuelles (Cassandra Summit). Les contributeurs incluent des ingenieurs d'Apple, Netflix et DataStax.",
            "job_market": "Demande specialisee mais bien remuneree. Les postes de DBA Cassandra ou d'ingenieur Big Data mentionnant Cassandra offrent des salaires superieurs a la moyenne."
        },
        "traits": {
            "performance": 8,
            "developer_speed": 4,
            "learning_curve": 7,
            "ecosystem_size": 5,
            "type_safety": 5,
            "concurrency": 9,
            "memory_safety": 7,
            "scalability": 10
        }
    }
}
