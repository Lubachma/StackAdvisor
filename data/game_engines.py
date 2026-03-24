"""
Module de donnees pour le Stack Advisor CLI.
Contient les informations detaillees sur 3 moteurs de jeu video.
Toutes les descriptions sont en francais.
"""

TECHNOLOGIES = {
    # =========================================================================
    # 1. Unity
    # =========================================================================
    "unity": {
        "name": "Unity",
        "category": "game_engine",
        "year_created": 2005,
        "creator": "Unity Technologies",
        "paradigm": ["Composant", "Oriente Objet", "Evenementiel"],
        "typing": "C# (typage statique fort)",
        "sections": {
            "overview": (
                "Unity est un moteur de jeu video multiplateforme cree en 2005 par Unity "
                "Technologies, une entreprise fondee a Copenhague au Danemark par David Helgason, "
                "Joachim Ante et Nicholas Francis. A l'origine concu comme un moteur exclusif "
                "a macOS, Unity s'est rapidement impose comme l'un des moteurs de jeu les plus "
                "populaires et les plus accessibles au monde, democratisant la creation de jeux "
                "video en abaissant considerablement la barriere d'entree technique et financiere. "
                "La philosophie fondamentale de Unity repose sur le principe de 'democratisation "
                "du developpement' : rendre la creation de contenu interactif 3D et 2D accessible "
                "au plus grand nombre, des studios independants aux grandes entreprises. Le moteur "
                "utilise le langage C# comme langage de script principal, offrant un excellent "
                "compromis entre performances, securite du typage et productivite du developpeur. "
                "Unity se distingue par sa capacite a deployer sur plus de 25 plateformes "
                "differentes a partir d'une seule base de code, incluant PC, consoles (PlayStation, "
                "Xbox, Nintendo Switch), appareils mobiles (iOS, Android), navigateurs web (WebGL), "
                "et casques de realite virtuelle et augmentee (Meta Quest, HoloLens, Vision Pro). "
                "Cette polyvalence en fait le moteur le plus utilise au monde en termes de nombre "
                "de projets, representant environ 50% des jeux mobiles et une part significative "
                "des experiences de realite virtuelle. Au-dela du jeu video, Unity est de plus "
                "en plus utilise dans l'industrie automobile, l'architecture, le cinema "
                "(previsualization), la formation medicale, et la simulation industrielle, "
                "temoignant de la maturite et de la polyvalence de son ecosysteme technique."
            ),
            "history": (
                "L'histoire de Unity commence en 2004 dans un sous-sol a Copenhague, ou trois "
                "developpeurs danois — David Helgason, Joachim Ante et Nicholas Francis — "
                "travaillent sur un moteur de jeu initialement appele 'Over the Edge Entertainment'. "
                "La premiere version publique, Unity 1.0, est lancee en juin 2005 exclusivement "
                "pour macOS, une decision strategique inhabituelle a l'epoque ou Windows dominait "
                "le marche du jeu video. En 2007, Unity s'ouvre a la plateforme Windows et commence "
                "a attirer l'attention des developpeurs independants. L'annee 2008 marque un tournant "
                "majeur avec le lancement du support iPhone, positionant Unity comme un acteur "
                "incontournable du marche naissant des jeux mobiles. Unity 3.0 (2010) introduit "
                "le support d'Android, du navigateur web via un plugin, et ameliore considerablement "
                "le pipeline de rendu avec l'ajout de l'eclairage differe (deferred rendering). "
                "Unity 4.0 (2012) apporte le support de DirectX 11, le systeme d'animation Mecanim, "
                "et l'integration de la physique tissu (cloth physics). L'annee 2014 est decisive : "
                "Unity 5.0 revolutionne le modele economique en rendant le moteur gratuit pour les "
                "petits studios (revenus inferieurs a 100 000 dollars), une decision qui accelere "
                "massivement l'adoption. Unity 5 introduit egalement le Global Illumination en temps "
                "reel base sur Enlighten, le Physically Based Rendering (PBR), et un systeme audio "
                "completement revu. En 2017, Unity adopte un systeme de versionnage base sur l'annee "
                "(Unity 2017.x) et commence le developpement du Scriptable Render Pipeline (SRP), "
                "permettant aux developpeurs de personnaliser le pipeline de rendu. Unity 2018 "
                "introduit le Lightweight Render Pipeline (LWRP, devenu URP) et le High Definition "
                "Render Pipeline (HDRP), ainsi que le debut du Entity Component System (ECS) avec "
                "le package DOTS. Unity 2019 et 2020 poursuivent la maturation de ces systemes. "
                "En 2021, Unity Technologies entre en bourse (NYSE : U), valorisant l'entreprise "
                "a plusieurs milliards de dollars. Unity 2022 et les versions LTS subsequentes "
                "continuent d'ameliorer les performances avec DOTS, le rendu graphique avec URP "
                "et HDRP, et l'integration de services cloud. En 2023, une controverse eclate "
                "autour de la tentative d'introduction du 'Runtime Fee', un modele de tarification "
                "base sur le nombre d'installations, provoquant une revolte de la communaute et "
                "conduisant a un retrait partiel de cette politique."
            ),
            "architecture": (
                "L'architecture de Unity repose sur un modele de composition par composants "
                "(Component-Based Architecture) qui est au coeur de sa conception. Chaque element "
                "du jeu est un GameObject, un conteneur generique auquel on attache des composants "
                "(Components) qui definissent son comportement et ses proprietes. Par exemple, un "
                "personnage jouable serait un GameObject avec un composant Transform (position, "
                "rotation, echelle), un MeshRenderer (rendu visuel), un Rigidbody (physique), un "
                "Collider (detection de collision), un Animator (animations), et un ou plusieurs "
                "scripts C# personnalises (logique de jeu). Cette architecture favorise la "
                "reutilisabilite et la flexibilite par rapport a l'heritage classique oriente objet. "
                "Le pipeline de rendu de Unity est hautement configurable. Le Built-in Render Pipeline "
                "historique offre un rendu forward ou deferred. Le Universal Render Pipeline (URP), "
                "anciennement LWRP, est optimise pour un large spectre de plateformes, du mobile "
                "au PC, avec un bon equilibre entre qualite visuelle et performances. Le High "
                "Definition Render Pipeline (HDRP) cible les plateformes haut de gamme (PC et "
                "consoles) avec des fonctionnalites avancees comme le ray tracing en temps reel, "
                "le Screen Space Global Illumination (SSGI), les volumes de brouillard volumetrique, "
                "et les materiaux complexes (subsurface scattering, transluminescence). Le systeme "
                "de physique repose sur NVIDIA PhysX pour la physique 3D, offrant des collisions, "
                "des corps rigides, des articulations (joints) et des ragdolls. Pour la physique "
                "2D, Unity utilise Box2D. Le systeme de script est base sur Mono (implementation "
                "open source du .NET Framework) et, pour les builds finaux, sur le compilateur "
                "IL2CPP qui convertit le bytecode C# en code C++ natif, offrant des performances "
                "significativement ameliorees. Le Data-Oriented Technology Stack (DOTS) introduit "
                "un paradigme alternatif base sur l'Entity Component System (ECS) et le Job System "
                "pour exploiter pleinement les processeurs multi-coeurs. Le Burst Compiler genere "
                "du code SIMD hautement optimise a partir du C# avec le sous-ensemble HPC#. Le "
                "systeme d'assets de Unity gere l'importation, la conversion et la serialisation "
                "de tous les types de ressources (textures, modeles 3D, sons, animations, shaders) "
                "dans un format interne optimise. L'Addressable Asset System permet le chargement "
                "asynchrone et la gestion de bundles d'assets pour optimiser l'utilisation memoire."
            ),
            "pros_cons": {
                "pros": [
                    "Deploiement multiplateforme inegale : plus de 25 plateformes depuis une seule base de code",
                    "Courbe d'apprentissage relativement douce grace au C# et a l'editeur intuitif",
                    "Asset Store extremement riche avec des milliers de plugins, assets et outils",
                    "Communaute massive et abondance de tutoriels, cours et documentation en ligne",
                    "Excellent pour le developpement 2D et 3D, avec des outils dedies pour chaque cas",
                    "Support natif de la realite virtuelle et augmentee tres mature (Meta Quest, HoloLens, Vision Pro)",
                    "Gratuit pour les petits studios (revenus < 200 000 dollars), abaissant la barriere d'entree",
                    "DOTS/ECS permet des performances proches du natif pour les projets exigeants"
                ],
                "cons": [
                    "Performances graphiques inferieures a Unreal Engine pour les projets AAA haut de gamme",
                    "Le rendu par defaut necessite un travail consequent pour atteindre une qualite visuelle realiste",
                    "La dette technique accumulee rend certaines API inconsistantes entre anciens et nouveaux systemes",
                    "Le modele de licence et les politiques tarifaires ont subi des changements controverses (Runtime Fee 2023)",
                    "Les projets volumineux peuvent souffrir de longs temps de compilation et d'importation d'assets",
                    "DOTS/ECS reste complexe a maitriser et n'est pas encore pleinement integre a toutes les fonctionnalites",
                    "La gestion du multijoueur natif (Netcode for GameObjects) est encore moins mature que les solutions concurrentes",
                    "Les performances sur mobile peuvent necessiter une optimisation manuelle considerable"
                ]
            },
            "use_cases": (
                "Unity est le moteur de predilection pour une gamme extremement large de projets. "
                "Dans le domaine du jeu video mobile, Unity domine le marche avec environ 50% des "
                "jeux sur iOS et Android, grace a son deploiement multiplateforme et ses outils "
                "d'optimisation mobile (adaptive performance, asset bundles). Des jeux a succes "
                "comme Pokemon GO, Monument Valley, Genshin Impact (version mobile), et Among Us "
                "ont ete developpes avec Unity. Pour les jeux independants en 2D, le systeme "
                "Tilemap, le Sprite Editor, le systeme d'animation 2D et le 2D Renderer offrent "
                "un workflow complet et efficace. Des titres acclames comme Hollow Knight, Cuphead, "
                "et Ori and the Blind Forest utilisent Unity. En 3D, Unity est utilise pour des jeux "
                "allant de l'indie a des productions de taille moyenne comme Escape from Tarkov, "
                "Rust, Cities: Skylines, et Hearthstone. La realite virtuelle est un domaine ou "
                "Unity excelle particulierement : Beat Saber, le jeu VR le plus vendu de tous les "
                "temps, est developpe avec Unity. Le moteur supporte nativement les SDK Meta Quest, "
                "SteamVR, OpenXR, et les casques de realite mixte comme le HoloLens et le Vision "
                "Pro d'Apple. En dehors du jeu video, Unity est de plus en plus utilise dans "
                "l'industrie automobile pour la visualisation de vehicules en temps reel, dans "
                "l'architecture et le BTP pour les visites virtuelles, dans la formation medicale "
                "pour les simulations chirurgicales, dans le cinema pour la previsualisation de "
                "scenes, et dans la defense pour les simulateurs d'entrainement. Unity Reflect "
                "permet d'importer des modeles BIM et CAD pour des applications de visualisation "
                "architecturale. Le secteur de la publicite interactive et des configurateurs "
                "produit 3D en ligne (WebGL) utilise egalement beaucoup Unity."
            ),
            "ecosystem": (
                "L'ecosysteme de Unity est l'un des plus vastes et des plus actifs du domaine "
                "des moteurs de jeu. L'Asset Store, lancee en 2010, est la marketplace officielle "
                "qui propose des dizaines de milliers d'assets, plugins, outils et extensions "
                "crees par la communaute et des editeurs tiers. On y trouve des modeles 3D, des "
                "textures, des systemes audio, des shaders, des frameworks de gameplay complets, "
                "des solutions de multijoueur, et des outils d'IA. Parmi les plugins les plus "
                "populaires, citons : DOTween (animation procedurale), TextMeshPro (rendu de texte "
                "avance, desormais integre), Cinemachine (camera cinematique, integre), ProBuilder "
                "(modelisation dans l'editeur, integre), Shader Graph (creation visuelle de shaders), "
                "Visual Effect Graph (effets de particules avances), et Addressables (gestion "
                "d'assets). Pour le multijoueur, Unity propose Netcode for GameObjects et Netcode "
                "for Entities, tandis que des solutions tierces comme Photon (PUN/Fusion), Mirror, "
                "et Fish-Networking sont tres utilisees. Le Package Manager permet d'installer et "
                "de gerer des packages officiels Unity et des packages provenant de registres "
                "custom ou Git. Pour le controle de version, Unity propose Plastic SCM (integre) "
                "et supporte Git avec le plugin Git LFS pour les fichiers binaires. Les IDE "
                "recommandes sont Visual Studio, Visual Studio Code et JetBrains Rider, ce dernier "
                "etant considere comme le meilleur IDE pour le developpement Unity grace a son "
                "integration poussee. Unity Cloud Services propose des services en ligne : "
                "Unity Analytics (telemetrie), Unity Ads (monetisation publicitaire), Unity IAP "
                "(achats in-app), Unity Cloud Build (CI/CD), et Unity Gaming Services (UGS) "
                "qui regroupe des services comme Relay, Lobby, Matchmaker et Cloud Save. La "
                "documentation officielle est tres complete et regulierement mise a jour, "
                "accompagnee de tutoriels officiels, de projets exemples (Starter Assets, FPS "
                "Microgame, Karting Microgame) et de cours via Unity Learn."
            ),
            "companies": [
                "Niantic (Pokemon GO, Ingress, Peridot)",
                "Innersloth (Among Us)",
                "Team Cherry (Hollow Knight, Hollow Knight: Silksong)",
                "Battlestate Games (Escape from Tarkov)",
                "Colossal Order (Cities: Skylines, Cities: Skylines II)",
                "Beat Games (Beat Saber)",
                "Facepunch Studios (Rust, Garry's Mod successeur)",
                "Blizzard Entertainment (Hearthstone)"
            ],
            "code_example": (
                "using UnityEngine;\n\n"
                "/// <summary>\n"
                "/// Controleur de personnage jouable en 3D.\n"
                "/// Gere le deplacement, le saut et la detection du sol.\n"
                "/// </summary>\n"
                "public class PlayerController : MonoBehaviour\n"
                "{\n"
                "    [Header(\"Parametres de deplacement\")]\n"
                "    [SerializeField] private float vitesseDeplacement = 6f;\n"
                "    [SerializeField] private float forceSaut = 8f;\n"
                "    [SerializeField] private float gravite = -20f;\n\n"
                "    [Header(\"Detection du sol\")]\n"
                "    [SerializeField] private Transform pointDeSol;\n"
                "    [SerializeField] private float rayonDetection = 0.3f;\n"
                "    [SerializeField] private LayerMask masqueSol;\n\n"
                "    private CharacterController controleur;\n"
                "    private Vector3 velocite;\n"
                "    private bool estAuSol;\n\n"
                "    private void Awake()\n"
                "    {\n"
                "        controleur = GetComponent<CharacterController>();\n"
                "    }\n\n"
                "    private void Update()\n"
                "    {\n"
                "        // Detection du sol par sphere de collision\n"
                "        estAuSol = Physics.CheckSphere(\n"
                "            pointDeSol.position, rayonDetection, masqueSol);\n\n"
                "        if (estAuSol && velocite.y < 0f)\n"
                "            velocite.y = -2f;\n\n"
                "        // Lecture des entrees horizontales et verticales\n"
                "        float h = Input.GetAxis(\"Horizontal\");\n"
                "        float v = Input.GetAxis(\"Vertical\");\n\n"
                "        // Deplacement relatif a l'orientation du personnage\n"
                "        Vector3 direction = transform.right * h + transform.forward * v;\n"
                "        controleur.Move(direction * vitesseDeplacement * Time.deltaTime);\n\n"
                "        // Saut\n"
                "        if (Input.GetButtonDown(\"Jump\") && estAuSol)\n"
                "            velocite.y = Mathf.Sqrt(forceSaut * -2f * gravite);\n\n"
                "        // Application de la gravite\n"
                "        velocite.y += gravite * Time.deltaTime;\n"
                "        controleur.Move(velocite * Time.deltaTime);\n"
                "    }\n"
                "}"
            ),
            "performance": {
                "startup_time": "Moyen a lent selon la taille du projet et les assets charges au demarrage",
                "throughput": "Bon avec IL2CPP, excellent avec DOTS/Burst pour les calculs intensifs",
                "memory": "Modere, le ramasse-miettes C# peut causer des pics de latence (GC spikes) necessitant une gestion attentive",
                "concurrency_model": "Job System (DOTS) pour le parallelisme, coroutines pour l'asynchrone, C# async/await supporte"
            },
            "learning_curve": "Moderee (le C# et l'editeur sont accessibles, mais maitriser DOTS, les pipelines de rendu et l'optimisation mobile demande du temps)",
            "community_size": "Tres grande (plus grande communaute de moteur de jeu au monde, forums actifs, Discord officiel, subreddit r/Unity3D)",
            "job_market": "Tres fort (jeu mobile, VR/AR, simulations industrielles, fort en freelance et startups, nombreuses offres en France et a l'international)"
        },
        "traits": {
            "performance": 7,
            "developer_speed": 8,
            "learning_curve": 5,
            "ecosystem_size": 9,
            "type_safety": 8,
            "concurrency": 6,
            "memory_safety": 7,
            "scalability": 7
        }
    },

    # =========================================================================
    # 2. Unreal Engine
    # =========================================================================
    "unreal": {
        "name": "Unreal Engine",
        "category": "game_engine",
        "year_created": 1998,
        "creator": "Epic Games",
        "paradigm": ["Composant", "Oriente Objet", "Blueprint Visual Scripting"],
        "typing": "C++ (typage statique fort) + Blueprints",
        "sections": {
            "overview": (
                "Unreal Engine est un moteur de jeu video de classe mondiale developpe par Epic "
                "Games, largement considere comme la reference en matiere de rendu graphique haut "
                "de gamme et de production de jeux AAA. Cree a l'origine par Tim Sweeney pour "
                "le jeu Unreal (1998), le moteur a evolue sur plus de vingt-cinq ans pour devenir "
                "l'un des outils les plus puissants et les plus complets de l'industrie du jeu "
                "video et du divertissement interactif. La philosophie d'Unreal Engine repose sur "
                "l'excellence graphique, la performance maximale et la capacite a produire des "
                "experiences visuelles de qualite cinematographique en temps reel. Le moteur utilise "
                "le C++ comme langage de programmation principal, offrant un controle fin sur la "
                "memoire et les performances, tout en proposant Blueprints, un systeme de script "
                "visuel puissant qui permet aux designers et aux artistes de creer de la logique "
                "de jeu sans ecrire une seule ligne de code. Cette double approche — C++ pour les "
                "ingenieurs, Blueprints pour les non-programmeurs — est l'une des forces "
                "distinctives d'Unreal Engine et permet a des equipes interdisciplinaires de "
                "collaborer efficacement. Unreal Engine 5, lance en 2022, a introduit des "
                "technologies revolutionnaires comme Nanite (geometrie virtualisee permettant "
                "des milliards de polygones en temps reel), Lumen (illumination globale dynamique "
                "et reflexions en temps reel), et MetaHuman (creation de personnages humains "
                "photorealistes). Ces innovations ont repositionne Unreal Engine non seulement "
                "comme un moteur de jeu, mais comme une plateforme de creation de contenu 3D "
                "temps reel pour le cinema (production virtuelle avec LED walls), l'architecture, "
                "l'automobile, la mode, et les evenements en direct. Le modele economique d'Unreal "
                "est genereux : le moteur est entierement gratuit jusqu'a un million de dollars "
                "de revenus bruts, apres quoi une redevance de 5% s'applique."
            ),
            "history": (
                "L'histoire d'Unreal Engine est indissociable de celle d'Epic Games et de son "
                "fondateur Tim Sweeney. Sweeney, passione de programmation depuis l'adolescence, "
                "fonde Potomac Computer Systems en 1991 (renomme Epic MegaGames puis Epic Games) "
                "et commence a developper le moteur qui propulsera le jeu Unreal. La premiere "
                "version du moteur, Unreal Engine 1, est lancee en 1998 avec le jeu eponyme "
                "Unreal, un FPS qui impressionne par la qualite de ses environnements et de son "
                "eclairage, rivalisant directement avec le moteur id Tech de John Carmack. Le "
                "moteur est rapidement licencie a d'autres studios, etablissant le modele "
                "commercial de licence de moteur. Unreal Engine 2 (2002) accompagne Unreal "
                "Tournament 2003 et America's Army, introduisant un systeme de rendu ameliore "
                "et le langage de script UnrealScript. Unreal Engine 3 (2006) marque un tournant "
                "majeur dans l'industrie : lance avec Gears of War, il introduit le rendu "
                "programmable avec des shaders avances, Kismet (un systeme de script visuel "
                "precurseur des Blueprints), et un editeur de materiaux visuel. UE3 devient le "
                "moteur dominant de la generation PlayStation 3 / Xbox 360, propulsant des "
                "centaines de jeux dont Mass Effect, BioShock, Batman: Arkham, et Borderlands. "
                "Unreal Engine 4 est annonce en 2012 et lance en mars 2014 avec un nouveau modele "
                "economique revolutionnaire : un abonnement de 19 dollars par mois avec acces "
                "complet au code source. En 2015, UE4 devient totalement gratuit avec une "
                "redevance de 5% apres le premier million de dollars. UE4 remplace UnrealScript "
                "par le C++ natif et les Blueprints, introduit le Physically Based Rendering, "
                "et offre un acces complet au code source via GitHub. UE4 propulse des titres "
                "majeurs comme Fortnite (qui deviendra le jeu le plus rentable d'Epic), Final "
                "Fantasy VII Remake, Star Wars Jedi: Fallen Order, et Hellblade: Senua's Sacrifice. "
                "Unreal Engine 5 est annonce en mai 2020 avec une demo technique spectaculaire "
                "(Lumen in the Land of Nanite) et lance officiellement en avril 2022. UE5 "
                "introduit Nanite (geometrie virtualisee), Lumen (illumination globale dynamique), "
                "Virtual Shadow Maps, World Partition (streaming de mondes ouverts), et MetaHuman. "
                "UE5 propulse des titres comme Fortnite Chapter 4+, The Matrix Awakens (demo), "
                "Senua's Saga: Hellblade II, et Black Myth: Wukong. En 2023, le modele economique "
                "evolue : Unreal est gratuit jusqu'a un million de dollars de revenus."
            ),
            "architecture": (
                "L'architecture d'Unreal Engine est un systeme massif et hautement optimise, "
                "ecrit principalement en C++ avec environ 30 millions de lignes de code source "
                "accessibles aux developpeurs. Le coeur du moteur repose sur un systeme d'acteurs "
                "(Actors) et de composants (Components). Un Actor est toute entite pouvant etre "
                "placee dans un niveau : personnages, cameras, lumieres, declencheurs. Chaque "
                "Actor contient des Components qui definissent ses capacites : StaticMeshComponent "
                "(rendu d'un modele 3D), SkeletalMeshComponent (modele anime), CapsuleComponent "
                "(collision), CharacterMovementComponent (deplacement), et des composants "
                "personnalises. Le systeme de gameplay repose sur la hierarchie Pawn (entite "
                "controlable) > Character (pawn humanoide avec mouvement) > PlayerController "
                "(logique du joueur) > GameMode (regles du jeu). Le pipeline de rendu d'UE5 est "
                "l'un des plus avances de l'industrie. Nanite est un systeme de geometrie "
                "virtualisee qui decoupe les meshes en clusters hierarchiques et effectue un "
                "culling (elimination) au niveau du cluster et du triangle, permettant de rendre "
                "des scenes avec des milliards de polygones source a un cout fixe. Lumen est un "
                "systeme d'illumination globale entierement dynamique qui combine le ray tracing "
                "logiciel (software ray tracing sur les Signed Distance Fields et les cartes de "
                "surface) avec le ray tracing materiel optionnel pour produire des reflexions et "
                "un eclairage indirect en temps reel sans precalcul de lightmaps. Le systeme de "
                "physique repose sur Chaos, le moteur physique interne d'Epic qui a remplace "
                "PhysX, offrant des destructions en temps reel, des simulations de corps rigides "
                "et souples, et des vehicules. Le systeme de Blueprints est un langage de "
                "programmation visuel complet base sur des noeuds connectes par des fils. Il "
                "permet de creer de la logique de gameplay, des interfaces utilisateur, des "
                "animations, et meme des shaders (Material Editor) sans ecrire de C++. Les "
                "Blueprints sont compiles en bytecode puis en code natif (nativization), offrant "
                "des performances proches du C++ pur. Le World Partition d'UE5 divise le monde "
                "en grilles chargees dynamiquement, permettant la creation de mondes ouverts "
                "massifs sans loading screens. Le systeme de materiaux base sur des noeuds offre "
                "des capacites PBR avancees avec support du Substrate (anciennement Strata), un "
                "nouveau modele de materiaux multi-couches. Le systeme Niagara gere les effets "
                "visuels de particules avec des simulations GPU et des champs de forces complexes."
            ),
            "pros_cons": {
                "pros": [
                    "Rendu graphique de classe mondiale, le meilleur de l'industrie pour les projets photoralistes",
                    "Nanite et Lumen revolutionnent la gestion de la geometrie et de l'eclairage en temps reel",
                    "Blueprints permettent aux non-programmeurs de creer de la logique de jeu complexe",
                    "Code source complet accessible gratuitement via GitHub, permettant toute modification",
                    "Gratuit jusqu'a un million de dollars de revenus, tres genereux pour les independants",
                    "Pipeline de production virtuelle (LED walls) adopte par Hollywood (The Mandalorian, Westworld)",
                    "MetaHuman permet la creation rapide de personnages humains photorealistes",
                    "World Partition et streaming natif pour les mondes ouverts de grande envergure"
                ],
                "cons": [
                    "Courbe d'apprentissage tres raide, specialement pour le C++ avec les macros UE (UPROPERTY, UFUNCTION, UCLASS)",
                    "Temps de compilation C++ extremement longs sur les gros projets (plusieurs minutes pour un rebuild complet)",
                    "Consommation de ressources machine elevee : l'editeur necessite un PC puissant avec beaucoup de RAM",
                    "La taille des builds finaux est generalement plus importante que celle des concurrents",
                    "Le developpement 2D pur est possible mais nettement moins adapte et outille que Unity ou Godot",
                    "La complexite du moteur et de son architecture rend le debogage parfois ardu",
                    "Les mises a jour majeures du moteur peuvent casser la compatibilite avec les projets existants",
                    "La documentation, bien que vaste, est parfois lacunaire ou obsolete sur certains systemes avances"
                ]
            },
            "use_cases": (
                "Unreal Engine est le moteur de reference pour les productions AAA a gros budget. "
                "Des franchises majeures comme Fortnite (Epic Games), Final Fantasy VII Remake et "
                "Final Fantasy VII Rebirth (Square Enix), Star Wars Jedi (Respawn/EA), Senua's "
                "Saga: Hellblade II (Ninja Theory/Xbox), Black Myth: Wukong (Game Science), et "
                "Kingdom Hearts (Square Enix) utilisent Unreal Engine. Le moteur excelle "
                "particulierement dans les jeux d'action-aventure en troisieme personne, les "
                "FPS, les jeux monde ouvert, et tout projet ou la qualite visuelle est un facteur "
                "differentiant. Pour les jeux multijoueur, le framework reseau d'Unreal (Replication "
                "System) est mature et eprouve, ayant ete perfectionne avec Fortnite pour gerer "
                "des centaines de joueurs simultanes. Au-dela du jeu video, Unreal Engine connait "
                "une adoption massive dans la production virtuelle pour le cinema et la television : "
                "les LED walls alimentes par Unreal permettent de projeter des environnements 3D "
                "en temps reel derriere les acteurs, remplacant les fonds verts traditionnels. "
                "Des productions comme The Mandalorian, Westworld, et de nombreuses publicites "
                "haut de gamme utilisent cette technologie. L'industrie automobile utilise Unreal "
                "pour la visualisation de vehicules en temps reel, les configurateurs interactifs "
                "et les experiences de showroom virtuel (BMW, McLaren, Volvo). L'architecture et "
                "l'immobilier utilisent Unreal pour des visualisations architecturales realistes "
                "et des visites virtuelles de batiments en cours de construction. La formation "
                "et la simulation, notamment dans les domaines militaire et aeronautique, "
                "exploitent les capacites de rendu realiste et de physique d'Unreal. Le broadcast "
                "en direct et l'esport utilisent Unreal pour des graphiques en temps reel et "
                "des replays cinematiques."
            ),
            "ecosystem": (
                "L'ecosysteme d'Unreal Engine est riche et professionnel, cible vers les equipes "
                "de production serieuses. Le Marketplace officiel propose des milliers d'assets, "
                "plugins et outils, avec une curassion stricte et un programme mensuel d'assets "
                "gratuits. Fab (anciennement Quixel Bridge) donne acces a la Megascans Library, "
                "une bibliotheque de milliers d'assets photogrammetriques haute resolution "
                "(roches, surfaces, plantes, decors urbains) entierement gratuits pour une "
                "utilisation avec Unreal Engine. MetaHuman Creator est un outil cloud gratuit "
                "pour creer des personnages humains photorealistes directement importables dans "
                "UE. Le code source complet du moteur est accessible via GitHub pour les "
                "utilisateurs enregistres, permettant de modifier, deboguer et etendre n'importe "
                "quelle partie du moteur. Le systeme de plugins permet d'etendre les capacites "
                "du moteur et de l'editeur. Les solutions de multijoueur incluent le systeme "
                "de replication integre, EOS (Epic Online Services) pour le matchmaking, le "
                "voice chat et les amis cross-platform, et des solutions tierces comme Gamelift "
                "(AWS). Pour la CI/CD, UnrealBuildTool et UnrealAutomationTool permettent de "
                "scripter les builds et les deploiements. Les IDE recommandes sont Visual Studio "
                "(Windows, avec le plugin UnrealVS) et Rider (multiplateforme, excellent support "
                "UE). Le Live Coding permet de recompiler et d'injecter du code C++ pendant que "
                "l'editeur tourne, accelerant l'iteration. Le systeme de controle de version "
                "recommande est Perforce (standard de l'industrie pour les gros projets), bien "
                "que Git avec LFS soit egalement supporte. La documentation officielle est "
                "hebergee sur docs.unrealengine.com, accompagnee de tutoriels video officiels "
                "sur la chaine YouTube Unreal Engine et de cours gratuits sur la plateforme "
                "Unreal Online Learning. Les forums officiels, le Discord, et le subreddit "
                "r/unrealengine sont des ressources communautaires actives. Epic organise "
                "annuellement Unreal Fest et le State of Unreal a la GDC."
            ),
            "companies": [
                "Epic Games (Fortnite, Unreal Tournament, Gears of War)",
                "Square Enix (Final Fantasy VII Remake/Rebirth, Kingdom Hearts IV)",
                "CD Projekt Red (The Witcher 4 — transition vers UE5)",
                "Crystal Dynamics (Tomb Raider — prochaine generation sur UE5)",
                "Ninja Theory / Xbox Game Studios (Hellblade: Senua's Saga)",
                "Game Science (Black Myth: Wukong)",
                "The Coalition (Gears of War series)",
                "Respawn Entertainment / EA (Star Wars Jedi: Survivor)"
            ],
            "code_example": (
                "// Fichier : APersonnageJouable.h\n"
                "#pragma once\n"
                "#include \"CoreMinimal.h\"\n"
                "#include \"GameFramework/Character.h\"\n"
                "#include \"PersonnageJouable.generated.h\"\n\n"
                "/**\n"
                " * Personnage jouable avec deplacement et saut.\n"
                " * Exemple de classe C++ Unreal Engine.\n"
                " */\n"
                "UCLASS()\n"
                "class MONJEU_API APersonnageJouable : public ACharacter\n"
                "{\n"
                "    GENERATED_BODY()\n\n"
                "public:\n"
                "    APersonnageJouable();\n\n"
                "protected:\n"
                "    virtual void BeginPlay() override;\n"
                "    virtual void Tick(float DeltaTime) override;\n"
                "    virtual void SetupPlayerInputComponent(\n"
                "        class UInputComponent* PlayerInputComponent) override;\n\n"
                "    /** Vitesse de deplacement du personnage. */\n"
                "    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = \"Deplacement\")\n"
                "    float VitesseDeplacement = 600.f;\n\n"
                "    /** Force du saut. */\n"
                "    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = \"Deplacement\")\n"
                "    float ForceSaut = 420.f;\n\n"
                "    /** Points de vie du personnage. */\n"
                "    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = \"Stats\")\n"
                "    float PointsDeVie = 100.f;\n\n"
                "private:\n"
                "    void Avancer(float Valeur);\n"
                "    void AllerADroite(float Valeur);\n"
                "    void Sauter();\n"
                "};\n\n"
                "// Fichier : APersonnageJouable.cpp\n"
                "#include \"PersonnageJouable.h\"\n"
                "#include \"GameFramework/CharacterMovementComponent.h\"\n\n"
                "APersonnageJouable::APersonnageJouable()\n"
                "{\n"
                "    PrimaryActorTick.bCanEverTick = true;\n"
                "    GetCharacterMovement()->MaxWalkSpeed = VitesseDeplacement;\n"
                "    GetCharacterMovement()->JumpZVelocity = ForceSaut;\n"
                "}\n\n"
                "void APersonnageJouable::SetupPlayerInputComponent(\n"
                "    UInputComponent* PlayerInputComponent)\n"
                "{\n"
                "    Super::SetupPlayerInputComponent(PlayerInputComponent);\n"
                "    PlayerInputComponent->BindAxis(\"Avancer\", this,\n"
                "        &APersonnageJouable::Avancer);\n"
                "    PlayerInputComponent->BindAxis(\"AllerADroite\", this,\n"
                "        &APersonnageJouable::AllerADroite);\n"
                "    PlayerInputComponent->BindAction(\"Sauter\", IE_Pressed,\n"
                "        this, &APersonnageJouable::Sauter);\n"
                "}\n\n"
                "void APersonnageJouable::Avancer(float Valeur)\n"
                "{\n"
                "    if (Valeur != 0.f)\n"
                "    {\n"
                "        FVector Direction = GetActorForwardVector();\n"
                "        AddMovementInput(Direction, Valeur);\n"
                "    }\n"
                "}\n\n"
                "void APersonnageJouable::Sauter()\n"
                "{\n"
                "    Jump();\n"
                "}"
            ),
            "performance": {
                "startup_time": "Lent (l'editeur est gourmand en ressources, les temps de chargement de projets volumineux sont significatifs)",
                "throughput": "Excellent, l'un des meilleurs de l'industrie grace au C++ natif et aux optimisations agressives du moteur",
                "memory": "Eleve (le moteur consomme beaucoup de memoire, mais offre un controle fin via le C++ et le systeme d'allocation custom)",
                "concurrency_model": "TaskGraph pour le parallelisme interne, systeme de threads du moteur, async loading, Replication System pour le reseau"
            },
            "learning_curve": "Tres elevee (le C++ avec les macros UE, l'architecture complexe du moteur, et la quantite de systemes a maitriser rendent l'apprentissage long, meme si les Blueprints facilitent l'acces initial)",
            "community_size": "Grande (communaute professionnelle et passionnee, forums officiels actifs, Discord, subreddit, evenements Unreal Fest, forte presence dans l'industrie AAA)",
            "job_market": "Tres fort pour les postes AAA et les grandes productions (studios de jeu majeurs, cinema, automobile, architecture), salaires generalement plus eleves que pour Unity en raison de la rarete des profils C++/UE"
        },
        "traits": {
            "performance": 10,
            "developer_speed": 5,
            "learning_curve": 8,
            "ecosystem_size": 8,
            "type_safety": 7,
            "concurrency": 7,
            "memory_safety": 4,
            "scalability": 9
        }
    },

    # =========================================================================
    # 3. Godot Engine
    # =========================================================================
    "godot": {
        "name": "Godot Engine",
        "category": "game_engine",
        "year_created": 2014,
        "creator": "Juan Linietsky & Ariel Manzur",
        "paradigm": ["Scene/Node", "Oriente Objet", "Evenementiel"],
        "typing": "GDScript (dynamique) / C# / C++",
        "sections": {
            "overview": (
                "Godot Engine est un moteur de jeu video open source et entierement gratuit, "
                "developpe initialement par les developpeurs argentins Juan Linietsky et Ariel "
                "Manzur. Lance publiquement en 2014 et place sous licence MIT, Godot se distingue "
                "fondamentalement de ses concurrents par sa nature completement libre : aucun "
                "frais de licence, aucune redevance sur les revenus, aucune restriction d'usage, "
                "et un code source entierement ouvert et modifiable. La philosophie de Godot repose "
                "sur trois piliers : la liberte totale de l'utilisateur, la simplicite de "
                "l'architecture, et l'accessibilite pour les debutants tout en offrant une "
                "profondeur suffisante pour les projets ambitieux. Le moteur propose une "
                "architecture unique basee sur un systeme de scenes et de noeuds (Scene/Node) "
                "qui permet de decomposer un jeu en arbres de noeuds reutilisables et composables, "
                "offrant une elegance conceptuelle que beaucoup de developpeurs trouvent plus "
                "intuitive que le modele GameObject/Component de Unity. Godot propose son propre "
                "langage de script, GDScript, un langage dynamique inspire de Python concu "
                "specifiquement pour le developpement de jeux, qui s'integre parfaitement avec "
                "l'editeur et offre une productivite de developpement remarquable. En complement, "
                "Godot supporte le C# (via .NET), le C++ (via GDExtension), et theoriquement "
                "tout langage via des bindings communautaires (Rust, Swift, Kotlin). Le moteur "
                "est leger : l'editeur complet pese environ 40 Mo, se lance en quelques secondes, "
                "et fonctionne sur des machines modestes. Godot a connu une croissance explosive "
                "de sa communaute, notamment apres les controverses de licence de Unity en 2023, "
                "attirant un afflux massif de developpeurs a la recherche d'une alternative libre "
                "et perenne. Bien que Godot soit historiquement plus adapte aux jeux 2D et aux "
                "projets de petite a moyenne envergure, Godot 4.x a considerablement ameliore "
                "ses capacites 3D avec un nouveau moteur de rendu base sur Vulkan, positionnant "
                "le moteur comme un concurrent de plus en plus serieux face a Unity et Unreal "
                "pour certains types de projets."
            ),
            "history": (
                "L'histoire de Godot commence en 2001, lorsque Juan Linietsky et Ariel Manzur, "
                "deux developpeurs argentins, commencent a developper un moteur de jeu interne "
                "pour des clients de leur societe de conseil en Amerique latine. Pendant plus "
                "d'une decennie, le moteur evolue en interne, utilise pour divers projets "
                "commerciaux sans etre public. En janvier 2014, Linietsky et Manzur prennent "
                "la decision historique de publier le moteur sous licence MIT sur GitHub, le "
                "rendant entierement gratuit et open source. Le nom 'Godot' est un hommage a "
                "la piece de theatre 'En attendant Godot' de Samuel Beckett, symbolisant "
                "l'attente prolongee avant la publication du moteur. La premiere version publique, "
                "Godot 1.0, est lancee en decembre 2014. Malgre des fonctionnalites limitees par "
                "rapport a la concurrence, le moteur attire l'attention par sa legerete, sa "
                "simplicite et sa licence permissive. Godot 2.0 (2016) apporte un editeur visuel "
                "completement reecrit, un nouveau systeme de physique 2D et 3D, et ameliore "
                "significativement la documentation. C'est avec Godot 3.0 (janvier 2018) que le "
                "moteur fait un bond qualitatif majeur : introduction d'un nouveau moteur de rendu "
                "3D base sur OpenGL ES 3.0 (avec un fallback OpenGL ES 2.0), support du Physically "
                "Based Rendering, du GI (Global Illumination) precalcule, des particules GPU, du "
                "son 3D, et de GDNative (permettant d'ecrire des extensions en C, C++, Rust). "
                "Godot 3.0 introduit egalement le support du C# via Mono, ouvrant le moteur aux "
                "developpeurs issus de l'ecosysteme .NET et Unity. Les versions 3.1 a 3.5 "
                "apportent des ameliorations continues : systeme de navigation, support OpenXR "
                "pour la VR, ameliorations du rendu 2D, editeur visuel de shaders, et de "
                "nombreuses corrections. Le projet rejoint la Software Freedom Conservancy en "
                "2015 puis cree la Godot Foundation en 2022, une fondation a but non lucratif "
                "basee aux Pays-Bas pour assurer la perennite et l'independance du projet. Godot "
                "4.0, lance en mars 2023 apres des annees de developpement, est une refonte "
                "majeure : nouveau moteur de rendu base sur Vulkan (avec des backends pour les "
                "plateformes ne supportant pas Vulkan), GDScript 2.0 avec des annotations et "
                "des ameliorations syntaxiques, nouveau systeme de multiplicateur, GDExtension "
                "(remplacant GDNative), et des ameliorations massives du rendu 3D. Les versions "
                "4.1, 4.2 et 4.3 stabilisent et enrichissent ces fondations. La controverse "
                "Unity Runtime Fee de septembre 2023 provoque un afflux sans precedent de "
                "developpeurs vers Godot, faisant exploser les etoiles GitHub et les dons "
                "a la fondation."
            ),
            "architecture": (
                "L'architecture de Godot repose sur un modele de scenes et de noeuds (Scene/Node "
                "Tree) qui est unique dans l'industrie et constitue l'identite technique du moteur. "
                "Chaque element du jeu est un noeud (Node), une unite fondamentale qui possede un "
                "nom, des proprietes, et qui peut recevoir des callbacks (fonctions appelees par "
                "le moteur a chaque frame, lors d'evenements physiques, etc.). Les noeuds sont "
                "organises en arbres hierarchiques : un noeud parent peut avoir des enfants, et "
                "les transformations (position, rotation, echelle) se propagent dans la hierarchie. "
                "Une scene est un arbre de noeuds sauvegarde dans un fichier .tscn (format texte) "
                "ou .scn (format binaire), et chaque scene peut etre instanciee dans d'autres "
                "scenes, permettant une composition tres flexible. Par exemple, une scene "
                "'Ennemi' contenant un Sprite, un CollisionShape et un script peut etre instanciee "
                "des centaines de fois dans une scene 'Niveau'. Ce systeme remplace a la fois le "
                "prefab system et le component system des autres moteurs. Les types de noeuds "
                "sont hierarchises : Node (base) > Node2D (pour la 2D) > Sprite2D, "
                "CharacterBody2D, Camera2D, TileMap, etc. De meme : Node > Node3D > "
                "MeshInstance3D, CharacterBody3D, Camera3D, DirectionalLight3D, etc. Le systeme "
                "de signaux (Signals) est le mecanisme d'evenements de Godot, inspire du pattern "
                "Observer : un noeud peut emettre un signal (par exemple 'body_entered' pour une "
                "zone de collision) et d'autres noeuds peuvent s'y connecter pour reagir. Ce "
                "systeme decouple les composants et favorise une architecture propre. Le pipeline "
                "de rendu de Godot 4 est base sur Vulkan (backend RenderingDevice) avec des "
                "backends de compatibilite pour OpenGL 3.3 / OpenGL ES 3.0 pour les plateformes "
                "plus anciennes et le mobile. Le rendu supporte le forward+ rendering, le "
                "clustered lighting, les ombres en temps reel (shadow maps cascadees, omnidirectionnelles), "
                "le Screen Space Ambient Occlusion (SSAO), le Screen Space Reflections (SSR), "
                "le Global Illumination via SDFGI (Signed Distance Field Global Illumination) "
                "ou VoxelGI, et le glow/bloom. Le systeme de physique utilise GodotPhysics "
                "(moteur physique interne) pour la 2D et la 3D, offrant des corps rigides, "
                "cinematiques et statiques, des joints, et des raycasts. Jolt Physics est "
                "disponible comme extension pour ameliorer les performances physiques 3D. Le "
                "systeme de ressources (Resources) permet de definir des objets de donnees "
                "reutilisables (textures, meshes, materiaux, scripts, scenes) qui sont charges "
                "une seule fois et partages entre les noeuds, optimisant l'utilisation memoire. "
                "GDScript est un langage interprete compile en bytecode, avec un typage optionnel "
                "qui permet au compilateur d'optimiser le code type. GDExtension permet d'ecrire "
                "des modules natifs en C, C++, Rust ou tout langage compilant vers du C, avec "
                "un acces complet aux API du moteur."
            ),
            "pros_cons": {
                "pros": [
                    "Entierement gratuit et open source sous licence MIT, aucune redevance ni restriction",
                    "Editeur extremement leger (~40 Mo) qui demarre en secondes, meme sur des machines modestes",
                    "Architecture Scene/Node elegante et intuitive, facile a comprendre et a organiser",
                    "GDScript est un langage simple et productif, ideal pour le prototypage rapide et l'apprentissage",
                    "Excellent support 2D natif, souvent considere comme le meilleur de tous les moteurs de jeu",
                    "Pas de verrouillage fournisseur (vendor lock-in), liberte totale de modification et distribution",
                    "Communaute open source dynamique et en croissance explosive depuis 2023",
                    "Support de plusieurs langages (GDScript, C#, C++ via GDExtension, bindings communautaires Rust/Swift)"
                ],
                "cons": [
                    "Capacites 3D encore en retrait par rapport a Unity et surtout Unreal Engine pour les projets AAA",
                    "Ecosysteme d'assets et de plugins plus petit que ceux de Unity ou Unreal (pas de marketplace officielle comparable)",
                    "Moins de tutoriels et de ressources d'apprentissage disponibles que pour Unity, bien que la situation s'ameliore rapidement",
                    "Le marche de l'emploi pour Godot est encore limite compare a Unity et Unreal dans le milieu professionnel",
                    "GDScript, bien que pratique, n'est pas un langage transferable en dehors de Godot",
                    "Le support console (PlayStation, Xbox, Nintendo Switch) necessite des portages tiers payants (pas d'export natif)",
                    "Les performances 3D sur mobile et les plateformes a faibles ressources peuvent etre limitees",
                    "Certaines fonctionnalites avancees (multijoueur, streaming de monde) sont moins matures que chez les concurrents"
                ]
            },
            "use_cases": (
                "Godot est particulierement adapte au developpement de jeux video 2D, un domaine "
                "dans lequel il est souvent considere comme le meilleur moteur disponible. Son "
                "systeme de noeuds 2D natifs (Sprite2D, AnimatedSprite2D, TileMap, Camera2D, "
                "ParallaxBackground) est specifiquement concu pour la 2D et non une adaptation "
                "d'un moteur 3D, offrant un rendu pixel-perfect et des performances excellentes. "
                "Des jeux comme Dome Keeper, Cassette Beasts, Brotato, et Halls of Torment "
                "illustrent la capacite de Godot a produire des jeux 2D commercialement viables "
                "et acclames. Pour les jeux 3D de petite a moyenne envergure, Godot 4.x offre "
                "desormais des capacites solides avec le rendu Vulkan, le GI dynamique (SDFGI), "
                "et un systeme de materiaux PBR complet. Des projets comme The Mirror et "
                "Precipice demontrent le potentiel 3D du moteur. Godot est un choix excellent "
                "pour les game jams grace a son temps de demarrage quasi instantane, la rapidite "
                "d'iteration en GDScript, et la facilite de deploiement. Le moteur est egalement "
                "tres populaire dans l'enseignement du developpement de jeux video : sa gratuite "
                "totale, sa legerete et la simplicite de GDScript en font un outil pedagogique "
                "ideal. De nombreuses ecoles et universites l'adoptent comme moteur d'enseignement. "
                "Pour les outils et applications non-jeu, l'editeur Godot etant lui-meme construit "
                "avec le moteur, il est possible de creer des applications de bureau, des editeurs "
                "de niveaux personnalises, des outils de visualisation, et des interfaces interactives "
                "avec Godot. La realite virtuelle est supportee via OpenXR depuis Godot 4.0, "
                "permettant de developper des experiences VR pour Meta Quest et SteamVR, bien "
                "que l'ecosysteme VR soit moins mature que celui de Unity. Les jeux pour "
                "navigateur web sont un cas d'usage naturel grace a l'export HTML5/WebAssembly, "
                "permettant de publier des jeux jouables directement sur des plateformes comme "
                "itch.io sans plugin."
            ),
            "ecosystem": (
                "L'ecosysteme de Godot est plus modeste que celui d'Unity ou d'Unreal mais croit "
                "rapidement, porte par la nature open source du projet et l'enthousiasme de sa "
                "communaute. L'Asset Library officielle (asset library sur le site godotengine.org) "
                "propose des centaines d'extensions, plugins et assets gratuits crees par la "
                "communaute, directement installables depuis l'editeur. Parmi les addons les plus "
                "populaires, citons : Dialogic (systeme de dialogues), GodotSteam (integration "
                "Steamworks), Phantom Camera (camera cinematique), Terrain3D (terrain procedral), "
                "Limbo AI (arbres de comportement pour l'IA), et SmartShape2D (formes 2D "
                "procedurales). Le systeme de GDExtension permet d'ecrire des modules natifs en "
                "C++ ou Rust avec des performances natives, et des projets communautaires comme "
                "godot-rust (bindings Rust) et godot-cpp (bindings C++) facilitent cette "
                "integration. Pour le multijoueur, Godot propose un systeme de haut niveau "
                "(MultiplayerSynchronizer, MultiplayerSpawner) et un API RPC/replication integre, "
                "avec des solutions tierces comme Nakama et le support ENet et WebSocket natif. "
                "Le controle de version est facilite par le fait que les scenes .tscn et les "
                "ressources .tres sont en format texte, rendant les diffs Git lisibles et les "
                "conflits de fusion resolvables. L'editeur de shaders visuel et le langage de "
                "shading (similaire a GLSL) permettent de creer des effets visuels avances. Le "
                "systeme d'animation est integre directement dans l'editeur avec AnimationPlayer "
                "et AnimationTree, permettant d'animer pratiquement toute propriete de tout noeud "
                "sans outil externe. Pour le developpement, les IDE recommandes sont l'editeur "
                "integre de Godot (completion, debogueur, profileur) pour GDScript, et Visual "
                "Studio / Rider pour le C#. La documentation officielle est hebergee sur "
                "docs.godotengine.org, entierement libre et contribuee par la communaute, avec "
                "des tutoriels pas-a-pas allant des bases jusqu'aux sujets avances. Le subreddit "
                "r/godot, le Discord officiel (avec des dizaines de milliers de membres), et les "
                "forums communautaires sont des lieux d'entraide tres actifs. Plusieurs livres "
                "et cours en ligne (GDQuest, Heartbeast, KidsCanCode) couvrent le moteur en "
                "profondeur."
            ),
            "companies": [
                "W4 Games (fondee par des contributeurs Godot, support commercial et portage console)",
                "Bitbrain (Brotato, succes commercial majeur en 2D sur Steam)",
                "Bippinbits (Dome Keeper, roguelike minier acclame)",
                "Bytten Studio (Cassette Beasts, RPG monster-catching)",
                "Chasing Carrots (Halls of Torment, action-survival 2D)",
                "Virtual Reef (simulations ecologiques interactives)",
                "Serkantoto / Lone Developer Studios (nombreux jeux indie a succes sur itch.io et Steam)"
            ],
            "code_example": (
                "extends CharacterBody2D\n\n"
                "## Controleur de personnage 2D avec deplacement et saut.\n"
                "## Utilise le systeme de physique integre de Godot.\n\n"
                "# Constantes de deplacement\n"
                "const VITESSE_DEPLACEMENT := 300.0\n"
                "const VITESSE_SAUT := -400.0\n"
                "const GRAVITE_MULTIPLICATEUR := 2.0\n\n"
                "# Variables d'etat\n"
                "var points_de_vie: int = 100\n"
                "var direction: float = 0.0\n"
                "var est_en_vie: bool = true\n\n"
                "# Reference au noeud AnimatedSprite2D\n"
                "@onready var sprite: AnimatedSprite2D = $AnimatedSprite2D\n"
                "@onready var collision: CollisionShape2D = $CollisionShape2D\n\n"
                "# Signal personnalise emis quand le personnage meurt\n"
                "signal personnage_mort\n"
                "signal degats_recus(quantite: int)\n\n\n"
                "func _physics_process(delta: float) -> void:\n"
                "    if not est_en_vie:\n"
                "        return\n\n"
                "    # Appliquer la gravite si le personnage n'est pas au sol\n"
                "    if not is_on_floor():\n"
                "        velocity.y += get_gravity().y * GRAVITE_MULTIPLICATEUR * delta\n\n"
                "    # Gerer le saut\n"
                "    if Input.is_action_just_pressed(\"sauter\") and is_on_floor():\n"
                "        velocity.y = VITESSE_SAUT\n\n"
                "    # Lire la direction horizontale\n"
                "    direction = Input.get_axis(\"gauche\", \"droite\")\n\n"
                "    if direction != 0.0:\n"
                "        velocity.x = direction * VITESSE_DEPLACEMENT\n"
                "        sprite.flip_h = direction < 0\n"
                "        sprite.play(\"marcher\")\n"
                "    else:\n"
                "        velocity.x = move_toward(velocity.x, 0, VITESSE_DEPLACEMENT)\n"
                "        sprite.play(\"repos\")\n\n"
                "    # Appliquer le mouvement avec detection de collision\n"
                "    move_and_slide()\n\n\n"
                "func recevoir_degats(quantite: int) -> void:\n"
                "    points_de_vie -= quantite\n"
                "    degats_recus.emit(quantite)\n\n"
                "    if points_de_vie <= 0:\n"
                "        mourir()\n\n\n"
                "func mourir() -> void:\n"
                "    est_en_vie = false\n"
                "    sprite.play(\"mort\")\n"
                "    collision.set_deferred(\"disabled\", true)\n"
                "    personnage_mort.emit()\n"
            ),
            "performance": {
                "startup_time": "Tres rapide (l'editeur demarre en quelques secondes, les builds exportes sont egalement rapides au lancement)",
                "throughput": "Bon en 2D, correct en 3D (en progression constante avec chaque version 4.x, le rendu Vulkan ameliore significativement les performances)",
                "memory": "Faible a modere (l'editeur et les builds sont legers, le systeme de ressources partagees optimise l'utilisation memoire)",
                "concurrency_model": "Threads via l'API Thread de Godot, chargement de ressources asynchrone, appels RPC pour le multijoueur, pas de job system avance comme Unity DOTS"
            },
            "learning_curve": "Faible a moderee (GDScript est accessible aux debutants, l'architecture Scene/Node est intuitive, la documentation est claire, mais maitriser le C#, GDExtension et les fonctionnalites 3D avancees demande plus d'effort)",
            "community_size": "Grande et en croissance tres rapide (plus de 90 000 etoiles sur GitHub, l'un des projets open source les plus populaires, Discord et subreddit tres actifs, forte communaute francophone)",
            "job_market": "Emergent (encore peu d'offres d'emploi formelles comparees a Unity/Unreal, mais en croissance dans le milieu indie, l'enseignement, et les studios adoptant l'open source ; W4 Games developpe un ecosysteme commercial autour de Godot)"
        },
        "traits": {
            "performance": 6,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 5,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 6,
            "scalability": 5
        }
    },
}
