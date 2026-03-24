"""
Module de donnees pour les frameworks et bibliotheques frontend.
Fait partie de l'outil Stack Advisor CLI.
Tout le contenu est redige en francais.
"""

TECHNOLOGIES = {
    "react": {
        "name": "React",
        "category": "frontend",
        "year_created": 2013,
        "creator": "Facebook (Meta)",
        "paradigm": ["Composant", "Declaratif", "Fonctionnel"],
        "typing": "JavaScript (TypeScript optionnel)",
        "sections": {
            "overview": (
                "React est une bibliotheque JavaScript open source concue pour construire des "
                "interfaces utilisateur interactives et dynamiques. Creee par Jordan Walke, un "
                "ingenieur chez Facebook, elle a ete rendue publique en 2013 et a depuis "
                "revolutionne la maniere dont les developpeurs concoivent les applications web. "
                "Le concept central de React repose sur la decomposition de l'interface en "
                "composants reutilisables, chacun gerant son propre etat et son propre rendu. "
                "Cette approche modulaire favorise la maintenabilite, la testabilite et la "
                "reutilisation du code a travers differentes parties d'une application.\n\n"
                "React introduit le concept de Virtual DOM, une representation en memoire de "
                "l'arbre DOM reel du navigateur. Lorsqu'un changement d'etat survient, React "
                "calcule les differences entre le Virtual DOM actuel et le precedent (processus "
                "appele reconciliation), puis applique uniquement les modifications necessaires "
                "au DOM reel. Cette strategie reduit considerablement le nombre d'operations "
                "couteuses sur le DOM et ameliore les performances de rendu.\n\n"
                "Depuis la version 16.8, React propose les Hooks, un mecanisme qui permet "
                "d'utiliser l'etat et d'autres fonctionnalites de React dans des composants "
                "fonctionnels, sans avoir besoin de classes. Les Hooks comme useState, useEffect "
                "et useContext ont profondement transforme les patterns de developpement React, "
                "rendant le code plus concis, plus lisible et plus facile a tester. "
                "L'ecosysteme React est le plus vaste de tous les frameworks frontend, avec "
                "des milliers de bibliotheques tierces, une communaute massive et un support "
                "industriel solide de la part de Meta."
            ),
            "history": (
                "L'histoire de React commence en 2011 lorsque Jordan Walke, ingenieur chez "
                "Facebook, cree un prototype appele FaxJS. Ce prototype visait a resoudre les "
                "problemes de performance et de complexite rencontres par Facebook dans la "
                "gestion de son fil d'actualite, qui necessitait des mises a jour frequentes "
                "et complexes de l'interface utilisateur. Le prototype a ete deploye en interne "
                "sur le fil d'actualite de Facebook en 2011, puis sur Instagram en 2012.\n\n"
                "En mai 2013, React a ete officiellement presente lors de la conference "
                "JSConf US et rendu open source. L'accueil initial fut mitige : beaucoup de "
                "developpeurs etaient sceptiques face au melange de HTML et JavaScript propose "
                "par JSX, considere comme une violation du principe de separation des "
                "responsabilites. Cependant, a mesure que les developpeurs experimentaient "
                "avec la bibliotheque, ses avantages en termes de productivite et de "
                "performance devenaient evidents.\n\n"
                "React 0.14 (2015) a introduit la distinction entre react et react-dom, "
                "preparant le terrain pour React Native. React 15 (2016) a ameliore le "
                "rendu SVG et les messages d'erreur. React 16 (2017), surnomme 'Fiber', "
                "a ete une reecriture complete du moteur de reconciliation, introduisant "
                "le rendu asynchrone et les Error Boundaries. React 16.8 (2019) a apporte "
                "les Hooks, un changement de paradigme majeur. React 17 (2020) s'est "
                "concentre sur les mises a jour progressives. React 18 (2022) a introduit "
                "le rendu concurrent, les transitions automatiques et le Suspense pour le "
                "chargement de donnees. React 19 (2024) a apporte les Server Components, "
                "les Actions et un compilateur optimisant, marquant une nouvelle ere pour "
                "la bibliotheque avec une integration plus profonde du rendu cote serveur."
            ),
            "architecture": (
                "L'architecture de React repose sur plusieurs concepts fondamentaux qui "
                "fonctionnent ensemble pour offrir des performances elevees et une experience "
                "de developpement agreable. Le premier pilier est le Virtual DOM, un arbre "
                "d'objets JavaScript leger qui represente la structure de l'interface. Quand "
                "l'etat d'un composant change, React cree un nouveau Virtual DOM, le compare "
                "avec la version precedente via un algorithme de diffing en O(n), puis genere "
                "une liste minimale de mutations a appliquer au DOM reel.\n\n"
                "Le moteur Fiber, introduit dans React 16, est une reecriture complete de "
                "l'algorithme de reconciliation. Contrairement a l'ancien algorithme recursif "
                "qui etait synchrone et bloquait le thread principal, Fiber decoupe le travail "
                "en unites (fibers) qui peuvent etre interrompues, reprises et priorisees. "
                "Chaque fiber correspond a un noeud dans l'arbre de composants et possede des "
                "pointeurs vers son parent, son premier enfant et son frere suivant, formant "
                "une liste chainee traversable de maniere iterative.\n\n"
                "Le cycle de vie d'un composant React suit plusieurs phases : le montage "
                "(creation et insertion dans le DOM), la mise a jour (re-rendu suite a un "
                "changement de props ou d'etat) et le demontage (suppression du DOM). Avec "
                "les composants fonctionnels et les Hooks, ces phases sont gerees via "
                "useEffect et son mecanisme de nettoyage. Le flux de donnees dans React est "
                "unidirectionnel : les donnees descendent des composants parents vers les "
                "enfants via les props, tandis que les evenements remontent via des callbacks. "
                "Ce flux previsible simplifie le debogage et le raisonnement sur l'etat de "
                "l'application. Le rendu concurrent de React 18 permet de preparer plusieurs "
                "versions de l'interface simultanement, offrant des transitions fluides et "
                "une reactivite accrue meme lors de mises a jour complexes."
            ),
            "pros_cons": {
                "pros": [
                    "Ecosysteme extremement riche avec des milliers de bibliotheques tierces",
                    "Communaute massive offrant documentation, tutoriels et support abondants",
                    "Virtual DOM performant pour les interfaces complexes avec mises a jour frequentes",
                    "Reutilisabilite elevee des composants a travers differents projets",
                    "Hooks permettant une logique composable, testable et reutilisable",
                    "React Native permet le developpement mobile multiplateforme avec les memes concepts",
                    "Support industriel solide de Meta et adoption par des milliers d'entreprises",
                    "Server Components (React 19) ouvrent de nouvelles possibilites d'optimisation",
                ],
                "cons": [
                    "N'est qu'une bibliotheque de vue : necessite des choix supplementaires pour le routage, la gestion d'etat, etc.",
                    "JSX melange HTML et JavaScript, ce qui peut derouter les debutants",
                    "Taille du bundle initiale importante sans optimisation et tree-shaking",
                    "Rythme rapide d'evolution pouvant entrainer de la fatigue chez les developpeurs",
                    "La flexibilite excessive peut mener a des architectures inconsistantes en equipe",
                    "Performance par defaut inferieure aux approches compilees comme Svelte",
                    "Complexite de la gestion d'etat global (Redux, Zustand, Jotai, etc.)",
                ],
            },
            "use_cases": (
                "React excelle dans les applications web interactives a page unique (SPA) ou "
                "les mises a jour de l'interface sont frequentes et complexes. Il est "
                "particulierement adapte aux tableaux de bord, aux reseaux sociaux, aux outils "
                "collaboratifs en temps reel et aux applications e-commerce riches. Grace a "
                "React Native, il permet egalement le developpement d'applications mobiles "
                "multiplateformes (iOS et Android) en partageant une grande partie de la "
                "logique metier. Combine avec Next.js, React est aussi un excellent choix "
                "pour les sites necessitant du rendu cote serveur (SSR) ou de la generation "
                "statique (SSG), comme les blogs, les sites marketing et les applications "
                "orientees contenu necessitant un bon referencement (SEO)."
            ),
            "ecosystem": (
                "L'ecosysteme React est le plus vaste du monde frontend. Pour la gestion "
                "d'etat, on retrouve Redux (et Redux Toolkit), Zustand, Jotai, Recoil et "
                "MobX. Le routage est assure par React Router ou TanStack Router. Pour le "
                "fetching de donnees, TanStack Query (React Query), SWR et Apollo Client "
                "(GraphQL) sont les solutions les plus populaires. Cote formulaires, React "
                "Hook Form et Formik dominent. Pour les tests, Jest, React Testing Library, "
                "Vitest et Cypress sont largement utilises. Les bibliotheques d'interface "
                "incluent Material UI (MUI), Ant Design, Chakra UI, Shadcn/UI et Radix UI. "
                "Le styling peut etre gere via CSS Modules, Tailwind CSS, Styled Components "
                "ou Emotion. Pour le bundling, Vite a largement remplace Create React App "
                "comme outil de demarrage recommande."
            ),
            "companies": [
                "Facebook (Meta)",
                "Netflix",
                "Airbnb",
                "Uber",
                "Discord",
                "Dropbox",
                "Twitter (X)",
                "Shopify",
                "Notion",
            ],
            "code_example": (
                "import { useState, useEffect } from 'react';\n\n"
                "function TaskList() {\n"
                "  const [tasks, setTasks] = useState([]);\n"
                "  const [input, setInput] = useState('');\n\n"
                "  useEffect(() => {\n"
                "    const saved = localStorage.getItem('tasks');\n"
                "    if (saved) setTasks(JSON.parse(saved));\n"
                "  }, []);\n\n"
                "  useEffect(() => {\n"
                "    localStorage.setItem('tasks', JSON.stringify(tasks));\n"
                "  }, [tasks]);\n\n"
                "  const addTask = () => {\n"
                "    if (input.trim()) {\n"
                "      setTasks([...tasks, { id: Date.now(), text: input, done: false }]);\n"
                "      setInput('');\n"
                "    }\n"
                "  };\n\n"
                "  const toggleTask = (id) => {\n"
                "    setTasks(tasks.map(t =>\n"
                "      t.id === id ? { ...t, done: !t.done } : t\n"
                "    ));\n"
                "  };\n\n"
                "  return (\n"
                "    <div>\n"
                "      <h1>Liste de taches</h1>\n"
                "      <input value={input} onChange={e => setInput(e.target.value)} />\n"
                "      <button onClick={addTask}>Ajouter</button>\n"
                "      <ul>\n"
                "        {tasks.map(task => (\n"
                "          <li key={task.id} onClick={() => toggleTask(task.id)}\n"
                "              style={{ textDecoration: task.done ? 'line-through' : 'none' }}>\n"
                "            {task.text}\n"
                "          </li>\n"
                "        ))}\n"
                "      </ul>\n"
                "    </div>\n"
                "  );\n"
                "}\n\n"
                "export default TaskList;"
            ),
            "performance": {
                "startup_time": (
                    "Le temps de demarrage de React depend fortement de la taille du bundle. "
                    "Le runtime React pese environ 40-45 Ko (minifie et gzippe). Le premier "
                    "rendu necessite le parsing du JavaScript, la construction du Virtual DOM "
                    "et la reconciliation initiale. Les techniques de code splitting, de lazy "
                    "loading (React.lazy et Suspense) et de prerendu cote serveur permettent "
                    "de reduire significativement le temps d'affichage initial."
                ),
                "throughput": (
                    "React offre de bonnes performances de rendu grace au Virtual DOM et au "
                    "batching automatique des mises a jour (ameliore en React 18). Pour les "
                    "listes longues, react-window ou react-virtuoso permettent la virtualisation. "
                    "Le rendu concurrent de React 18 evite le blocage de l'interface lors de "
                    "mises a jour lourdes en les decoupant en tranches interruptibles."
                ),
                "memory": (
                    "Le Virtual DOM consomme de la memoire supplementaire par rapport a une "
                    "manipulation directe du DOM. Chaque composant, chaque fiber et chaque "
                    "hook occupe de l'espace en memoire. Les fuites memoire sont possibles "
                    "si les effets (useEffect) ne sont pas correctement nettoyes ou si des "
                    "closures capturent des references obsoletes."
                ),
                "concurrency_model": (
                    "React 18 introduit le rendu concurrent (Concurrent Rendering), qui permet "
                    "de preparer des mises a jour en arriere-plan sans bloquer le thread "
                    "principal. Les transitions (useTransition, startTransition) marquent "
                    "certaines mises a jour comme non urgentes, permettant a React de prioriser "
                    "les interactions utilisateur. Le Suspense permet de gerer les etats de "
                    "chargement de maniere declarative."
                ),
            },
            "learning_curve": (
                "La courbe d'apprentissage de React est moderee. Les concepts de base "
                "(composants, props, state, JSX) sont accessibles aux developpeurs ayant "
                "des bases en JavaScript et HTML. Cependant, la maitrise des Hooks avances "
                "(useReducer, useMemo, useCallback, useRef), des patterns de composition, "
                "de la gestion d'etat global et de l'optimisation des performances necessite "
                "un investissement significatif. La comprehension du fonctionnement interne "
                "du Virtual DOM, de la reconciliation et du rendu concurrent demande une "
                "experience approfondie. De plus, comme React n'est qu'une bibliotheque de "
                "vue, le developpeur doit faire des choix architecturaux et apprendre des "
                "outils complementaires (routeur, gestionnaire d'etat, solution CSS), ce "
                "qui ajoute a la complexite globale de l'apprentissage."
            ),
            "community_size": (
                "React possede la plus grande communaute de tous les frameworks frontend. "
                "Avec plus de 230 000 etoiles sur GitHub, des millions de telechargements "
                "hebdomadaires sur npm et des centaines de milliers de questions sur Stack "
                "Overflow, c'est l'outil le plus documente et le plus discute de l'ecosysteme "
                "JavaScript. La communaute est active, diversifiee et repartie sur tous les "
                "continents, avec de nombreuses conferences dediees (React Conf, React Summit, "
                "React Day Berlin, etc.)."
            ),
            "job_market": (
                "React domine largement le marche de l'emploi frontend. Il est mentionne dans "
                "la majorite des offres d'emploi pour des postes de developpeur frontend ou "
                "fullstack. Les salaires pour les developpeurs React sont parmi les plus "
                "eleves du secteur web, en raison de la forte demande et de l'adoption "
                "massive par les entreprises de toutes tailles, des startups aux grandes "
                "multinationales. La connaissance de React est souvent consideree comme un "
                "prerequis dans l'industrie du developpement web."
            ),
        },
        "traits": {
            "performance": 7,
            "developer_speed": 7,
            "learning_curve": 5,
            "ecosystem_size": 10,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 8,
        },
    },

    "vue": {
        "name": "Vue.js",
        "category": "frontend",
        "year_created": 2014,
        "creator": "Evan You",
        "paradigm": ["Composant", "Declaratif", "Reactif"],
        "typing": "JavaScript (TypeScript optionnel, support natif depuis Vue 3)",
        "sections": {
            "overview": (
                "Vue.js est un framework JavaScript progressif concu pour construire des "
                "interfaces utilisateur. Cree par Evan You en 2014, alors ancien ingenieur "
                "chez Google ayant travaille sur AngularJS, Vue a ete pense pour extraire "
                "les meilleures idees des frameworks existants tout en restant leger et "
                "accessible. Le terme 'progressif' est central dans la philosophie de Vue : "
                "il signifie que le framework peut etre adopte incrementalement, d'un simple "
                "script ajoute a une page HTML existante jusqu'a une application monopage "
                "complexe avec routage, gestion d'etat et rendu cote serveur.\n\n"
                "Le systeme de reactivite de Vue est au coeur de son fonctionnement. Dans "
                "Vue 3, il repose sur les Proxies JavaScript (ES2015), qui permettent de "
                "detecter automatiquement les lectures et les ecritures sur les donnees "
                "reactives. Quand une propriete reactive est lue dans un composant, Vue "
                "enregistre une dependance. Quand cette propriete est modifiee, Vue sait "
                "exactement quels composants doivent etre re-rendus, sans avoir besoin "
                "d'un mecanisme de diffing complet comme le Virtual DOM de React.\n\n"
                "Vue se distingue par sa documentation exceptionnelle, consideree comme "
                "une reference dans le monde du developpement web. La syntaxe des Single "
                "File Components (SFC) avec les fichiers .vue permet de regrouper template, "
                "logique et style dans un meme fichier, offrant une experience de "
                "developpement cohesive. L'API Composition, introduite dans Vue 3, offre "
                "une alternative flexible a l'API Options, permettant une meilleure "
                "reutilisation de la logique et un support TypeScript ameliore. Vue est "
                "particulierement apprecie en Asie (Chine, Japon, Coree) ainsi qu'en "
                "Europe, et beneficie d'un ecosysteme officiel bien maintenu."
            ),
            "history": (
                "Evan You a commence a developper Vue fin 2013, alors qu'il travaillait chez "
                "Google sur des projets utilisant AngularJS. Il souhaitait creer un outil "
                "qui reprendrait les aspects positifs d'Angular (binding de donnees, templates "
                "declaratifs) tout en eliminant la complexite excessive et les concepts "
                "abstraits difficiles a apprehender. La premiere version publique de Vue "
                "(0.8) a ete lancee en fevrier 2014.\n\n"
                "Vue 1.0 (octobre 2015), surnomme 'Evangelion', a introduit un systeme de "
                "composants mature et des transitions integrees. Vue 2.0 (septembre 2016), "
                "surnomme 'Ghost in the Shell', a ete une reecriture majeure introduisant "
                "le Virtual DOM (inspire de React), les fonctions de rendu et une amelioration "
                "significative des performances. Cette version a propulse Vue dans le trio de "
                "tete des frameworks frontend aux cotes de React et Angular.\n\n"
                "Vue 3.0 (septembre 2020), surnomme 'One Piece', a marque une nouvelle ere "
                "avec une reecriture complete en TypeScript, un nouveau systeme de reactivite "
                "base sur les Proxies, l'API Composition (inspiree des Hooks de React mais "
                "avec une approche distincte), le Teleport, Suspense et les Fragments. Le "
                "moteur de rendu a ete rendu modulaire, permettant des cibles de rendu "
                "personnalisees. Vue 3.3 et 3.4 ont ameliore le support TypeScript avec "
                "des macros de type dans les SFC. Vue 3.5 (2024) a apporte des optimisations "
                "du systeme de reactivite et de nouvelles fonctionnalites pour les composants. "
                "Evan You a egalement cree Vite, un outil de build nouvelle generation qui "
                "est devenu un standard au-dela de l'ecosysteme Vue, utilise aussi par React, "
                "Svelte et d'autres frameworks."
            ),
            "architecture": (
                "L'architecture de Vue repose sur un systeme de reactivite granulaire qui "
                "constitue sa principale innovation technique. Dans Vue 3, chaque propriete "
                "reactive est enveloppee dans un Proxy JavaScript. Lorsqu'un composant "
                "s'execute (rendu), Vue trace automatiquement quelles proprietes reactives "
                "sont accedees (tracking de dependances). Quand une propriete est modifiee, "
                "Vue declenche uniquement les effets et les composants qui dependent de cette "
                "propriete specifique, offrant une mise a jour tres ciblee.\n\n"
                "Vue utilise egalement un Virtual DOM, mais son approche est optimisee par "
                "rapport a React grace au compilateur de templates. Le compilateur analyse "
                "les templates au moment du build et genere du code de rendu optimise qui "
                "marque les parties statiques (hoisting statique) et les parties dynamiques, "
                "reduisant considerablement le travail de diffing a l'execution. Cette "
                "compilation informed (compiler-informed) est un avantage unique de Vue.\n\n"
                "Les Single File Components (SFC) sont le format de fichier standard de Vue. "
                "Un fichier .vue contient trois sections : <template> pour le HTML declaratif, "
                "<script> pour la logique (avec l'API Options ou l'API Composition) et <style> "
                "pour le CSS (avec support scoped pour l'encapsulation). L'API Composition "
                "organise le code par fonctionnalite logique plutot que par type d'option "
                "(data, methods, computed, watch), facilitant l'extraction et la reutilisation "
                "de logique via des 'composables' (equivalent aux custom hooks de React). "
                "Le systeme de reactivite de Vue avec ref() et reactive() offre un controle "
                "fin et explicite sur la reactivite, evitant les pieges courants comme les "
                "re-rendus excessifs que l'on peut rencontrer avec React."
            ),
            "pros_cons": {
                "pros": [
                    "Documentation exceptionnelle, claire et complete, ideale pour l'apprentissage",
                    "Courbe d'apprentissage douce : syntaxe intuitive et progressive",
                    "Systeme de reactivite granulaire performant et elegant",
                    "Single File Components offrant une excellente experience de developpement",
                    "Ecosysteme officiel coherent (Vue Router, Pinia, Vite, Vitest)",
                    "API Composition permettant une reutilisation avancee de la logique",
                    "Support TypeScript natif et de qualite dans Vue 3",
                    "Compilateur de templates optimisant automatiquement le code de rendu",
                ],
                "cons": [
                    "Ecosysteme tiers moins vaste que celui de React",
                    "Moins d'offres d'emploi que React dans les marches occidentaux",
                    "Migration de Vue 2 a Vue 3 complexe et couteuse pour les grands projets",
                    "Moins de ressources et de tutoriels disponibles en comparaison avec React",
                    "Quelques bibliotheques de l'ecosysteme Vue 2 n'ont pas ete portees vers Vue 3",
                    "La communaute, bien que dynamique, est plus petite que celle de React",
                ],
            },
            "use_cases": (
                "Vue.js est ideal pour les applications web de taille petite a moyenne, "
                "les prototypes rapides et les projets ou la vitesse de developpement est "
                "prioritaire. Il excelle dans les tableaux de bord d'administration, les "
                "interfaces internes d'entreprise et les applications progressives. Grace "
                "a Nuxt.js, Vue est egalement performant pour les sites avec rendu cote "
                "serveur (SSR), la generation de sites statiques (SSG) et les applications "
                "hybrides. Vue est aussi tres utilise dans l'ecosysteme Laravel (PHP) comme "
                "framework frontend de choix. Il convient parfaitement aux equipes qui "
                "souhaitent un framework opinione mais flexible, avec une courbe d'apprentissage "
                "accessible pour les nouveaux developpeurs."
            ),
            "ecosystem": (
                "L'ecosysteme officiel de Vue est remarquablement coherent. Pinia est le "
                "gestionnaire d'etat officiel (successeur de Vuex), offrant une API simple "
                "et un excellent support TypeScript. Vue Router est le routeur officiel. "
                "Vite, cree par Evan You, est l'outil de build recommande, offrant un "
                "demarrage quasi instantane en developpement grace aux modules ES natifs. "
                "Vitest est le framework de test unite rapide base sur Vite. Nuxt.js est "
                "le meta-framework pour le SSR et le SSG. VueUse est une collection de "
                "composables utilitaires tres populaire. Pour les composants UI, Vuetify, "
                "PrimeVue, Naive UI et Element Plus sont les choix principaux. Vue Devtools "
                "est une extension navigateur officielle pour le debogage."
            ),
            "companies": [
                "Alibaba",
                "Xiaomi",
                "GitLab",
                "Nintendo",
                "BMW",
                "Louis Vuitton",
                "Adobe",
                "Grammarly",
            ],
            "code_example": (
                "<script setup>\n"
                "import { ref, computed } from 'vue'\n\n"
                "const tasks = ref([])\n"
                "const input = ref('')\n\n"
                "const completedCount = computed(() =>\n"
                "  tasks.value.filter(t => t.done).length\n"
                ")\n\n"
                "function addTask() {\n"
                "  if (input.value.trim()) {\n"
                "    tasks.value.push({\n"
                "      id: Date.now(),\n"
                "      text: input.value,\n"
                "      done: false\n"
                "    })\n"
                "    input.value = ''\n"
                "  }\n"
                "}\n\n"
                "function toggleTask(id) {\n"
                "  const task = tasks.value.find(t => t.id === id)\n"
                "  if (task) task.done = !task.done\n"
                "}\n"
                "</script>\n\n"
                "<template>\n"
                "  <div>\n"
                "    <h1>Liste de taches ({{ completedCount }} terminees)</h1>\n"
                "    <input v-model=\"input\" @keyup.enter=\"addTask\" />\n"
                "    <button @click=\"addTask\">Ajouter</button>\n"
                "    <ul>\n"
                "      <li v-for=\"task in tasks\" :key=\"task.id\"\n"
                "          @click=\"toggleTask(task.id)\"\n"
                "          :class=\"{ done: task.done }\">\n"
                "        {{ task.text }}\n"
                "      </li>\n"
                "    </ul>\n"
                "  </div>\n"
                "</template>\n\n"
                "<style scoped>\n"
                ".done { text-decoration: line-through; color: gray; }\n"
                "</style>"
            ),
            "performance": {
                "startup_time": (
                    "Vue est plus leger que React avec un runtime d'environ 33 Ko (minifie "
                    "et gzippe). Le compilateur de templates genere du code optimise qui "
                    "reduit le travail a l'execution. Le tree-shaking natif de Vue 3 permet "
                    "de n'inclure que les fonctionnalites reellement utilisees, reduisant "
                    "encore la taille du bundle."
                ),
                "throughput": (
                    "Le systeme de reactivite granulaire de Vue evite les re-rendus "
                    "inutiles en ne mettant a jour que les composants dependant des donnees "
                    "modifiees. Le hoisting statique du compilateur elimine le cout de "
                    "comparaison pour les parties invariables du template. Ces optimisations "
                    "combinées offrent d'excellentes performances de rendu."
                ),
                "memory": (
                    "Vue 3 est plus econome en memoire que Vue 2 grace a son architecture "
                    "modulaire et son systeme de reactivite base sur les Proxies. Les Proxies "
                    "permettent une reactivite a la demande plutot qu'une observation "
                    "systematique de toutes les proprietes, reduisant l'empreinte memoire "
                    "pour les grands objets de donnees."
                ),
                "concurrency_model": (
                    "Vue ne propose pas de mecanisme de rendu concurrent comparable a celui "
                    "de React 18. Les mises a jour sont traitees de maniere synchrone mais "
                    "groupees efficacement dans un meme tick du micro-task queue via "
                    "nextTick(). Pour les operations lourdes, il revient au developpeur "
                    "d'utiliser des Web Workers ou de decouper le travail manuellement."
                ),
            },
            "learning_curve": (
                "Vue est repute pour sa courbe d'apprentissage parmi les plus douces du "
                "monde des frameworks frontend. La syntaxe de template basee sur le HTML "
                "est immediatement familiere aux developpeurs web. Les directives comme "
                "v-if, v-for et v-model sont intuitives et bien documentees. L'API Options "
                "organise le code de maniere claire avec data, methods, computed et watch. "
                "La progression vers l'API Composition est naturelle et introduit des "
                "concepts plus avances (ref, reactive, composables) de maniere incrementale. "
                "La documentation officielle est consideree comme l'une des meilleures de "
                "l'industrie, avec des exemples interactifs, des guides detailles et un "
                "tutoriel pas-a-pas. Un developpeur junior peut devenir productif en quelques "
                "jours, tandis que la maitrise complete du framework et de son ecosysteme "
                "necessite quelques semaines."
            ),
            "community_size": (
                "Vue possede une communaute active et passionnee, avec plus de 210 000 "
                "etoiles sur GitHub (un des projets les plus staries). La communaute est "
                "particulierement forte en Asie (Chine, Japon, Coree du Sud) et en Europe. "
                "Les conferences VueConf, Vue.js Amsterdam et Vue.js Nation rassemblent "
                "des milliers de developpeurs. Le forum officiel, Discord et les reseaux "
                "sociaux sont des lieux d'echange actifs."
            ),
            "job_market": (
                "Le marche de l'emploi Vue est solide, surtout en Europe et en Asie. "
                "Il se situe en deuxieme ou troisieme position derriere React selon les "
                "regions. Vue est tres demande dans l'ecosysteme PHP/Laravel et dans les "
                "entreprises de taille moyenne. Les salaires sont comparables a ceux de "
                "React dans les marches ou Vue est bien etabli. La demande croit "
                "regulierement, portee par l'adoption croissante de Vue 3 et Nuxt 3."
            ),
        },
        "traits": {
            "performance": 7,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 7,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 7,
        },
    },

    "angular": {
        "name": "Angular",
        "category": "frontend",
        "year_created": 2016,
        "creator": "Google",
        "paradigm": ["Composant", "Declaratif", "Oriente objet", "Reactif"],
        "typing": "TypeScript (obligatoire)",
        "sections": {
            "overview": (
                "Angular est un framework frontend complet et opinione developpe par Google. "
                "Contrairement a React (bibliotheque) ou Vue (framework progressif), Angular "
                "fournit une solution integrale pour le developpement d'applications web "
                "d'entreprise : routage, gestion de formulaires, client HTTP, injection de "
                "dependances, tests unitaires et end-to-end, internationalisation et bien "
                "plus sont inclus nativement. Cette approche 'batteries incluses' garantit "
                "la coherence architecturale et reduit le nombre de decisions techniques "
                "a prendre lors du demarrage d'un projet.\n\n"
                "Angular impose l'utilisation de TypeScript, ce qui offre un typage statique "
                "robuste, une meilleure autocompletion dans les IDE, une detection precoce "
                "des erreurs et une refactorisation facilitee. Le framework repose fortement "
                "sur des concepts de programmation orientee objet : classes, decorateurs, "
                "injection de dependances et modules. Il integre RxJS pour la programmation "
                "reactive, offrant un modele puissant pour gerer les flux de donnees "
                "asynchrones, les evenements utilisateur et les requetes HTTP.\n\n"
                "La philosophie d'Angular est de fournir un cadre strict et structure "
                "qui guide les developpeurs vers des pratiques coherentes. Bien que cette "
                "approche augmente la courbe d'apprentissage initiale, elle s'avere "
                "particulierement benefique pour les grandes equipes et les projets a "
                "long terme, ou la coherence du code et la maintenabilite sont cruciales. "
                "Le CLI Angular (ng) est un outil en ligne de commande puissant qui "
                "genere automatiquement composants, services, modules et autres artefacts, "
                "assurant le respect des conventions du framework. Angular est utilise "
                "par de nombreuses entreprises du Fortune 500 pour des applications "
                "critiques de grande envergure."
            ),
            "history": (
                "L'histoire d'Angular est marquee par une rupture majeure entre AngularJS "
                "(Angular 1.x, 2010) et Angular (2+, 2016). AngularJS, cree par Misko Hevery "
                "chez Google, a ete l'un des premiers frameworks SPA populaires. Il a "
                "introduit le two-way data binding, les directives et l'injection de "
                "dependances dans le monde du developpement web. Cependant, ses limitations "
                "de performance (cycle de digest couteux) et architecturales sont devenues "
                "evidentes avec la croissance des applications.\n\n"
                "Google a alors decide de reecrire completement le framework. Angular 2 "
                "(septembre 2016) est un produit entierement nouveau, ecrit en TypeScript, "
                "avec une architecture basee sur les composants et un systeme de detection "
                "de changements radicalement different. Cette rupture a ete controversee car "
                "il n'y avait aucune compatibilite ascendante avec AngularJS, forcant des "
                "migrations couteuses.\n\n"
                "Depuis Angular 2, le framework suit un cycle de release semestriel previsible. "
                "Angular 4 (2017) a ameliore les animations et le compilateur AOT. Angular 6 "
                "(2018) a introduit les schematics et le CLI workspace. Angular 8 (2019) a "
                "apporte le lazy loading par defaut avec import() dynamique. Angular 9 (2020) "
                "a active Ivy, le nouveau moteur de rendu, par defaut. Angular 14 (2022) a "
                "introduit les standalone components, eliminant progressivement le besoin de "
                "NgModules. Angular 16 (2023) a introduit les Signals, un nouveau modele "
                "de reactivite granulaire inspire de Solid.js et Vue. Angular 17 (2023) a "
                "apporte la nouvelle syntaxe de flux de controle (@if, @for, @switch) et "
                "le rendu differe (@defer). Angular 18 et 19 (2024) ont continue a "
                "moderniser le framework avec des Signals plus matures et des optimisations "
                "de performance significatives."
            ),
            "architecture": (
                "L'architecture d'Angular est basee sur plusieurs piliers fondamentaux. Les "
                "composants sont les briques de construction de l'interface : chaque composant "
                "est une classe TypeScript decoree par @Component, associee a un template "
                "HTML et optionnellement a des styles CSS. Les composants sont organises en "
                "arbre hierarchique, chaque composant ayant un cycle de vie complet (ngOnInit, "
                "ngOnChanges, ngOnDestroy, etc.).\n\n"
                "L'injection de dependances (DI) est un mecanisme central d'Angular. Les "
                "services sont des classes decorees par @Injectable qui encapsulent la logique "
                "metier, l'acces aux donnees et les fonctionnalites partagees. Le systeme de "
                "DI hierarchique d'Angular permet de fournir des instances de services a "
                "differents niveaux de l'arbre de composants, offrant flexibilite et controle "
                "sur le scope des donnees.\n\n"
                "La detection de changements dans Angular est un mecanisme qui parcourt "
                "l'arbre de composants pour verifier si les donnees ont change et si le "
                "DOM doit etre mis a jour. Par defaut, Angular utilise la strategie "
                "CheckAlways, qui verifie chaque composant a chaque cycle. La strategie "
                "OnPush, combinee avec des Observables RxJS ou des Signals, optimise "
                "drastiquement les performances en ne verifiant un composant que lorsque "
                "ses entrees changent ou qu'un evenement est emis.\n\n"
                "Les Signals, introduits a partir d'Angular 16, representent un nouveau "
                "modele de reactivite qui remplacera progressivement la detection de "
                "changements classique basee sur Zone.js. Un Signal est une valeur "
                "reactive qui notifie automatiquement les consommateurs (composants, "
                "computed signals, effects) lorsqu'elle change, permettant des mises "
                "a jour tres granulaires et performantes sans le surcout de Zone.js. "
                "Cette evolution rapproche Angular des modeles de reactivite de Vue et "
                "Solid.js."
            ),
            "pros_cons": {
                "pros": [
                    "Framework complet 'batteries incluses' : routage, formulaires, HTTP, DI, i18n integres",
                    "TypeScript obligatoire garantissant un typage fort et une detection precoce des erreurs",
                    "Injection de dependances puissante favorisant la testabilite et la modularite",
                    "CLI Angular riche automatisant la generation de code et les bonnes pratiques",
                    "Architecture coherente et opinione, ideale pour les grandes equipes",
                    "RxJS integre pour une gestion avancee des flux asynchrones",
                    "Support long terme (LTS) et cycle de release previsible",
                    "Signals modernisant la reactivite avec des performances granulaires",
                ],
                "cons": [
                    "Courbe d'apprentissage tres prononcee : TypeScript, RxJS, DI, decorateurs, modules",
                    "Verbeux et ceremonial : beaucoup de code boilerplate meme pour des taches simples",
                    "Bundle initial plus volumineux que React ou Vue",
                    "RxJS peut etre complexe a maitriser pour les developpeurs debutants",
                    "Migrations majeures parfois couteuses entre versions",
                    "Moins flexible que React pour les choix architecturaux non standards",
                    "Ecosysteme tiers moins diversifie que celui de React",
                ],
            },
            "use_cases": (
                "Angular est le choix de predilection pour les applications d'entreprise "
                "de grande envergure, les systemes internes complexes, les portails "
                "d'administration, les applications bancaires et financieres, et les "
                "plateformes e-commerce a fort trafic. Son architecture structuree et "
                "son typage strict en font un excellent choix pour les equipes nombreuses "
                "travaillant sur des projets a long terme. Angular est egalement adapte "
                "aux applications necessitant des formulaires complexes avec validation "
                "avancee, des flux de donnees asynchrones sophistiques (grace a RxJS) et "
                "une internationalisation native. Les Progressive Web Apps (PWA) sont "
                "bien supportees grace a @angular/pwa."
            ),
            "ecosystem": (
                "Angular fournit un ecosysteme officiel complet. Angular Router gere le "
                "routage avec lazy loading, guards et resolvers. Angular Forms offre deux "
                "approches : les formulaires pilotes par le template (template-driven) et "
                "les formulaires reactifs (reactive forms). HttpClient est le client HTTP "
                "integre basee sur RxJS. Angular Material est la bibliotheque de composants "
                "UI officielle implementant Material Design. NgRx est le gestionnaire d'etat "
                "inspire de Redux pour Angular, utilisant RxJS et les Signals. Angular CDK "
                "(Component Dev Kit) fournit des primitives pour creer des composants "
                "accessibles. Nx est un outil de monorepo puissant tres utilise avec Angular. "
                "Pour les tests, Jasmine et Karma sont integres par defaut, mais Jest et "
                "Cypress sont de plus en plus adoptes."
            ),
            "companies": [
                "Google",
                "Microsoft (Office 365)",
                "Deutsche Bank",
                "Samsung",
                "Forbes",
                "Upwork",
                "PayPal",
                "BMW",
            ],
            "code_example": (
                "import { Component, signal, computed } from '@angular/core';\n\n"
                "interface Task {\n"
                "  id: number;\n"
                "  text: string;\n"
                "  done: boolean;\n"
                "}\n\n"
                "@Component({\n"
                "  selector: 'app-task-list',\n"
                "  standalone: true,\n"
                "  template: `\n"
                "    <h1>Liste de taches ({{ completedCount() }} terminees)</h1>\n"
                "    <input [(ngModel)]=\"inputText\" (keyup.enter)=\"addTask()\" />\n"
                "    <button (click)=\"addTask()\">Ajouter</button>\n"
                "    <ul>\n"
                "      @for (task of tasks(); track task.id) {\n"
                "        <li (click)=\"toggleTask(task.id)\"\n"
                "            [class.done]=\"task.done\">\n"
                "          {{ task.text }}\n"
                "        </li>\n"
                "      }\n"
                "    </ul>\n"
                "  `,\n"
                "  styles: [`.done { text-decoration: line-through; color: gray; }`]\n"
                "})\n"
                "export class TaskListComponent {\n"
                "  tasks = signal<Task[]>([]);\n"
                "  inputText = '';\n\n"
                "  completedCount = computed(() =>\n"
                "    this.tasks().filter(t => t.done).length\n"
                "  );\n\n"
                "  addTask() {\n"
                "    if (this.inputText.trim()) {\n"
                "      this.tasks.update(tasks => [\n"
                "        ...tasks,\n"
                "        { id: Date.now(), text: this.inputText, done: false }\n"
                "      ]);\n"
                "      this.inputText = '';\n"
                "    }\n"
                "  }\n\n"
                "  toggleTask(id: number) {\n"
                "    this.tasks.update(tasks =>\n"
                "      tasks.map(t => t.id === id ? { ...t, done: !t.done } : t)\n"
                "    );\n"
                "  }\n"
                "}"
            ),
            "performance": {
                "startup_time": (
                    "Angular a historiquement un temps de demarrage plus long que React ou "
                    "Vue en raison de la taille de son runtime. La compilation AOT "
                    "(Ahead-of-Time) reduit ce temps en pre-compilant les templates au moment "
                    "du build. Le tree-shaking du compilateur Ivy elimine le code non utilise. "
                    "Le lazy loading des modules permet de ne charger que le code necessaire "
                    "pour la route active."
                ),
                "throughput": (
                    "Les performances de rendu d'Angular se sont considerablement ameliorees "
                    "avec Ivy et les Signals. La strategie OnPush combinee avec les Signals "
                    "permet des mises a jour tres ciblees. Le rendu differe (@defer) permet "
                    "de charger des parties de la page uniquement quand elles deviennent "
                    "visibles ou necessaires, ameliorant le temps d'affichage initial."
                ),
                "memory": (
                    "Angular consomme plus de memoire que des frameworks plus legers en raison "
                    "de son runtime complet, de Zone.js (en voie de deprecation) et de "
                    "l'infrastructure d'injection de dependances. L'adoption des Signals et "
                    "la suppression progressive de Zone.js devraient reduire significativement "
                    "l'empreinte memoire dans les versions futures."
                ),
                "concurrency_model": (
                    "Angular s'appuie sur RxJS pour la gestion de la concurrence et de "
                    "l'asynchronisme. Les Observables permettent de modeliser des flux de "
                    "donnees complexes, de gerer les annulations, les debounces, les "
                    "combinaisons de flux et les retries. Cette approche est puissante "
                    "mais ajoute une complexite significative. Les Signals offriront une "
                    "alternative plus simple pour de nombreux cas d'usage."
                ),
            },
            "learning_curve": (
                "Angular possede la courbe d'apprentissage la plus prononcee des principaux "
                "frameworks frontend. Le developpeur doit maitriser TypeScript (obligatoire), "
                "les concepts de programmation orientee objet, les decorateurs, l'injection "
                "de dependances, RxJS et la programmation reactive, le systeme de modules "
                "(ou les standalone components), le routage avance, les formulaires reactifs "
                "et la detection de changements. Chacun de ces concepts necessite un "
                "investissement significatif. Cependant, une fois ces concepts maitrises, "
                "le developpeur dispose d'un cadre extremement puissant et coherent. "
                "Angular est souvent recommande aux developpeurs ayant une experience "
                "prealable en Java, C# ou d'autres langages orientes objet, car les "
                "patterns sont familiers. La documentation officielle est complete et "
                "le CLI facilite le demarrage, mais la courbe reste raide pour les "
                "debutants en developpement web."
            ),
            "community_size": (
                "Angular possede une communaute large et mature, soutenue par Google. "
                "Avec environ 97 000 etoiles sur GitHub, il est moins populaire que React "
                "ou Vue en termes de stars, mais tres solidement ancre dans l'ecosysteme "
                "d'entreprise. Les conferences ng-conf, Angular Connect et AngularNL "
                "rassemblent des milliers de developpeurs. La communaute est particulierement "
                "active dans les grandes entreprises et les milieux corporate."
            ),
            "job_market": (
                "Angular est tres demande dans les grandes entreprises, les banques, les "
                "administrations publiques et les societes de consulting. Il est souvent "
                "le framework de choix pour les projets d'envergure necessitant structure "
                "et maintenabilite a long terme. Les salaires sont comparables a ceux de "
                "React, avec une forte demande dans les secteurs bancaire, financier et "
                "gouvernemental. Le nombre d'offres est globalement inferieur a React "
                "mais reste substantial dans les marches d'entreprise."
            ),
        },
        "traits": {
            "performance": 6,
            "developer_speed": 5,
            "learning_curve": 7,
            "ecosystem_size": 8,
            "type_safety": 8,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 9,
        },
    },

    "svelte": {
        "name": "Svelte",
        "category": "frontend",
        "year_created": 2016,
        "creator": "Rich Harris",
        "paradigm": ["Composant", "Declaratif", "Compile", "Reactif"],
        "typing": "JavaScript (TypeScript supporte)",
        "sections": {
            "overview": (
                "Svelte est un framework frontend radicalement different de ses concurrents. "
                "Cree par Rich Harris en 2016, alors journaliste et developpeur au New York "
                "Times, Svelte adopte une approche de compilation plutot que d'interpretation. "
                "Contrairement a React ou Vue qui embarquent un runtime (Virtual DOM, systeme "
                "de reactivite) dans le navigateur, Svelte compile les composants en code "
                "JavaScript imperatif hautement optimise au moment du build. Le resultat est "
                "un code qui manipule directement le DOM sans couche d'abstraction intermediaire, "
                "offrant des performances exceptionnelles et un bundle tres leger.\n\n"
                "La philosophie de Svelte est de deplacer le travail du navigateur vers le "
                "compilateur. Le compilateur analyse le code source des composants .svelte, "
                "comprend la structure des dependances entre les donnees et le DOM, et genere "
                "du code chirurgical qui met a jour exactement les elements DOM concernes "
                "lorsqu'une variable change. Il n'y a pas de diffing de Virtual DOM, pas de "
                "reconciliation, pas de comparaison d'arbres : juste des affectations directes "
                "au DOM, ce qui est inherement plus rapide.\n\n"
                "Svelte 5, la derniere version majeure, a introduit les 'runes', un nouveau "
                "systeme de reactivite base sur des signaux granulaires qui remplace la "
                "reactivite implicite des versions precedentes. Les runes ($state, $derived, "
                "$effect) offrent un controle explicite et fin sur la reactivite tout en "
                "conservant la concision qui fait la reputation de Svelte. Cette evolution "
                "aligne Svelte avec la tendance generale vers les signaux (Angular Signals, "
                "Vue ref/reactive, Solid.js) tout en maintenant son avantage compile. "
                "Svelte est regulierement classe en tete des enquetes de satisfaction des "
                "developpeurs, grace a sa simplicite, ses performances et l'elegance de "
                "sa syntaxe."
            ),
            "history": (
                "Rich Harris a cree Svelte en 2016 alors qu'il travaillait au New York Times "
                "sur des projets de data-journalisme interactif. Il avait besoin d'un outil "
                "capable de produire des applications web performantes avec des bundles "
                "extremement legers, car les visualisations interactives devaient se charger "
                "rapidement meme sur des connexions lentes. Les frameworks existants (React, "
                "Angular) embarquaient des runtimes trop volumineux pour ces besoins.\n\n"
                "Svelte 1 (novembre 2016) a introduit le concept de framework compile, ou "
                "le framework disparait a l'execution et ne laisse que du JavaScript vanilla "
                "optimise. Svelte 2 (avril 2018) a ameliore la syntaxe et les performances "
                "du compilateur. Svelte 3 (avril 2019) a ete une reecriture majeure qui a "
                "popularise le framework. Cette version a introduit la reactivite implicite "
                "basee sur les affectations : une simple affectation comme count = count + 1 "
                "declenche automatiquement la mise a jour du DOM, sans appel explicite a "
                "setState ou equivalent.\n\n"
                "En 2020, Rich Harris a rejoint Vercel et a commence a developper SvelteKit, "
                "le meta-framework officiel pour Svelte (equivalent a Next.js pour React). "
                "SvelteKit 1.0 a ete lance en decembre 2022. Svelte 4 (juin 2023) a apporte "
                "des ameliorations de performance et une reduction de la taille du package. "
                "Svelte 5 (octobre 2024) a introduit les runes, un changement fondamental "
                "du modele de reactivite qui remplace la magie du compilateur par des "
                "primitives explicites basees sur des signaux, offrant plus de previsibilite "
                "et de composabilite tout en conservant l'approche compilee qui fait la "
                "force de Svelte."
            ),
            "architecture": (
                "L'architecture de Svelte est fondamentalement differente de celle des autres "
                "frameworks car elle repose sur un compilateur plutot que sur un runtime. "
                "Un composant Svelte est ecrit dans un fichier .svelte qui contient trois "
                "sections : <script> pour la logique, le markup HTML pour le template et "
                "<style> pour le CSS (automatiquement scope au composant). Le compilateur "
                "Svelte analyse ce fichier et genere du code JavaScript optimise.\n\n"
                "L'approche sans Virtual DOM est le point d'architecture le plus distinctif "
                "de Svelte. Quand on ecrit {count} dans un template Svelte, le compilateur "
                "genere du code qui cree un noeud texte dans le DOM et une instruction "
                "qui met a jour directement ce noeud texte quand la variable count change. "
                "Il n'y a pas de representation intermediaire, pas de comparaison d'arbres, "
                "pas de diffing : le compilateur sait statiquement quels elements du DOM "
                "dependent de quelles variables et genere le code de mise a jour minimal.\n\n"
                "Avec Svelte 5 et les runes, le systeme de reactivite est devenu explicite. "
                "$state() cree une variable reactive, $derived() cree une valeur calculee "
                "qui se met a jour automatiquement quand ses dependances changent, et "
                "$effect() execute du code en reaction aux changements. Ces primitives "
                "sont transformees par le compilateur en code efficace. Contrairement aux "
                "Hooks de React qui s'executent a chaque rendu, les runes de Svelte "
                "etablissent des connexions reactives au moment de la creation et ne "
                "re-executent que le code necessaire lors des changements.\n\n"
                "SvelteKit, le meta-framework, ajoute le routage base sur le systeme de "
                "fichiers, le rendu cote serveur (SSR), la generation de sites statiques "
                "(SSG), le chargement de donnees cote serveur (load functions), les "
                "actions de formulaires et un systeme d'adaptateurs permettant de "
                "deployer sur n'importe quelle plateforme (Node, Cloudflare, Vercel, "
                "Netlify, Deno, etc.)."
            ),
            "pros_cons": {
                "pros": [
                    "Performances exceptionnelles grace a l'approche compilee sans Virtual DOM",
                    "Bundles extremement legers : pas de runtime a embarquer",
                    "Syntaxe concise et expressive, moins de code boilerplate",
                    "CSS scope par defaut dans chaque composant sans configuration",
                    "Animations et transitions integrees nativement dans le framework",
                    "Accessibilite : le compilateur emet des avertissements pour les problemes a11y",
                    "Runes (Svelte 5) offrant une reactivite explicite et composable",
                    "SvelteKit fournissant un meta-framework complet et flexible",
                ],
                "cons": [
                    "Ecosysteme tiers significativement plus petit que React, Vue ou Angular",
                    "Communaute plus restreinte, moins de ressources d'apprentissage disponibles",
                    "Moins d'offres d'emploi que les trois grands frameworks",
                    "La syntaxe specifique (.svelte) necessite un outillage dedie",
                    "Moins eprouve pour les applications de tres grande envergure",
                    "Le changement de modele de reactivite (Svelte 3/4 vers 5) peut derouter",
                    "Debugging parfois moins intuitif car le code execute differe du code source",
                ],
            },
            "use_cases": (
                "Svelte excelle dans les cas ou la performance et la taille du bundle sont "
                "critiques : visualisations de donnees interactives, widgets embarques dans "
                "des sites tiers, applications destinees a des connexions lentes ou des "
                "appareils peu puissants, Progressive Web Apps et applications embarquees. "
                "Il est egalement ideal pour les projets de petite a moyenne taille ou la "
                "productivite du developpeur est prioritaire. Avec SvelteKit, Svelte "
                "convient aussi aux sites web avec SSR/SSG, aux blogs, aux portfolios et "
                "aux applications fullstack moderees. Les projets de data-journalisme et "
                "de storytelling interactif sont un terrain de predilection historique "
                "de Svelte."
            ),
            "ecosystem": (
                "L'ecosysteme Svelte est plus petit que ceux de React ou Vue mais en "
                "croissance constante. SvelteKit est le meta-framework officiel pour le "
                "SSR, SSG et le routage. Svelte Store est le systeme de gestion d'etat "
                "natif (basique mais suffisant pour beaucoup de cas). Pour les composants "
                "UI, Skeleton UI, Flowbite Svelte et DaisyUI (via Tailwind) sont populaires. "
                "Svelte Motion et Svelte Spring gerent les animations avancees. Pour les "
                "tests, Vitest et Playwright sont recommandes. Superforms est une "
                "bibliotheque de formulaires puissante pour SvelteKit. Paraglide et "
                "svelte-i18n gerent l'internationalisation. L'integration avec Vite est "
                "native via vite-plugin-svelte."
            ),
            "companies": [
                "The New York Times",
                "Apple (documentation interne)",
                "Spotify",
                "Square",
                "Rakuten",
                "Ikea",
                "Philips",
            ],
            "code_example": (
                "<script>\n"
                "  let tasks = $state([]);\n"
                "  let input = $state('');\n\n"
                "  let completedCount = $derived(\n"
                "    tasks.filter(t => t.done).length\n"
                "  );\n\n"
                "  function addTask() {\n"
                "    if (input.trim()) {\n"
                "      tasks.push({\n"
                "        id: Date.now(),\n"
                "        text: input,\n"
                "        done: false\n"
                "      });\n"
                "      input = '';\n"
                "    }\n"
                "  }\n\n"
                "  function toggleTask(id) {\n"
                "    const task = tasks.find(t => t.id === id);\n"
                "    if (task) task.done = !task.done;\n"
                "  }\n"
                "</script>\n\n"
                "<h1>Liste de taches ({completedCount} terminees)</h1>\n"
                "<input bind:value={input} onkeydown={(e) => e.key === 'Enter' && addTask()} />\n"
                "<button onclick={addTask}>Ajouter</button>\n"
                "<ul>\n"
                "  {#each tasks as task (task.id)}\n"
                "    <li\n"
                "      onclick={() => toggleTask(task.id)}\n"
                "      class:done={task.done}\n"
                "    >\n"
                "      {task.text}\n"
                "    </li>\n"
                "  {/each}\n"
                "</ul>\n\n"
                "<style>\n"
                "  .done { text-decoration: line-through; color: gray; }\n"
                "</style>"
            ),
            "performance": {
                "startup_time": (
                    "Svelte offre le temps de demarrage le plus rapide de tous les frameworks "
                    "majeurs. Sans runtime a charger et a initialiser, le code compile est "
                    "immediatement executable. Les bundles sont typiquement 30 a 50 % plus "
                    "legers que ceux de React pour des applications equivalentes. Le code "
                    "genere est du JavaScript vanilla optimise qui s'execute sans surcout "
                    "d'abstraction."
                ),
                "throughput": (
                    "Les performances de mise a jour de Svelte sont parmi les meilleures "
                    "du marche. La manipulation directe du DOM, sans passer par un Virtual "
                    "DOM, elimine les couts de creation et de comparaison d'arbres virtuels. "
                    "Les mises a jour sont chirurgicales : seuls les noeuds DOM concernes "
                    "sont touches. Dans les benchmarks, Svelte se classe regulierement "
                    "dans le top 3 pour les performances de rendu."
                ),
                "memory": (
                    "L'empreinte memoire de Svelte est minimale. Sans Virtual DOM en memoire, "
                    "sans systeme de reconciliation et sans runtime volumineux, l'utilisation "
                    "memoire est proche de celle d'une application JavaScript vanilla. C'est "
                    "un avantage decisif sur les appareils mobiles et les environnements "
                    "contraints en ressources."
                ),
                "concurrency_model": (
                    "Svelte ne propose pas de mecanisme de concurrence avance au niveau du "
                    "framework. Les mises a jour sont synchrones et groupees par microtask. "
                    "Pour les operations lourdes, le developpeur peut utiliser des Web Workers "
                    "ou des strategies de decouplage manuelles. SvelteKit gere l'asynchronisme "
                    "cote serveur via les load functions et le streaming SSR."
                ),
            },
            "learning_curve": (
                "Svelte est reconnu pour avoir l'une des courbes d'apprentissage les plus "
                "douces parmi les frameworks modernes. La syntaxe est proche du HTML, CSS "
                "et JavaScript standards, avec un minimum de concepts specifiques au framework. "
                "Un composant Svelte ressemble a un fichier HTML enrichi, ce qui le rend "
                "immediatement familier. Les directives de template ({#if}, {#each}, "
                "{#await}) sont intuitives. La reactivite, que ce soit la reactivite "
                "implicite de Svelte 3/4 ou les runes de Svelte 5, est elegante et "
                "facile a comprendre. Le tutoriel interactif officiel (learn.svelte.dev) "
                "est excellent et permet de maitriser les bases en quelques heures. "
                "La principale difficulte reside dans le fait que certains concepts "
                "comme la compilation et le code genere peuvent etre deroutants pour "
                "le debogage, et que l'ecosysteme plus restreint oblige parfois a "
                "implementer des solutions soi-meme."
            ),
            "community_size": (
                "La communaute Svelte est plus petite que celles de React, Vue ou Angular, "
                "mais elle est passionnee et en croissance rapide. Avec environ 80 000 "
                "etoiles sur GitHub, Svelte attire de plus en plus de developpeurs. "
                "Le Svelte Summit est la conference annuelle dediee. Le serveur Discord "
                "de Svelte est un lieu d'echange actif. Le framework est regulierement "
                "classe premier en satisfaction developpeur dans les enquetes State of JS."
            ),
            "job_market": (
                "Le marche de l'emploi Svelte est encore en developpement. Les offres "
                "sont nettement moins nombreuses que pour React, Vue ou Angular, mais "
                "elles sont en augmentation constante. Svelte est souvent choisi par des "
                "startups innovantes et des equipes techniques avancees. La connaissance "
                "de Svelte est un atout differenciateur sur un CV, temoignant d'une "
                "curiosite technique et d'une ouverture aux nouvelles approches. Les "
                "salaires sont comparables aux autres frameworks pour les postes qui "
                "le demandent."
            ),
        },
        "traits": {
            "performance": 9,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 4,
            "type_safety": 6,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 6,
        },
    },

    "nextjs": {
        "name": "Next.js",
        "category": "frontend",
        "year_created": 2016,
        "creator": "Vercel",
        "paradigm": ["Composant", "Declaratif", "Hybride (SSR/SSG/CSR)", "Fullstack"],
        "typing": "JavaScript/TypeScript (support natif)",
        "sections": {
            "overview": (
                "Next.js est un meta-framework React developpe par Vercel qui etend les "
                "capacites de React en ajoutant le rendu cote serveur (SSR), la generation "
                "de sites statiques (SSG), le routage base sur le systeme de fichiers, "
                "l'optimisation automatique des images, les routes API et bien d'autres "
                "fonctionnalites essentielles a la production. Si React est une bibliotheque "
                "de vue, Next.js est le framework complet qui transforme React en solution "
                "de production prete a l'emploi.\n\n"
                "L'innovation majeure de Next.js est de permettre un rendu hybride : chaque "
                "page d'une meme application peut choisir independamment sa strategie de "
                "rendu. Une page marketing peut etre generee statiquement (SSG) pour des "
                "performances maximales, tandis qu'un tableau de bord utilisateur peut "
                "utiliser le rendu cote serveur (SSR) pour afficher des donnees fraiches "
                "a chaque requete. Les pages interactives peuvent opter pour le rendu "
                "cote client (CSR) classique. Cette flexibilite est unique et permet "
                "d'optimiser chaque partie de l'application independamment.\n\n"
                "Depuis la version 13, Next.js a introduit l'App Router, base sur les "
                "React Server Components (RSC). Ce nouveau paradigme permet de rendre "
                "des composants entierement cote serveur, sans envoyer leur JavaScript "
                "au navigateur, reduisant drastiquement la taille du bundle client. Les "
                "Server Actions permettent d'appeler des fonctions cote serveur directement "
                "depuis les composants client, eliminant le besoin de creer des routes API "
                "pour les mutations de donnees. Next.js est devenu le framework React "
                "recommande par l'equipe React elle-meme et est le choix par defaut pour "
                "de nombreux nouveaux projets React en production."
            ),
            "history": (
                "Next.js a ete cree par Guillermo Rauch et l'equipe de Zeit (rebaptise "
                "Vercel en 2020) en octobre 2016. L'objectif initial etait de simplifier "
                "la creation d'applications React avec rendu cote serveur, qui necessitait "
                "alors une configuration complexe de webpack, babel et express. L'approche "
                "'zero configuration' de Next.js a immediatement seduit les developpeurs.\n\n"
                "Les premieres versions de Next.js se concentraient sur le SSR et le "
                "routage base sur les fichiers. Next.js 3 (2017) a introduit l'export "
                "statique. Next.js 9 (2019) a apporte les routes API, transformant "
                "Next.js en solution fullstack. Next.js 9.3 a introduit getStaticProps "
                "et getServerSideProps, clarifiant les strategies de rendu. Next.js 10 "
                "(2020) a ajoute l'optimisation automatique des images avec next/image "
                "et l'internationalisation integree.\n\n"
                "Next.js 12 (2021) a introduit le compilateur SWC (ecrit en Rust), "
                "remplacant Babel pour des compilations 5 a 17 fois plus rapides, ainsi "
                "que le middleware Edge. Next.js 13 (2022) a ete une revolution avec "
                "l'introduction de l'App Router et des React Server Components, "
                "changeant fondamentalement l'architecture des applications Next.js. "
                "Next.js 14 (2023) a stabilise les Server Actions et ameliore les "
                "performances. Next.js 15 (2024) a introduit le support de React 19, "
                "le Partial Prerendering (PPR) qui combine SSG et SSR dans une meme "
                "page, et des ameliorations significatives du caching. Aujourd'hui, "
                "Next.js est le meta-framework React le plus populaire et est utilise "
                "par des centaines de milliers de sites en production."
            ),
            "architecture": (
                "L'architecture de Next.js repose sur plusieurs couches qui etendent "
                "React de maniere significative. Le systeme de routage est base sur le "
                "systeme de fichiers : dans l'App Router, chaque dossier dans app/ "
                "correspond a un segment de route, et les fichiers speciaux (page.tsx, "
                "layout.tsx, loading.tsx, error.tsx, not-found.tsx) definissent le "
                "comportement de chaque route. Les layouts sont imbriques et persistants, "
                "evitant les re-rendus inutiles lors de la navigation.\n\n"
                "Les React Server Components (RSC) sont au coeur de l'App Router. Par "
                "defaut, tous les composants sont des Server Components : ils s'executent "
                "uniquement sur le serveur, peuvent acceder directement aux bases de donnees "
                "et aux fichiers, et n'envoient aucun JavaScript au client. Seuls les "
                "composants marques avec 'use client' sont envoyes au navigateur pour "
                "l'interactivite (evenements, state, effects). Cette separation permet de "
                "garder le bundle client minimal tout en beneficiant d'un rendu riche.\n\n"
                "Next.js propose quatre strategies de rendu : le Static Site Generation "
                "(SSG) genere les pages HTML au moment du build pour des performances "
                "maximales et un cout d'hebergement minimal ; le Server-Side Rendering "
                "(SSR) genere la page a chaque requete pour des donnees toujours fraiches ; "
                "l'Incremental Static Regeneration (ISR) permet de regenerer des pages "
                "statiques en arriere-plan apres un delai configurable ; et le Partial "
                "Prerendering (PPR, experimental) combine une coquille statique avec des "
                "parties dynamiques en streaming, offrant le meilleur des deux mondes.\n\n"
                "Les Server Actions permettent de definir des fonctions cote serveur "
                "appelables depuis des formulaires ou du code client. Elles gerent "
                "automatiquement la serialisation, la validation, le revalidation du "
                "cache et les redirections, simplifiant enormement les mutations de "
                "donnees. Le middleware Next.js s'execute a l'edge (avant le serveur) "
                "et permet l'authentification, la redirection, les A/B tests et "
                "la personnalisation a faible latence."
            ),
            "pros_cons": {
                "pros": [
                    "Rendu hybride flexible : SSG, SSR, ISR, CSR et PPR dans une meme application",
                    "React Server Components reduisant drastiquement la taille du bundle client",
                    "Routage base sur le systeme de fichiers, intuitif et puissant",
                    "Optimisation automatique des images, des polices et des scripts",
                    "Server Actions simplifiant les mutations de donnees cote serveur",
                    "Compilateur SWC ultra-rapide ecrit en Rust",
                    "Deploiement facilite sur Vercel avec optimisations automatiques",
                    "Enorme ecosysteme herite de React, avec adoption croissante",
                    "Support TypeScript natif et complet",
                ],
                "cons": [
                    "Complexite croissante avec l'App Router et les Server Components",
                    "Distinction Server/Client Components deroutante pour les debutants",
                    "Couplage percu avec la plateforme Vercel pour les fonctionnalites avancees",
                    "Strategies de cache parfois opaques et difficiles a deboguer",
                    "Migrations entre versions majeures parfois couteuses (Pages Router vers App Router)",
                    "Temps de build potentiellement long pour les tres grands sites statiques",
                    "La courbe d'apprentissage de React s'ajoute a celle de Next.js",
                ],
            },
            "use_cases": (
                "Next.js est le choix ideal pour pratiquement tous les types de sites web "
                "et d'applications React en production. Il excelle particulierement pour : "
                "les sites marketing et e-commerce necessitant un excellent SEO grace au SSR "
                "et SSG ; les applications SaaS combinant pages publiques statiques et "
                "tableaux de bord dynamiques ; les blogs et sites de contenu beneficiant "
                "de la generation statique ; les plateformes fullstack utilisant les Server "
                "Actions et les routes API ; les sites a fort trafic tirant parti de l'ISR "
                "et du CDN ; et les applications d'entreprise necessitant authentification, "
                "internationalisation et performances optimales. Next.js est recommande "
                "par l'equipe React comme le point de depart pour tout nouveau projet React."
            ),
            "ecosystem": (
                "Next.js herite de l'ensemble de l'ecosysteme React et y ajoute ses propres "
                "outils. next/image optimise automatiquement les images avec lazy loading et "
                "formats modernes (WebP, AVIF). next/font optimise le chargement des polices. "
                "next/link pre-charge les pages liees pour une navigation instantanee. Le "
                "middleware Edge permet l'execution de code a l'edge du reseau. NextAuth.js "
                "(Auth.js) est la solution d'authentification la plus populaire. Contentlayer, "
                "Sanity et Strapi sont utilises pour la gestion de contenu. Prisma, Drizzle "
                "et Supabase pour l'acces aux donnees. Tailwind CSS est le choix de styling "
                "le plus courant. Pour les tests, Jest, React Testing Library, Playwright "
                "et Cypress sont recommandes. Turbopack (successeur de webpack, ecrit en "
                "Rust) est en cours d'integration pour des builds encore plus rapides."
            ),
            "companies": [
                "Vercel",
                "Netflix",
                "TikTok",
                "Twitch",
                "Hulu",
                "Nike",
                "Target",
                "Notion",
                "Washington Post",
            ],
            "code_example": (
                "// app/tasks/page.tsx - Server Component (par defaut)\n"
                "import { TaskList } from './task-list'\n\n"
                "export const metadata = {\n"
                "  title: 'Mes taches',\n"
                "  description: 'Gestionnaire de taches Next.js'\n"
                "}\n\n"
                "async function getTasks() {\n"
                "  const res = await fetch('https://api.exemple.com/tasks', {\n"
                "    next: { revalidate: 60 } // ISR : regeneration toutes les 60s\n"
                "  })\n"
                "  return res.json()\n"
                "}\n\n"
                "export default async function TasksPage() {\n"
                "  const initialTasks = await getTasks()\n\n"
                "  return (\n"
                "    <main>\n"
                "      <h1>Liste de taches</h1>\n"
                "      <TaskList initialTasks={initialTasks} />\n"
                "    </main>\n"
                "  )\n"
                "}\n\n"
                "// app/tasks/task-list.tsx - Client Component\n"
                "'use client'\n"
                "import { useState } from 'react'\n"
                "import { addTaskAction } from './actions'\n\n"
                "export function TaskList({ initialTasks }) {\n"
                "  const [tasks, setTasks] = useState(initialTasks)\n"
                "  const [input, setInput] = useState('')\n\n"
                "  return (\n"
                "    <div>\n"
                "      <form action={async (formData) => {\n"
                "        const newTask = await addTaskAction(formData)\n"
                "        setTasks([...tasks, newTask])\n"
                "      }}>\n"
                "        <input name=\"text\" value={input}\n"
                "               onChange={e => setInput(e.target.value)} />\n"
                "        <button type=\"submit\">Ajouter</button>\n"
                "      </form>\n"
                "      <ul>\n"
                "        {tasks.map(task => (\n"
                "          <li key={task.id}>{task.text}</li>\n"
                "        ))}\n"
                "      </ul>\n"
                "    </div>\n"
                "  )\n"
                "}\n\n"
                "// app/tasks/actions.ts - Server Action\n"
                "'use server'\n"
                "import { revalidatePath } from 'next/cache'\n\n"
                "export async function addTaskAction(formData: FormData) {\n"
                "  const text = formData.get('text') as string\n"
                "  // Insertion directe en base de donnees cote serveur\n"
                "  const task = await db.task.create({ data: { text, done: false } })\n"
                "  revalidatePath('/tasks')\n"
                "  return task\n"
                "}"
            ),
            "performance": {
                "startup_time": (
                    "Next.js optimise le temps de chargement initial via plusieurs mecanismes. "
                    "Le SSR et le SSG permettent d'envoyer du HTML pre-rendu, offrant un "
                    "First Contentful Paint (FCP) rapide. Les React Server Components "
                    "reduisent le JavaScript envoye au client en gardant le code serveur "
                    "hors du bundle. L'hydratation selective et le streaming SSR (via "
                    "React Suspense) permettent d'afficher et de rendre interactives les "
                    "parties critiques en priorite."
                ),
                "throughput": (
                    "Le throughput de Next.js depend de la strategie de rendu choisie. Les "
                    "pages SSG sont servies depuis un CDN avec des performances maximales. "
                    "Le SSR necessite un serveur Node.js (ou une fonction serverless) pour "
                    "chaque requete. L'ISR combine les avantages du SSG et du SSR en "
                    "regenerant les pages en arriere-plan. Le PPR promet de combiner une "
                    "coquille statique instantanee avec du contenu dynamique en streaming."
                ),
                "memory": (
                    "L'utilisation memoire de Next.js cote serveur depend du nombre de "
                    "requetes SSR simultanees et de la taille des composants rendus. "
                    "Les Server Components sont rendus en streaming, limitant la memoire "
                    "necessaire. Cote client, le code splitting automatique et les RSC "
                    "maintiennent un bundle compact. Le pre-chargement intelligent des "
                    "routes optimise l'utilisation de la memoire navigateur."
                ),
                "concurrency_model": (
                    "Next.js tire parti du modele de concurrence de React 18 (rendu concurrent, "
                    "Suspense, transitions) cote client. Cote serveur, le streaming SSR permet "
                    "de commencer a envoyer du HTML avant que le rendu complet soit termine, "
                    "ameliorant le Time to First Byte (TTFB). Le middleware Edge s'execute "
                    "dans un runtime V8 leger, offrant des temps de reponse extremement bas "
                    "pour l'authentification, les redirections et la personnalisation."
                ),
            },
            "learning_curve": (
                "La courbe d'apprentissage de Next.js est moderee a prononcee, car elle "
                "se superpose a celle de React. Un developpeur maitrisant React trouvera "
                "le Pages Router relativement accessible : le routage par fichiers, "
                "getStaticProps et getServerSideProps sont des concepts simples a "
                "apprehender. L'App Router, en revanche, introduit des paradigmes "
                "fondamentalement nouveaux : les React Server Components, la distinction "
                "server/client, les Server Actions, le streaming, le caching et les "
                "strategies de revalidation. Ces concepts necessitent une comprehension "
                "profonde du fonctionnement du rendu serveur et client, ainsi que des "
                "implications sur le flux de donnees et la serialisation. La complexite "
                "du systeme de cache de Next.js est un point de friction frequemment "
                "cite par les developpeurs. La documentation officielle est complete "
                "mais la richesse des fonctionnalites peut etre intimidante pour les "
                "debutants."
            ),
            "community_size": (
                "Next.js possede une communaute massive et en croissance rapide, avec plus "
                "de 130 000 etoiles sur GitHub. Porte par Vercel, le framework beneficie "
                "d'un marketing actif et d'une visibilite forte. Next.js Conf est une "
                "conference annuelle majeure. La communaute est active sur GitHub, Discord, "
                "Twitter/X et les forums de Vercel. De nombreux tutoriels, cours en ligne "
                "et ressources sont disponibles. L'adoption par de grandes entreprises "
                "et l'adoubement par l'equipe React renforcent sa position dominante."
            ),
            "job_market": (
                "Next.js est de plus en plus demande sur le marche de l'emploi, souvent "
                "mentionne en complement de React dans les offres. La connaissance de "
                "Next.js est un avantage significatif pour les postes de developpeur "
                "frontend senior et fullstack. Les entreprises recherchent des "
                "developpeurs capables de tirer parti du SSR, du SSG et des Server "
                "Components pour des applications performantes et bien referencees. "
                "Les salaires pour les developpeurs Next.js sont parmi les plus eleves "
                "du secteur frontend, refletant la demande croissante et la valeur ajoutee "
                "de ces competences. La tendance est clairement a la hausse."
            ),
        },
        "traits": {
            "performance": 8,
            "developer_speed": 8,
            "learning_curve": 5,
            "ecosystem_size": 8,
            "type_safety": 7,
            "concurrency": 6,
            "memory_safety": 5,
            "scalability": 9,
        },
    },

    # =========================================================================
    # Nuxt.js
    # =========================================================================
    "nuxtjs": {
        "name": "Nuxt.js",
        "category": "frontend",
        "year_created": 2016,
        "creator": "Sebastien & Alexandre Chopin",
        "paradigm": ["Composant", "Declaratif", "SSR/SSG"],
        "typing": "JavaScript/TypeScript",
        "sections": {
            "overview": (
                "Nuxt.js est un framework open source base sur Vue.js, concu pour simplifier "
                "le developpement d'applications web universelles (server-side rendering), "
                "de sites statiques (static site generation) et d'applications monopages (SPA). "
                "Cree par Sebastien et Alexandre Chopin en 2016, Nuxt s'inspire directement de "
                "Next.js dans l'ecosysteme React, en proposant une approche conventionnelle et "
                "opiniatree du developpement Vue.js. Le framework fournit une structure de projet "
                "claire, un systeme de routage automatique base sur l'arborescence des fichiers, "
                "et une configuration minimale grace a des conventions intelligentes.\n\n"
                "Nuxt abstrait la complexite de la configuration de webpack, Vite, Vue Router et "
                "du rendu cote serveur, permettant aux developpeurs de se concentrer sur la logique "
                "metier plutot que sur la plomberie technique. Le framework supporte nativement le "
                "rendu hybride, ou chaque route peut individuellement etre configuree pour le SSR, "
                "le SSG, le SPA ou meme le rendu cote serveur uniquement (server-only). Cette "
                "flexibilite permet d'adapter la strategie de rendu aux besoins specifiques de "
                "chaque page de l'application.\n\n"
                "Depuis Nuxt 3, le framework repose entierement sur Vue 3 et son API Composition, "
                "offrant un systeme de reactivite ameliore, des performances accrues et un support "
                "natif de TypeScript. Le moteur Nitro, developpe specifiquement pour Nuxt 3, fournit "
                "un serveur leger et universel qui peut etre deploye sur pratiquement toutes les "
                "plateformes : Node.js, Deno, Cloudflare Workers, Vercel, Netlify et bien d'autres. "
                "Nuxt propose egalement un systeme de modules extremement puissant qui permet "
                "d'etendre les fonctionnalites du framework de maniere modulaire et reutilisable, "
                "avec plus de 200 modules communautaires couvrant des besoins varies comme "
                "l'authentification, le SEO, l'internationalisation et l'integration de CMS headless."
            ),
            "history": (
                "L'histoire de Nuxt.js commence fin 2016 lorsque Sebastien Chopin, inspire par "
                "Next.js dans l'ecosysteme React, decide de creer un equivalent pour Vue.js. "
                "Avec son frere Alexandre, ils developpent un framework capable de generer des "
                "applications Vue.js avec rendu cote serveur de maniere simple et opiniatree. "
                "La premiere version stable de Nuxt (1.0) est publiee en janvier 2018, apportant "
                "le routage automatique, le support SSR et SSG, ainsi qu'un systeme de middleware "
                "et de layouts.\n\n"
                "Nuxt 2, sorti en septembre 2018, a marque une etape majeure avec une refonte "
                "complete du coeur du framework, un mecanisme de modules ameliore, le support de "
                "webpack 4, et une meilleure gestion des erreurs. Cette version a propulse Nuxt "
                "au rang de framework incontournable dans l'ecosysteme Vue.js, adopte par de "
                "nombreuses entreprises pour leurs sites institutionnels, e-commerce et applications "
                "web. Le module @nuxt/content a popularise l'utilisation de Nuxt comme generateur "
                "de sites statiques orientee contenu.\n\n"
                "Nuxt 3, annonce en 2021 et publie en version stable en novembre 2022, represente "
                "une reecriture complete du framework. Base sur Vue 3 et son API Composition, il "
                "introduit le moteur serveur Nitro, le support natif de TypeScript, un nouveau "
                "systeme de build base sur Vite, les composants auto-importes, et un systeme de "
                "rendu hybride permettant de configurer la strategie de rendu par route. Nuxt 3 "
                "beneficie egalement d'un DevTools integre offrant une visibilite complete sur "
                "l'etat de l'application, les routes, les composants et les modules. Le framework "
                "continue d'evoluer avec des mises a jour regulieres, renforçant son ecosysteme "
                "et son integration avec les plateformes de deploiement modernes."
            ),
            "architecture": (
                "L'architecture de Nuxt.js repose sur plusieurs couches qui travaillent ensemble "
                "pour offrir une experience de developpement fluide et des performances optimales. "
                "Au coeur du framework se trouve Vue.js, qui gere le systeme de composants, la "
                "reactivite et le rendu de l'interface. Au-dessus, Nuxt ajoute une couche de "
                "conventions et d'abstractions qui structurent le projet et automatisent de "
                "nombreuses taches de configuration.\n\n"
                "Le systeme de routage de Nuxt est base sur le systeme de fichiers : chaque fichier "
                "Vue place dans le repertoire pages/ genere automatiquement une route correspondante. "
                "Les routes dynamiques sont definies par des crochets dans le nom du fichier "
                "(par exemple [id].vue), et les routes imbriquees suivent la hierarchie des "
                "repertoires. Ce systeme elimine le besoin de configurer manuellement Vue Router "
                "et garantit une correspondance claire entre la structure du projet et les URLs "
                "de l'application.\n\n"
                "Le moteur Nitro, introduit dans Nuxt 3, est un serveur universel qui gere le "
                "rendu cote serveur, les routes API et le pre-rendu statique. Nitro compile le "
                "code serveur en un bundle optimise qui peut etre deploye sur de multiples cibles "
                "(Node.js, workers edge, serverless). Il utilise un systeme de stockage abstrait "
                "(unstorage) pour le cache et les donnees, et un systeme de routes API basees sur "
                "les fichiers dans le repertoire server/. Le rendu hybride permet de definir des "
                "regles de rendu par route : certaines pages peuvent etre pre-rendues a la "
                "construction, d'autres rendues cote serveur a chaque requete, et d'autres encore "
                "fonctionner comme une SPA classique. Les composables Nuxt (useAsyncData, useFetch, "
                "useState, useHead) fournissent une API reactive et isomorphe pour la gestion des "
                "donnees, de l'etat et des metadonnees, fonctionnant de maniere transparente aussi "
                "bien cote serveur que cote client."
            ),
            "pros_cons": {
                "pros": [
                    "Configuration minimale grace aux conventions intelligentes et aux auto-imports",
                    "Rendu hybride flexible (SSR, SSG, SPA, ISR) configurable par route",
                    "Moteur Nitro performant et deployable sur toutes les plateformes modernes",
                    "Systeme de modules riche avec plus de 200 modules communautaires",
                    "Support natif de TypeScript avec inference de types avancee",
                    "Routage automatique base sur le systeme de fichiers, intuitif et productif",
                    "DevTools integre offrant une visibilite complete sur l'application",
                    "Excellente integration avec l'ecosysteme Vue.js et ses bibliotheques",
                ],
                "cons": [
                    "Courbe d'apprentissage liee a la comprehension des multiples modes de rendu",
                    "Les conventions strictes peuvent etre contraignantes pour les projets atypiques",
                    "Ecosysteme de modules moins vaste que celui de Next.js dans l'univers React",
                    "La transition de Nuxt 2 a Nuxt 3 a ete longue et a fragmente la communaute",
                    "La documentation peut manquer d'exemples avances pour les cas d'utilisation complexes",
                    "Le debogage des problemes d'hydratation SSR reste un defi technique",
                    "Certains modules communautaires ne sont pas encore portes vers Nuxt 3",
                ],
            },
            "use_cases": (
                "Nuxt.js excelle dans le developpement de sites web necessitant un bon "
                "referencement naturel (SEO), comme les sites institutionnels, les blogs, les "
                "magazines en ligne et les sites e-commerce. Grace au SSR et au SSG, les pages "
                "sont indexables par les moteurs de recherche et offrent un temps d'affichage "
                "initial rapide, ameliorant l'experience utilisateur et le classement SEO.\n\n"
                "Les plateformes e-commerce beneficient particulierement de Nuxt grace au rendu "
                "hybride : les pages produits peuvent etre pre-rendues statiquement pour des "
                "performances maximales, tandis que le panier et le processus de commande "
                "fonctionnent en mode SPA interactif. Les sites de contenu et les documentations "
                "techniques tirent parti du module @nuxt/content pour gerer du contenu en Markdown "
                "avec un systeme de requetes puissant.\n\n"
                "Nuxt est egalement adapte aux applications web d'entreprise necessitant une "
                "architecture claire et maintenable. Les grandes equipes apprecient les conventions "
                "imposees par le framework, qui garantissent une structure de projet coherente. "
                "Les applications temps reel, les tableaux de bord et les portails internes "
                "peuvent tirer parti du mode SPA de Nuxt tout en beneficiant de l'infrastructure "
                "du framework. Enfin, les applications JAMstack et les sites generes statiquement "
                "deployes sur des CDN comme Netlify, Vercel ou Cloudflare Pages sont un cas "
                "d'utilisation tres populaire de Nuxt."
            ),
            "ecosystem": (
                "L'ecosysteme de Nuxt.js s'appuie sur la richesse de l'ecosysteme Vue.js tout "
                "en ajoutant ses propres outils et modules. Le systeme de modules Nuxt est l'un "
                "de ses points forts les plus distinctifs, avec plus de 200 modules communautaires "
                "couvrant un large eventail de besoins. Parmi les plus populaires, on trouve "
                "@nuxt/content pour la gestion de contenu en Markdown et YAML, @nuxt/image pour "
                "l'optimisation automatique des images, @nuxtjs/i18n pour l'internationalisation, "
                "@sidebase/nuxt-auth pour l'authentification, et @nuxt/ui pour une bibliotheque "
                "de composants d'interface integree.\n\n"
                "Cote outils de developpement, Nuxt DevTools offre une interface graphique integree "
                "pour inspecter les composants, les routes, les modules, l'etat et les appels API "
                "de l'application. Le framework utilise Vite comme bundler par defaut, offrant un "
                "rechargement a chaud quasi instantane. Pour les tests, Nuxt s'integre avec Vitest "
                "et @nuxt/test-utils pour les tests unitaires et d'integration. Pinia est le "
                "gestionnaire d'etat recommande, remplacant Vuex. TailwindCSS et UnoCSS sont les "
                "solutions de styling les plus populaires dans l'ecosysteme Nuxt. Pour le deploiement, "
                "Nuxt supporte nativement de nombreuses plateformes grace aux presets Nitro : Vercel, "
                "Netlify, Cloudflare, AWS Lambda, Azure, et bien d'autres."
            ),
            "companies": [
                "GitLab",
                "Upwork",
                "Ecosia",
                "Line (messagerie japonaise)",
                "Backmarket",
                "Lego",
                "Rakuten",
                "Roland Garros",
                "Nintendo (sites web)",
            ],
            "code_example": (
                "<!-- pages/index.vue -->\n"
                "<template>\n"
                "  <div>\n"
                "    <h1>Liste des articles</h1>\n"
                "    <div v-if=\"pending\">Chargement...</div>\n"
                "    <div v-else>\n"
                "      <article v-for=\"article in articles\" :key=\"article.id\">\n"
                "        <NuxtLink :to=\"`/articles/${article.id}`\">\n"
                "          <h2>{{ article.titre }}</h2>\n"
                "        </NuxtLink>\n"
                "        <p>{{ article.resume }}</p>\n"
                "      </article>\n"
                "    </div>\n"
                "  </div>\n"
                "</template>\n\n"
                "<script setup lang=\"ts\">\n"
                "interface Article {\n"
                "  id: number;\n"
                "  titre: string;\n"
                "  resume: string;\n"
                "  contenu: string;\n"
                "}\n\n"
                "const { data: articles, pending } = await useFetch<Article[]>('/api/articles');\n\n"
                "useHead({\n"
                "  title: 'Accueil - Mon Blog',\n"
                "  meta: [\n"
                "    { name: 'description', content: 'Decouvrez nos derniers articles' },\n"
                "  ],\n"
                "});\n"
                "</script>\n\n"
                "<!-- server/api/articles.get.ts -->\n"
                "export default defineEventHandler(async () => {\n"
                "  const articles = [\n"
                "    { id: 1, titre: 'Decouvrir Nuxt 3', resume: 'Un guide complet...', contenu: '...' },\n"
                "    { id: 2, titre: 'Le rendu hybride', resume: 'SSR, SSG et SPA...', contenu: '...' },\n"
                "  ];\n"
                "  return articles;\n"
                "});"
            ),
            "performance": {
                "startup_time": (
                    "Le temps de demarrage d'une application Nuxt depend du mode de rendu choisi. "
                    "En mode SSG, les pages pre-rendues sont servies comme du HTML statique, offrant "
                    "des temps de chargement extremement rapides car aucun traitement serveur n'est "
                    "necessaire. En mode SSR, le serveur Nitro genere le HTML a chaque requete, "
                    "ajoutant une latence liee au rendu mais permettant un contenu toujours a jour. "
                    "Le framework optimise automatiquement le code splitting par route, ne chargeant "
                    "que le JavaScript necessaire pour la page courante."
                ),
                "throughput": (
                    "Nitro, le moteur serveur de Nuxt 3, est concu pour des performances elevees "
                    "avec un faible overhead. En mode SSG, le debit est essentiellement limite par "
                    "le serveur de fichiers statiques ou le CDN, offrant des performances excellentes. "
                    "En mode SSR, Nitro exploite les workers et le cache pour maximiser le nombre "
                    "de requetes traitees par seconde. Le rendu hybride avec ISR (Incremental Static "
                    "Regeneration) combine les avantages des deux approches en regenerant les pages "
                    "statiques de maniere incrementale."
                ),
                "memory": (
                    "La consommation memoire de Nuxt varie selon le mode de deploiement. En mode "
                    "statique, l'empreinte cote serveur est negligeable. En mode SSR, chaque requete "
                    "necessite la creation d'une instance Vue pour le rendu, ce qui consomme de la "
                    "memoire. Nitro optimise cette consommation en reutilisant les ressources et en "
                    "gerant efficacement le cycle de vie des instances. Cote client, la consommation "
                    "est comparable a une application Vue.js classique, avec l'overhead d'hydratation "
                    "lors du premier chargement."
                ),
                "concurrency_model": (
                    "Nuxt.js repose sur le modele de concurrence de Node.js (boucle evenementielle "
                    "asynchrone) pour le rendu cote serveur via Nitro. Les requetes sont traitees "
                    "de maniere non bloquante, permettant a un seul processus de gerer de nombreuses "
                    "connexions simultanees. Pour les deploiements edge, Nitro utilise les workers "
                    "des plateformes (Cloudflare Workers, Deno Deploy) qui offrent une isolation "
                    "et une scalabilite horizontale natives."
                ),
            },
            "learning_curve": (
                "La courbe d'apprentissage de Nuxt.js est moderee pour les developpeurs ayant "
                "deja une experience avec Vue.js. Les conventions du framework (routage par fichiers, "
                "auto-imports, layouts) sont intuitives et reduisent le temps de configuration "
                "initial. Cependant, la maitrise des differents modes de rendu (SSR, SSG, SPA, "
                "ISR) et de leurs implications sur le cycle de vie des composants, l'hydratation "
                "et le fetching de donnees necessite un investissement significatif. La comprehension "
                "du fonctionnement de Nitro, des composables isomorphes (useAsyncData, useFetch) et "
                "de la distinction entre code serveur et code client est essentielle pour eviter "
                "les erreurs courantes. Les developpeurs venant d'autres frameworks SSR comme "
                "Next.js retrouveront des concepts familiers, facilitant la transition."
            ),
            "community_size": (
                "Nuxt.js possede une communaute active et passionnee, avec plus de 55 000 etoiles "
                "sur GitHub pour Nuxt 3. La communaute est particulierement forte en Europe et en "
                "Asie, ou Vue.js jouit d'une grande popularite. Le serveur Discord officiel de Nuxt "
                "rassemble des dizaines de milliers de membres actifs. NuxtNation est la conference "
                "annuelle dediee au framework. La communaute contribue activement aux modules, "
                "aux correctifs et a la documentation. Bien que plus petite que celle de Next.js, "
                "la communaute Nuxt est reconnue pour sa bienveillance et son accessibilite."
            ),
            "job_market": (
                "Le marche de l'emploi pour Nuxt.js est en croissance constante, suivant la "
                "tendance d'adoption de Vue.js dans l'industrie. Les offres mentionnant Nuxt "
                "sont particulierement frequentes en Europe (France, Allemagne, Pays-Bas), en "
                "Asie (Japon, Chine, Coree du Sud) et dans les entreprises qui ont adopte Vue.js "
                "comme framework frontend principal. Les postes de developpeur Nuxt sont souvent "
                "associes a des competences fullstack, incluant la gestion du rendu serveur et "
                "le deploiement. Les salaires sont competitifs et en hausse, refletant la demande "
                "croissante pour des developpeurs capables de construire des applications web "
                "performantes et bien referencees avec les techniques modernes de rendu."
            ),
        },
        "traits": {
            "performance": 7,
            "developer_speed": 8,
            "learning_curve": 4,
            "ecosystem_size": 7,
            "type_safety": 6,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 8,
        },
    },

    "astro": {
        "name": "Astro",
        "category": "frontend",
        "year_created": 2021,
        "creator": "Fred K. Schott",
        "paradigm": ["Island Architecture", "Multi-framework", "Content-first"],
        "typing": "JavaScript/TypeScript",
        "sections": {
            "overview": (
                "Astro est un framework web moderne concu pour creer des sites web orientes "
                "contenu, rapides par defaut. Lance en 2021 par Fred K. Schott et l'equipe "
                "derriere le bundler Snowpack, Astro se distingue par son approche radicalement "
                "differente du rendu : par defaut, il genere du HTML statique pur sans aucun "
                "JavaScript cote client. Cette philosophie, appelee 'Zero JS by default', "
                "permet d'obtenir des scores de performance exceptionnels sur des outils comme "
                "Lighthouse, avec des temps de chargement extremement rapides.\n\n"
                "Le concept central d'Astro est l'Island Architecture (architecture en ilots). "
                "Plutot que d'hydrater l'ensemble de la page en une seule application JavaScript "
                "monolithique, Astro permet de definir des 'ilots' interactifs independants au "
                "sein d'une page autrement statique. Chaque ilot peut etre hydrate selon une "
                "strategie specifique : au chargement de la page (client:load), lorsqu'il "
                "devient visible dans le viewport (client:visible), lorsque le navigateur est "
                "inactif (client:idle), ou uniquement sur un evenement media query (client:media). "
                "Cette granularite permet un controle precis du JavaScript envoye au navigateur.\n\n"
                "L'un des atouts les plus distinctifs d'Astro est son support multi-framework. "
                "Un meme projet Astro peut integrer des composants React, Vue, Svelte, SolidJS, "
                "Preact, Lit ou Alpine.js, chacun fonctionnant comme un ilot independant. Cette "
                "flexibilite est particulierement precieuse pour les equipes qui souhaitent "
                "migrer progressivement d'un framework a un autre, ou qui veulent utiliser le "
                "meilleur outil pour chaque partie de leur interface. Le systeme de templates "
                "d'Astro utilise une syntaxe propre (.astro) qui ressemble a du HTML enrichi "
                "avec des expressions JavaScript, offrant une prise en main rapide pour les "
                "developpeurs familiers avec le HTML et JSX. Avec sa collection de contenus "
                "type-safe, son support natif de Markdown et MDX, et ses integrations pour les "
                "CMS headless, Astro s'est impose comme le choix de reference pour les sites "
                "de contenu performants."
            ),
            "history": (
                "L'histoire d'Astro commence avec Snowpack, un outil de build JavaScript "
                "cree par Fred K. Schott qui exploitait les modules ES natifs du navigateur "
                "pour accelerer le developpement. Fort de cette experience, Schott et son "
                "equipe ont imagine un framework qui repenserait fondamentalement la maniere "
                "dont les sites web sont construits et livres au navigateur.\n\n"
                "Astro a ete annonce publiquement en mars 2021 et a immediatement suscite "
                "un vif interet dans la communaute JavaScript. La version 0.x a pose les "
                "bases de l'Island Architecture et du support multi-framework. Astro 1.0 "
                "est sorti en aout 2022, marquant la premiere version stable du framework "
                "avec un engagement de stabilite de l'API. Astro 2.0 (janvier 2023) a "
                "introduit les Content Collections, un systeme type-safe pour gerer le "
                "contenu Markdown et MDX, revolutionnant la maniere de structurer les "
                "sites de contenu. Astro 3.0 (aout 2023) a apporte View Transitions, "
                "permettant des animations de navigation fluides entre les pages sans "
                "JavaScript supplementaire significatif. Astro 4.0 (decembre 2023) a "
                "ameliore la barre d'outils de developpement, les routes internationalisees "
                "et l'API de journalisation. Astro 5.0 (2024) a introduit la couche de "
                "contenu, les Server Islands et des ameliorations de performance "
                "significatives. Le framework continue d'evoluer rapidement tout en "
                "maintenant sa philosophie centrale : livrer moins de JavaScript au "
                "navigateur pour des sites plus rapides."
            ),
            "architecture": (
                "L'architecture d'Astro repose sur le concept fondamental d'Island "
                "Architecture, une approche qui represente un changement de paradigme dans "
                "la construction de sites web. Contrairement aux frameworks SPA traditionnels "
                "qui hydratent la page entiere en une seule application JavaScript, Astro "
                "decoupe l'interface en regions independantes appelees 'ilots' (islands). "
                "Chaque ilot est un composant interactif autonome entoure de HTML statique. "
                "Le serveur genere l'integralite du HTML de la page, et seuls les ilots "
                "necessitant de l'interactivite recoivent du JavaScript.\n\n"
                "Le processus de build d'Astro est en deux phases. D'abord, le framework "
                "compile les fichiers .astro, Markdown et MDX en HTML statique. Les "
                "composants de framework (React, Vue, Svelte, etc.) sont rendus cote "
                "serveur pour produire leur HTML. Ensuite, pour les ilots marques avec "
                "une directive client:*, Astro genere des bundles JavaScript individuels "
                "qui seront charges et hydrateront ces composants specifiques cote client.\n\n"
                "Astro utilise Vite comme moteur de build sous-jacent, beneficiant de son "
                "rechargement a chaud ultra-rapide en developpement et de son bundling "
                "optimise en production. Le systeme de routage est base sur les fichiers : "
                "chaque fichier dans le dossier src/pages correspond a une route. Astro "
                "supporte plusieurs modes de sortie : statique (par defaut, generation de "
                "fichiers HTML), serveur (rendu a la demande avec SSR), et hybride (combinaison "
                "des deux). Le moteur de rendu est concu pour etre extensible via un systeme "
                "d'integrations qui permettent d'ajouter des frameworks UI, des outils CSS, "
                "des adaptateurs de deploiement et d'autres fonctionnalites."
            ),
            "pros_cons": {
                "pros": [
                    "Performance exceptionnelle par defaut grace au zero JavaScript cote client",
                    "Island Architecture permettant un controle precis de l'hydratation",
                    "Support multi-framework unique : React, Vue, Svelte, Solid, etc. dans un meme projet",
                    "Excellent support du contenu avec Markdown, MDX et Content Collections type-safe",
                    "View Transitions integrees pour des navigations fluides entre pages",
                    "Courbe d'apprentissage douce grace a une syntaxe proche du HTML standard",
                    "Ecosysteme d'integrations riche et croissant avec plus de 500 themes et plugins",
                    "SEO optimal grace au rendu statique complet du HTML",
                ],
                "cons": [
                    "Moins adapte aux applications hautement interactives de type SPA complexe",
                    "L'ecosysteme est encore jeune compare a React ou Vue, certains outils manquent",
                    "Le modele mental de l'Island Architecture peut derouter les developpeurs habitues aux SPA",
                    "Le partage d'etat entre ilots de frameworks differents peut etre complexe",
                    "Le mode SSR est moins mature que celui de Next.js ou Nuxt",
                    "Les applications temps reel avec de nombreuses mises a jour d'etat ne sont pas le cas d'usage ideal",
                ],
            },
            "use_cases": (
                "Astro excelle dans la creation de sites web orientes contenu ou la performance "
                "et le SEO sont des priorites absolues. Les blogs, sites de documentation, "
                "portfolios et sites marketing sont les cas d'utilisation les plus naturels du "
                "framework. Les sites e-commerce a catalogue, les pages d'atterrissage et les "
                "sites institutionnels beneficient enormement de la generation statique d'Astro "
                "combinee a des ilots interactifs pour les paniers d'achat ou les formulaires.\n\n"
                "Les sites de documentation technique sont un autre cas d'utilisation phare, "
                "avec le theme Starlight qui offre une solution cle en main pour creer des "
                "documentations performantes et accessibles. Les sites de presse et les magazines "
                "en ligne, qui privilegient le temps de chargement et le referencement, sont "
                "egalement des candidats ideaux. Les equipes qui souhaitent migrer progressivement "
                "d'un framework a un autre trouvent dans Astro un outil de transition puissant "
                "grace au support multi-framework."
            ),
            "ecosystem": (
                "L'ecosysteme d'Astro croit rapidement et s'articule autour de plusieurs axes. "
                "Le systeme d'integrations officielles couvre les principaux frameworks UI "
                "(React, Vue, Svelte, Solid, Preact, Lit, Alpine.js), les outils CSS (Tailwind "
                "CSS, UnoCSS), les optimisateurs d'images (@astrojs/image) et les adaptateurs "
                "de deploiement (Vercel, Netlify, Cloudflare, Node, Deno).\n\n"
                "Starlight est le theme de documentation officiel d'Astro, devenu une reference "
                "dans le domaine des sites de documentation statiques. Le catalogue Astro "
                "propose plus de 500 themes et composants communautaires. Pour le contenu, "
                "Astro s'integre avec les principaux CMS headless : Contentful, Strapi, "
                "Sanity, Storyblok, WordPress (via API REST), Prismic et bien d'autres. "
                "Cote authentification et base de donnees, Astro DB fournit une solution "
                "integree, tandis que des integrations avec Supabase, Firebase, Turso et "
                "Drizzle ORM sont disponibles. L'outil de build sous-jacent Vite permet "
                "d'utiliser l'ensemble de l'ecosysteme de plugins Vite et Rollup."
            ),
            "companies": [
                "Google (Firebase docs)",
                "Porsche",
                "Microsoft (documentation)",
                "Nordstrom",
                "The Guardian",
                "Rokt",
                "Trivago",
            ],
            "code_example": (
                "---\n"
                "// src/pages/index.astro\n"
                "import Layout from '../layouts/Layout.astro';\n"
                "import Card from '../components/Card.astro';\n"
                "import Compteur from '../components/Compteur.jsx';\n"
                "import { getCollection } from 'astro:content';\n\n"
                "const articles = await getCollection('blog');\n"
                "const articlesRecents = articles\n"
                "  .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf())\n"
                "  .slice(0, 5);\n"
                "---\n\n"
                "<Layout titre=\"Accueil\">\n"
                "  <main>\n"
                "    <h1>Bienvenue sur mon site</h1>\n"
                "    <p>Construit avec Astro pour une performance optimale.</p>\n\n"
                "    <!-- Ilot interactif React, hydrate quand visible -->\n"
                "    <Compteur client:visible initial={0} />\n\n"
                "    <section>\n"
                "      <h2>Articles recents</h2>\n"
                "      {articlesRecents.map((article) => (\n"
                "        <Card\n"
                "          titre={article.data.titre}\n"
                "          description={article.data.description}\n"
                "          url={`/blog/${article.slug}`}\n"
                "        />\n"
                "      ))}\n"
                "    </section>\n"
                "  </main>\n"
                "</Layout>"
            ),
            "performance": {
                "startup_time": (
                    "Le temps de demarrage des sites Astro est exceptionnel. En mode statique, "
                    "les pages sont de purs fichiers HTML sans JavaScript a parser ni a executer, "
                    "ce qui permet un First Contentful Paint (FCP) quasi instantane. Meme en mode "
                    "SSR, le rendu cote serveur est extremement rapide car le framework ne charge "
                    "que le strict minimum de JavaScript. Les metriques Core Web Vitals sont "
                    "naturellement excellentes sans optimisation particuliere."
                ),
                "throughput": (
                    "Le debit des sites Astro statiques depend principalement du serveur web ou "
                    "du CDN qui les heberge, car les pages sont pre-generees. En mode SSR, le "
                    "rendu est efficient grace a un moteur de templates optimise et a l'absence "
                    "de framework lourd cote serveur. Les pages contenant des ilots interactifs "
                    "chargent le JavaScript de maniere incrementale, evitant les goulets "
                    "d'etranglement au chargement."
                ),
                "memory": (
                    "La consommation memoire cote client est minimale pour les pages purement "
                    "statiques. Seuls les ilots interactifs consomment de la memoire JavaScript, "
                    "et chaque ilot est isole, evitant les fuites memoire liees a une application "
                    "monolithique. Cote serveur, lors du build, Astro peut consommer une quantite "
                    "significative de memoire pour les sites tres volumineux avec des milliers "
                    "de pages a generer."
                ),
                "concurrency_model": (
                    "Astro n'impose pas de modele de concurrence specifique cote client, car "
                    "chaque ilot fonctionne de maniere independante. En mode SSR, le serveur "
                    "peut traiter les requetes de maniere concurrente grace aux adaptateurs "
                    "Node.js, Deno ou Cloudflare Workers. Les ilots etant independants, ils "
                    "peuvent etre hydrater en parallele sans conflit."
                ),
            },
            "learning_curve": (
                "La courbe d'apprentissage d'Astro est l'une des plus douces parmi les "
                "frameworks web modernes. La syntaxe des fichiers .astro est tres proche du "
                "HTML standard, avec un frontmatter en JavaScript delimite par des tirets (---). "
                "Les developpeurs ayant des bases en HTML, CSS et JavaScript peuvent devenir "
                "productifs en quelques heures. Les concepts de routage par fichiers et de "
                "composants sont intuitifs. Cependant, la maitrise de l'Island Architecture, "
                "des strategies d'hydratation (client:load, client:visible, client:idle), des "
                "Content Collections et des differents modes de rendu (statique, SSR, hybride) "
                "necessite un apprentissage supplementaire. Les developpeurs habitues aux SPA "
                "traditionnels doivent adapter leur modele mental a l'approche 'HTML-first' "
                "d'Astro, ce qui peut demander un certain temps d'ajustement."
            ),
            "community_size": (
                "La communaute Astro connait une croissance rapide et impressionnante depuis "
                "sa creation. Le depot GitHub du framework depasse les 48 000 etoiles et "
                "continue de croitre regulierement. Le serveur Discord officiel regroupe des "
                "dizaines de milliers de membres actifs et constitue le principal lieu d'echange "
                "et de support. Astro organise des evenements communautaires reguliers et "
                "dispose d'un programme d'ambassadeurs. La communaute est reconnue pour son "
                "ouverture, sa bienveillance et sa reactivite. Bien que plus petite que celles "
                "de React ou Vue, elle est extremement engagee et contribue activement a "
                "l'ecosysteme via des themes, des integrations et des tutoriels."
            ),
            "job_market": (
                "Le marche de l'emploi pour Astro est encore emergent mais en forte croissance. "
                "Les offres mentionnant Astro se concentrent principalement dans les agences "
                "web, les equipes de documentation technique et les entreprises axees sur le "
                "contenu et le marketing digital. La demande est particulierement forte pour "
                "les roles lies au developpement de sites performants et bien references. "
                "Les developpeurs maitrisant Astro sont souvent recherches pour des missions "
                "de refonte visant a ameliorer les performances web. Comme Astro permet "
                "d'utiliser React, Vue ou Svelte, la competence Astro est souvent combinee "
                "avec la maitrise d'un de ces frameworks, augmentant l'employabilite globale "
                "du developpeur."
            ),
        },
        "traits": {
            "performance": 9,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 5,
            "type_safety": 6,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 7,
        },
    },

    "solidjs": {
        "name": "SolidJS",
        "category": "frontend",
        "year_created": 2018,
        "creator": "Ryan Carniato",
        "paradigm": ["Reactif fin", "Declaratif", "Compile"],
        "typing": "JavaScript/TypeScript",
        "sections": {
            "overview": (
                "SolidJS est un framework JavaScript declaratif et performant pour construire "
                "des interfaces utilisateur. Cree par Ryan Carniato et rendu public en 2018, "
                "SolidJS se distingue par son approche unique de la reactivite a grain fin "
                "(fine-grained reactivity) et par l'absence totale de Virtual DOM. Contrairement "
                "a React qui utilise un DOM virtuel et un mecanisme de reconciliation pour "
                "detecter les changements, SolidJS compile les composants en instructions "
                "imperatives qui mettent a jour le DOM reel de maniere chirurgicale, uniquement "
                "la ou les donnees ont change.\n\n"
                "Le systeme de reactivite de SolidJS repose sur trois primitives fondamentales : "
                "les signaux (createSignal), les effets (createEffect) et les memos "
                "(createMemo). Un signal est une valeur reactive qui peut etre lue et modifiee. "
                "Lorsqu'un signal est lu a l'interieur d'un effet ou d'un calcul derive, "
                "SolidJS enregistre automatiquement cette dependance. Quand la valeur du signal "
                "change, seuls les effets et les parties du DOM qui dependent de ce signal "
                "specifique sont mis a jour, sans recalculer l'ensemble de l'arbre de "
                "composants.\n\n"
                "Cette approche offre des performances remarquables qui rivalisent avec du "
                "JavaScript vanille optimise. Dans les benchmarks JS Framework, SolidJS se "
                "classe regulierement parmi les frameworks les plus rapides, souvent en tete "
                "du classement. La syntaxe de SolidJS ressemble volontairement a celle de "
                "React avec l'utilisation de JSX, ce qui facilite la transition pour les "
                "developpeurs React. Cependant, sous cette syntaxe familiere se cache un "
                "modele d'execution fondamentalement different : les composants SolidJS ne "
                "s'executent qu'une seule fois (pas de re-rendu), et c'est le systeme de "
                "reactivite qui se charge de maintenir le DOM a jour. Cette difference "
                "subtile mais fondamentale elimine des categories entieres de problemes "
                "de performance comme les re-rendus inutiles, les dependances manquantes "
                "dans les hooks et les problemes de memoisation."
            ),
            "history": (
                "L'histoire de SolidJS commence en 2016 lorsque Ryan Carniato, alors "
                "developpeur front-end experimeme, commence a explorer les limites du "
                "Virtual DOM et les alternatives possibles. Inspire par les systemes de "
                "reactivite de Knockout.js et de MobX, mais aussi par les techniques de "
                "compilation de Svelte, Carniato entreprend de creer un framework qui "
                "combinerait la reactivite a grain fin avec une syntaxe familiere de "
                "type JSX.\n\n"
                "Les premieres versions de SolidJS ont ete publiees sur npm des 2018, "
                "mais le framework est reste relativement confidentiel pendant ses "
                "premieres annees. La version 1.0 a ete publiee en juin 2021, marquant "
                "un jalon important de stabilite et de maturite. Cette sortie a ete "
                "accompagnee d'une visibilite accrue dans la communaute JavaScript, "
                "notamment grace aux benchmarks impressionnants du framework.\n\n"
                "En 2022, SolidJS a remporte le prix du projet open source le plus "
                "innovant lors des OS Awards, confirmant sa reconnaissance par la "
                "communaute. SolidStart, le meta-framework officiel pour le rendu cote "
                "serveur et le routage, a ete annonce et developpe activement. La "
                "version 1.7 (2023) et les versions suivantes ont apporte des "
                "ameliorations continues en termes de taille de bundle, de performances "
                "de compilation et de support TypeScript. Le projet Solid 2.0 est en "
                "cours de developpement avec des ameliorations significatives du systeme "
                "de reactivite et du compilateur."
            ),
            "architecture": (
                "L'architecture de SolidJS se distingue fondamentalement des frameworks "
                "bases sur le Virtual DOM par son approche de reactivite a grain fin sans "
                "VDOM. Dans SolidJS, la reactivite est la brique de base sur laquelle tout "
                "le systeme est construit. Le compilateur transforme le JSX en appels DOM "
                "reels optimises a la compilation, eliminant le besoin d'un algorithme de "
                "diffing au runtime.\n\n"
                "Le systeme de reactivite repose sur un graphe de dependances automatique. "
                "Lorsqu'un composant s'execute pour la premiere fois, SolidJS cree les "
                "elements DOM et etablit les liaisons reactives. Chaque expression reactive "
                "dans le JSX est enveloppee dans un effet qui s'abonne automatiquement aux "
                "signaux qu'elle lit. Quand un signal change, seuls les effets concernes "
                "sont re-executes, mettant a jour directement les noeuds DOM correspondants "
                "sans toucher au reste de l'arbre.\n\n"
                "Cette architecture elimine plusieurs couches d'abstraction presentes dans "
                "les frameworks a Virtual DOM : pas de creation d'arbre virtuel, pas de "
                "diffing, pas de reconciliation, pas de re-rendu de composants entiers. "
                "Le resultat est une empreinte memoire reduite et des mises a jour quasi "
                "instantanees. Le compilateur SolidJS joue un role crucial en analysant "
                "le JSX pour identifier les parties statiques et dynamiques du template. "
                "Les parties statiques sont creees une seule fois via des clones de "
                "template HTML, tandis que les parties dynamiques sont connectees au "
                "systeme reactif. Cette separation permet des optimisations impossibles "
                "dans les frameworks qui recalculent l'arbre entier a chaque mise a jour."
            ),
            "pros_cons": {
                "pros": [
                    "Performances parmi les meilleures de tous les frameworks, proches du JavaScript vanille",
                    "Reactivite a grain fin eliminant les re-rendus inutiles et les problemes de memoisation",
                    "Syntaxe JSX familiere facilitant la transition depuis React",
                    "Taille de bundle tres reduite grace a la compilation et au tree-shaking agressif",
                    "Composants executes une seule fois, simplifiant le modele mental d'execution",
                    "Primitives reactives puissantes et composables (signaux, effets, memos)",
                    "Support TypeScript solide et natif",
                ],
                "cons": [
                    "Ecosysteme encore restreint par rapport a React ou Vue, moins de bibliotheques tierces",
                    "Communaute plus petite limitant les ressources d'apprentissage disponibles",
                    "SolidStart (meta-framework) est encore en phase de maturation",
                    "Les differences subtiles avec React (pas de re-rendu, destructuration interdite des props) peuvent creer de la confusion",
                    "Moins d'offres d'emploi specifiquement dediees a SolidJS",
                    "Le modele de reactivite a grain fin peut surprendre les developpeurs habitues au Virtual DOM",
                ],
            },
            "use_cases": (
                "SolidJS excelle dans les applications ou la performance est une priorite "
                "absolue. Les tableaux de bord interactifs avec de nombreuses mises a jour "
                "en temps reel, les visualisations de donnees complexes, les editeurs en "
                "ligne et les applications de type feuille de calcul tirent pleinement parti "
                "de la reactivite a grain fin de SolidJS. Les interfaces avec des milliers "
                "d'elements interactifs, ou les frameworks bases sur le Virtual DOM montrent "
                "leurs limites, sont un terrain ideal pour SolidJS.\n\n"
                "Les applications embarquees et les widgets tiers beneficient de la petite "
                "taille de bundle de SolidJS. Les projets necessitant une reactivite "
                "ultra-rapide, comme les outils de trading, les jeux dans le navigateur "
                "ou les applications musicales interactives, trouvent dans SolidJS un "
                "framework capable de rivaliser avec du code natif. Les developpeurs React "
                "insatisfaits des problemes de performance ou du modele de re-rendu "
                "trouvent dans SolidJS une alternative familiere mais fondamentalement "
                "plus performante."
            ),
            "ecosystem": (
                "L'ecosysteme de SolidJS, bien que plus jeune et plus petit que celui de "
                "React, croit de maniere soutenue et couvre les besoins essentiels du "
                "developpement web moderne. SolidStart est le meta-framework officiel "
                "fournissant le rendu cote serveur (SSR), le routage base sur les fichiers "
                "et les fonctions serveur, similaire a ce que Next.js offre pour React.\n\n"
                "Pour le routage cote client, @solidjs/router est la solution officielle. "
                "Solid Primitives est une collection de primitives reactives utilitaires "
                "inspiree de VueUse et de react-use. Pour la gestion d'etat, les signaux "
                "natifs de Solid sont suffisants pour la plupart des cas, mais des "
                "bibliotheques comme solid-zustand et solid-jotai offrent des patterns "
                "familiers aux developpeurs React. Kobalte fournit des composants "
                "d'interface accessibles et sans style, similaires a Radix UI. "
                "TanStack (Query, Table, Virtual) supporte officiellement SolidJS. "
                "Pour le styling, Tailwind CSS, UnoCSS et vanilla-extract s'integrent "
                "parfaitement. Les outils de test incluent solid-testing-library et Vitest. "
                "L'ecosysteme beneficie egalement de la compatibilite avec la plupart des "
                "plugins Vite, Vite etant le bundler utilise par defaut."
            ),
            "companies": [
                "eBay",
                "Cloudflare",
                "Rakuten",
                "Tencent",
                "Builder.io",
                "Netlify",
            ],
            "code_example": (
                "import { createSignal, createEffect, For, Show } from 'solid-js';\n\n"
                "function ListeTaches() {\n"
                "  const [taches, setTaches] = createSignal([]);\n"
                "  const [saisie, setSaisie] = createSignal('');\n"
                "  const [filtre, setFiltre] = createSignal('toutes');\n\n"
                "  // Effet reactif : sauvegarde automatique\n"
                "  createEffect(() => {\n"
                "    localStorage.setItem('taches', JSON.stringify(taches()));\n"
                "  });\n\n"
                "  const tachesFiltrees = () => {\n"
                "    const f = filtre();\n"
                "    if (f === 'actives') return taches().filter(t => !t.faite);\n"
                "    if (f === 'terminees') return taches().filter(t => t.faite);\n"
                "    return taches();\n"
                "  };\n\n"
                "  const ajouterTache = () => {\n"
                "    if (saisie().trim()) {\n"
                "      setTaches([...taches(), {\n"
                "        id: Date.now(),\n"
                "        texte: saisie(),\n"
                "        faite: false\n"
                "      }]);\n"
                "      setSaisie('');\n"
                "    }\n"
                "  };\n\n"
                "  const basculer = (id) => {\n"
                "    setTaches(taches().map(t =>\n"
                "      t.id === id ? { ...t, faite: !t.faite } : t\n"
                "    ));\n"
                "  };\n\n"
                "  return (\n"
                "    <div>\n"
                "      <h1>Liste de taches</h1>\n"
                "      <input\n"
                "        value={saisie()}\n"
                "        onInput={(e) => setSaisie(e.target.value)}\n"
                "        placeholder=\"Nouvelle tache...\"\n"
                "      />\n"
                "      <button onClick={ajouterTache}>Ajouter</button>\n\n"
                "      <div>\n"
                "        <button onClick={() => setFiltre('toutes')}>Toutes</button>\n"
                "        <button onClick={() => setFiltre('actives')}>Actives</button>\n"
                "        <button onClick={() => setFiltre('terminees')}>Terminees</button>\n"
                "      </div>\n\n"
                "      <ul>\n"
                "        <For each={tachesFiltrees()}>\n"
                "          {(tache) => (\n"
                "            <li\n"
                "              onClick={() => basculer(tache.id)}\n"
                "              style={{ 'text-decoration': tache.faite ? 'line-through' : 'none' }}\n"
                "            >\n"
                "              {tache.texte}\n"
                "            </li>\n"
                "          )}\n"
                "        </For>\n"
                "      </ul>\n\n"
                "      <Show when={taches().length > 0}>\n"
                "        <p>{taches().filter(t => !t.faite).length} taches restantes</p>\n"
                "      </Show>\n"
                "    </div>\n"
                "  );\n"
                "}\n\n"
                "export default ListeTaches;"
            ),
            "performance": {
                "startup_time": (
                    "Le temps de demarrage de SolidJS est parmi les plus rapides de tous "
                    "les frameworks JavaScript. Le runtime de SolidJS est extremement leger "
                    "(environ 7 Ko minifie et gzippe), bien plus petit que React ou Vue. "
                    "Les composants etant compiles en instructions DOM directes, il n'y a "
                    "pas de Virtual DOM a initialiser ni d'arbre de composants a construire. "
                    "Le premier rendu est quasi instantane, avec un Time to Interactive (TTI) "
                    "minimal."
                ),
                "throughput": (
                    "Le debit de SolidJS est exceptionnel grace a l'absence de Virtual DOM "
                    "et a la reactivite a grain fin. Chaque mise a jour ne touche que les "
                    "noeuds DOM concernes, sans recalcul ni comparaison d'arbre. Dans les "
                    "benchmarks JS Framework, SolidJS affiche des temps de mise a jour "
                    "jusqu'a 2 a 5 fois plus rapides que React pour les operations sur les "
                    "listes et les mises a jour partielles. Le batching automatique des "
                    "mises a jour evite les re-rendus superflus."
                ),
                "memory": (
                    "La consommation memoire de SolidJS est remarquablement faible. "
                    "L'absence de Virtual DOM elimine la duplication de la structure de "
                    "l'interface en memoire. Chaque signal occupe un espace minimal et les "
                    "abonnements reactifs sont legers. Les benchmarks montrent une utilisation "
                    "memoire 30 a 50 pourcent inferieure a React pour des applications "
                    "equivalentes. Le garbage collector est moins sollicite car il n'y a "
                    "pas de creation et destruction repetees d'arbres virtuels."
                ),
                "concurrency_model": (
                    "SolidJS gere la concurrence via son systeme de batching reactif. Les "
                    "mises a jour de signaux au sein d'une meme transaction sont regroupees "
                    "et appliquees de maniere synchrone, evitant les etats intermediaires "
                    "incoherents. Les transitions (useTransition) permettent de marquer "
                    "certaines mises a jour comme non urgentes, similairement a React 18. "
                    "Le modele synchrone de SolidJS simplifie le raisonnement sur l'ordre "
                    "des mises a jour par rapport au rendu concurrent asynchrone."
                ),
            },
            "learning_curve": (
                "La courbe d'apprentissage de SolidJS est moderee, avec des nuances "
                "importantes selon l'experience du developpeur. Pour les developpeurs React, "
                "la syntaxe JSX et les concepts de composants sont immediatement familiers, "
                "permettant une prise en main rapide des bases. Cependant, les differences "
                "fondamentales avec React representent un defi subtil : les composants ne "
                "s'executent qu'une seule fois, les props ne doivent pas etre destructurees "
                "(car cela casse la reactivite), et les signaux doivent etre appeles comme "
                "des fonctions pour lire leur valeur. Ces differences, bien que simples en "
                "theorie, necessitent un changement de reflexes profondement ancres chez les "
                "developpeurs React. La maitrise du systeme de reactivite a grain fin, des "
                "stores, des contextes et des patterns avances de composition reactive demande "
                "un investissement significatif. Les developpeurs venant de Knockout.js ou "
                "MobX retrouveront des concepts familiers et auront une transition plus douce."
            ),
            "community_size": (
                "La communaute SolidJS est encore modeste en taille mais extremement passionnee "
                "et active. Le depot GitHub compte plus de 33 000 etoiles, temoignant d'un "
                "interet significatif malgre la jeunesse relative du framework. Le serveur "
                "Discord officiel est le principal lieu d'echange, avec plusieurs milliers de "
                "membres actifs. Ryan Carniato, le createur, est tres present et accessible, "
                "participant regulierement aux discussions et repondant aux questions. La "
                "communaute contribue activement aux bibliotheques de l'ecosysteme et a la "
                "documentation. Des contenus educatifs (articles de blog, videos YouTube, "
                "cours) emergent de maniere croissante, bien que les ressources restent "
                "moins abondantes que pour React ou Vue."
            ),
            "job_market": (
                "Le marche de l'emploi specifiquement dedie a SolidJS est encore restreint "
                "en 2025, le framework etant principalement adopte par des equipes techniques "
                "avancees et des entreprises privilegiant la performance maximale. Les offres "
                "d'emploi mentionnant SolidJS sont rares mais souvent associees a des postes "
                "techniques de haut niveau. Cependant, la maitrise de SolidJS est un signal "
                "fort de competence technique approfondie qui est valorise lors des entretiens, "
                "meme pour des postes React. La comprehension de la reactivite a grain fin et "
                "de la compilation de templates sont des competences transferables a l'ensemble "
                "de l'ecosysteme frontend moderne, ou ces concepts influencent de plus en plus "
                "les frameworks etablis (Signals dans Angular, Fine-grained Reactivity dans "
                "Vue Vapor). Les developpeurs SolidJS sont souvent recrutes pour des roles "
                "d'architecte frontend ou de lead technique."
            ),
        },
        "traits": {
            "performance": 10,
            "developer_speed": 7,
            "learning_curve": 4,
            "ecosystem_size": 4,
            "type_safety": 7,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 7,
        },
    },
}
