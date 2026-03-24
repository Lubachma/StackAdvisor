"""
Donnees sur les frameworks de developpement desktop.
Chaque entree documente un framework avec son histoire, son architecture,
ses cas d'usage et ses caracteristiques techniques.
"""

TECHNOLOGIES = {
    "electron": {
        "name": "Electron",
        "category": "desktop",
        "year_created": 2013,
        "creator": "GitHub",
        "paradigm": ["evenementiel", "composants", "multiprocessus", "web-based"],
        "typing": "dynamique (JavaScript) / statique optionnel (TypeScript)",
        "sections": {
            "overview": (
                "Electron est un framework open source qui permet de creer des\n"
                "applications de bureau multiplateformes en utilisant les technologies\n"
                "web : HTML, CSS et JavaScript. Il combine le moteur de rendu\n"
                "Chromium avec le runtime Node.js, offrant aux developpeurs web\n"
                "la possibilite de creer des applications natives pour Windows,\n"
                "macOS et Linux.\n\n"
                "Le principe d'Electron est simple mais puissant : chaque application\n"
                "embarque un navigateur Chromium et un runtime Node.js. Le processus\n"
                "principal (main process) gere le cycle de vie de l'application et\n"
                "a acces aux API systeme via Node.js, tandis que les processus de\n"
                "rendu (renderer processes) affichent l'interface dans des fenetres\n"
                "Chromium.\n\n"
                "Cette approche permet de reutiliser les competences et les outils\n"
                "du developpement web : React, Vue, Angular, Svelte, webpack, et\n"
                "l'ensemble de l'ecosysteme npm. Un developpeur web peut creer\n"
                "une application desktop complete sans apprendre de nouveau langage.\n\n"
                "Electron a revolutionne le developpement desktop en le rendant\n"
                "accessible a l'enorme communaute de developpeurs web. Des\n"
                "applications majeures comme Visual Studio Code, Slack, Discord,\n"
                "Figma et Notion sont construites avec Electron, prouvant que\n"
                "l'approche peut produire des applications de qualite professionnelle.\n\n"
                "Cependant, l'embarquement d'un navigateur complet a un cout :\n"
                "les applications Electron sont reputees pour leur consommation\n"
                "memoire elevee et leur taille d'installation importante, ce qui\n"
                "a suscite la creation d'alternatives comme Tauri."
            ),
            "history": (
                "Electron a ete cree en 2013 par Cheng Zhao chez GitHub, initialement\n"
                "sous le nom d'Atom Shell. Le projet est ne pour servir de fondation\n"
                "a Atom, l'editeur de texte open source de GitHub. L'idee etait\n"
                "audacieuse : utiliser les technologies web pour creer un editeur\n"
                "de code natif et extensible.\n\n"
                "Le projet Atom avait commence avec le Chromium Embedded Framework\n"
                "(CEF) mais les limitations de cette approche ont conduit l'equipe\n"
                "a creer leur propre solution, combinant directement Chromium et\n"
                "Node.js.\n\n"
                "En 2014, Atom et Atom Shell ont ete publies en open source.\n"
                "L'interet de la communaute pour le framework lui-meme a rapidement\n"
                "depasse celui pour l'editeur. De nombreux developpeurs ont commence\n"
                "a utiliser Atom Shell pour leurs propres applications.\n\n"
                "En avril 2015, le projet a ete renomme Electron pour refleter son\n"
                "ambition au-dela d'Atom. Ce changement de nom a coincide avec une\n"
                "acceleration massive de l'adoption.\n\n"
                "L'adoption d'Electron par Microsoft pour Visual Studio Code en\n"
                "2015 a ete un tournant decisif. Le succes fulgurant de VS Code\n"
                "a prouve que Electron pouvait produire des applications performantes\n"
                "et professionnelles, dissipant une partie des doutes sur l'approche.\n\n"
                "Slack, Discord, WhatsApp Desktop, Figma, Notion et des centaines\n"
                "d'autres applications ont suivi. Ironiquement, GitHub lui-meme\n"
                "a ete rachete par Microsoft en 2018, et l'editeur Atom a ete\n"
                "abandonne en 2022 au profit de VS Code.\n\n"
                "Les versions recentes d'Electron ont ameliore les performances,\n"
                "la securite (context isolation, process sandboxing) et l'experience\n"
                "developpeur. Electron Forge simplifie le scaffolding et le packaging."
            ),
            "architecture": (
                "L'architecture d'Electron repose sur un modele multiprocessus\n"
                "herite de Chromium :\n\n"
                "Processus principal (Main Process) : C'est le point d'entree de\n"
                "l'application. Il s'execute dans un environnement Node.js et a\n"
                "acces complet aux API systeme : systeme de fichiers, notifications\n"
                "natives, menus, tray, raccourcis globaux, etc. Il cree et gere\n"
                "les fenetres (BrowserWindow).\n\n"
                "Processus de rendu (Renderer Processes) : Chaque fenetre s'execute\n"
                "dans son propre processus de rendu, isolee des autres. Le processus\n"
                "de rendu affiche du contenu web (HTML/CSS/JS) via Chromium. Depuis\n"
                "Electron 12+, le context isolation et le sandboxing sont actives\n"
                "par defaut pour la securite.\n\n"
                "Communication inter-processus (IPC) : Le main process et les\n"
                "renderer processes communiquent via ipcMain et ipcRenderer.\n"
                "Le preload script sert de pont securise entre le contexte\n"
                "Node.js et le contexte web, exposant selectivement des API\n"
                "via contextBridge.\n\n"
                "Chromium Embedded : Electron embarque une version specifique de\n"
                "Chromium. Cela garantit un rendu web identique sur toutes les\n"
                "plateformes mais explique la taille importante des applications\n"
                "(~150-200 Mo minimum).\n\n"
                "Node.js Embedded : Le runtime Node.js complet est disponible\n"
                "dans le main process, donnant acces a tous les modules npm\n"
                "et aux API systeme de bas niveau.\n\n"
                "Packaging : Electron Builder ou Electron Forge empaquetent\n"
                "l'application avec Chromium et Node.js en executables natifs\n"
                "(.exe, .dmg, .AppImage, .deb, .snap) avec support des mises\n"
                "a jour automatiques."
            ),
            "pros_cons": {
                "pros": [
                    "Reutilisation complete des competences et outils web (HTML, CSS, JS, React, Vue)",
                    "Multiplateforme reel : un seul codebase pour Windows, macOS et Linux",
                    "Acces a l'immense ecosysteme npm avec des millions de packages",
                    "Rendu web identique sur toutes les plateformes grace a Chromium",
                    "Outillage de developpement mature (DevTools, hot reload, debugger)",
                    "Communaute massive et nombreux exemples d'applications en production",
                    "Mises a jour automatiques integrees et bien supportees",
                    "Prouve par des applications a grande echelle (VS Code, Slack, Discord)"
                ],
                "cons": [
                    "Consommation memoire elevee (chaque fenetre est un processus Chromium)",
                    "Taille d'installation importante (~150-200 Mo minimum) a cause de Chromium",
                    "Temps de demarrage plus lent qu'une application native pure",
                    "Performances inferieures aux applications natives pour les taches intensives",
                    "Surface d'attaque de securite elargie (Chromium + Node.js)",
                    "Chaque application embarque sa propre version de Chromium (duplication)",
                    "La consommation d'energie/batterie est superieure aux alternatives natives",
                    "Perception negative aupres de certains utilisateurs ('encore une app Electron')"
                ]
            },
            "use_cases": (
                "Electron est ideal pour les applications necessitant une interface\n"
                "riche et les competences web : editeurs de texte et de code (VS Code),\n"
                "applications de communication (Slack, Discord), outils de design\n"
                "(Figma), applications de productivite (Notion, Obsidian), clients\n"
                "API (Postman, Insomnia), outils de developpement, et applications\n"
                "d'entreprise internes. Il convient moins aux applications necessitant\n"
                "des performances maximales ou une empreinte memoire minimale."
            ),
            "ecosystem_size": (
                "L'ecosysteme Electron beneficie de l'ecosysteme web entier. Electron\n"
                "Forge et Electron Builder pour le scaffolding et le packaging.\n"
                "Electron Store pour la persistance de configuration. Electron\n"
                "Updater pour les mises a jour automatiques. Tous les frameworks\n"
                "web (React, Vue, Angular, Svelte) fonctionnent nativement.\n"
                "Electron Fiddle permet de prototyper rapidement. Les outils\n"
                "de test Spectron (deprecie) sont remplaces par Playwright\n"
                "ou Selenium."
            ),
            "companies": [
                "Microsoft (Visual Studio Code, Teams)",
                "Slack Technologies",
                "Discord",
                "Figma",
                "Notion",
                "WhatsApp (desktop)",
                "Twitch (desktop)",
                "1Password"
            ],
            "code_example": (
                "// main.js - Processus principal\n"
                "const { app, BrowserWindow, ipcMain } = require('electron');\n"
                "const path = require('path');\n\n"
                "function creerFenetre() {\n"
                "  const fenetre = new BrowserWindow({\n"
                "    width: 800,\n"
                "    height: 600,\n"
                "    webPreferences: {\n"
                "      preload: path.join(__dirname, 'preload.js'),\n"
                "      contextIsolation: true,\n"
                "      sandbox: true\n"
                "    }\n"
                "  });\n"
                "  fenetre.loadFile('index.html');\n"
                "}\n\n"
                "app.whenReady().then(creerFenetre);\n\n"
                "// Gestion IPC securisee\n"
                "ipcMain.handle('lire-fichier', async (event, chemin) => {\n"
                "  const fs = require('fs/promises');\n"
                "  return await fs.readFile(chemin, 'utf-8');\n"
                "});\n\n"
                "// preload.js - Pont securise\n"
                "const { contextBridge, ipcRenderer } = require('electron');\n"
                "contextBridge.exposeInMainWorld('api', {\n"
                "  lireFichier: (chemin) => ipcRenderer.invoke('lire-fichier', chemin)\n"
                "});"
            ),
            "performance": {
                "startup_time": "Demarrage relativement lent : 1-5 secondes selon la complexite. Le chargement de Chromium et Node.js constitue un overhead incompressible.",
                "throughput": "Performances de rendu identiques a un navigateur web moderne. Suffisant pour la majorite des interfaces, mais inadapte aux applications graphiques intensives.",
                "memory": "Consommation elevee : 150-500+ Mo selon la complexite. Chaque fenetre BrowserWindow est un processus Chromium independant consommant au minimum 30-50 Mo.",
                "concurrency_model": "Modele multiprocessus de Chromium. Le main process gere la logique applicative, chaque renderer process gere une fenetre. Communication asynchrone via IPC. Web Workers disponibles dans les renderers."
            },
            "learning_curve": (
                "La courbe d'apprentissage est tres douce pour les developpeurs web.\n"
                "Les technologies (HTML, CSS, JS) et les frameworks (React, Vue)\n"
                "sont identiques. L'apprentissage specifique concerne le modele\n"
                "main/renderer, l'IPC, le preload, la securite (context isolation),\n"
                "et le packaging. Un developpeur web peut etre productif en\n"
                "quelques jours."
            ),
            "community_size": "Plus de 113 000 etoiles sur GitHub. L'une des plus grandes communautes de frameworks desktop. Documentation complete et nombreux tutoriels.",
            "job_market": "Bonne demande, souvent combinee avec des competences React/TypeScript. Les postes mentionnant Electron recherchent generalement des developpeurs fullstack capables de creer des outils internes."
        },
        "traits": {
            "performance": 3,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 8,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 4
        }
    },

    "tauri": {
        "name": "Tauri",
        "category": "desktop",
        "year_created": 2020,
        "creator": "Tauri Contributors",
        "paradigm": ["evenementiel", "composants", "natif", "web-based"],
        "typing": "statique (Rust backend) / dynamique ou statique (frontend web)",
        "sections": {
            "overview": (
                "Tauri est un framework open source pour construire des applications\n"
                "de bureau legeres et securisees en utilisant les technologies web\n"
                "pour l'interface et Rust pour le backend. Contrairement a Electron\n"
                "qui embarque Chromium, Tauri utilise le WebView natif du systeme\n"
                "d'exploitation (WebView2 sur Windows, WKWebView sur macOS, WebKitGTK\n"
                "sur Linux), reduisant drastiquement la taille des applications.\n\n"
                "Le backend Rust de Tauri offre des performances proches du natif,\n"
                "une securite memoire garantie a la compilation, et un controle\n"
                "precis des ressources systeme. Le frontend peut utiliser n'importe\n"
                "quel framework web : React, Vue, Svelte, SolidJS, ou meme du\n"
                "HTML/JS vanilla.\n\n"
                "Tauri adopte une approche 'security-first' : par defaut, le\n"
                "frontend n'a acces a aucune API systeme. Chaque permission doit\n"
                "etre explicitement declaree dans la configuration, suivant le\n"
                "principe de moindre privilege. Ce modele de securite est\n"
                "fondamentalement plus robuste que celui d'Electron.\n\n"
                "La taille des applications Tauri est remarquablement reduite :\n"
                "une application simple pese entre 600 Ko et 3 Mo, contre 150-200 Mo\n"
                "pour l'equivalent Electron. La consommation memoire est egalement\n"
                "bien inferieure.\n\n"
                "Tauri 2.0, sorti en 2024, a etendu le support au mobile (iOS et\n"
                "Android) en plus du desktop, positionnant Tauri comme une\n"
                "alternative credible pour le developpement multiplateforme\n"
                "unifie."
            ),
            "history": (
                "Le projet Tauri a ete lance en 2019 par Daniel Thompson-Yvetot\n"
                "et Lucas Fernandes Nogueira, motives par les frustrations liees\n"
                "a l'empreinte d'Electron. L'idee initiale etait d'utiliser le\n"
                "WebView natif plutot qu'un Chromium embarque pour reduire\n"
                "drastiquement la taille et la consommation des applications.\n\n"
                "Le choix de Rust comme langage backend etait delibere : Rust\n"
                "offre des performances proches du C/C++ tout en garantissant\n"
                "la securite memoire a la compilation. Ce choix s'est avere\n"
                "strategiquement brillant, Rust gagnant en popularite annee\n"
                "apres annee.\n\n"
                "Tauri 1.0 est sorti en version stable en juin 2022, marquant\n"
                "une etape majeure. Le framework supportait Windows, macOS et\n"
                "Linux avec un ecosysteme de plugins en croissance.\n\n"
                "La version 1.x a connu une adoption rapide, attirant des\n"
                "developpeurs soucieux de l'impact environnemental et de\n"
                "l'experience utilisateur (applications plus legeres, plus\n"
                "rapides, moins consommatrices de batterie).\n\n"
                "Tauri 2.0, publie en octobre 2024, a ete une refonte majeure\n"
                "apportant le support mobile (iOS et Android), un nouveau\n"
                "systeme de permissions granulaire, les plugins IPC, et\n"
                "une architecture amelioree. Le support mobile place Tauri\n"
                "en concurrence directe avec Flutter et React Native.\n\n"
                "L'ecosysteme Tauri continue de croitre rapidement, avec une\n"
                "communaute passionnee et des entreprises qui commencent a\n"
                "migrer leurs applications Electron vers Tauri pour reduire\n"
                "leur empreinte."
            ),
            "architecture": (
                "L'architecture de Tauri separe clairement le backend (Rust)\n"
                "du frontend (web) avec un modele de securite strict :\n\n"
                "Core Rust : Le coeur de l'application est ecrit en Rust.\n"
                "Il gere le cycle de vie de l'application, les fenetres,\n"
                "les menus, les tray icons, les raccourcis globaux, et\n"
                "fournit les commandes Tauri invocables depuis le frontend.\n\n"
                "WebView natif : Au lieu d'embarquer Chromium, Tauri utilise\n"
                "le WebView natif du systeme : WRY (la bibliotheque Rust\n"
                "multiplateforme) abstrait les differences entre WebView2\n"
                "(Windows), WKWebView (macOS) et WebKitGTK (Linux).\n\n"
                "TAO : La bibliotheque de fenetrage multiplateforme qui gere\n"
                "la creation de fenetres, les evenements systeme et l'interaction\n"
                "avec le gestionnaire de fenetres.\n\n"
                "Systeme de commandes : Le frontend invoque des fonctions Rust\n"
                "via le systeme de commandes Tauri (invoke). Les commandes\n"
                "sont typees, serialisees/deserialisees automatiquement via\n"
                "serde, et executees dans le runtime Tokio async.\n\n"
                "Modele de securite : Tauri 2.0 introduit un systeme de\n"
                "permissions declaratives. Chaque API systeme (fichiers, reseau,\n"
                "clipboard, etc.) doit etre explicitement autorisee dans la\n"
                "configuration. Le frontend est sandboxe par defaut.\n\n"
                "Plugins : Le systeme de plugins permet d'etendre les capacites\n"
                "avec des modules Rust cote backend et JavaScript cote frontend.\n"
                "Des plugins officiels existent pour le stockage, les dialogues,\n"
                "les notifications, le shell, et le systeme de fichiers.\n\n"
                "Build : Tauri compile le backend Rust en binaire natif et\n"
                "bundle le frontend web. Le resultat est un executable\n"
                "autonome de petite taille."
            ),
            "pros_cons": {
                "pros": [
                    "Taille d'application minuscule (600 Ko - 3 Mo vs 150-200 Mo pour Electron)",
                    "Consommation memoire et CPU bien inferieure a Electron",
                    "Backend Rust offrant performances, securite memoire et fiabilite",
                    "Modele de securite strict avec permissions granulaires par defaut",
                    "Support multiplateforme : desktop (Windows, macOS, Linux) et mobile (iOS, Android)",
                    "Compatible avec tous les frameworks frontend web (React, Vue, Svelte, etc.)",
                    "Consommation d'energie reduite, meilleure pour la batterie des portables",
                    "Communaute passionnee et en croissance rapide"
                ],
                "cons": [
                    "Le WebView natif peut avoir des comportements differents selon l'OS",
                    "L'ecosysteme de plugins est moins mature que celui d'Electron",
                    "La connaissance de Rust est necessaire pour le backend (courbe d'apprentissage)",
                    "Le debugging cross-platform est plus complexe (WebViews differents)",
                    "Le WebView de Linux (WebKitGTK) est parfois en retard sur les standards web",
                    "Moins d'entreprises ont prouve Tauri en production a grande echelle",
                    "Le support mobile (Tauri 2.0) est encore jeune et en maturation"
                ]
            },
            "use_cases": (
                "Tauri est ideal pour les applications desktop necessitant une\n"
                "empreinte legere : outils de productivite, lanceurs d'applications,\n"
                "clients API, outils de developpement, applications de gestion,\n"
                "et toute application ou la taille et les performances comptent.\n"
                "Il convient particulierement aux entreprises soucieuses de\n"
                "l'empreinte carbone de leurs logiciels et aux developpeurs\n"
                "migrant depuis Electron pour des raisons de performances."
            ),
            "ecosystem_size": (
                "L'ecosysteme Tauri est en croissance. Plugins officiels : fs\n"
                "(systeme de fichiers), dialog (dialogues natifs), notification,\n"
                "clipboard, shell, store (persistance), updater (mises a jour\n"
                "automatiques), http, os, process. Le CLI Tauri gere la creation\n"
                "de projets, le developpement et le build. create-tauri-app\n"
                "propose des templates pour React, Vue, Svelte, SolidJS,\n"
                "Vanilla JS et Yew (Rust). Les outils de test Tauri Driver\n"
                "permettent les tests d'integration via WebDriver."
            ),
            "companies": [
                "CrabNebula (societe fondee par les createurs de Tauri)",
                "LLDAP (gestionnaire LDAP)",
                "Spacedrive (gestionnaire de fichiers distribue)",
                "AppFlowy (alternative a Notion)",
                "Padloc (gestionnaire de mots de passe)",
                "Aleph.im (cloud decentralise)"
            ],
            "code_example": (
                "// src-tauri/src/main.rs - Backend Rust\n"
                "use tauri::Manager;\n\n"
                "#[tauri::command]\n"
                "fn saluer(nom: &str) -> String {\n"
                "    format!(\"Bonjour, {} ! Bienvenue dans Tauri.\", nom)\n"
                "}\n\n"
                "#[tauri::command]\n"
                "async fn lire_fichier(chemin: String) -> Result<String, String> {\n"
                "    tokio::fs::read_to_string(&chemin)\n"
                "        .await\n"
                "        .map_err(|e| format!(\"Erreur de lecture : {}\", e))\n"
                "}\n\n"
                "fn main() {\n"
                "    tauri::Builder::default()\n"
                "        .invoke_handler(tauri::generate_handler![saluer, lire_fichier])\n"
                "        .run(tauri::generate_context!())\n"
                "        .expect(\"Erreur lors du lancement de l'application\");\n"
                "}\n\n"
                "// src/App.jsx - Frontend React\n"
                "import { invoke } from '@tauri-apps/api/core';\n\n"
                "function App() {\n"
                "  const [message, setMessage] = useState('');\n\n"
                "  const saluer = async () => {\n"
                "    const reponse = await invoke('saluer', { nom: 'Utilisateur' });\n"
                "    setMessage(reponse);\n"
                "  };\n\n"
                "  return (\n"
                "    <div>\n"
                "      <button onClick={saluer}>Saluer</button>\n"
                "      <p>{message}</p>\n"
                "    </div>\n"
                "  );\n"
                "}"
            ),
            "performance": {
                "startup_time": "Demarrage tres rapide : le binaire Rust se lance en millisecondes, le WebView natif est plus rapide a charger qu'un Chromium embarque. Typiquement sous la seconde.",
                "throughput": "Performances du backend quasi natives grace a Rust compile. Le frontend a les performances du WebView natif, generalement equivalentes ou superieures a Chromium pour les interfaces standard.",
                "memory": "Consommation memoire considerablement reduite : une application simple consomme 20-50 Mo contre 150-500 Mo pour Electron. Le WebView partage les ressources avec le systeme.",
                "concurrency_model": "Backend Rust avec le runtime async Tokio pour la concurrence. Les commandes Tauri sont executees de maniere asynchrone. Le frontend utilise le modele de concurrence standard du JavaScript."
            },
            "learning_curve": (
                "La courbe d'apprentissage est moderee a elevee. Le frontend est\n"
                "accessible aux developpeurs web. Le backend Rust represente le\n"
                "defi principal : Rust a une courbe d'apprentissage notoire\n"
                "(ownership, borrowing, lifetimes). Cependant, pour des backends\n"
                "simples, les bases de Rust suffisent. Le systeme de permissions\n"
                "et la configuration Tauri necessitent egalement un apprentissage\n"
                "specifique."
            ),
            "community_size": "Plus de 85 000 etoiles sur GitHub et en forte croissance. Communaute enthousiaste sur Discord. Le projet beneficie d'un interet croissant des developpeurs Rust et web.",
            "job_market": "Marche emergent mais en croissance. Encore peu d'offres specifiques Tauri, mais les competences Rust + web sont tres valorisees. Les entreprises commencent a explorer Tauri comme alternative a Electron."
        },
        "traits": {
            "performance": 8,
            "developer_speed": 6,
            "learning_curve": 5,
            "ecosystem_size": 4,
            "type_safety": 8,
            "concurrency": 7,
            "memory_safety": 9,
            "scalability": 6
        }
    },

    "qt": {
        "name": "Qt",
        "category": "desktop",
        "year_created": 1995,
        "creator": "Trolltech/Qt Company",
        "paradigm": ["oriente objet", "signal-slot", "declaratif (QML)", "imperatif"],
        "typing": "statique (C++ / QML)",
        "sections": {
            "overview": (
                "Qt (prononce 'cute') est un framework multiplateforme complet pour\n"
                "le developpement d'applications desktop, mobiles et embarquees.\n"
                "Ecrit en C++, Qt fournit un ensemble exhaustif de modules couvrant\n"
                "les interfaces graphiques, le reseau, les bases de donnees, le\n"
                "multimedia, les graphiques 3D, la communication serie, et bien plus.\n\n"
                "Qt se distingue par son systeme Signal-Slot, un mecanisme elegant\n"
                "de communication entre objets qui decouple les emetteurs des\n"
                "recepteurs. Ce pattern est devenu l'une des innovations les plus\n"
                "influentes de Qt, inspire par de nombreux frameworks par la suite.\n\n"
                "Le framework propose deux approches pour les interfaces : Qt Widgets\n"
                "(approche classique C++ avec des widgets predefinis) et Qt Quick/QML\n"
                "(approche declarative moderne avec un langage de description\n"
                "d'interface). Qt Quick est particulierement adapte aux interfaces\n"
                "tactiles, animees et fluides.\n\n"
                "Qt fournit son propre systeme de build (qmake, remplace par CMake\n"
                "depuis Qt 6), un IDE complet (Qt Creator), et des outils de design\n"
                "visuel (Qt Designer, Qt Design Studio). Le Meta-Object Compiler\n"
                "(moc) enrichit le C++ avec l'introspection, les proprietes\n"
                "dynamiques et le systeme signal-slot.\n\n"
                "Qt est disponible sous double licence : commerciale et open source\n"
                "(LGPL/GPL). Cette dualite permet son utilisation gratuite dans de\n"
                "nombreux contextes tout en finançant son developpement continu\n"
                "via les licences commerciales."
            ),
            "history": (
                "Qt a ete cree en 1991 par Haavard Nord et Eirik Chambe-Eng en\n"
                "Norvege. Le developpement a debute quand Haavard Nord travaillait\n"
                "sur un projet necessitant une interface graphique multiplateforme.\n"
                "Ils ont fonde la societe Trolltech en 1994 pour commercialiser\n"
                "le framework.\n\n"
                "La premiere version publique, Qt 1.0, est sortie en 1995. Le nom\n"
                "'Qt' vient de l'esthetique de la lettre 'Q' dans l'editeur de texte\n"
                "Emacs utilise par Haavard, et 't' pour 'toolkit'.\n\n"
                "En 1996, le projet KDE (K Desktop Environment) a choisi Qt comme\n"
                "base de son environnement de bureau Linux. Ce choix a genere une\n"
                "controverse sur la licence proprietary de Qt, menant eventullement\n"
                "a la creation de GNOME comme alternative utilisant GTK. Trolltech\n"
                "a resolu le probleme en publiant Qt sous licence open source.\n\n"
                "Nokia a rachete Trolltech en 2008 pour 150 millions de dollars,\n"
                "utilisant Qt comme base de son ecosysteme mobile (Symbian, MeeGo).\n"
                "L'abandon de cette strategie au profit de Windows Phone a ete\n"
                "un coup dur pour Qt.\n\n"
                "En 2012, Digia a rachete Qt a Nokia, puis a cree The Qt Company\n"
                "en 2014 comme entite independante. Qt 5.0 (2012) a apporte une\n"
                "refonte majeure avec Qt Quick 2 et le rendu OpenGL.\n\n"
                "Qt 6.0, sorti en decembre 2020, est une modernisation profonde :\n"
                "support de C++17/20, nouveau systeme de proprietes, compilation\n"
                "QML, CMake comme systeme de build officiel, et integration\n"
                "amelioree du rendu 3D.\n\n"
                "Qt est utilise dans des milliers de produits industriels,\n"
                "automobiles (tableaux de bord), medicaux et grand public."
            ),
            "architecture": (
                "L'architecture de Qt est modulaire, organisee autour d'un\n"
                "noyau central et de modules specialises :\n\n"
                "Qt Core : Le module fondamental fournit le Meta-Object System\n"
                "(introspection, proprietes dynamiques, signal-slot), la gestion\n"
                "des evenements, les threads, les timers, les conteneurs (QList,\n"
                "QMap, QHash), les chaines (QString avec Unicode natif), et\n"
                "le systeme de fichiers.\n\n"
                "Meta-Object Compiler (moc) : Un pre-processeur specifique a Qt\n"
                "qui analyse les fichiers C++ contenant la macro Q_OBJECT et\n"
                "genere du code C++ additionnel pour le systeme signal-slot,\n"
                "l'introspection et les proprietes dynamiques.\n\n"
                "Signal-Slot : Le mecanisme de communication type-safe entre\n"
                "objets. Un signal est emis quand un evenement se produit,\n"
                "les slots connectes sont automatiquement appeles. Les\n"
                "connexions peuvent traverser les threads de maniere securisee.\n\n"
                "Qt Widgets : Le systeme classique de widgets pour les interfaces\n"
                "desktop. Les widgets sont organises en hierarchie parent-enfant\n"
                "avec un systeme de layout automatique. Le style est gerempar\n"
                "le systeme de style natif ou par des style sheets (QSS).\n\n"
                "Qt Quick/QML : Le systeme declaratif moderne. QML est un langage\n"
                "de description d'interface integrant JavaScript. Le Scene Graph\n"
                "accelere par GPU gere le rendu. Depuis Qt 6, QML peut etre\n"
                "compile en C++ pour de meilleures performances.\n\n"
                "Boucle d'evenements : Qt utilise une boucle d'evenements\n"
                "sophistiquee (QEventLoop) qui gere les evenements de l'interface,\n"
                "les timers, les sockets reseau et les signaux inter-threads."
            ),
            "pros_cons": {
                "pros": [
                    "Framework complet couvrant GUI, reseau, BDD, multimedia, 3D, serie, etc.",
                    "Performances natives C++ avec un aspect visuel professionnel",
                    "Systeme signal-slot elegant et type-safe pour la communication entre objets",
                    "Multiplateforme veritable : desktop, mobile, embarque, automobile",
                    "Double approche : Widgets (classique) et QML (moderne, declaratif)",
                    "Qt Creator est un IDE mature et productif",
                    "Documentation exhaustive et de haute qualite",
                    "Utilise massivement dans l'industrie (automobile, medical, aeronautique)"
                ],
                "cons": [
                    "La licence commerciale est couteuse pour les petites entreprises",
                    "Le Meta-Object Compiler (moc) ajoute une etape de compilation non standard",
                    "La taille des binaires est importante en raison du linking des modules Qt",
                    "C++ est un langage complexe avec une courbe d'apprentissage elevee",
                    "Les mises a jour entre versions majeures (5 -> 6) peuvent etre penibles",
                    "L'apparence par defaut peut sembler 'non native' sur certaines plateformes",
                    "La politique de licence a change plusieurs fois, creant de l'incertitude"
                ]
            },
            "use_cases": (
                "Qt excelle dans le developpement d'applications de bureau\n"
                "professionnelles, d'interfaces embarquees (tableaux de bord\n"
                "automobiles, dispositifs medicaux, systemes industriels), de\n"
                "logiciels de CAO/DAO, d'outils multimedia, et d'applications\n"
                "necessitant des performances natives et une apparence\n"
                "professionnelle. Il est le choix de reference pour les\n"
                "applications C++ multiplateformes."
            ),
            "ecosystem_size": (
                "L'ecosysteme Qt est mature et complet. Qt Creator est l'IDE\n"
                "officiel avec designer visuel integre. Qt Design Studio\n"
                "permet le design d'interfaces QML. Qt Linguist gere\n"
                "l'internationalisation. Qt Test fournit un framework de\n"
                "tests unitaires. Les modules Qt couvrent : Qt Network,\n"
                "Qt SQL, Qt Multimedia, Qt WebEngine (Chromium), Qt 3D,\n"
                "Qt Charts, Qt Data Visualization, Qt Serial Port,\n"
                "Qt Bluetooth, et Qt for MCUs (microcontroleurs)."
            ),
            "companies": [
                "Mercedes-Benz (tableaux de bord)",
                "BMW (systemes d'info-divertissement)",
                "LG Electronics",
                "Volvo",
                "Tesla (interface de la console centrale)",
                "Autodesk (Maya, 3ds Max)",
                "VLC Media Player",
                "KDE (environnement de bureau Linux)"
            ],
            "code_example": (
                "// Exemple Qt Widgets - C++\n"
                "#include <QApplication>\n"
                "#include <QMainWindow>\n"
                "#include <QPushButton>\n"
                "#include <QVBoxLayout>\n"
                "#include <QLabel>\n\n"
                "class FenetreCompteur : public QMainWindow {\n"
                "    Q_OBJECT\n"
                "public:\n"
                "    FenetreCompteur() : compte(0) {\n"
                "        auto *widget = new QWidget(this);\n"
                "        auto *layout = new QVBoxLayout(widget);\n\n"
                "        etiquette = new QLabel(\"Compteur : 0\", this);\n"
                "        etiquette->setAlignment(Qt::AlignCenter);\n\n"
                "        auto *bouton = new QPushButton(\"Incrementer\", this);\n"
                "        connect(bouton, &QPushButton::clicked, this, &FenetreCompteur::incrementer);\n\n"
                "        layout->addWidget(etiquette);\n"
                "        layout->addWidget(bouton);\n"
                "        setCentralWidget(widget);\n"
                "        setWindowTitle(\"Compteur Qt\");\n"
                "    }\n\n"
                "private slots:\n"
                "    void incrementer() {\n"
                "        compte++;\n"
                "        etiquette->setText(QString(\"Compteur : %1\").arg(compte));\n"
                "    }\n\n"
                "private:\n"
                "    int compte;\n"
                "    QLabel *etiquette;\n"
                "};\n\n"
                "int main(int argc, char *argv[]) {\n"
                "    QApplication app(argc, argv);\n"
                "    FenetreCompteur fenetre;\n"
                "    fenetre.show();\n"
                "    return app.exec();\n"
                "}"
            ),
            "performance": {
                "startup_time": "Demarrage rapide, comparable a une application native. Le chargement des modules Qt ajoute un leger overhead par rapport a du C++ pur.",
                "throughput": "Performances natives C++ pour le traitement de donnees. Le rendu Qt Widgets est base sur le systeme de peinture natif. Qt Quick utilise un Scene Graph accelere par GPU.",
                "memory": "Consommation memoire moderee. Inferieure a Electron mais superieure a du C++ pur sans framework. Le linking dynamique des modules Qt reduit l'empreinte.",
                "concurrency_model": "Modele base sur les QThreads avec communication inter-thread via signal-slot. Les signaux traversent automatiquement les frontieres de threads. QThreadPool et QtConcurrent pour le parallelisme."
            },
            "learning_curve": (
                "La courbe d'apprentissage de Qt est elevee. C++ est un prerequis\n"
                "exigeant. Les concepts specifiques a Qt (moc, signal-slot,\n"
                "gestion memoire parent-enfant, modele-vue) demandent un\n"
                "investissement significatif. QML est plus accessible mais\n"
                "necessite de comprendre l'interaction avec le backend C++.\n"
                "La documentation officielle est cependant excellente."
            ),
            "community_size": "Communaute industrielle large et mature. Le forum Qt et la mailing list sont actifs. Conferences annuelles Qt World Summit. Le projet KDE est un contributeur majeur.",
            "job_market": "Forte demande dans l'industrie (automobile, medical, aeronautique, defense). Les postes Qt/C++ offrent generalement des salaires eleves. Moins d'offres dans les startups web."
        },
        "traits": {
            "performance": 9,
            "developer_speed": 5,
            "learning_curve": 7,
            "ecosystem_size": 7,
            "type_safety": 7,
            "concurrency": 7,
            "memory_safety": 4,
            "scalability": 7
        }
    },

    "gtk": {
        "name": "GTK",
        "category": "desktop",
        "year_created": 1998,
        "creator": "GNOME Project",
        "paradigm": ["oriente objet (via GObject)", "evenementiel", "callbacks", "imperatif"],
        "typing": "statique (C avec GObject) / variable selon le binding",
        "sections": {
            "overview": (
                "GTK (GIMP Toolkit, renomme simplement GTK depuis la version 4)\n"
                "est un toolkit de creation d'interfaces graphiques multiplateformes,\n"
                "principalement utilise sur Linux comme base de l'environnement de\n"
                "bureau GNOME. Ecrit en C avec le systeme d'objets GObject, GTK\n"
                "offre un modele oriente objet complet dans un langage imperatif.\n\n"
                "GTK est ne de la necessite d'avoir un toolkit graphique libre pour\n"
                "Linux. Suite a la controverse sur la licence de Qt dans les annees\n"
                "1990, GTK est devenu l'alternative open source de reference, et\n"
                "GNOME l'a adopte comme fondation de son environnement de bureau.\n\n"
                "Le systeme GObject, sur lequel repose GTK, apporte au langage C\n"
                "des fonctionnalites orientees objet : heritage, encapsulation,\n"
                "polymorphisme, signaux (similaires aux signaux Qt), proprietes\n"
                "dynamiques et introspection. GObject Introspection permet de\n"
                "generer automatiquement des bindings pour Python, JavaScript,\n"
                "Rust, Vala et d'autres langages.\n\n"
                "GTK 4, sorti en decembre 2020, est une refonte majeure avec un\n"
                "nouveau modele de rendu base sur GPU (via GSK, le GPU Scene\n"
                "Kit), un nouveau systeme d'evenements, et des APIs modernisees.\n"
                "Les performances de GTK 4 sont significativement ameliorees\n"
                "par rapport a GTK 3.\n\n"
                "Bien que GTK fonctionne sur Windows et macOS, son integration\n"
                "y est moins polie que sur Linux. GTK reste avant tout le\n"
                "toolkit natif de l'ecosysteme Linux/GNOME."
            ),
            "history": (
                "GTK a ete initialement developpe en 1996 par Spencer Kimball,\n"
                "Peter Mattis et Josh MacDonald dans le cadre du projet GIMP\n"
                "(GNU Image Manipulation Program). Ils avaient besoin d'un\n"
                "toolkit graphique libre pour remplacer Motif, qui etait\n"
                "proprietaire.\n\n"
                "GTK+ 1.0 est sorti en 1998. Le '+' (abandonne depuis GTK 4)\n"
                "distinguait le toolkit de la version initiale liee uniquement\n"
                "a GIMP. Le projet GNOME, lance par Miguel de Icaza et Federico\n"
                "Mena en 1997, a choisi GTK+ comme toolkit en reaction aux\n"
                "preoccupations sur la licence de Qt a l'epoque.\n\n"
                "GTK+ 2.0 (2002) a ete une refonte majeure avec le systeme\n"
                "GObject, le framework de rendu de texte Pango, le systeme\n"
                "d'accessibilite ATK, et le moteur de theme. Cette version\n"
                "a etabli l'architecture qui perdure aujourd'hui.\n\n"
                "GTK+ 3.0 (2011) a apporte le support CSS pour le theming,\n"
                "le rendu Cairo, le support HiDPI, les gestes tactiles,\n"
                "et la transition vers Wayland. La migration depuis GTK 2\n"
                "a ete longue et parfois douloureuse pour les applications.\n\n"
                "GTK 4.0 (decembre 2020) represente la version la plus\n"
                "ambitieuse : rendu GPU via Vulkan/OpenGL (GSK), nouveau\n"
                "modele d'evenements, widgets de liste scalables (GtkListView),\n"
                "animations basees sur les transitions CSS, et une refonte\n"
                "de la gestion du drag-and-drop.\n\n"
                "L'ecosysteme GNOME continue d'evoluer avec des bibliotheques\n"
                "complementaires comme libadwaita (suivant les GNOME Human\n"
                "Interface Guidelines), et un interet croissant pour le\n"
                "developpement en Rust via gtk-rs."
            ),
            "architecture": (
                "L'architecture de GTK repose sur plusieurs couches de\n"
                "bibliotheques formant la pile GNOME :\n\n"
                "GLib : La bibliotheque de base fournissant la boucle\n"
                "d'evenements (GMainLoop), les types fondamentaux, les\n"
                "structures de donnees (GList, GHashTable), les threads,\n"
                "les I/O asynchrones (GIO), et les utilitaires systeme.\n\n"
                "GObject : Le systeme d'objets en C offrant l'heritage,\n"
                "les signaux, les proprietes et l'introspection. Chaque\n"
                "widget GTK derive de GObject. Le systeme de reference\n"
                "counting gere la duree de vie des objets.\n\n"
                "GSK (GPU Scene Kit) : Le moteur de rendu de GTK 4.\n"
                "GSK traduit l'arbre de widgets en un arbre de noeuds\n"
                "de rendu optimise pour le GPU via Vulkan, OpenGL ou\n"
                "un renderer Cairo de fallback.\n\n"
                "GDK (GIMP Drawing Kit) : La couche d'abstraction\n"
                "graphique qui interface GTK avec le systeme de fenetrage\n"
                "(X11, Wayland, Win32, Quartz). GDK gere les surfaces,\n"
                "les evenements d'entree, et le contexte graphique.\n\n"
                "Widgets et layout : Les widgets GTK sont organises en\n"
                "hierarchie. Les conteneurs (GtkBox, GtkGrid, GtkStack)\n"
                "gerent la disposition. Le systeme de taille alloue\n"
                "l'espace en deux passes (measure puis allocate).\n\n"
                "GObject Introspection : Un systeme de metadonnees\n"
                "permettant de generer automatiquement des bindings\n"
                "pour d'autres langages. Les fichiers .gir (XML) et\n"
                ".typelib (binaire) decrivent l'API complete de chaque\n"
                "bibliotheque."
            ),
            "pros_cons": {
                "pros": [
                    "Integration native parfaite avec l'environnement GNOME/Linux",
                    "Licence LGPL permissive sans cout commercial",
                    "GObject Introspection permet des bindings automatiques pour de nombreux langages",
                    "GTK 4 offre un rendu GPU performant et des animations fluides",
                    "Accessibilite integree (ATK) conforme aux standards d'accessibilite",
                    "L'ecosysteme Rust (gtk-rs) modernise le developpement GTK",
                    "Theming flexible via CSS",
                    "Bibliotheque libadwaita fournissant des widgets GNOME modernes et elegants"
                ],
                "cons": [
                    "L'aspect visuel est moins natif sur Windows et macOS que sur Linux",
                    "Le developpement en C avec GObject est verbeux et complexe",
                    "L'ecosysteme est fortement lie a GNOME, ce qui peut etre limitant",
                    "Moins de documentation et de tutoriels que Qt ou Electron",
                    "Les migrations entre versions majeures (GTK 3 -> 4) sont penibles",
                    "Moins de modules integres que Qt (pas d'equivalent Qt Network, Qt Multimedia)",
                    "La communaute est plus petite que celle de Qt ou Electron"
                ]
            },
            "use_cases": (
                "GTK est le choix naturel pour les applications Linux natives,\n"
                "en particulier celles s'integrant a l'environnement GNOME :\n"
                "editeurs de texte (GNOME Text Editor), gestionnaires de\n"
                "fichiers (Nautilus/Files), navigateurs web (GNOME Web/Epiphany),\n"
                "outils systeme, et applications d'entreprise deployees sur\n"
                "des postes Linux. Avec gtk-rs, il attire les developpeurs\n"
                "Rust souhaitant creer des applications desktop."
            ),
            "ecosystem_size": (
                "L'ecosysteme GTK est centre autour de GNOME. libadwaita\n"
                "fournit les widgets et patterns GNOME modernes. GNOME Builder\n"
                "est l'IDE officiel. Flatpak est le format de distribution\n"
                "recommande. Meson est le systeme de build standard. GStreamer\n"
                "gere le multimedia. Les bindings principaux : PyGObject\n"
                "(Python), gtk-rs (Rust), GJS (JavaScript/GNOME), Vala\n"
                "(langage dedie GNOME). Glade est le designer d'interface\n"
                "visuel (remplace par Cambalache pour GTK 4)."
            ),
            "companies": [
                "Red Hat (GNOME, applications systeme RHEL)",
                "Canonical (Ubuntu, certaines applications)",
                "GIMP (editeur d'images)",
                "Inkscape (editeur vectoriel)",
                "GNOME Foundation",
                "Purism (Librem, PureOS)"
            ],
            "code_example": (
                "// Exemple GTK 4 en C\n"
                "#include <gtk/gtk.h>\n\n"
                "static int compte = 0;\n"
                "static GtkWidget *etiquette;\n\n"
                "static void sur_clic(GtkButton *bouton, gpointer donnees) {\n"
                "    compte++;\n"
                "    char texte[50];\n"
                "    g_snprintf(texte, sizeof(texte), \"Compteur : %d\", compte);\n"
                "    gtk_label_set_text(GTK_LABEL(etiquette), texte);\n"
                "}\n\n"
                "static void activer(GtkApplication *app, gpointer donnees) {\n"
                "    GtkWidget *fenetre = gtk_application_window_new(app);\n"
                "    gtk_window_set_title(GTK_WINDOW(fenetre), \"Compteur GTK\");\n"
                "    gtk_window_set_default_size(GTK_WINDOW(fenetre), 300, 200);\n\n"
                "    GtkWidget *boite = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);\n"
                "    gtk_widget_set_margin_start(boite, 20);\n"
                "    gtk_widget_set_margin_end(boite, 20);\n"
                "    gtk_widget_set_margin_top(boite, 20);\n"
                "    gtk_widget_set_margin_bottom(boite, 20);\n\n"
                "    etiquette = gtk_label_new(\"Compteur : 0\");\n"
                "    GtkWidget *bouton = gtk_button_new_with_label(\"Incrementer\");\n"
                "    g_signal_connect(bouton, \"clicked\", G_CALLBACK(sur_clic), NULL);\n\n"
                "    gtk_box_append(GTK_BOX(boite), etiquette);\n"
                "    gtk_box_append(GTK_BOX(boite), bouton);\n"
                "    gtk_window_set_child(GTK_WINDOW(fenetre), boite);\n"
                "    gtk_window_present(GTK_WINDOW(fenetre));\n"
                "}\n\n"
                "int main(int argc, char *argv[]) {\n"
                "    GtkApplication *app = gtk_application_new(\n"
                "        \"fr.exemple.compteur\", G_APPLICATION_DEFAULT_FLAGS);\n"
                "    g_signal_connect(app, \"activate\", G_CALLBACK(activer), NULL);\n"
                "    int statut = g_application_run(G_APPLICATION(app), argc, argv);\n"
                "    g_object_unref(app);\n"
                "    return statut;\n"
                "}"
            ),
            "performance": {
                "startup_time": "Demarrage rapide, comparable a une application native. GTK 4 est plus rapide au lancement que GTK 3 grace a l'optimisation du chargement CSS et des ressources.",
                "throughput": "Performances de rendu excellentes avec GTK 4 grace au rendu GPU (GSK). Les listes virtualisees (GtkListView) gerent efficacement des millions d'elements.",
                "memory": "Consommation memoire raisonnable pour une application native. Inferieure a Qt Widgets dans les cas simples. Le reference counting GObject est efficace mais peut causer des fuites si mal utilise.",
                "concurrency_model": "Boucle d'evenements GMainLoop. Le threading est supporte via GThread mais le toolkit lui-meme n'est pas thread-safe (les operations GUI doivent s'executer dans le thread principal via g_idle_add)."
            },
            "learning_curve": (
                "La courbe d'apprentissage varie selon le langage utilise.\n"
                "En C, elle est elevee : la verbosity de GObject, la gestion\n"
                "manuelle de la memoire et les macros de casting rendent le\n"
                "code complexe. En Python (PyGObject) ou Rust (gtk-rs), la\n"
                "courbe est plus douce. La documentation officielle est\n"
                "correcte mais moins fournie que celle de Qt."
            ),
            "community_size": "Communaute concentree autour de GNOME. Le projet est soutenu par Red Hat, Canonical et des contributeurs benevoles. Les forums GNOME Discourse et Matrix sont les canaux principaux.",
            "job_market": "Demande de niche, principalement dans les entreprises Linux (Red Hat, Canonical, SUSE) et les projets open source. Les postes sont rares mais la concurrence est egalement faible."
        },
        "traits": {
            "performance": 8,
            "developer_speed": 4,
            "learning_curve": 7,
            "ecosystem_size": 5,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 4,
            "scalability": 5
        }
    }
}
