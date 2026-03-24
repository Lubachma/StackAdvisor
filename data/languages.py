"""
Module de donnees pour le Stack Advisor CLI.
Contient les informations detaillees sur 14 langages de programmation.
Toutes les descriptions sont en francais.
"""

TECHNOLOGIES = {
    # =========================================================================
    # 1. C
    # =========================================================================
    "c": {
        "name": "C",
        "category": "language",
        "year_created": 1972,
        "creator": "Dennis Ritchie",
        "paradigm": ["Procedural", "Imperatif"],
        "typing": "Statique faible",
        "sections": {
            "overview": (
                "Le langage C est l'un des langages de programmation les plus influents "
                "et les plus anciens encore largement utilises aujourd'hui. Cree en 1972 par "
                "Dennis Ritchie aux laboratoires Bell d'AT&T, il a ete concu initialement "
                "pour reecrire le systeme d'exploitation UNIX, qui etait auparavant ecrit "
                "en assembleur. Le C est un langage de programmation procedurale de bas niveau "
                "qui offre un acces direct a la memoire via les pointeurs, une gestion manuelle "
                "de la memoire, et une correspondance etroite avec le langage machine. "
                "Sa philosophie fondamentale repose sur la confiance accordee au programmeur : "
                "le langage ne fait presque aucune verification a l'execution, ce qui permet "
                "des performances maximales mais impose une grande rigueur au developpeur. "
                "Le C est souvent qualifie de 'langage assembleur portable' car il permet "
                "d'ecrire du code proche du materiel tout en restant relativement independant "
                "de l'architecture cible. Il constitue la base sur laquelle sont construits "
                "de nombreux systemes d'exploitation modernes (Linux, Windows, macOS), "
                "des bases de donnees (PostgreSQL, SQLite), des interpreteurs de langages "
                "(CPython, Ruby MRI) et des systemes embarques. Le C reste incontournable "
                "dans les domaines ou les performances et le controle de la memoire sont "
                "critiques : noyaux de systemes d'exploitation, pilotes de peripheriques, "
                "systemes temps reel, et programmation embarquee. Malgre son age, le langage "
                "continue d'evoluer avec des normes regulieres (C11, C17, C23) qui ajoutent "
                "des fonctionnalites modernes tout en preservant sa simplicite et son efficacite."
            ),
            "history": (
                "L'histoire du C commence au debut des annees 1970 aux Bell Labs, ou Dennis "
                "Ritchie travaillait avec Ken Thompson sur le systeme UNIX. Thompson avait "
                "initialement cree le langage B, lui-meme inspire du BCPL de Martin Richards, "
                "pour programmer UNIX. Cependant, le B etait un langage sans types qui ne "
                "tirait pas pleinement parti des capacites du PDP-11, la nouvelle machine sur "
                "laquelle UNIX devait tourner. Ritchie a alors entrepris de creer un successeur "
                "au B, qu'il a naturellement appele C. Entre 1971 et 1973, le langage a evolue "
                "rapidement, avec l'ajout de types de donnees (int, char, float), de structures, "
                "et d'un preprocesseur. En 1973, le noyau UNIX a ete reecrit en C, une premiere "
                "historique pour un systeme d'exploitation. En 1978, Brian Kernighan et Dennis "
                "Ritchie ont publie 'The C Programming Language', communement appele K&R C, "
                "qui est devenu la reference informelle du langage pendant des annees. Face "
                "a la proliferation des compilateurs et des variantes, l'ANSI a entrepris la "
                "standardisation du langage, aboutissant a la norme ANSI C (C89) en 1989, "
                "adoptee par l'ISO en 1990 sous le nom C90. Cette norme a unifie le langage "
                "et defini les regles que tous les compilateurs devaient respecter. La norme "
                "C99 a apporte des ameliorations significatives : types entiers de taille fixe "
                "(stdint.h), support des commentaires // a la C++, les tableaux de longueur "
                "variable (VLA), le type _Bool, et les fonctions inline. La norme C11 (2011) "
                "a introduit le support des threads (_Thread_local, <threads.h>), les expressions "
                "generiques (_Generic), et le support des caracteres Unicode. C17 (2018) etait "
                "principalement une mise a jour corrective. La norme C23, la plus recente, "
                "apporte des ameliorations comme nullptr, les attributs standardises, et de "
                "nouvelles fonctionnalites pour la securite. L'influence du C sur l'informatique "
                "est incalculable : C++, Java, C#, JavaScript, PHP, et de nombreux autres "
                "langages ont emprunte sa syntaxe et ses concepts."
            ),
            "architecture": (
                "Le C est un langage compile qui produit directement du code machine natif "
                "pour la plateforme cible. Le processus de compilation se deroule en plusieurs "
                "etapes distinctes. D'abord, le preprocesseur traite les directives (#include, "
                "#define, #ifdef) et produit une unite de traduction. Ensuite, le compilateur "
                "transforme cette unite en code assembleur, puis l'assembleur produit du code "
                "objet (fichiers .o). Enfin, l'editeur de liens (linker) combine les fichiers "
                "objets et les bibliotheques pour produire un executable. Ce modele de compilation "
                "separee permet de compiler chaque fichier source independamment et de ne relier "
                "les composants qu'a la fin. Le modele de memoire du C est tres proche du "
                "materiel : la memoire est vue comme un tableau lineaire d'octets, et les "
                "pointeurs sont essentiellement des adresses memoire. Le programmeur gere "
                "manuellement l'allocation (malloc, calloc, realloc) et la liberation (free) "
                "de la memoire sur le tas (heap). La pile (stack) est utilisee pour les variables "
                "locales et les appels de fonctions. Le C n'a pas de ramasse-miettes (garbage "
                "collector), ce qui signifie que toute fuite de memoire ou toute utilisation "
                "de memoire liberee (use-after-free) est de la responsabilite du programmeur. "
                "Le systeme de types du C est relativement simple : types entiers de differentes "
                "tailles (char, short, int, long, long long), types flottants (float, double), "
                "pointeurs, tableaux, structures (struct), unions, et enumerations (enum). Le "
                "C permet les conversions de types implicites et explicites (casts), ce qui "
                "peut etre source de bugs subtils. L'ABI (Application Binary Interface) du C "
                "est devenue la reference universelle : pratiquement tous les langages modernes "
                "peuvent appeler des fonctions C via une FFI (Foreign Function Interface). "
                "Les compilateurs modernes (GCC, Clang, MSVC) effectuent des optimisations "
                "extremement agressives basees sur le comportement indefini et les regles "
                "d'aliasing strict, ce qui permet au C d'atteindre des performances proches "
                "de l'assembleur ecrit a la main."
            ),
            "pros_cons": {
                "pros": [
                    "Performances proches du code machine, ideal pour les applications critiques",
                    "Controle total sur la memoire et les ressources materielles",
                    "Langage extremement portable, disponible sur quasiment toutes les plateformes",
                    "ABI universelle servant de pont entre tous les autres langages",
                    "Syntaxe simple et minimaliste, langage avec peu de mots-cles",
                    "Ecosysteme mature avec des decennies de bibliotheques eprouvees",
                    "Ideal pour la programmation systeme, embarquee et temps reel",
                    "Compilation rapide et executables legers"
                ],
                "cons": [
                    "Gestion manuelle de la memoire source de bugs critiques (fuites, buffer overflow)",
                    "Aucune securite memoire integree, vulnerabilites frequentes",
                    "Pas de support natif de la programmation orientee objet",
                    "Systeme de modules rudimentaire base sur le preprocesseur (#include)",
                    "Gestion des chaines de caracteres primitive et source d'erreurs",
                    "Comportements indefinis nombreux pouvant causer des bugs subtils",
                    "Pas de gestion native des exceptions, gestion d'erreurs par codes retour",
                    "Pas de generiques (avant C11 _Generic, et encore tres limite)"
                ]
            },
            "use_cases": (
                "Le C est le langage de predilection pour la programmation systeme. Les noyaux "
                "des systemes d'exploitation majeurs (Linux, FreeBSD, parties de Windows et "
                "macOS) sont ecrits en C. Les pilotes de peripheriques, qui necessitent un "
                "acces direct au materiel et des contraintes de performance strictes, sont "
                "quasi exclusivement ecrits en C. Dans le domaine de l'embarque, le C domine "
                "completement : microcontroleurs, systemes temps reel (RTOS), firmware d'appareils "
                "IoT, controleurs automobiles, et avionique. Les contraintes de memoire et de "
                "puissance de calcul de ces environnements rendent le C incontournable. Les "
                "bases de donnees hautes performances comme PostgreSQL, MySQL et SQLite sont "
                "ecrites en C, tirant parti du controle fin de la memoire et des optimisations "
                "possibles. Les interpreteurs et machines virtuelles de nombreux langages de "
                "haut niveau sont implementes en C : CPython (Python), Ruby MRI, Lua, et PHP. "
                "Le C est egalement tres utilise dans le developpement de jeux video pour les "
                "moteurs de rendu bas niveau et les bibliotheques graphiques (OpenGL, Vulkan). "
                "Dans le domaine du reseau, les serveurs haute performance comme Nginx et "
                "Redis sont ecrits en C. Les bibliotheques de cryptographie (OpenSSL, libsodium) "
                "et les outils de securite necessitent la precision et les performances du C. "
                "Le calcul scientifique et le traitement du signal utilisent egalement le C "
                "pour les noyaux de calcul intensif. Enfin, le C est utilise pour les "
                "bibliotheques partagees qui doivent etre appelees depuis d'autres langages, "
                "grace a son ABI stable et universelle."
            ),
            "ecosystem": (
                "L'ecosysteme du C est vaste mais moins centralise que celui des langages "
                "modernes. Il n'existe pas de gestionnaire de paquets officiel equivalent "
                "a pip ou npm, bien que des outils comme Conan et vcpkg comblent ce manque. "
                "Les systemes de build principaux sont Make (historique et toujours tres utilise), "
                "CMake (devenu le standard de facto pour les projets multi-plateformes), Meson, "
                "et Ninja. Les compilateurs majeurs sont GCC (GNU Compiler Collection), Clang "
                "(base sur LLVM, connu pour ses messages d'erreur clairs), et MSVC (Microsoft "
                "Visual C++). Pour l'analyse statique, des outils comme Clang Static Analyzer, "
                "Coverity, PVS-Studio, et cppcheck sont essentiels pour detecter les bugs "
                "avant l'execution. Valgrind est l'outil de reference pour detecter les "
                "fuites de memoire et les acces invalides a l'execution. AddressSanitizer "
                "(ASan) et MemorySanitizer (MSan) de LLVM offrent des capacites similaires "
                "avec un surcout moindre. Les bibliotheques fondamentales incluent la libc "
                "(bibliotheque standard), glib (types et utilitaires etendus), OpenSSL/LibreSSL "
                "(cryptographie), libcurl (HTTP), zlib (compression), libpng/libjpeg (images), "
                "et SDL/GLFW (multimedia et graphiques). Pour le developpement embarque, les "
                "toolchains specifiques (ARM GCC, AVR-GCC) et les IDE comme Keil, IAR, et "
                "STM32CubeIDE sont incontournables. Les IDE generalistes comme CLion (JetBrains), "
                "Visual Studio Code avec l'extension C/C++, et Visual Studio offrent un excellent "
                "support du C avec completion de code, debogage, et refactoring. GDB et LLDB "
                "sont les debogueurs principaux en ligne de commande. La documentation est "
                "riche avec les pages man, les specifications du langage (standards ISO), et "
                "des ressources classiques comme 'The C Programming Language' de Kernighan "
                "et Ritchie."
            ),
            "companies": [
                "Apple (noyau XNU de macOS/iOS)",
                "Microsoft (noyau Windows, parties de SQL Server)",
                "Google (parties de Chrome, Android bas niveau)",
                "Intel (compilateurs, firmware, pilotes)",
                "Red Hat (noyau Linux, systemd, outils systeme)",
                "Cisco (firmware reseau, IOS)",
                "Oracle (MySQL, parties de la JVM HotSpot)"
            ],
            "code_example": (
                "#include <stdio.h>\n"
                "#include <stdlib.h>\n"
                "#include <string.h>\n\n"
                "typedef struct {\n"
                "    char    *nom;\n"
                "    int     age;\n"
                "    double  moyenne;\n"
                "} Etudiant;\n\n"
                "Etudiant *creer_etudiant(const char *nom, int age, double moyenne) {\n"
                "    Etudiant *e = malloc(sizeof(Etudiant));\n"
                "    if (!e)\n"
                "        return NULL;\n"
                "    e->nom = strdup(nom);\n"
                "    e->age = age;\n"
                "    e->moyenne = moyenne;\n"
                "    return e;\n"
                "}\n\n"
                "void afficher_etudiant(const Etudiant *e) {\n"
                '    printf("Nom: %s, Age: %d, Moyenne: %.2f\\n",\n'
                "           e->nom, e->age, e->moyenne);\n"
                "}\n\n"
                "void liberer_etudiant(Etudiant *e) {\n"
                "    if (e) {\n"
                "        free(e->nom);\n"
                "        free(e);\n"
                "    }\n"
                "}\n\n"
                "int main(void) {\n"
                '    Etudiant *e = creer_etudiant("Alice", 21, 15.75);\n'
                "    if (e) {\n"
                "        afficher_etudiant(e);\n"
                "        liberer_etudiant(e);\n"
                "    }\n"
                "    return 0;\n"
                "}"
            ),
            "performance": {
                "startup_time": "Tres rapide (pas de runtime)",
                "throughput": "Tres eleve",
                "memory": "Tres faible (controle manuel)",
                "concurrency_model": "Threads POSIX (pthreads), C11 threads"
            },
            "learning_curve": "Elevee",
            "community_size": "Grande (historique et stable)",
            "job_market": "Fort (systeme, embarque, securite)"
        },
        "traits": {
            "performance": 9,
            "developer_speed": 3,
            "learning_curve": 7,
            "ecosystem_size": 6,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 2,
            "scalability": 5
        }
    },

    # =========================================================================
    # 2. C++
    # =========================================================================
    "cpp": {
        "name": "C++",
        "category": "language",
        "year_created": 1985,
        "creator": "Bjarne Stroustrup",
        "paradigm": ["Oriente Objet", "Procedural", "Generique", "Fonctionnel"],
        "typing": "Statique fort",
        "sections": {
            "overview": (
                "Le C++ est un langage de programmation multi-paradigme qui etend le C avec "
                "des fonctionnalites de programmation orientee objet, de programmation generique "
                "et, depuis les normes recentes, de programmation fonctionnelle. Cree par Bjarne "
                "Stroustrup a partir de 1979 sous le nom de 'C with Classes', il a ete concu "
                "pour combiner la puissance et l'efficacite du C avec des abstractions de haut "
                "niveau sans sacrifier les performances. La philosophie du C++ repose sur le "
                "principe 'zero-overhead abstraction' : les abstractions ne doivent pas couter "
                "plus cher a l'execution que le code equivalent ecrit a la main en C. Ce "
                "principe fait du C++ un langage unique qui permet de travailler a un tres "
                "bas niveau (manipulation de bits, pointeurs) tout en utilisant des concepts "
                "de tres haut niveau (templates metaprogramming, RAII, smart pointers). Le "
                "C++ est aujourd'hui l'un des langages les plus utilises au monde, dominant "
                "dans des domaines ou les performances sont critiques : jeux video (Unreal "
                "Engine, moteurs de rendu), systemes d'exploitation, navigateurs web (Chrome, "
                "Firefox), bases de donnees (MongoDB, MySQL), systemes financiers haute "
                "frequence, et intelligence artificielle (TensorFlow, PyTorch les couches "
                "bas niveau). Le langage est notoirement complexe, avec une courbe "
                "d'apprentissage tres raide, mais cette complexite est le prix a payer pour "
                "sa flexibilite et ses performances. Le C++ moderne (C++11 et versions "
                "ulterieures) a considerablement ameliore l'ergonomie du langage avec des "
                "fonctionnalites comme les lambdas, auto, les move semantics, et les smart "
                "pointers, rendant le code plus sur et plus expressif."
            ),
            "history": (
                "L'histoire du C++ commence en 1979 lorsque Bjarne Stroustrup, alors "
                "chercheur aux Bell Labs, a commence a travailler sur une extension du C "
                "qu'il a appelee 'C with Classes'. Inspire par le langage Simula, qui offrait "
                "des concepts de programmation orientee objet, Stroustrup voulait combiner "
                "l'efficacite du C avec les capacites d'abstraction de Simula. En 1983, le "
                "langage a ete renomme C++ (l'operateur d'incrementation du C symbolisant "
                "l'evolution par rapport au C). La premiere edition de 'The C++ Programming "
                "Language' a ete publiee en 1985. Les annees 1990 ont vu l'ajout de "
                "fonctionnalites majeures : les templates, les exceptions, les espaces de noms, "
                "et la STL (Standard Template Library), creee par Alexander Stepanov. La "
                "premiere norme ISO, C++98, a ete publiee en 1998, suivie d'une correction "
                "mineure C++03. Pendant presque une decennie, le langage a stagne en termes "
                "de standardisation, mais les travaux sur 'C++0x' ont finalement abouti a "
                "C++11, une mise a jour majeure qui a transforme le langage. C++11 a introduit "
                "les move semantics, les lambdas, auto, nullptr, les threads standardises, "
                "les smart pointers (unique_ptr, shared_ptr), les range-based for loops, et "
                "bien d'autres fonctionnalites. Depuis, le comite de standardisation a adopte "
                "un cycle de publication triennal : C++14 (ameliorations de C++11), C++17 "
                "(optional, variant, filesystem, structured bindings), C++20 (concepts, "
                "coroutines, ranges, modules, format), et C++23 (ameliorations des ranges, "
                "expected, mdspan). C++26 est en cours de developpement avec des fonctionnalites "
                "comme la reflexion statique. L'evolution du C++ montre une tendance claire "
                "vers plus de securite et d'expressivite tout en maintenant la compatibilite "
                "avec le code existant."
            ),
            "architecture": (
                "Le C++ est un langage compile qui produit du code machine natif, tout comme "
                "le C. Le processus de compilation est similaire : preprocesseur, compilation, "
                "assemblage, et edition de liens. Cependant, le C++ ajoute une complexite "
                "significative a chaque etape. Les templates sont instancies a la compilation, "
                "ce qui peut entrainar des temps de compilation tres longs et des executables "
                "volumineux (template bloat), mais permet des optimisations a la compilation "
                "impossibles dans d'autres langages. Le modele objet du C++ inclut l'heritage "
                "simple et multiple, les fonctions virtuelles (implementees via des vtables), "
                "les classes abstraites, et le polymorphisme. Le RAII (Resource Acquisition "
                "Is Initialization) est un idiome fondamental du C++ : les ressources sont "
                "acquises dans les constructeurs et liberees dans les destructeurs, garantissant "
                "une gestion deterministe des ressources. Les smart pointers (unique_ptr, "
                "shared_ptr, weak_ptr) automatisent la gestion de la memoire sur le tas tout "
                "en evitant les fuites. Les move semantics, introduites en C++11, permettent "
                "de transferer la propriete des ressources sans copie, ameliorant "
                "significativement les performances. La STL (Standard Template Library) fournit "
                "des conteneurs generiques (vector, map, unordered_map), des algorithmes "
                "(sort, find, transform), et des iterateurs qui operent a un niveau "
                "d'abstraction eleve sans surcout a l'execution grace aux templates. Le "
                "modele de memoire du C++ (defini depuis C++11) specifie le comportement "
                "des operations atomiques et de la concurrence, permettant d'ecrire du code "
                "multithread portable et correct. Les coroutines (C++20) ajoutent le support "
                "de la programmation asynchrone au niveau du langage. Les modules (C++20) "
                "remplacent progressivement le systeme d'inclusion par preprocesseur, "
                "ameliorant les temps de compilation et l'encapsulation."
            ),
            "pros_cons": {
                "pros": [
                    "Performances proches du code machine avec des abstractions haut niveau",
                    "Multi-paradigme : oriente objet, generique, fonctionnel, procedural",
                    "RAII et smart pointers pour une gestion deterministe des ressources",
                    "STL riche avec conteneurs et algorithmes optimises",
                    "Compatibilite quasi totale avec le C existant",
                    "Templates permettant la metaprogrammation a la compilation",
                    "Ecosysteme immense et mature dans tous les domaines",
                    "Controle fin de la memoire et des performances"
                ],
                "cons": [
                    "Complexite extreme du langage, courbe d'apprentissage tres raide",
                    "Temps de compilation pouvant etre tres longs (surtout avec les templates)",
                    "Messages d'erreur des templates souvent incomprehensibles",
                    "Comportements indefinis herites du C toujours presents",
                    "Heritage multiple source de problemes (diamond problem)",
                    "Pas de gestionnaire de paquets standard officiel",
                    "ABI instable entre les differentes versions et compilateurs",
                    "Systeme de build complexe et fragmente (CMake, Make, Bazel, etc.)"
                ]
            },
            "use_cases": (
                "Le C++ est le langage dominant dans le developpement de jeux video. Les "
                "moteurs de jeux majeurs comme Unreal Engine, CryEngine, et id Tech sont "
                "ecrits en C++, car les jeux necessitent des performances maximales pour "
                "le rendu graphique, la physique, et l'intelligence artificielle en temps "
                "reel. Les navigateurs web modernes (Chrome/Chromium, Firefox, Safari WebKit) "
                "sont principalement ecrits en C++ pour gerer efficacement le rendu HTML/CSS, "
                "l'execution JavaScript, et le reseau. Dans la finance quantitative, le C++ "
                "est utilise pour les systemes de trading haute frequence ou chaque "
                "microseconde compte. Les bases de donnees performantes comme MongoDB, "
                "RocksDB, et ClickHouse sont ecrites en C++. Dans le domaine de "
                "l'intelligence artificielle, les frameworks majeurs utilisent le C++ pour "
                "leurs noyaux de calcul : TensorFlow, PyTorch (libtorch), ONNX Runtime. "
                "Les compilateurs et outils de developpement sont souvent ecrits en C++ : "
                "LLVM/Clang, GCC (en partie), le moteur V8 de JavaScript. Les systemes "
                "embarques haut de gamme (automobile, avionique) utilisent le C++ pour "
                "combiner performances et abstractions. Le traitement d'images et la vision "
                "par ordinateur (OpenCV) reposent largement sur le C++. Les applications "
                "de bureau performantes comme Adobe Photoshop, Microsoft Office, et les "
                "suites de creation 3D (Blender, Maya, 3ds Max) sont ecrites en C++. "
                "La simulation scientifique, le calcul haute performance (HPC), et les "
                "moteurs physiques utilisent egalement le C++ pour maximiser l'utilisation "
                "du materiel."
            ),
            "ecosystem": (
                "L'ecosysteme du C++ est riche mais historiquement fragmente en ce qui "
                "concerne la gestion des dependances. Les gestionnaires de paquets les plus "
                "utilises sont Conan (le plus populaire, multi-plateforme), vcpkg (de "
                "Microsoft, bien integre a Visual Studio), et Hunter. Pour les systemes de "
                "build, CMake est devenu le standard de facto, supporte par la grande majorite "
                "des projets et des IDE. D'autres options incluent Meson (plus simple et "
                "rapide), Bazel (de Google, pour les tres grands projets), et les fichiers "
                "Make classiques. Les compilateurs principaux sont GCC, Clang/LLVM, et MSVC, "
                "chacun avec ses forces et ses optimisations specifiques. La bibliotheque "
                "standard du C++ (STL) est extremement riche : conteneurs (vector, map, set, "
                "unordered_map), algorithmes (sort, find, transform, accumulate), utilitaires "
                "(optional, variant, tuple, any), et facilites de concurrence (thread, mutex, "
                "future, atomic). Les bibliotheques tierces majeures incluent Boost (collection "
                "immense de bibliotheques complementaires a la STL), Qt (framework GUI multi-"
                "plateforme), Eigen (algebre lineaire), OpenCV (vision par ordinateur), POCO "
                "(reseau et utilitaires), gRPC (RPC haute performance), et Abseil (de Google). "
                "Pour les tests, Google Test, Catch2, et Boost.Test sont les frameworks les "
                "plus utilises. Les outils d'analyse incluent Clang-Tidy (linting), "
                "AddressSanitizer, ThreadSanitizer, Valgrind, et les profilers comme perf et "
                "Intel VTune. Les IDE majeurs incluent CLion (JetBrains), Visual Studio "
                "(Microsoft), Visual Studio Code avec des extensions, et Qt Creator. La "
                "documentation est riche avec cppreference.com comme reference incontournable."
            ),
            "companies": [
                "Epic Games (Unreal Engine)",
                "Google (Chrome, TensorFlow, infrastructure)",
                "Microsoft (Windows, Office, Visual Studio, Azure)",
                "Meta (infrastructure backend, HHVM historiquement)",
                "Bloomberg (systemes financiers temps reel)",
                "Amazon (infrastructure AWS, moteurs de bases de donnees)",
                "Adobe (Photoshop, Premiere Pro, suite Creative Cloud)"
            ],
            "code_example": (
                "#include <iostream>\n"
                "#include <vector>\n"
                "#include <algorithm>\n"
                "#include <memory>\n"
                "#include <string>\n\n"
                "class Animal {\n"
                "public:\n"
                "    Animal(std::string nom, int age)\n"
                "        : nom_(std::move(nom)), age_(age) {}\n"
                "    virtual ~Animal() = default;\n\n"
                "    virtual std::string cri() const = 0;\n\n"
                "    void afficher() const {\n"
                '        std::cout << nom_ << " (" << age_ << " ans) fait: "\n'
                "                  << cri() << std::endl;\n"
                "    }\n\n"
                "    const std::string& nom() const { return nom_; }\n"
                "    int age() const { return age_; }\n\n"
                "private:\n"
                "    std::string nom_;\n"
                "    int age_;\n"
                "};\n\n"
                "class Chat : public Animal {\n"
                "public:\n"
                "    using Animal::Animal;\n"
                '    std::string cri() const override { return "Miaou!"; }\n'
                "};\n\n"
                "class Chien : public Animal {\n"
                "public:\n"
                "    using Animal::Animal;\n"
                '    std::string cri() const override { return "Ouaf!"; }\n'
                "};\n\n"
                "int main() {\n"
                "    std::vector<std::unique_ptr<Animal>> animaux;\n"
                '    animaux.push_back(std::make_unique<Chat>("Felix", 3));\n'
                '    animaux.push_back(std::make_unique<Chien>("Rex", 5));\n'
                '    animaux.push_back(std::make_unique<Chat>("Moustache", 2));\n\n'
                "    // Tri par age avec lambda\n"
                "    std::ranges::sort(animaux, [](const auto& a, const auto& b) {\n"
                "        return a->age() < b->age();\n"
                "    });\n\n"
                "    for (const auto& animal : animaux)\n"
                "        animal->afficher();\n\n"
                "    return 0;\n"
                "}"
            ),
            "performance": {
                "startup_time": "Tres rapide (pas de runtime significatif)",
                "throughput": "Tres eleve",
                "memory": "Faible a moyen (controle fin possible)",
                "concurrency_model": "std::thread, std::async, coroutines (C++20), execution policies"
            },
            "learning_curve": "Tres elevee",
            "community_size": "Tres grande",
            "job_market": "Fort (jeux video, finance, systemes)"
        },
        "traits": {
            "performance": 9,
            "developer_speed": 3,
            "learning_curve": 8,
            "ecosystem_size": 7,
            "type_safety": 6,
            "concurrency": 7,
            "memory_safety": 3,
            "scalability": 7
        }
    },

    # =========================================================================
    # 3. Python
    # =========================================================================
    "python": {
        "name": "Python",
        "category": "language",
        "year_created": 1991,
        "creator": "Guido van Rossum",
        "paradigm": ["Oriente Objet", "Fonctionnel", "Procedural"],
        "typing": "Dynamique (typage statique optionnel via type hints)",
        "sections": {
            "overview": (
                "Python est un langage de programmation interprete de haut niveau, reconnu "
                "pour sa syntaxe claire et lisible, sa philosophie 'batteries included', et "
                "sa polyvalence. Cree par Guido van Rossum et publie pour la premiere fois "
                "en 1991, Python a ete concu avec une priorite absolue : la lisibilite du "
                "code. Le 'Zen of Python' (PEP 20) encapsule cette philosophie avec des "
                "principes comme 'Readability counts', 'Simple is better than complex', et "
                "'There should be one obvious way to do it'. Python utilise l'indentation "
                "significative (plutot que des accolades) pour delimiter les blocs de code, "
                "ce qui force les developpeurs a ecrire du code visuellement structure. "
                "Python est un langage multi-paradigme : il supporte la programmation orientee "
                "objet (tout est un objet en Python), la programmation fonctionnelle (fonctions "
                "de premiere classe, comprehensions, generateurs, iterateurs), et la "
                "programmation procedurale. Son systeme de typage dynamique permet un "
                "prototypage rapide et une grande flexibilite, tandis que les type hints "
                "(introduits dans Python 3.5) permettent d'ajouter des annotations de type "
                "optionnelles verifiables par des outils comme mypy. Python est devenu le "
                "langage dominant dans plusieurs domaines : science des donnees, intelligence "
                "artificielle et machine learning, scripting et automatisation, developpement "
                "web (backend), et enseignement de la programmation. Son ecosysteme de "
                "bibliotheques est l'un des plus riches au monde, avec plus de 500 000 "
                "paquets sur PyPI. Malgre ses performances limitees par rapport aux langages "
                "compiles, Python compense par une productivite de developpement exceptionnelle "
                "et une communaute massive et active."
            ),
            "history": (
                "L'histoire de Python commence a la fin des annees 1980, lorsque Guido van "
                "Rossum, travaillant au Centrum Wiskunde & Informatica (CWI) aux Pays-Bas, "
                "a commence a concevoir un successeur au langage ABC. Van Rossum a commence "
                "l'implementation de Python pendant les vacances de Noel 1989 comme un projet "
                "personnel. Le nom 'Python' vient du groupe humoristique britannique Monty "
                "Python, dont van Rossum etait fan. La version 0.9.0 a ete publiee en 1991, "
                "incluant deja des classes avec heritage, des exceptions, des fonctions, et "
                "les types de base (listes, dictionnaires, chaines). Python 1.0 est sorti en "
                "1994, ajoutant des outils de programmation fonctionnelle (lambda, map, filter, "
                "reduce). Python 2.0 (2000) a introduit les list comprehensions, le garbage "
                "collector par comptage de references avec detection de cycles, et le support "
                "Unicode. La communaute Python a grandi regulierement, et van Rossum a ete "
                "surnomme 'Benevolent Dictator For Life' (BDFL). Python 3.0, sorti en 2008, "
                "a ete une refonte majeure non retrocompatible avec Python 2. Parmi les "
                "changements : print devenant une fonction, les chaines etant Unicode par "
                "defaut, la division entiere avec //, et la suppression de types obsoletes. "
                "La coexistence de Python 2 et 3 a dure plus d'une decennie, Python 2 ayant "
                "atteint sa fin de vie en janvier 2020. Les versions recentes de Python 3 ont "
                "apporte des ameliorations significatives : les f-strings (3.6), les data "
                "classes (3.7), l'operateur walrus := (3.8), les dictionnaires d'union | "
                "(3.9), le match/case (3.10), les groupes d'exceptions (3.11), et des "
                "ameliorations de performances majeures (3.11 est 25% plus rapide). Le projet "
                "'Faster CPython', soutenu par Microsoft ou van Rossum travaille, vise a "
                "multiplier les performances par 5 sur plusieurs versions."
            ),
            "architecture": (
                "Python est un langage interprete qui utilise une machine virtuelle. Le code "
                "source (.py) est d'abord compile en bytecode (.pyc), un format intermediaire "
                "stocke dans le dossier __pycache__. Ce bytecode est ensuite execute par la "
                "Python Virtual Machine (PVM). L'implementation de reference, CPython, est "
                "ecrite en C et est de loin la plus utilisee. D'autres implementations existent : "
                "PyPy (avec compilation JIT, beaucoup plus rapide pour certains workloads), "
                "Jython (sur la JVM), IronPython (sur .NET), et GraalPython (sur GraalVM). "
                "CPython utilise un compteur de references comme mecanisme principal de "
                "gestion de la memoire, complete par un ramasse-miettes generationnel pour "
                "detecter les cycles de references. Le GIL (Global Interpreter Lock) est une "
                "caracteristique controversee de CPython : c'est un verrou global qui empeche "
                "l'execution simultanee de plusieurs threads Python. Cela signifie que le "
                "multithreading en Python n'offre pas de parallelisme reel pour le code "
                "CPU-bound, bien qu'il soit utile pour le code I/O-bound. Pour le parallelisme "
                "reel, Python offre le module multiprocessing (processus separes) et le module "
                "concurrent.futures. L'async/await (asyncio) fournit de la concurrence "
                "cooperative pour les operations d'entree/sortie. Le modele objet de Python "
                "est extremement dynamique : les attributs peuvent etre ajoutes ou supprimes "
                "a l'execution, les classes peuvent etre modifiees dynamiquement (monkey patching), "
                "et les metaclasses permettent de controler la creation des classes elles-memes. "
                "Le protocole de descripteurs, les decorateurs, et les gestionnaires de contexte "
                "sont des mecanismes puissants d'abstraction. Python 3.12 introduit "
                "experimentalement le support de sous-interpreteurs avec des GIL separes, et "
                "Python 3.13 prevoit un mode free-threaded experimental sans GIL."
            ),
            "pros_cons": {
                "pros": [
                    "Syntaxe claire et lisible, ideal pour l'apprentissage et le prototypage",
                    "Ecosysteme de bibliotheques immense (PyPI, plus de 500 000 paquets)",
                    "Dominant en data science, IA, et machine learning",
                    "Productivite de developpement tres elevee",
                    "Communaute massive et tres active",
                    "Multi-paradigme : OOP, fonctionnel, procedural",
                    "Excellent pour le scripting et l'automatisation",
                    "Type hints optionnels pour une meilleure maintenabilite"
                ],
                "cons": [
                    "Performances significativement inferieures aux langages compiles",
                    "GIL limitant le parallelisme multithread natif",
                    "Consommation memoire elevee par rapport au C/Rust/Go",
                    "Typage dynamique pouvant masquer des erreurs jusqu'a l'execution",
                    "Packaging et gestion des environnements historiquement complexes",
                    "Pas ideal pour les applications mobiles ou le developpement frontend",
                    "Les lambdas sont limitees a une seule expression",
                    "La migration Python 2 vers 3 a fragmente l'ecosysteme pendant des annees"
                ]
            },
            "use_cases": (
                "Python est le langage de reference pour la science des donnees et le machine "
                "learning. Les bibliotheques NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch, "
                "et Keras forment un ecosysteme inegale pour l'analyse de donnees, la "
                "visualisation (Matplotlib, Seaborn, Plotly), et l'entrainement de modeles "
                "d'IA. Les notebooks Jupyter permettent un workflow interactif ideal pour "
                "l'exploration de donnees. Dans le developpement web backend, Django (framework "
                "complet 'batteries included') et Flask/FastAPI (micro-frameworks) sont tres "
                "populaires. FastAPI, en particulier, combine performances (basees sur Starlette "
                "et Pydantic) et productivite pour les APIs modernes. Python excelle dans "
                "l'automatisation et le scripting : administration systeme, DevOps (Ansible "
                "est ecrit en Python), scripts de build, ETL (extraction-transformation-"
                "chargement), et web scraping (Beautiful Soup, Scrapy). L'analyse financiere "
                "et le trading algorithmique utilisent largement Python pour le backtesting "
                "et l'analyse quantitative. Le traitement du langage naturel (NLP) est domine "
                "par Python avec des outils comme spaCy, NLTK, et Hugging Face Transformers. "
                "Python est aussi largement utilise dans la bio-informatique, l'astronomie, "
                "et les sciences en general grace a SciPy et aux bibliotheques specialisees. "
                "L'education utilise massivement Python comme premier langage d'apprentissage "
                "grace a sa lisibilite. Enfin, Python sert de 'colle' entre des composants "
                "ecrits dans d'autres langages, tirant parti de sa facilite d'integration "
                "avec le C (ctypes, cffi, Cython) et le C++ (pybind11)."
            ),
            "ecosystem": (
                "L'ecosysteme Python est l'un des plus vastes de tous les langages de "
                "programmation. PyPI (Python Package Index) heberge plus de 500 000 paquets. "
                "Le gestionnaire de paquets standard est pip, souvent utilise avec venv ou "
                "virtualenv pour l'isolation des environnements. Des outils modernes comme "
                "Poetry, PDM, et uv (de chez Astral, extremement rapide) simplifient la "
                "gestion des dependances et des projets. Conda est populaire dans l'ecosysteme "
                "scientifique pour gerer a la fois les paquets Python et les dependances "
                "systeme. Pour le developpement web, Django est le framework complet le plus "
                "populaire, offrant un ORM, un systeme d'authentification, et un panneau "
                "d'administration. Flask est le micro-framework classique, tandis que FastAPI "
                "est en pleine croissance pour les APIs asynchrones. Pour la science des "
                "donnees, NumPy (calcul numerique), Pandas (manipulation de donnees), "
                "Matplotlib/Seaborn (visualisation), et Jupyter (notebooks interactifs) "
                "sont incontournables. Pour le machine learning, Scikit-learn, TensorFlow, "
                "PyTorch, et JAX dominent. Les outils de test incluent pytest (le plus "
                "populaire), unittest (standard), et tox (tests multi-environnements). Pour "
                "le linting et le formatage, flake8, pylint, black, isort, et ruff (tres "
                "rapide, ecrit en Rust) sont les references. mypy, pyright, et pytype "
                "permettent la verification de types statique. Les IDE majeurs sont PyCharm "
                "(JetBrains), Visual Studio Code avec l'extension Python, et Jupyter Lab. "
                "Pour le packaging, setuptools, flit, hatch, et maturin (pour les extensions "
                "Rust) sont utilises. Docker est tres utilise pour le deploiement d'applications "
                "Python en production."
            ),
            "companies": [
                "Instagram (backend Django massif)",
                "Spotify (pipelines data et machine learning)",
                "Netflix (analyse de donnees, outils internes)",
                "Google (parties d'infrastructure, IA, YouTube)",
                "Dropbox (client desktop historiquement en Python)",
                "Reddit (backend historiquement en Python)",
                "Stripe (outils internes, analyse de donnees)"
            ],
            "code_example": (
                "from dataclasses import dataclass, field\n"
                "from typing import Optional\n"
                "from statistics import mean\n\n\n"
                "@dataclass\n"
                "class Etudiant:\n"
                "    nom: str\n"
                "    age: int\n"
                "    notes: list[float] = field(default_factory=list)\n\n"
                "    @property\n"
                "    def moyenne(self) -> Optional[float]:\n"
                "        return mean(self.notes) if self.notes else None\n\n"
                "    def est_admis(self, seuil: float = 10.0) -> bool:\n"
                "        return self.moyenne is not None and self.moyenne >= seuil\n\n"
                "    def __str__(self) -> str:\n"
                '        moy = f"{self.moyenne:.2f}" if self.moyenne else "N/A"\n'
                '        return f"{self.nom} (age {self.age}) - Moyenne: {moy}"\n\n\n'
                "def afficher_palmares(etudiants: list[Etudiant]) -> None:\n"
                "    admis = [e for e in etudiants if e.est_admis()]\n"
                "    admis.sort(key=lambda e: e.moyenne or 0, reverse=True)\n\n"
                '    print("=== Palmares des admis ===")\n'
                "    for rang, etudiant in enumerate(admis, start=1):\n"
                '        print(f"  {rang}. {etudiant}")\n\n\n'
                "if __name__ == \"__main__\":\n"
                "    etudiants = [\n"
                '        Etudiant("Alice", 21, [15.5, 14.0, 16.5]),\n'
                '        Etudiant("Bob", 22, [8.0, 9.5, 7.0]),\n'
                '        Etudiant("Claire", 20, [18.0, 17.5, 19.0]),\n'
                '        Etudiant("David", 23, [10.0, 11.0, 9.5]),\n'
                "    ]\n"
                "    afficher_palmares(etudiants)\n"
            ),
            "performance": {
                "startup_time": "Moyen",
                "throughput": "Faible-Moyen",
                "memory": "Moyen-Eleve",
                "concurrency_model": "Async/await (asyncio), multiprocessing, threading (limite par le GIL)"
            },
            "learning_curve": "Faible",
            "community_size": "Tres grande",
            "job_market": "Tres fort (data science, backend, DevOps, IA)"
        },
        "traits": {
            "performance": 3,
            "developer_speed": 9,
            "learning_curve": 2,
            "ecosystem_size": 9,
            "type_safety": 4,
            "concurrency": 4,
            "memory_safety": 5,
            "scalability": 6
        }
    },

    # =========================================================================
    # 4. JavaScript
    # =========================================================================
    "javascript": {
        "name": "JavaScript",
        "category": "language",
        "year_created": 1995,
        "creator": "Brendan Eich",
        "paradigm": ["Oriente Objet (prototypal)", "Fonctionnel", "Evenementiel"],
        "typing": "Dynamique faible",
        "sections": {
            "overview": (
                "JavaScript est le langage de programmation du web, et il est aujourd'hui l'un "
                "des langages les plus utilises au monde. Cree en 1995 par Brendan Eich chez "
                "Netscape en seulement 10 jours, JavaScript a evolue d'un simple langage de "
                "script pour navigateurs web en un langage polyvalent utilise tant cote client "
                "que cote serveur. JavaScript est le seul langage de programmation nativement "
                "supporte par tous les navigateurs web, ce qui en fait un pilier incontournable "
                "du developpement web. Sa nature evenementielle et son modele de concurrence "
                "base sur une boucle d'evenements (event loop) le rendent particulierement "
                "adapte aux applications interactives et aux operations d'entree/sortie "
                "asynchrones. JavaScript est un langage multi-paradigme qui supporte la "
                "programmation orientee objet (basee sur les prototypes plutot que les classes, "
                "bien que la syntaxe class ait ete ajoutee en ES6), la programmation fonctionnelle "
                "(fonctions de premiere classe, closures, fonctions d'ordre superieur), et la "
                "programmation evenementielle. Son typage dynamique et faible (avec des "
                "conversions de type implicites parfois surprenantes) est a la fois une source "
                "de flexibilite et de bugs. L'ecosysteme JavaScript est le plus vaste de tous "
                "les langages, avec plus de 2 millions de paquets sur npm. Avec l'avenement "
                "de Node.js (2009), JavaScript s'est impose cote serveur, permettant le "
                "developpement 'fullstack' dans un seul langage. Les frameworks frontend comme "
                "React, Vue.js, et Angular dominent le developpement d'interfaces utilisateur "
                "web modernes. JavaScript continue d'evoluer rapidement avec des mises a jour "
                "annuelles de la specification ECMAScript."
            ),
            "history": (
                "L'histoire de JavaScript est fascinante et mouvementee. En 1995, Netscape "
                "Communications voulait un langage de script pour son navigateur Navigator. "
                "Brendan Eich a ete recrute pour creer ce langage et l'a developpe en "
                "seulement 10 jours en mai 1995. Initialement appele Mocha, puis LiveScript, "
                "il a ete renomme JavaScript pour des raisons marketing (la popularite de Java "
                "a l'epoque), bien qu'il n'ait aucun lien technique avec Java. Microsoft a "
                "rapidement cree JScript, sa propre implementation pour Internet Explorer. "
                "Pour eviter la fragmentation, Netscape a soumis le langage a Ecma International "
                "en 1996, donnant naissance a la specification ECMAScript. ECMAScript 3 (1999) "
                "a ete la premiere version largement adoptee. Les travaux sur ECMAScript 4 "
                "ont ete abandonnes a cause de desaccords au sein du comite, menant a une "
                "longue periode de stagnation. ECMAScript 5 (2009) a apporte des ameliorations "
                "importantes : le mode strict, JSON.parse/stringify, et les methodes d'Array "
                "(forEach, map, filter). La revolution est venue avec ECMAScript 2015 (ES6), "
                "une mise a jour massive qui a modernise le langage : let/const, classes, "
                "arrow functions, Promises, template literals, destructuring, modules, "
                "iterateurs, et generateurs. Depuis, le comite TC39 publie une nouvelle "
                "version chaque annee : async/await (ES2017), rest/spread operators, optional "
                "chaining ?. (ES2020), et bien d'autres. En parallele, Node.js (cree par Ryan "
                "Dahl en 2009, utilisant le moteur V8 de Chrome) a revoluTionne l'utilisation "
                "de JavaScript en le rendant viable cote serveur. Plus recemment, Deno (2018, "
                "egalement par Ryan Dahl) et Bun (2022) sont apparus comme des runtimes "
                "alternatifs modernes. L'ecosysteme des outils JavaScript a explose avec "
                "Webpack, Babel, ESLint, Prettier, et plus recemment Vite, esbuild, et "
                "les outils bases sur Rust (swc, Turbopack)."
            ),
            "architecture": (
                "JavaScript est un langage interprete, bien que les moteurs modernes utilisent "
                "la compilation Just-In-Time (JIT) pour des performances proches du code natif. "
                "Le moteur V8 de Google (utilise dans Chrome et Node.js) est le plus performant : "
                "il compile le JavaScript directement en code machine via deux compilateurs, "
                "Ignition (interpreteur bytecode) et TurboFan (compilateur optimisant). "
                "SpiderMonkey (Firefox) et JavaScriptCore (Safari) utilisent des approches "
                "similaires. Le modele d'execution de JavaScript repose sur une boucle "
                "d'evenements (event loop) mono-thread. Le code s'execute dans un seul thread, "
                "mais les operations asynchrones (I/O, timers, requetes reseau) sont delegees "
                "au systeme d'exploitation ou a des threads de travail internes, et leurs "
                "callbacks sont places dans une file d'attente (task queue ou microtask queue) "
                "pour etre executes lorsque le thread principal est libre. Ce modele est tres "
                "efficace pour les applications I/O-bound mais peut etre problematique pour "
                "les calculs CPU-intensifs, qui bloquent le thread principal. Les Web Workers "
                "(navigateur) et les Worker Threads (Node.js) permettent de deleguer des "
                "calculs a des threads separes. La gestion de la memoire est automatique via "
                "un ramasse-miettes (garbage collector). V8 utilise un GC generationnel avec "
                "une young generation (minor GC rapide) et une old generation (major GC plus "
                "lent). Le modele objet de JavaScript est base sur les prototypes : chaque "
                "objet a un prototype dont il herite les proprietes et les methodes. La "
                "syntaxe class (ES6) est du sucre syntaxique sur le systeme de prototypes. "
                "Les closures sont une fonctionnalite fondamentale : une fonction capture les "
                "variables de son scope englobant, permettant des patterns comme les modules, "
                "les factories, et la programmation fonctionnelle. Le systeme de modules a "
                "evolue des patterns IIFE vers CommonJS (Node.js) puis vers les ES Modules "
                "(import/export), qui sont maintenant le standard."
            ),
            "pros_cons": {
                "pros": [
                    "Langage universel du web, fonctionne dans tous les navigateurs",
                    "Ecosysteme npm le plus vaste au monde (plus de 2 millions de paquets)",
                    "Permet le developpement fullstack (frontend + backend)",
                    "Modele evenementiel tres adapte aux applications I/O-bound",
                    "Communaute massive et ressources d'apprentissage abondantes",
                    "Evolution rapide et constante du langage (mises a jour annuelles)",
                    "Fonctions de premiere classe et programmation fonctionnelle",
                    "JSON natif, ideal pour les APIs web"
                ],
                "cons": [
                    "Typage dynamique faible avec des coercitions implicites surprenantes",
                    "Mono-thread par defaut, inadapte au calcul CPU-intensif",
                    "Historique de choix de design discutables (typeof null === 'object')",
                    "Fatigue de l'ecosysteme (trop de choix d'outils et de frameworks)",
                    "Gestion des erreurs parfois difficile avec les callbacks et les Promises",
                    "Securite cote client limitee (code visible et modifiable)",
                    "Performances inferieures aux langages compiles pour le calcul pur",
                    "Incoherences du langage dues a sa creation rapide"
                ]
            },
            "use_cases": (
                "JavaScript est absolument incontournable pour le developpement web frontend. "
                "Tous les sites web interactifs modernes utilisent JavaScript, souvent via des "
                "frameworks comme React (Meta), Vue.js, Angular (Google), ou Svelte. Les "
                "Single Page Applications (SPA), les Progressive Web Apps (PWA), et les "
                "applications web temps reel (chat, collaboration) sont le domaine de "
                "predilection de JavaScript. Cote serveur, Node.js est largement utilise "
                "pour les APIs REST et GraphQL, les microservices, et les applications temps "
                "reel (WebSockets). Express.js, Fastify, NestJS, et Koa sont les frameworks "
                "backend les plus populaires. Next.js et Nuxt.js offrent du rendu cote serveur "
                "(SSR) et de la generation de sites statiques (SSG), combinant le meilleur "
                "des deux mondes. Le developpement d'applications mobiles est possible avec "
                "React Native (applications natives multiplateformes) et Ionic/Capacitor "
                "(applications hybrides). Electron permet de creer des applications de "
                "bureau multiplateformes avec des technologies web (VS Code, Discord, Slack, "
                "Figma sont construits avec Electron ou des technologies similaires). "
                "JavaScript est egalement utilise pour les outils de build et de developpement "
                "(Webpack, Vite, ESLint), les extensions de navigateurs, les jeux video "
                "simples (Canvas API, WebGL, Three.js), et meme l'IoT (Johnny-Five). Les "
                "fonctions serverless (AWS Lambda, Cloudflare Workers, Vercel Edge Functions) "
                "supportent largement JavaScript. L'emergence de runtimes comme Deno et Bun "
                "ouvre de nouvelles possibilites pour JavaScript cote serveur."
            ),
            "ecosystem": (
                "L'ecosysteme JavaScript est le plus vaste et le plus dynamique de tous les "
                "langages de programmation. npm (Node Package Manager) est le plus grand "
                "registre de paquets au monde avec plus de 2 millions de paquets. Des "
                "alternatives comme yarn (Meta) et pnpm (plus rapide et plus economique "
                "en espace disque) sont egalement populaires. Pour le frontend, les "
                "frameworks dominants sont React (le plus populaire, approche composant), "
                "Vue.js (progressif, facile a apprendre), Angular (complet, oriente entreprise), "
                "et Svelte (compile vers du JS vanilla). Les meta-frameworks comme Next.js "
                "(React), Nuxt.js (Vue), SvelteKit (Svelte), et Astro (multi-framework) "
                "offrent du SSR, SSG, et des fonctionnalites fullstack. Pour le bundling et "
                "les outils de build, Vite (rapide, base sur esbuild et Rollup) a remplace "
                "Webpack comme choix par defaut. esbuild et swc (ecrit en Rust) offrent des "
                "performances de compilation extremes. Babel reste utilise pour la transpilation. "
                "Pour le styling, les options incluent CSS Modules, Tailwind CSS, Styled "
                "Components, et Emotion. Les frameworks de test incluent Jest (le plus "
                "populaire), Vitest (compatible Vite, rapide), Mocha, et Cypress/Playwright "
                "pour les tests end-to-end. ESLint est l'outil de linting standard, et "
                "Prettier le formateur de code. TypeScript, bien que techniquement un langage "
                "separe, fait partie integrante de l'ecosysteme JavaScript et est utilise par "
                "la majorite des projets professionnels. Pour le backend, Express.js est le "
                "framework historique, Fastify est oriente performances, et NestJS offre une "
                "architecture structuree. Les bases de donnees comme Prisma et Drizzle (ORM) "
                "facilitent l'acces aux donnees. Visual Studio Code est l'IDE dominant, "
                "offrant un support exceptionnel de JavaScript/TypeScript."
            ),
            "companies": [
                "Meta (React, infrastructure web)",
                "Google (Angular, V8, parties de YouTube)",
                "Netflix (interface utilisateur, Node.js backend)",
                "Airbnb (frontend React, outils internes)",
                "Uber (interface web et mobile, Node.js microservices)",
                "PayPal (migration historique de Java vers Node.js)",
                "LinkedIn (frontend, services Node.js)"
            ],
            "code_example": (
                "// Exemple: gestionnaire de taches asynchrone\n\n"
                "class GestionnaireTaches {\n"
                "  #taches = new Map();\n"
                "  #compteur = 0;\n\n"
                "  ajouter(nom, priorite = 'normale') {\n"
                "    const id = ++this.#compteur;\n"
                "    this.#taches.set(id, {\n"
                "      id,\n"
                "      nom,\n"
                "      priorite,\n"
                "      terminee: false,\n"
                "      creeLe: new Date(),\n"
                "    });\n"
                "    return id;\n"
                "  }\n\n"
                "  terminer(id) {\n"
                "    const tache = this.#taches.get(id);\n"
                "    if (!tache) throw new Error(`Tache ${id} introuvable`);\n"
                "    tache.terminee = true;\n"
                "    return tache;\n"
                "  }\n\n"
                "  get enAttente() {\n"
                "    return [...this.#taches.values()].filter(t => !t.terminee);\n"
                "  }\n\n"
                "  async executerAvecDelai(id, delaiMs) {\n"
                "    await new Promise(resolve => setTimeout(resolve, delaiMs));\n"
                "    return this.terminer(id);\n"
                "  }\n"
                "}\n\n"
                "// Utilisation\n"
                "const gestionnaire = new GestionnaireTaches();\n"
                "const id1 = gestionnaire.ajouter('Ecrire le rapport', 'haute');\n"
                "const id2 = gestionnaire.ajouter('Relire le code');\n\n"
                "console.log('En attente:', gestionnaire.enAttente.length);\n"
                "gestionnaire.terminer(id1);\n"
                "console.log('En attente apres:', gestionnaire.enAttente.length);\n"
            ),
            "performance": {
                "startup_time": "Rapide (V8 optimise)",
                "throughput": "Moyen (JIT compile)",
                "memory": "Moyen",
                "concurrency_model": "Event loop mono-thread, Promises, async/await, Web Workers"
            },
            "learning_curve": "Faible a moyenne",
            "community_size": "La plus grande au monde",
            "job_market": "Tres fort (le langage le plus demande)"
        },
        "traits": {
            "performance": 5,
            "developer_speed": 8,
            "learning_curve": 3,
            "ecosystem_size": 10,
            "type_safety": 2,
            "concurrency": 6,
            "memory_safety": 5,
            "scalability": 7
        }
    },

    # =========================================================================
    # 5. TypeScript
    # =========================================================================
    "typescript": {
        "name": "TypeScript",
        "category": "language",
        "year_created": 2012,
        "creator": "Anders Hejlsberg (Microsoft)",
        "paradigm": ["Oriente Objet", "Fonctionnel", "Evenementiel"],
        "typing": "Statique structurel (superset de JavaScript)",
        "sections": {
            "overview": (
                "TypeScript est un superset type de JavaScript cree par Microsoft et dirige "
                "par Anders Hejlsberg (egalement createur de C# et Turbo Pascal). Lance en "
                "2012, TypeScript ajoute un systeme de types statique optionnel a JavaScript, "
                "permettant de detecter les erreurs a la compilation plutot qu'a l'execution. "
                "Tout code JavaScript valide est aussi du code TypeScript valide, ce qui permet "
                "une adoption progressive dans les projets existants. Le systeme de types de "
                "TypeScript est l'un des plus expressifs parmi les langages mainstream : types "
                "union et intersection, types generiques, types conditionnels, types mappes, "
                "types template literal, et inference de types avancee. TypeScript utilise un "
                "typage structurel (duck typing statique) plutot que nominal : deux types sont "
                "compatibles si leurs structures correspondent, independamment de leurs noms. "
                "La philosophie de TypeScript est pragmatique : le systeme de types est concu "
                "pour modeliser les patterns JavaScript existants plutot que d'imposer un "
                "paradigme strict. Le compilateur TypeScript (tsc) transpile le code TypeScript "
                "en JavaScript pur, ce qui signifie que le code TypeScript peut s'executer "
                "partout ou JavaScript fonctionne. TypeScript est devenu un standard de facto "
                "pour les projets JavaScript professionnels : la grande majorite des grandes "
                "bibliotheques et frameworks offrent des declarations de types TypeScript. "
                "L'adoption de TypeScript a explose ces dernieres annees, avec des enquetes "
                "montrant qu'il est utilise par plus de 70% des developpeurs JavaScript "
                "professionnels. Il est considere comme le meilleur compromis entre la "
                "flexibilite de JavaScript et la securite des langages types statiquement."
            ),
            "history": (
                "TypeScript a ete annonce publiquement par Microsoft en octobre 2012 (version "
                "0.8) apres environ deux ans de developpement interne. Le projet etait dirige "
                "par Anders Hejlsberg, un architecte de langages legendaire chez Microsoft, "
                "connu pour avoir cree Turbo Pascal, Delphi, et C#. La motivation principale "
                "etait de rendre le developpement JavaScript a grande echelle plus geraable, "
                "en ajoutant un systeme de types statique et de meilleurs outils de "
                "developpement (autocompletion, refactoring, navigation dans le code). Les "
                "premieres versions de TypeScript offraient des fonctionnalites basiques : "
                "annotations de types, interfaces, classes (avant ES6), et enumerations. "
                "TypeScript 1.0 est sorti en 2014. La version 2.0 (2016) a apporte des "
                "ameliorations majeures au systeme de types : types non-nullable par defaut "
                "(--strictNullChecks), types union discrimines, et le mode strict. TypeScript "
                "3.0 (2018) a introduit les types tuple avec rest elements, et les versions "
                "3.x ont affine le systeme de types avec les types conditionnels, les types "
                "mappes ameliores, et les types template literal. TypeScript 4.0 (2020) a "
                "ajoute les types tuple variadiques et les types template literal plus "
                "puissants. TypeScript 5.0 (2023) a apporte les decorateurs standards (stage "
                "3), de meilleures performances du compilateur, et de nouvelles fonctionnalites "
                "de types. L'adoption de TypeScript a connu une croissance exponentielle : "
                "Angular (Google) a ete le premier grand framework a l'adopter des 2016, "
                "suivi par Vue.js 3, puis pratiquement tout l'ecosysteme. Aujourd'hui, les "
                "nouveaux projets JavaScript utilisent TypeScript par defaut. Des runtimes "
                "comme Deno et Bun supportent TypeScript nativement sans etape de compilation "
                "explicite. Node.js a commence a integrer un support experimental du stripping "
                "de types TypeScript."
            ),
            "architecture": (
                "TypeScript est fondamentalement un transpileur : il transforme le code "
                "TypeScript en JavaScript pur. Le compilateur TypeScript (tsc), ecrit "
                "lui-meme en TypeScript, effectue la verification des types a la compilation, "
                "puis supprime toutes les annotations de types pour produire du JavaScript "
                "standard. Cette architecture signifie que les types TypeScript n'existent "
                "qu'au moment de la compilation et n'ont aucun impact sur l'execution (type "
                "erasure). Le processus de compilation comprend le parsing du code source en "
                "AST (Abstract Syntax Tree), la resolution des symboles et des types, la "
                "verification des types, et l'emission du code JavaScript. Le systeme de "
                "types de TypeScript est Turing-complet, ce qui signifie qu'il peut exprimer "
                "des logiques de types arbitrairement complexes (bien que cela puisse ralentir "
                "la compilation). Le systeme de types structurel signifie que la compatibilite "
                "des types est basee sur la forme des donnees plutot que sur les declarations "
                "explicites d'implementation. Les fichiers de declaration (.d.ts) permettent "
                "de decrire les types de bibliotheques JavaScript existantes sans les modifier. "
                "Le depot DefinitelyTyped (@types/*) heberge des declarations de types pour "
                "des milliers de bibliotheques. Le Language Server Protocol (LSP) de TypeScript "
                "alimente les fonctionnalites d'edition dans tous les IDE majeurs : "
                "autocompletion, navigation, refactoring, et verification en temps reel. "
                "TypeScript supporte la compilation incrementale et les project references "
                "pour gerer les grandes bases de code. Des alternatives au compilateur tsc "
                "ont emerge pour des performances de compilation superieures : esbuild (Go), "
                "swc (Rust), et le nouveau compilateur TypeScript ecrit en Go par l'equipe "
                "TypeScript elle-meme (annonce en 2025, promettant des performances 10x). "
                "L'architecture de type erasure a l'avantage que le code TypeScript compile "
                "est du JavaScript idiomatique et debuggable, avec des source maps pour "
                "le mapping entre les deux."
            ),
            "pros_cons": {
                "pros": [
                    "Detection des erreurs a la compilation plutot qu'a l'execution",
                    "Systeme de types extremement expressif et flexible",
                    "Compatible a 100% avec l'ecosysteme JavaScript existant",
                    "Excellents outils de developpement (autocompletion, refactoring)",
                    "Adoption progressive possible dans les projets JavaScript",
                    "Documentation implicite via les types (code auto-documente)",
                    "Refactoring sur et fiable dans les grandes bases de code",
                    "Soutenu par Microsoft avec une equipe dediee"
                ],
                "cons": [
                    "Etape de compilation supplementaire ralentissant le workflow",
                    "Complexite du systeme de types avance (types conditionnels, mappes)",
                    "Les types complexes peuvent ralentir significativement le compilateur",
                    "Pas de verification de types a l'execution (type erasure)",
                    "Faux sentiment de securite si le code interagit avec du JS non type",
                    "Configuration parfois complexe (tsconfig.json, nombreuses options)",
                    "Certains patterns JavaScript difficiles a typer correctement",
                    "Surcharge pour les petits projets ou les scripts rapides"
                ]
            },
            "use_cases": (
                "TypeScript est le choix par defaut pour les projets JavaScript de taille "
                "moyenne a grande. Dans le developpement frontend, TypeScript s'integre "
                "parfaitement avec React (typage des props, hooks, et etats), Angular (qui "
                "est entierement ecrit en TypeScript), Vue.js 3, et Svelte. Les grandes "
                "applications web comme Visual Studio Code (entierement ecrit en TypeScript), "
                "Figma, et Slack utilisent TypeScript pour gerer la complexite du code. Pour "
                "le developpement backend avec Node.js, TypeScript est devenu quasi standard. "
                "NestJS est un framework backend inspire d'Angular qui exploite pleinement "
                "les decorateurs et les types TypeScript. Les APIs GraphQL beneficient "
                "particulierement de TypeScript grace au typage fort des schemas et des "
                "resolvers (avec des outils comme GraphQL Code Generator). Les bibliotheques "
                "de donnees comme Prisma et Drizzle ORM generent des types TypeScript a "
                "partir des schemas de base de donnees, offrant un typage de bout en bout. "
                "Les monorepos beneficient de TypeScript avec les project references pour "
                "la compilation incrementale. TypeScript est egalement utilise pour les "
                "applications mobiles via React Native, les applications desktop via Electron, "
                "et les fonctions serverless. Dans le domaine des outils de developpement, "
                "de nombreux outils modernes sont ecrits en TypeScript : ESLint, Prettier "
                "(les plugins), les Language Servers, et les extensions VS Code. TypeScript "
                "est aussi de plus en plus utilise pour l'infrastructure as code avec des "
                "outils comme Pulumi et CDK (AWS). Le typage de bout en bout (frontend + "
                "backend + base de donnees) avec des outils comme tRPC est un cas d'utilisation "
                "tres populaire."
            ),
            "ecosystem": (
                "L'ecosysteme TypeScript est essentiellement l'ecosysteme JavaScript etendu "
                "avec des types. Tout paquet npm peut etre utilise en TypeScript, soit "
                "directement s'il inclut ses propres declarations de types, soit via les "
                "paquets @types/* du depot DefinitelyTyped. Les outils de build incluent "
                "tsc (le compilateur officiel), esbuild (extremement rapide, ecrit en Go), "
                "swc (ecrit en Rust), et Vite (qui utilise esbuild en dev et Rollup en "
                "production). Pour les frameworks frontend, React avec TypeScript offre un "
                "typage complet des composants, props, hooks, et du contexte. Angular utilise "
                "TypeScript nativement avec des decorateurs. Vue.js 3 avec le Composition "
                "API offre une excellent inference de types. Les frameworks fullstack comme "
                "Next.js, Nuxt.js, et SvelteKit supportent TypeScript nativement. Pour le "
                "backend, NestJS est le framework TypeScript-first le plus populaire, "
                "inspire d'Angular avec l'injection de dependances et les decorateurs. "
                "Fastify offre un excellent support TypeScript. Les ORM types comme "
                "Prisma (generation de types depuis le schema), Drizzle (TypeScript-first), "
                "et TypeORM sont tres utilises. Pour la validation de donnees a l'execution, "
                "Zod est devenu la reference, permettant d'inferer des types TypeScript "
                "depuis les schemas de validation. tRPC permet de creer des APIs type-safe "
                "de bout en bout sans generation de code. Pour les tests, Jest et Vitest "
                "supportent TypeScript via ts-jest ou nativement. Les outils de qualite "
                "incluent ESLint avec @typescript-eslint, Prettier, et les checks stricts "
                "de tsconfig. Visual Studio Code est l'IDE de reference avec un support "
                "TypeScript integre exceptionnel. WebStorm (JetBrains) offre egalement "
                "un excellent support."
            ),
            "companies": [
                "Microsoft (VS Code, Azure DevOps, Office Online)",
                "Google (Angular, Google Cloud Console)",
                "Airbnb (frontend, outils de design)",
                "Slack (application desktop Electron)",
                "Stripe (dashboard, bibliotheques clientes)",
                "Shopify (interface admin, Hydrogen framework)",
                "Vercel (Next.js, plateforme de deploiement)"
            ],
            "code_example": (
                "// Systeme de gestion d'inventaire type-safe\n\n"
                "interface Produit<T extends string = string> {\n"
                "  readonly id: number;\n"
                "  nom: string;\n"
                "  categorie: T;\n"
                "  prix: number;\n"
                "  stock: number;\n"
                "}\n\n"
                "type Categorie = 'electronique' | 'alimentaire' | 'vetement';\n\n"
                "class Inventaire<C extends string = Categorie> {\n"
                "  private produits: Map<number, Produit<C>> = new Map();\n\n"
                "  ajouter(produit: Produit<C>): void {\n"
                "    this.produits.set(produit.id, produit);\n"
                "  }\n\n"
                "  trouverParCategorie(categorie: C): Produit<C>[] {\n"
                "    return [...this.produits.values()]\n"
                "      .filter(p => p.categorie === categorie);\n"
                "  }\n\n"
                "  valeurTotale(): number {\n"
                "    return [...this.produits.values()]\n"
                "      .reduce((total, p) => total + p.prix * p.stock, 0);\n"
                "  }\n\n"
                "  rupture(): Produit<C>[] {\n"
                "    return [...this.produits.values()]\n"
                "      .filter(p => p.stock === 0);\n"
                "  }\n"
                "}\n\n"
                "// Utilisation avec types stricts\n"
                "const inventaire = new Inventaire<Categorie>();\n"
                "inventaire.ajouter({\n"
                "  id: 1,\n"
                "  nom: 'Ordinateur portable',\n"
                "  categorie: 'electronique',\n"
                "  prix: 999.99,\n"
                "  stock: 15,\n"
                "});\n\n"
                "const electroniques = inventaire.trouverParCategorie('electronique');\n"
                "console.log(`Valeur totale: ${inventaire.valeurTotale()} EUR`);\n"
            ),
            "performance": {
                "startup_time": "Rapide (une fois compile en JS)",
                "throughput": "Moyen (identique a JavaScript apres compilation)",
                "memory": "Moyen (identique a JavaScript)",
                "concurrency_model": "Identique a JavaScript : event loop, async/await, Workers"
            },
            "learning_curve": "Moyenne (si JavaScript deja connu)",
            "community_size": "Tres grande (en croissance rapide)",
            "job_market": "Tres fort (de plus en plus requis dans les offres)"
        },
        "traits": {
            "performance": 5,
            "developer_speed": 7,
            "learning_curve": 4,
            "ecosystem_size": 10,
            "type_safety": 8,
            "concurrency": 6,
            "memory_safety": 5,
            "scalability": 8
        }
    },

    # =========================================================================
    # 6. Rust
    # =========================================================================
    "rust": {
        "name": "Rust",
        "category": "language",
        "year_created": 2010,
        "creator": "Graydon Hoare (Mozilla)",
        "paradigm": ["Fonctionnel", "Imperatif", "Concurrent"],
        "typing": "Statique fort avec inference",
        "sections": {
            "overview": (
                "Rust est un langage de programmation systeme qui vise a offrir des performances "
                "comparables au C et au C++ tout en garantissant la securite memoire sans "
                "recourir a un ramasse-miettes. Cree par Graydon Hoare chez Mozilla Research "
                "et publie en version stable 1.0 en 2015, Rust a introduit un concept "
                "revolutionnaire : le systeme d'ownership (possession) avec borrow checking "
                "(verification d'emprunt) a la compilation. Ce systeme garantit qu'il n'y a "
                "pas de courses aux donnees (data races), pas de references pendantes (dangling "
                "pointers), pas de double liberations (double free), et pas de dereferencements "
                "de pointeurs nuls, le tout sans surcout a l'execution. La philosophie de "
                "Rust est 'fearless concurrency' : le systeme de types rend impossible "
                "l'ecriture de code concurrent avec des bugs de memoire. Rust est un langage "
                "multi-paradigme qui favorise la programmation fonctionnelle (pattern matching, "
                "closures, iterateurs, types algebriques via enums) tout en permettant un "
                "controle bas niveau quand necessaire (via unsafe). Le systeme de types de "
                "Rust est extremement puissant avec les traits (similaires aux interfaces "
                "mais plus flexibles), les generiques avec bounds, et les lifetimes "
                "(durees de vie) explicites. Rust a ete elu langage le plus aime par les "
                "developpeurs dans le sondage Stack Overflow pendant sept annees consecutives. "
                "Il est adopte par des entreprises majeures (Microsoft, Google, Amazon, Meta, "
                "Cloudflare) pour des composants critiques en performance et securite. Linux "
                "a commence a integrer du code Rust dans son noyau a partir de la version "
                "6.1, une premiere historique pour un langage autre que le C."
            ),
            "history": (
                "L'histoire de Rust commence en 2006 comme un projet personnel de Graydon "
                "Hoare, ingenieur chez Mozilla. Frustre par les bugs memoire recurrents dans "
                "les programmes C et C++ (et en particulier dans Firefox), Hoare a entrepris "
                "de concevoir un langage qui eliminerait ces categories de bugs tout en "
                "offrant des performances comparables. Mozilla a officiellement soutenu le "
                "projet a partir de 2009, et la premiere version pre-alpha a ete publiee "
                "en 2010. Les annees suivantes ont vu le langage evoluer considerablement. "
                "Le systeme de types a ete redesigne plusieurs fois : le systeme de garbage "
                "collection optionnel initial a ete abandonne au profit du systeme d'ownership "
                "et de borrow checking qui definit Rust aujourd'hui. La version 1.0 est sortie "
                "le 15 mai 2015, marquant la stabilisation du langage et l'engagement de "
                "compatibilite ascendante. Depuis, Rust suit un cycle de publication de "
                "six semaines pour les versions stables, avec un systeme d'editions (2015, "
                "2018, 2021, 2024) pour les changements plus importants tout en maintenant "
                "la retrocompatibilite. L'edition 2018 a apporte des changements majeurs "
                "d'ergonomie : le module system simplifie, les async/await (stabilises en "
                "1.39), et les NLL (Non-Lexical Lifetimes). Le projet Servo, un moteur de "
                "navigateur experimental ecrit en Rust par Mozilla, a prouve la viabilite "
                "du langage pour des projets systeme complexes. En 2020, les licenciements "
                "chez Mozilla ont menace le projet, mais la creation de la Rust Foundation "
                "en 2021 (soutenue par Amazon, Google, Microsoft, Huawei, et Mozilla) a "
                "assure sa perennite. L'adoption de Rust dans le noyau Linux a partir de "
                "2022 a ete un moment historique. Des projets majeurs ont ete reecrits en "
                "Rust pour la performance et la securite : ripgrep, fd, exa, Alacritty, "
                "et de nombreux outils de l'ecosysteme JavaScript (swc, Turbopack, Biome, "
                "Ruff pour Python)."
            ),
            "architecture": (
                "Rust est un langage compile qui utilise LLVM comme backend de compilation, "
                "produisant du code machine natif hautement optimise. Le compilateur rustc "
                "effectue une analyse statique approfondie a la compilation, ce qui resulte "
                "en des temps de compilation plus longs que le C mais en un code d'une "
                "surete superieure. Le systeme d'ownership est le coeur de l'architecture "
                "de Rust. Chaque valeur en Rust a un unique proprietaire, et la valeur est "
                "liberee (dropped) quand le proprietaire sort du scope. Les valeurs peuvent "
                "etre empruntees (borrowed) de maniere immutable (plusieurs emprunts "
                "simultanement) ou mutable (un seul emprunt exclusif), mais jamais les deux "
                "en meme temps. Le borrow checker verifie ces regles a la compilation, "
                "eliminant les courses aux donnees et les references pendantes. Le systeme "
                "de types utilise les traits pour le polymorphisme et l'abstraction. Les "
                "traits peuvent etre utilises pour le dispatch statique (monomorphisation, "
                "similaire aux templates C++) ou le dispatch dynamique (via dyn Trait, "
                "similaire aux interfaces avec vtable). Les enums de Rust sont des types "
                "algebriques (sum types) qui, combines avec le pattern matching exhaustif, "
                "offrent une alternative puissante aux exceptions et aux valeurs nulles. "
                "Result<T, E> pour la gestion d'erreurs et Option<T> pour les valeurs "
                "optionnelles sont utilises partout dans l'ecosysteme. Les lifetimes "
                "(durees de vie) sont des annotations qui permettent au compilateur de "
                "verifier que les references sont toujours valides. L'inference de lifetimes "
                "(elision) reduit le besoin d'annotations explicites dans la majorite des cas. "
                "Le systeme async de Rust est base sur les Futures et les runtimes async "
                "(Tokio, async-std). Contrairement a d'autres langages, Rust n'inclut pas "
                "de runtime async dans la bibliotheque standard, laissant le choix a "
                "l'utilisateur. Le mot-cle unsafe permet de desactiver certaines verifications "
                "du borrow checker pour les operations bas niveau (FFI, manipulation de "
                "pointeurs bruts), isolant clairement le code potentiellement dangereux. "
                "Cargo est a la fois le gestionnaire de paquets et le systeme de build, "
                "offrant une experience de developpement integree et coherente."
            ),
            "pros_cons": {
                "pros": [
                    "Securite memoire garantie a la compilation sans ramasse-miettes",
                    "Performances comparables au C et au C++",
                    "Concurrence sure (fearless concurrency) via le systeme de types",
                    "Systeme de types expressif avec enums, pattern matching, et traits",
                    "Excellent gestionnaire de paquets et systeme de build (Cargo)",
                    "Messages d'erreur du compilateur exceptionnellement clairs et utiles",
                    "Pas de null : Option<T> oblige a gerer explicitement l'absence",
                    "Ecosysteme de qualite avec des normes de documentation elevees"
                ],
                "cons": [
                    "Courbe d'apprentissage tres raide (ownership, lifetimes, borrow checker)",
                    "Temps de compilation plus longs que les langages comparables",
                    "Le 'combat avec le borrow checker' peut frustrer les debutants",
                    "Ecosysteme encore jeune par rapport a C++, Java, ou Python",
                    "Async Rust ajoute une complexite significative",
                    "Les macros procedurales sont puissantes mais complexes a ecrire",
                    "Moins de developpeurs disponibles sur le marche de l'emploi",
                    "Les lifetimes explicites peuvent rendre le code verbeux"
                ]
            },
            "use_cases": (
                "Rust excelle dans les domaines ou la performance et la securite sont toutes "
                "deux critiques. La programmation systeme est le cas d'utilisation premier : "
                "pilotes de peripheriques, composants de systemes d'exploitation (Rust dans le "
                "noyau Linux), et outils systeme (ripgrep, fd, bat, exa, starship). Les outils "
                "de developpement haute performance sont de plus en plus ecrits en Rust : "
                "swc (transpileur JavaScript/TypeScript), Turbopack (bundler), Biome (linter "
                "et formateur), Ruff (linter Python), et uv (gestionnaire de paquets Python). "
                "Le developpement web backend avec des frameworks comme Actix Web, Axum, et "
                "Rocket offre des performances exceptionnelles pour les APIs et les microservices. "
                "Les services reseau et les proxies (Cloudflare Workers, Linkerd, Pingora) "
                "tirent parti de la combinaison performance + securite de Rust. Les systemes "
                "embarques utilisent Rust pour des applications sans systeme d'exploitation "
                "(bare-metal) grace a no_std. Le WebAssembly est un domaine ou Rust brille "
                "particulierement, grace a wasm-pack et wasm-bindgen qui facilitent la "
                "compilation vers WebAssembly. Les bases de donnees et les moteurs de stockage "
                "(SurrealDB, Qdrant, Meilisearch) beneficient de la performance et de la "
                "fiabilite de Rust. La cryptographie et la blockchain utilisent egalement "
                "beaucoup Rust (Solana, Polkadot, Near). Les moteurs de jeux comme Bevy "
                "montrent le potentiel de Rust dans le game development. Les CLI (command-line "
                "interfaces) sont un cas d'utilisation populaire grace a Clap et a la rapidite "
                "de demarrage des executables Rust."
            ),
            "ecosystem": (
                "L'ecosysteme Rust est centre autour de Cargo, qui est simultanement le "
                "gestionnaire de paquets, le systeme de build, le lanceur de tests, et le "
                "generateur de documentation. crates.io est le registre officiel des paquets "
                "(crates) avec plus de 140 000 crates disponibles. Cargo offre une experience "
                "de developpement remarquablement coherente et integree. Pour la programmation "
                "asynchrone, Tokio est le runtime async dominant, offrant un scheduler "
                "multi-thread, des primitives d'I/O asynchrone, et un ecosysteme riche. "
                "async-std est une alternative plus proche de la bibliotheque standard. Les "
                "frameworks web incluent Actix Web (performances maximales), Axum (par l'equipe "
                "Tokio, bien integre a l'ecosysteme), et Rocket (ergonomique, avec macros). "
                "Pour la serialisation, Serde est une bibliotheque extraordinaire qui supporte "
                "JSON, YAML, TOML, MessagePack, et bien d'autres formats via un systeme de "
                "derive macros. Clap est le standard pour le parsing d'arguments en ligne de "
                "commande. Pour les bases de donnees, SQLx (requetes verifiees a la compilation), "
                "Diesel (ORM type-safe), et SeaORM sont les options principales. Les outils "
                "de test incluent le framework de test integre, proptest (property-based testing), "
                "et criterion (benchmarking). Pour l'analyse et le linting, Clippy (lint "
                "officiel) et rust-analyzer (serveur de langage) offrent un excellent support. "
                "rustfmt formate le code selon les conventions officielles. Pour le "
                "developpement embarque, embedded-hal fournit une abstraction portable pour "
                "le materiel. Le toolchain inclut rustup (gestionnaire de versions), "
                "cross (compilation croisee facile), et miri (interpreteur pour detecter "
                "les comportements indefinis dans le code unsafe). Les IDE majeurs sont "
                "VS Code avec rust-analyzer, RustRover (JetBrains), et Neovim/Helix avec "
                "LSP."
            ),
            "companies": [
                "Mozilla (Servo, parties de Firefox)",
                "Cloudflare (Pingora, Workers, infrastructure reseau)",
                "Amazon (Firecracker, Bottlerocket, Lambda runtime)",
                "Microsoft (Windows, Azure, outils de securite)",
                "Google (Android, Fuchsia, ChromeOS)",
                "Meta (outils de build Buck2, analyse source)",
                "Discord (services backend haute performance)"
            ],
            "code_example": (
                "use std::collections::HashMap;\n\n"
                "#[derive(Debug)]\n"
                "struct Etudiant {\n"
                "    nom: String,\n"
                "    notes: Vec<f64>,\n"
                "}\n\n"
                "impl Etudiant {\n"
                "    fn new(nom: &str, notes: Vec<f64>) -> Self {\n"
                "        Etudiant {\n"
                "            nom: nom.to_string(),\n"
                "            notes,\n"
                "        }\n"
                "    }\n\n"
                "    fn moyenne(&self) -> Option<f64> {\n"
                "        if self.notes.is_empty() {\n"
                "            None\n"
                "        } else {\n"
                "            let somme: f64 = self.notes.iter().sum();\n"
                "            Some(somme / self.notes.len() as f64)\n"
                "        }\n"
                "    }\n\n"
                "    fn est_admis(&self) -> bool {\n"
                "        self.moyenne().map_or(false, |m| m >= 10.0)\n"
                "    }\n"
                "}\n\n"
                "fn statistiques(etudiants: &[Etudiant]) -> HashMap<&str, usize> {\n"
                "    let mut stats = HashMap::new();\n"
                "    let admis = etudiants.iter().filter(|e| e.est_admis()).count();\n"
                '    stats.insert("admis", admis);\n'
                '    stats.insert("refuses", etudiants.len() - admis);\n'
                "    stats\n"
                "}\n\n"
                "fn main() {\n"
                "    let etudiants = vec![\n"
                '        Etudiant::new("Alice", vec![15.5, 14.0, 16.5]),\n'
                '        Etudiant::new("Bob", vec![8.0, 9.5, 7.0]),\n'
                '        Etudiant::new("Claire", vec![18.0, 17.5, 19.0]),\n'
                "    ];\n\n"
                "    for etudiant in &etudiants {\n"
                "        match etudiant.moyenne() {\n"
                "            Some(moy) => println!(\n"
                '                "{}: {:.2} - {}",\n'
                "                etudiant.nom,\n"
                "                moy,\n"
                '                if etudiant.est_admis() { "Admis" } else { "Refuse" }\n'
                "            ),\n"
                '            None => println!("{}: Aucune note", etudiant.nom),\n'
                "        }\n"
                "    }\n\n"
                "    let stats = statistiques(&etudiants);\n"
                '    println!("\\nStatistiques: {:?}", stats);\n'
                "}\n"
            ),
            "performance": {
                "startup_time": "Tres rapide (pas de runtime)",
                "throughput": "Tres eleve (comparable au C/C++)",
                "memory": "Tres faible (pas de GC, controle fin)",
                "concurrency_model": "Ownership + Send/Sync traits, async/await (Tokio), threads, channels"
            },
            "learning_curve": "Tres elevee",
            "community_size": "Grande (en croissance rapide)",
            "job_market": "En forte croissance (offres premium)"
        },
        "traits": {
            "performance": 9,
            "developer_speed": 4,
            "learning_curve": 9,
            "ecosystem_size": 6,
            "type_safety": 9,
            "concurrency": 9,
            "memory_safety": 10,
            "scalability": 9
        }
    },

    # =========================================================================
    # 7. Go
    # =========================================================================
    "go": {
        "name": "Go",
        "category": "language",
        "year_created": 2009,
        "creator": "Robert Griesemer, Rob Pike, Ken Thompson (Google)",
        "paradigm": ["Imperatif", "Concurrent", "Procedural"],
        "typing": "Statique fort avec inference",
        "sections": {
            "overview": (
                "Go (aussi appele Golang) est un langage de programmation cree par Google et "
                "publie en open source en 2009. Concu par Robert Griesemer, Rob Pike et Ken "
                "Thompson (co-createur d'UNIX et du langage C), Go a ete cree pour repondre "
                "aux defis de l'ingenierie logicielle a grande echelle chez Google. La "
                "philosophie de Go repose sur la simplicite radicale : le langage a ete "
                "deliberement concu avec un nombre minimal de fonctionnalites, chacune etant "
                "orthogonale aux autres. Le resultat est un langage facile a apprendre, "
                "facile a lire, et dont le code est remarquablement uniforme d'un projet "
                "a l'autre. Go brille particulierement dans le developpement de services "
                "backend, de microservices, et d'outils infrastructure. Sa force principale "
                "est son modele de concurrence base sur les goroutines et les channels, "
                "inspire du modele CSP (Communicating Sequential Processes) de Tony Hoare. "
                "Les goroutines sont des threads legers geres par le runtime Go, extremement "
                "peu couteux en memoire (quelques Ko par goroutine contre plusieurs Mo pour "
                "un thread OS), ce qui permet de lancer des centaines de milliers de goroutines "
                "simultanement. Go produit des executables statiques sans dependances, avec "
                "une compilation extremement rapide, ce qui en fait un choix ideal pour les "
                "conteneurs Docker et le deploiement cloud. Le ramasse-miettes de Go est "
                "optimise pour minimiser la latence, avec des pauses de l'ordre de la "
                "milliseconde. Go a deliberement omis certaines fonctionnalites considerees "
                "comme complexes : pas d'heritage de classes, pas de generiques (ajoutees en "
                "1.18), pas de surcharge de fonctions, pas d'exceptions. Cette approche "
                "minimaliste est controversee mais resulte en un code coherent et maintenable."
            ),
            "history": (
                "L'histoire de Go commence en 2007 chez Google, ou Robert Griesemer, Rob Pike "
                "et Ken Thompson, frustres par la complexite du C++ et les temps de compilation "
                "interminables des grands projets Google, ont commence a concevoir un nouveau "
                "langage. Les trois createurs apportaient chacun une expertise unique : "
                "Thompson avait co-cree UNIX et le langage C, Pike avait travaille sur Plan 9 "
                "et le systeme de fenetres d'UNIX, et Griesemer avait travaille sur la JVM "
                "HotSpot et le moteur JavaScript V8. Go a ete annonce publiquement en "
                "novembre 2009 et a atteint la version 1.0 en mars 2012, avec la promesse "
                "de compatibilite ascendante qui est toujours respectee aujourd'hui. Les "
                "premieres versions ont concentre les efforts sur la stabilite et la "
                "performance du runtime. Go 1.5 (2015) a ete une etape majeure : le "
                "compilateur et le runtime, initialement ecrits en C, ont ete entierement "
                "reecrits en Go (bootstrapping). Le ramasse-miettes a ete completement "
                "redesigne pour des pauses sub-milliseconde. Go 1.11 (2018) a introduit "
                "les Go Modules, resolvant enfin le probleme de la gestion des dependances "
                "qui avait longtemps ete un point faible du langage (l'ancien GOPATH). Go "
                "1.18 (2022) a ete la plus grande mise a jour depuis 1.0 : l'introduction "
                "des generiques (type parameters) a resolu la plainte la plus frequente de "
                "la communaute, qui devait auparavant recourir a des interface{} et du "
                "casting ou a la generation de code. Go 1.21 a introduit les fonctions "
                "min, max, et clear builtin, ainsi que le support des numeros de version "
                "dans les directives go. La communaute Go a adopte des outils et des "
                "conventions qui font partie integrante de l'ecosysteme : gofmt (formatage "
                "officiel), go vet (analyse statique), et le testing integre."
            ),
            "architecture": (
                "Go est un langage compile qui produit des executables natifs statiquement "
                "lies. Le compilateur Go est extremement rapide, une priorite de conception "
                "qui permet des cycles de developpement fluides meme pour les grands projets. "
                "Contrairement au C et au C++, Go inclut un runtime embarque dans chaque "
                "executable, qui fournit le ramasse-miettes, le scheduler de goroutines, et "
                "la gestion de la pile. Le modele de concurrence de Go est base sur le CSP "
                "(Communicating Sequential Processes). Les goroutines sont des unites "
                "d'execution concurrentes multiplexees sur un nombre reduit de threads OS "
                "par un scheduler cooperatif integre au runtime. Ce scheduler utilise le "
                "modele M:N (M goroutines sur N threads) et peut preempter les goroutines "
                "longues depuis Go 1.14. Les channels sont le mecanisme principal de "
                "communication entre goroutines, permettant d'envoyer et recevoir des "
                "valeurs de maniere synchronisee. Le select statement permet d'attendre "
                "simultanement sur plusieurs channels. Le ramasse-miettes de Go est un "
                "GC concurrent tri-colore (tri-color mark-and-sweep) optimise pour la "
                "latence plutot que le throughput. Les pauses GC sont typiquement "
                "inferieures a la milliseconde, meme pour les applications avec des "
                "gigaoctets de memoire. Le systeme de types de Go utilise les interfaces "
                "implicites : un type satisfait une interface simplement en implementant "
                "ses methodes, sans declaration explicite. Ce 'duck typing statique' offre "
                "flexibilite et decouplage. Les generiques (type parameters), ajoutees en "
                "Go 1.18, permettent d'ecrire du code parametrique type-safe avec des "
                "contraintes de types. Le modele de gestion d'erreurs de Go utilise des "
                "valeurs de retour multiples, ou la derniere valeur est conventionnellement "
                "un error. Les defer statements garantissent le nettoyage des ressources, "
                "tandis que panic/recover gerent les erreurs irrecuperables. La compilation "
                "croisee est triviale avec Go : il suffit de changer les variables GOOS "
                "et GOARCH pour compiler pour n'importe quelle plateforme supportee."
            ),
            "pros_cons": {
                "pros": [
                    "Concurrence native simple et puissante (goroutines, channels)",
                    "Compilation tres rapide vers des executables statiques",
                    "Simplicite du langage, facile a apprendre et a lire",
                    "Tooling excellent et uniforme (gofmt, go vet, go test)",
                    "Ideal pour les microservices et l'infrastructure cloud",
                    "Deploiement trivial (executable unique sans dependances)",
                    "Garbage collector optimise pour la latence",
                    "Compilation croisee tres facile"
                ],
                "cons": [
                    "Simplicite parfois excessive (gestion d'erreurs repetitive avec if err != nil)",
                    "Pas de generiques avant Go 1.18, generiques encore limitees",
                    "Pas d'enumerations (enums) expressives comme Rust ou Swift",
                    "Pas de types algebriques (sum types) pour les unions discriminees",
                    "Garbage collector inadapte aux applications a latence ultra-faible",
                    "Systeme de modules qui a mis longtemps a murir",
                    "Pas de surcharge d'operateurs ni de valeurs par defaut pour les arguments",
                    "La philosophie de simplicite peut sembler rigide pour certains developpeurs"
                ]
            },
            "use_cases": (
                "Go est le langage de predilection pour l'infrastructure cloud et les "
                "outils DevOps. L'ecosysteme Cloud Native est domine par des projets Go : "
                "Docker (conteneurs), Kubernetes (orchestration), Terraform (infrastructure "
                "as code), Prometheus (monitoring), Grafana (tableaux de bord), etcd "
                "(stockage cle-valeur distribue), et Consul (service mesh). Les microservices "
                "sont un cas d'utilisation ideal pour Go : la compilation vers des executables "
                "statiques produit des images Docker minuscules, les goroutines gerent "
                "efficacement la concurrence, et le tooling integre simplifie les tests et "
                "le deploiement. Les serveurs web et les APIs haute performance beneficient "
                "du excellent package net/http de la bibliotheque standard et des frameworks "
                "comme Gin, Echo, et Fiber. Les outils en ligne de commande (CLI) sont un "
                "domaine ou Go excelle : la compilation rapide, les executables sans "
                "dependances, et la portabilite multi-plateforme sont ideales (GitHub CLI, "
                "Hugo, Cobra). Les systemes distribues comme CockroachDB, TiDB, et InfluxDB "
                "utilisent Go pour sa concurrence et sa fiabilite. Les proxies et les load "
                "balancers (Caddy, Traefik) tirent parti du modele de concurrence de Go. "
                "Le traitement de donnees en streaming et les pipelines ETL beneficient des "
                "goroutines et des channels. Les applications reseau (DNS, HTTP/2, gRPC) sont "
                "un domaine naturel pour Go grace a sa bibliotheque standard riche en "
                "fonctionnalites reseau. Go est aussi utilise pour les blockchains (Ethereum "
                "avec go-ethereum/geth) et la securite informatique (outils de pentesting)."
            ),
            "ecosystem": (
                "L'ecosysteme Go est remarquablement bien integre grace aux outils fournis "
                "avec le langage. Go Modules (go mod) est le systeme officiel de gestion des "
                "dependances, utilisant une gestion de versions semantique et un proxy de "
                "modules (proxy.golang.org) pour la reproductibilite. La commande go inclut "
                "la compilation (go build), les tests (go test), le formatage (gofmt/go fmt), "
                "l'analyse statique (go vet), la documentation (go doc), et la generation de "
                "code (go generate). Ce tooling unifie garantit une experience coherente. "
                "La bibliotheque standard de Go est exceptionnellement riche : net/http pour "
                "les serveurs et clients HTTP, encoding/json pour la serialisation JSON, "
                "database/sql pour les bases de donnees, crypto/* pour la cryptographie, "
                "et testing pour les tests. Pour le developpement web, les frameworks "
                "populaires incluent Gin (le plus utilise, performant), Echo (minimaliste), "
                "Fiber (inspire d'Express.js), et Chi (compatible net/http). Pour les APIs, "
                "gRPC-Go est le standard pour les communications entre microservices. Les "
                "ORM et outils de base de donnees incluent GORM (le plus populaire), sqlx, "
                "et ent (par Meta). Pour les tests, testify est le framework d'assertions "
                "le plus utilise, et mockery/gomock pour le mocking. Les outils d'analyse "
                "statique incluent golangci-lint (meta-linter regroupant des dizaines de "
                "linters), staticcheck, et go vet. delve est le debogueur standard. Pour "
                "les CLI, Cobra (utilise par Docker, Kubernetes, Hugo) et urfave/cli sont "
                "les frameworks de reference. Les IDE majeurs sont GoLand (JetBrains) et "
                "VS Code avec l'extension officielle Go (gopls comme serveur de langage). "
                "Air permet le rechargement automatique en developpement."
            ),
            "companies": [
                "Google (infrastructure, Kubernetes, services internes)",
                "Docker (Docker Engine, Docker Compose)",
                "Hashicorp (Terraform, Vault, Consul, Nomad)",
                "Uber (services backend haute performance)",
                "Twitch (systemes de streaming video)",
                "Cloudflare (services reseau, WARP)",
                "Dropbox (migration de Python vers Go pour les performances)"
            ],
            "code_example": (
                "package main\n\n"
                "import (\n"
                '\t"fmt"\n'
                '\t"sync"\n'
                '\t"time"\n'
                ")\n\n"
                "type Resultat struct {\n"
                "\tURL     string\n"
                "\tStatut  string\n"
                "\tDuree   time.Duration\n"
                "}\n\n"
                "func verifierURL(url string, ch chan<- Resultat, wg *sync.WaitGroup) {\n"
                "\tdefer wg.Done()\n"
                "\tdebut := time.Now()\n\n"
                "\t// Simulation d'une requete HTTP\n"
                "\ttime.Sleep(100 * time.Millisecond)\n\n"
                "\tch <- Resultat{\n"
                "\t\tURL:    url,\n"
                '\t\tStatut: "OK",\n'
                "\t\tDuree:  time.Since(debut),\n"
                "\t}\n"
                "}\n\n"
                "func main() {\n"
                "\turls := []string{\n"
                '\t\t"https://example.com",\n'
                '\t\t"https://golang.org",\n'
                '\t\t"https://github.com",\n'
                '\t\t"https://google.com",\n'
                "\t}\n\n"
                "\tch := make(chan Resultat, len(urls))\n"
                "\tvar wg sync.WaitGroup\n\n"
                "\tfor _, url := range urls {\n"
                "\t\twg.Add(1)\n"
                "\t\tgo verifierURL(url, ch, &wg)\n"
                "\t}\n\n"
                "\t// Fermer le channel quand toutes les goroutines sont terminees\n"
                "\tgo func() {\n"
                "\t\twg.Wait()\n"
                "\t\tclose(ch)\n"
                "\t}()\n\n"
                "\t// Lire les resultats\n"
                "\tfor res := range ch {\n"
                '\t\tfmt.Printf("[%s] %s - %v\\n", res.Statut, res.URL, res.Duree)\n'
                "\t}\n"
                "}\n"
            ),
            "performance": {
                "startup_time": "Tres rapide",
                "throughput": "Eleve",
                "memory": "Moyen (GC)",
                "concurrency_model": "Goroutines (CSP), channels, sync.Mutex, sync.WaitGroup"
            },
            "learning_curve": "Faible",
            "community_size": "Grande (en croissance)",
            "job_market": "Tres fort (cloud, DevOps, backend)"
        },
        "traits": {
            "performance": 7,
            "developer_speed": 7,
            "learning_curve": 3,
            "ecosystem_size": 7,
            "type_safety": 7,
            "concurrency": 9,
            "memory_safety": 7,
            "scalability": 9
        }
    },

    # =========================================================================
    # 8. Java
    # =========================================================================
    "java": {
        "name": "Java",
        "category": "language",
        "year_created": 1995,
        "creator": "James Gosling (Sun Microsystems)",
        "paradigm": ["Oriente Objet", "Imperatif", "Concurrent"],
        "typing": "Statique fort",
        "sections": {
            "overview": (
                "Java est un langage de programmation oriente objet qui a profondement marque "
                "l'histoire de l'informatique depuis sa creation en 1995. Concu par James "
                "Gosling chez Sun Microsystems (rachetee par Oracle en 2010), Java a ete "
                "cree avec le slogan 'Write Once, Run Anywhere' (WORA), promettant la "
                "portabilite du code grace a la Java Virtual Machine (JVM). Cette promesse "
                "a ete largement tenue : le meme bytecode Java peut s'executer sur n'importe "
                "quelle plateforme disposant d'une JVM, de Windows a Linux en passant par "
                "macOS et les systemes embarques. Java est un langage strictement oriente "
                "objet (presque tout est un objet, sauf les types primitifs) avec un typage "
                "statique fort. Sa gestion automatique de la memoire par ramasse-miettes "
                "elimine de nombreuses categories de bugs memoire courants en C/C++, au "
                "prix d'une latence occasionnelle due aux pauses du GC. Java est le langage "
                "de choix pour les applications d'entreprise a grande echelle grace a son "
                "ecosysteme mature, sa robustesse, et sa scalabilite. La JVM est devenue "
                "une plateforme en soi, hebergeant d'autres langages comme Kotlin, Scala, "
                "Clojure, et Groovy. Java domine dans le backend d'entreprise (Spring), "
                "le Big Data (Hadoop, Spark), le developpement Android (historiquement), et "
                "les systemes financiers. Malgre les critiques sur sa verbosites, les versions "
                "recentes de Java (records, sealed classes, pattern matching, virtual threads) "
                "ont considerablement modernise le langage, le rendant plus concis et expressif."
            ),
            "history": (
                "L'histoire de Java commence en 1991 chez Sun Microsystems, ou James Gosling "
                "a debute le projet 'Green' visant a creer un langage pour l'electronique "
                "grand public et les appareils embarques. Le langage, initialement appele "
                "Oak (en reference a un chene devant le bureau de Gosling), devait etre "
                "portable, fiable, et sur. Apres la decouverte qu'un langage du meme nom "
                "existait deja, il a ete renomme Java. Le lancement public de Java 1.0 en "
                "1996 a coincide avec l'explosion du World Wide Web, et les applets Java "
                "permettant d'ajouter de l'interactivite aux pages web ont propulse le "
                "langage. Java 2 (J2SE 1.2, 1998) a ete une mise a jour majeure avec le "
                "framework Collections, Swing pour les GUI, et la JIT compilation. J2SE 5.0 "
                "(2004) a apporte les generiques, les enumerations, les annotations, l'autoboxing, "
                "et les boucles for-each. Java 6 (2006) et Java 7 (2011) ont ete plus "
                "incrementales. Java 8 (2014) a ete revolutionnaire : les lambdas, l'API "
                "Stream, les interfaces fonctionnelles, et les methodes par defaut dans les "
                "interfaces ont modernise le langage. Oracle a achete Sun en 2010 et a adopte "
                "un cycle de publication semestriel a partir de Java 9 (2017), avec des versions "
                "LTS (Long-Term Support) tous les deux ans. Java 9 a introduit le systeme de "
                "modules (JPMS/Jigsaw). Java 11 (LTS) a supprime les modules Java EE et les "
                "applets. Java 14 a apporte les records et le pattern matching pour instanceof. "
                "Java 17 (LTS) a introduit les sealed classes. Java 21 (LTS) est une version "
                "charniere avec les virtual threads (Project Loom, concurrence massivement "
                "legere), les sequenced collections, et le pattern matching avance. Java "
                "continue d'evoluer activement avec des projets comme Valhalla (value types), "
                "Panama (FFI), et Amber (ameliorations du langage)."
            ),
            "architecture": (
                "L'architecture de Java repose sur la Java Virtual Machine (JVM), une machine "
                "virtuelle sophistiquee qui execute le bytecode Java. Le code source (.java) "
                "est compile par javac en bytecode (.class), un format intermediaire independant "
                "de la plateforme. La JVM charge ensuite le bytecode et l'execute en utilisant "
                "l'interpretation et la compilation JIT (Just-In-Time). La JVM HotSpot "
                "(l'implementation de reference d'Oracle) utilise des compilateurs JIT "
                "sophistiques : C1 (rapide, moins d'optimisations) et C2 (plus lent, "
                "optimisations agressives). GraalVM est une JVM alternative qui offre un "
                "compilateur JIT base sur Graal et la capacite de compiler du Java en code "
                "natif (native-image). La gestion de la memoire en Java est entierement "
                "automatisee via le ramasse-miettes. La JVM organise la memoire en heap "
                "(pour les objets) et stack (pour les appels de methodes et les variables "
                "locales). Les GC modernes incluent G1 (par defaut depuis Java 9, bon "
                "compromis latence/throughput), ZGC (pauses sub-milliseconde, ideal pour les "
                "applications sensibles a la latence), et Shenandoah (similaire a ZGC, par "
                "Red Hat). Le systeme de types de Java est oriente objet avec heritage simple "
                "de classes et implementation multiple d'interfaces. Les generiques Java "
                "(ajoutees en Java 5) utilisent l'erasure de types, ce qui signifie que les "
                "informations de type generique sont supprimees a l'execution. Le classloading "
                "dynamique permet de charger des classes a l'execution, ce qui est a la base "
                "des frameworks d'injection de dependances (Spring). Les virtual threads "
                "(Java 21) revolutionnent la concurrence en Java : ce sont des threads legers "
                "geres par la JVM (similaires aux goroutines de Go), permettant des millions "
                "de threads concurrents. Le modele de memoire Java (Java Memory Model, JMM) "
                "definit formellement le comportement des operations concurrentes, garantissant "
                "la portabilite du code multithread."
            ),
            "pros_cons": {
                "pros": [
                    "Portabilite (Write Once, Run Anywhere via la JVM)",
                    "Ecosysteme d'entreprise extremement mature (Spring, Jakarta EE)",
                    "Ramasse-miettes avances (ZGC, Shenandoah pour latence ultra-faible)",
                    "Virtual threads (Java 21) pour la concurrence massive a moindre cout",
                    "Typage statique fort avec un excellent support IDE",
                    "Backward compatibility exemplaire sur des decennies",
                    "Documentation et ressources d'apprentissage abondantes",
                    "Grande base de developpeurs et marche de l'emploi fort"
                ],
                "cons": [
                    "Verbosity historique du langage (meme si en amelioration)",
                    "Temps de demarrage plus long que les langages compiles nativement",
                    "Consommation memoire elevee (JVM overhead)",
                    "Erasure des generiques limitant l'expressivite du systeme de types",
                    "Null pointer exceptions toujours possibles malgre Optional",
                    "Pas de types valeur natifs (avant le projet Valhalla)",
                    "Complexite de la configuration et du deploiement (JAR hell historique)",
                    "Les checked exceptions sont controversees et souvent contournees"
                ]
            },
            "use_cases": (
                "Java domine dans le developpement d'applications d'entreprise. Le framework "
                "Spring (et Spring Boot) est la reference pour les applications backend "
                "d'entreprise, offrant l'injection de dependances, la securite, l'acces aux "
                "donnees, et une architecture de microservices. Jakarta EE (anciennement "
                "Java EE) est le standard pour les applications d'entreprise deployees sur "
                "des serveurs d'applications. Le Big Data est un domaine ou Java et la JVM "
                "dominent : Apache Hadoop (traitement distribue), Apache Spark (traitement "
                "en memoire), Apache Kafka (streaming d'evenements), Apache Flink (streaming "
                "temps reel), et Elasticsearch (recherche et analytique). Le developpement "
                "Android a historiquement utilise Java comme langage principal (avant la "
                "transition vers Kotlin). Les systemes financiers et bancaires reposent "
                "massivement sur Java pour leur backend : systemes de trading, gestion "
                "des risques, et traitement des transactions. Les applications de gestion "
                "d'entreprise (ERP, CRM) sont souvent ecrites en Java. Le cloud computing "
                "et les microservices beneficient de l'ecosysteme Spring Cloud et des "
                "virtual threads pour la scalabilite. Les API RESTful et les services SOAP "
                "sont des cas d'utilisation classiques. Le testing et l'assurance qualite "
                "utilisent largement les outils Java (JUnit, Selenium, JMeter). Les serveurs "
                "d'applications comme Tomcat, Jetty, et WildFly sont ecrits en Java. Les "
                "projets scientifiques et de recherche utilisent la JVM pour des simulations "
                "et des analyses complexes."
            ),
            "ecosystem": (
                "L'ecosysteme Java est l'un des plus vastes et des plus matures de "
                "l'industrie. Maven et Gradle sont les systemes de build et de gestion des "
                "dependances dominants. Maven Central est le plus grand depot de bibliotheques "
                "Java avec des centaines de milliers d'artefacts. Le framework Spring est le "
                "coeur de l'ecosysteme d'entreprise : Spring Boot (applications autonomes), "
                "Spring MVC (web), Spring Data (acces aux donnees), Spring Security "
                "(authentification et autorisation), Spring Cloud (microservices). Hibernate "
                "est l'ORM de reference pour Java, implementant la specification JPA (Java "
                "Persistence API). Pour les tests, JUnit 5 est le framework standard, Mockito "
                "est le framework de mocking dominant, et AssertJ fournit des assertions "
                "fluentes. Pour le logging, SLF4J avec Logback ou Log4j2 est la norme. Les "
                "bibliotheques d'utilitaires comme Apache Commons, Guava (Google), et Lombok "
                "(reduction de la verbosity) sont omnipresen tes. Les serveurs d'applications "
                "incluent Tomcat, Jetty, et Undertow. Pour le monitoring, Micrometer et "
                "Spring Actuator sont utilises. Les IDE Java sont les meilleurs de l'industrie : "
                "IntelliJ IDEA (JetBrains, largement considere comme le meilleur IDE toutes "
                "categories), Eclipse, et NetBeans. Pour la conteneurisation, Jib (Google) "
                "permet de creer des images Docker sans Dockerfile. GraalVM offre la "
                "compilation native pour des temps de demarrage quasi instantanes. Quarkus "
                "(Red Hat) et Micronaut sont des frameworks optimises pour le cloud natif "
                "et GraalVM. Les outils d'analyse statique incluent SpotBugs, PMD, Checkstyle, "
                "et SonarQube. JMH (Java Microbenchmark Harness) est l'outil standard de "
                "benchmarking."
            ),
            "companies": [
                "Google (Android, services backend internes)",
                "Amazon (AWS, services de commerce electronique)",
                "Netflix (infrastructure de streaming, microservices)",
                "LinkedIn (backend, infrastructure data)",
                "Uber (services backend, traitement de donnees)",
                "Twitter/X (ancienne infrastructure, services JVM)",
                "Goldman Sachs (systemes de trading et de gestion des risques)"
            ],
            "code_example": (
                "import java.util.List;\n"
                "import java.util.Map;\n"
                "import java.util.stream.Collectors;\n\n"
                "// Utilisation de record (Java 16+) et sealed classes (Java 17+)\n"
                "sealed interface Forme permits Cercle, Rectangle, Triangle {}\n\n"
                "record Cercle(double rayon) implements Forme {\n"
                "    double aire() {\n"
                "        return Math.PI * rayon * rayon;\n"
                "    }\n"
                "}\n\n"
                "record Rectangle(double largeur, double hauteur) implements Forme {\n"
                "    double aire() {\n"
                "        return largeur * hauteur;\n"
                "    }\n"
                "}\n\n"
                "record Triangle(double base, double hauteur) implements Forme {\n"
                "    double aire() {\n"
                "        return (base * hauteur) / 2;\n"
                "    }\n"
                "}\n\n"
                "public class Main {\n"
                "    static String decrire(Forme forme) {\n"
                "        return switch (forme) {\n"
                '            case Cercle c -> "Cercle de rayon %.2f, aire: %.2f"\n'
                "                .formatted(c.rayon(), c.aire());\n"
                '            case Rectangle r -> "Rectangle %sx%s, aire: %.2f"\n'
                "                .formatted(r.largeur(), r.hauteur(), r.aire());\n"
                '            case Triangle t -> "Triangle base=%.2f h=%.2f, aire: %.2f"\n'
                "                .formatted(t.base(), t.hauteur(), t.aire());\n"
                "        };\n"
                "    }\n\n"
                "    public static void main(String[] args) {\n"
                "        var formes = List.of(\n"
                "            new Cercle(5),\n"
                "            new Rectangle(3, 4),\n"
                "            new Triangle(6, 8),\n"
                "            new Cercle(2.5)\n"
                "        );\n\n"
                "        formes.forEach(f -> System.out.println(decrire(f)));\n\n"
                "        // Grouper par type avec les streams\n"
                "        Map<String, List<Forme>> parType = formes.stream()\n"
                "            .collect(Collectors.groupingBy(\n"
                "                f -> f.getClass().getSimpleName()\n"
                "            ));\n"
                "        parType.forEach((type, liste) ->\n"
                '            System.out.printf("%s: %d forme(s)%n", type, liste.size())\n'
                "        );\n"
                "    }\n"
                "}\n"
            ),
            "performance": {
                "startup_time": "Moyen-Lent (JVM warmup) sauf avec GraalVM native",
                "throughput": "Eleve (JIT compile vers du code natif optimise)",
                "memory": "Moyen-Eleve (overhead de la JVM et du GC)",
                "concurrency_model": "Virtual threads (Loom), threads classiques, CompletableFuture, ExecutorService"
            },
            "learning_curve": "Moyenne",
            "community_size": "Tres grande (l'une des plus grandes)",
            "job_market": "Tres fort (entreprise, finance, backend)"
        },
        "traits": {
            "performance": 7,
            "developer_speed": 5,
            "learning_curve": 5,
            "ecosystem_size": 9,
            "type_safety": 8,
            "concurrency": 7,
            "memory_safety": 7,
            "scalability": 9
        }
    },

    # =========================================================================
    # 9. C#
    # =========================================================================
    "csharp": {
        "name": "C#",
        "category": "language",
        "year_created": 2000,
        "creator": "Anders Hejlsberg (Microsoft)",
        "paradigm": ["Oriente Objet", "Fonctionnel", "Imperatif", "Concurrent"],
        "typing": "Statique fort",
        "sections": {
            "overview": (
                "C# (prononce 'C sharp') est un langage de programmation moderne, multi-"
                "paradigme, concu par Anders Hejlsberg chez Microsoft et lance en 2000 dans "
                "le cadre de la plateforme .NET. C# a ete cree comme reponse de Microsoft a "
                "Java, combinant la puissance du C++ avec la simplicite de Visual Basic et "
                "la productivite de Java, tout en ajoutant des fonctionnalites innovantes. "
                "Le langage a evolue de maniere remarquable depuis sa creation, passant d'un "
                "langage principalement oriente objet a un langage multi-paradigme riche "
                "supportant la programmation fonctionnelle, generique, asynchrone, et "
                "reactive. C# est au coeur de l'ecosysteme .NET, qui a lui-meme evolue de "
                "maniere significative : de .NET Framework (Windows uniquement) a .NET Core "
                "(multi-plateforme) puis .NET 5+ (unifie). Cette transition a transforme C# "
                "d'un langage Windows-centrique en un langage veritablement multi-plateforme "
                "pour le web, le cloud, le mobile (via MAUI/Xamarin), les jeux (Unity), et "
                "les applications desktop. C# est reconnu pour son excellent outillage, "
                "son IDE de reference (Visual Studio), et son integration profonde avec "
                "l'ecosysteme Microsoft (Azure, SQL Server, Windows). Le langage est "
                "particulierement apprecie pour la programmation asynchrone avec async/await "
                "(C# l'a popularise avant la plupart des autres langages), LINQ (Language "
                "Integrated Query) pour la manipulation de collections, et les proprietes "
                "qui simplifient l'encapsulation. C# est l'un des langages les plus utilises "
                "au monde, dominant dans le developpement d'entreprise sur l'ecosysteme "
                "Microsoft et dans le developpement de jeux video via Unity."
            ),
            "history": (
                "L'histoire de C# est etroitement liee a celle de Microsoft et de la "
                "plateforme .NET. Au tournant du millenaire, Microsoft faisait face a Java "
                "de Sun Microsystems qui gagnait en popularite. Apres une tentative ratee de "
                "creer sa propre version de Java (J++, arretee suite a un proces de Sun), "
                "Microsoft a decide de creer un nouveau langage. Anders Hejlsberg, recrute "
                "de Borland ou il avait cree Turbo Pascal et Delphi, a dirige la conception "
                "de C#. Le langage a ete annonce en 2000 avec la plateforme .NET Framework. "
                "C# 1.0 (2002) offrait un langage oriente objet moderne. C# 2.0 (2005) a "
                "ajoute les generiques, les types nullable, les iterateurs, et les methodes "
                "anonymes. C# 3.0 (2007) a ete revolutionnaire avec LINQ, les expressions "
                "lambda, les types anonymes, et var (inference de type locale). C# 4.0 (2010) "
                "a introduit le typage dynamique (dynamic) et les parametres optionnels. "
                "C# 5.0 (2012) a lance async/await, un modele de programmation asynchrone "
                "qui a ensuite ete adopte par JavaScript, Python, Rust, et d'autres. C# 6.0 "
                "(2015) a commence l'ere Roslyn (le compilateur open source ecrit en C#) avec "
                "de nombreuses ameliorations syntaxiques. C# 7.0-7.3 (2017-2018) ont ajoute "
                "les tuples, le pattern matching, et les fonctions locales. La transition "
                "vers .NET Core (multi-plateforme et open source) a commence en 2016. C# 8.0 "
                "(2019) a introduit les nullable reference types, les interfaces avec "
                "implementation par defaut, et les async streams. C# 9.0 (2020) a ajoute "
                "les records et les init-only properties. C# 10-12 (2021-2023) ont continue "
                "a enrichir le langage avec les global usings, les primary constructors, "
                "et les collection expressions. L'open-sourcing de .NET et son unification "
                "sous .NET 5+ ont transforme la perception de C# comme un langage "
                "exclusivement Microsoft."
            ),
            "architecture": (
                "C# s'execute sur le Common Language Runtime (CLR), le runtime de la "
                "plateforme .NET. Le code source est compile en Common Intermediate Language "
                "(CIL, anciennement MSIL), un langage intermediaire independant de la "
                "plateforme, puis assemble dans des assemblies (.dll ou .exe). A l'execution, "
                "le compilateur JIT (Just-In-Time) RyuJIT compile le CIL en code machine natif "
                "optimise. Le CLR fournit la gestion automatique de la memoire via un ramasse-"
                "miettes generationnel (generation 0, 1, 2, et Large Object Heap) optimise "
                "pour differents scenarios. Le GC de .NET est hautement configurable avec "
                "plusieurs modes : Workstation GC (optimise pour la latence des applications "
                "desktop), Server GC (optimise pour le throughput des serveurs), et les "
                "configurations de concurrence. .NET propose egalement la compilation AOT "
                "(Ahead-Of-Time) via NativeAOT, qui compile directement en code machine "
                "natif, eliminant le besoin de JIT et reduisant le temps de demarrage. Le "
                "systeme de types de C# est unifie : tous les types heritent de System.Object, "
                "y compris les types valeur (struct) grace au boxing/unboxing. Les generiques "
                "en .NET sont reifiees (contrairement a Java), ce qui signifie que les "
                "informations de type sont preservees a l'execution. Le modele de concurrence "
                "de C# repose sur la Task Parallel Library (TPL) et async/await. Les taches "
                "(Task/Task<T>) representent des operations asynchrones, et le compilateur "
                "transforme les methodes async en machines a etats. Le systeme de types "
                "nullable reference types (C# 8+) permet d'eliminer la majorite des "
                "NullReferenceException a la compilation. LINQ fournit une syntaxe unifiee "
                "pour interroger des collections en memoire, des bases de donnees (via "
                "Entity Framework), et des documents XML, en utilisant des expressions "
                "lambda et le pattern d'expressions de requete."
            ),
            "pros_cons": {
                "pros": [
                    "Langage moderne et bien concu, en evolution constante",
                    "LINQ pour la manipulation de donnees puissante et expressive",
                    "Async/await natif et mature pour la programmation asynchrone",
                    "Ecosysteme .NET riche et multi-plateforme",
                    "Excellent IDE (Visual Studio) avec refactoring et debugging avances",
                    "Unity en fait le langage dominant du developpement de jeux",
                    "Nullable reference types pour reduire les erreurs null",
                    "Performance en amelioration constante (Span<T>, NativeAOT)"
                ],
                "cons": [
                    "Historiquement lie a l'ecosysteme Microsoft (moins vrai maintenant)",
                    "Moins populaire que Java dans les environnements non-Microsoft",
                    "Consommation memoire de la JVM .NET non negligeable",
                    "La complexite du langage augmente avec chaque version",
                    "Moins de bibliotheques tierces que Java ou JavaScript",
                    "L'heritage .NET Framework vs .NET Core peut preter a confusion",
                    "Le deploiement self-contained produit des executables volumineux",
                    "Courbe d'apprentissage pour les fonctionnalites avancees (Span, ref struct)"
                ]
            },
            "use_cases": (
                "C# est dominant dans le developpement de jeux video grace a Unity, le "
                "moteur de jeux le plus utilise au monde pour les jeux independants et "
                "mobiles. Des titres comme Hollow Knight, Cuphead, et Pokemon Go utilisent "
                "Unity et C#. Pour le developpement web backend, ASP.NET Core est un "
                "framework haute performance pour les APIs REST, les applications web MVC, "
                "et les services gRPC. Blazor permet de creer des interfaces web interactives "
                "en C# (compile en WebAssembly pour le mode client). Les applications "
                "d'entreprise sur l'ecosysteme Microsoft utilisent massivement C# : services "
                "Azure, integration avec Office 365, et applications de gestion interne. "
                "Le developpement d'applications desktop pour Windows utilise WPF (Windows "
                "Presentation Foundation), WinForms, et .NET MAUI (Multi-platform App UI) "
                "pour le multi-plateforme. Le developpement mobile multi-plateforme est "
                "possible avec .NET MAUI et Xamarin (son predecesseur). Les microservices "
                "et les architectures orientees evenements utilisent C# avec Azure Service "
                "Bus, MassTransit, et les fonctions Azure (serverless). Le traitement de "
                "donnees et l'ETL beneficient de LINQ et de bibliotheques comme ML.NET "
                "(machine learning par Microsoft). Les applications IoT peuvent etre "
                "developpees en C# avec .NET nanoFramework pour les microcontroleurs. "
                "L'automatisation de tests avec Selenium, SpecFlow, et NUnit est un cas "
                "d'utilisation courant. C# est egalement utilise pour les outils de "
                "developpement et les extensions Visual Studio."
            ),
            "ecosystem": (
                "L'ecosysteme C# est centre autour de la plateforme .NET et de NuGet, le "
                "gestionnaire de paquets officiel hebergeant plus de 350 000 paquets. Le SDK "
                ".NET fournit la CLI dotnet pour la creation de projets, la compilation, le "
                "test, et le deploiement. MSBuild est le systeme de build sous-jacent, "
                "configure via des fichiers .csproj en XML. Pour le developpement web, "
                "ASP.NET Core est le framework de reference, offrant MVC, Razor Pages, "
                "Blazor (SPA en C#), Minimal APIs, et SignalR (communication temps reel). "
                "Entity Framework Core est l'ORM principal, offrant du LINQ-to-SQL avec "
                "des migrations automatiques. Dapper est une alternative legere et performante. "
                "Pour les tests, xUnit est le framework recommande, NUnit et MSTest sont "
                "egalement populaires. Moq et NSubstitute sont les bibliotheques de mocking. "
                "FluentAssertions fournit des assertions expressives. Pour la validation, "
                "FluentValidation est la reference. Les bibliotheques de serialisation "
                "incluent System.Text.Json (integre) et Newtonsoft.Json (historique). "
                "MediatR implemente le pattern mediateur pour le CQRS. Polly fournit la "
                "resilience (retry, circuit breaker). AutoMapper simplifie le mapping "
                "entre objets. Pour le logging, Serilog est tres populaire, et Application "
                "Insights fournit le monitoring sur Azure. Les IDE incluent Visual Studio "
                "(le plus complet), Visual Studio Code avec l'extension C# Dev Kit, et "
                "JetBrains Rider (excellent IDE multi-plateforme). Pour le CI/CD, Azure "
                "DevOps et GitHub Actions offrent un excellent support .NET. BenchmarkDotNet "
                "est l'outil de benchmarking standard."
            ),
            "companies": [
                "Microsoft (Azure, Office, Windows, Teams, Visual Studio)",
                "Unity Technologies (moteur de jeux Unity)",
                "Stack Overflow (backend en C#/ASP.NET)",
                "Accenture (applications d'entreprise .NET)",
                "Epic Games (outils internes, Fortnite backend)",
                "GoDaddy (services d'hebergement web)",
                "Siemens (applications industrielles et IoT)"
            ],
            "code_example": (
                "using System;\n"
                "using System.Collections.Generic;\n"
                "using System.Linq;\n\n"
                "// Records pour les donnees immutables (C# 9+)\n"
                "record Produit(string Nom, decimal Prix, string Categorie);\n\n"
                "class Panier\n"
                "{\n"
                "    private readonly List<(Produit Produit, int Quantite)> _articles = new();\n\n"
                "    public void Ajouter(Produit produit, int quantite = 1)\n"
                "        => _articles.Add((produit, quantite));\n\n"
                "    // LINQ pour calculer le total\n"
                "    public decimal Total\n"
                "        => _articles.Sum(a => a.Produit.Prix * a.Quantite);\n\n"
                "    // Grouper par categorie avec LINQ\n"
                "    public IEnumerable<(string Categorie, decimal SousTotal)> ParCategorie()\n"
                "        => _articles\n"
                "            .GroupBy(a => a.Produit.Categorie)\n"
                "            .Select(g => (\n"
                "                Categorie: g.Key,\n"
                "                SousTotal: g.Sum(a => a.Produit.Prix * a.Quantite)\n"
                "            ));\n\n"
                "    // Pattern matching (C# 8+)\n"
                "    public string AppliquerRemise(decimal total) => total switch\n"
                "    {\n"
                '        >= 200m => $"Remise 20%: {total * 0.8m:C}",\n'
                '        >= 100m => $"Remise 10%: {total * 0.9m:C}",\n'
                '        >= 50m  => $"Remise 5%:  {total * 0.95m:C}",\n'
                '        _       => $"Pas de remise: {total:C}"\n'
                "    };\n"
                "}\n\n"
                "// Utilisation\n"
                "var panier = new Panier();\n"
                'panier.Ajouter(new Produit("Clavier", 79.99m, "Informatique"), 2);\n'
                'panier.Ajouter(new Produit("Souris", 49.99m, "Informatique"));\n'
                'panier.Ajouter(new Produit("Cafe", 12.50m, "Alimentaire"), 3);\n\n'
                'Console.WriteLine($"Total: {panier.Total:C}");\n'
                "foreach (var (cat, sousTotal) in panier.ParCategorie())\n"
                '    Console.WriteLine($"  {cat}: {sousTotal:C}");\n'
            ),
            "performance": {
                "startup_time": "Moyen (JIT) ou rapide (NativeAOT)",
                "throughput": "Eleve (JIT optimise, comparable a Java)",
                "memory": "Moyen (GC generationnel, Span<T> pour zero-alloc)",
                "concurrency_model": "async/await, Task Parallel Library, Channels, threads"
            },
            "learning_curve": "Moyenne",
            "community_size": "Grande",
            "job_market": "Fort (entreprise, jeux video, web)"
        },
        "traits": {
            "performance": 7,
            "developer_speed": 6,
            "learning_curve": 5,
            "ecosystem_size": 8,
            "type_safety": 8,
            "concurrency": 7,
            "memory_safety": 7,
            "scalability": 8
        }
    },

    # =========================================================================
    # 10. Swift
    # =========================================================================
    "swift": {
        "name": "Swift",
        "category": "language",
        "year_created": 2014,
        "creator": "Chris Lattner (Apple)",
        "paradigm": ["Oriente Objet", "Fonctionnel", "Oriente Protocole"],
        "typing": "Statique fort avec inference",
        "sections": {
            "overview": (
                "Swift est un langage de programmation moderne et puissant cree par Apple, "
                "principalement concu pour le developpement d'applications sur les plateformes "
                "Apple (iOS, macOS, watchOS, tvOS, visionOS). Lance en 2014 et open source "
                "depuis 2015, Swift a ete cree par Chris Lattner (egalement createur de LLVM) "
                "pour remplacer Objective-C, le langage historique d'Apple. Swift combine la "
                "puissance et les performances d'un langage compile avec la clarte syntaxique "
                "d'un langage de script moderne. Sa philosophie repose sur la securite par "
                "defaut : les optionnels (Optional) forcent le developpeur a gerer explicitement "
                "l'absence de valeur, les types valeur (structs) sont immutables par defaut, "
                "et le compilateur effectue de nombreuses verifications. Swift introduit le "
                "concept de 'Protocol-Oriented Programming' (POP), une approche de l'abstraction "
                "basee sur les protocoles (similaires aux interfaces mais avec des extensions "
                "de protocole fournissant des implementations par defaut). Ce paradigme est "
                "considere comme une alternative puissante a l'heritage de classes traditionnel. "
                "Swift utilise l'ARC (Automatic Reference Counting) pour la gestion de la "
                "memoire, une approche deterministe contrairement au garbage collection, qui "
                "elimine les pauses imprevisibles. Le langage evolue rapidement avec un "
                "processus de propositions ouvert (Swift Evolution). Les ajouts recents "
                "incluent la concurrence structuree avec async/await et les acteurs (Swift 5.5), "
                "les macros (Swift 5.9), et le support du ownership (Swift 5.9+). Bien que "
                "Swift soit principalement associe a Apple, il est de plus en plus utilise "
                "cote serveur (Vapor, Hummingbird) et sur d'autres plateformes."
            ),
            "history": (
                "L'histoire de Swift commence en 2010 lorsque Chris Lattner, ingenieur chez "
                "Apple et createur de l'infrastructure de compilation LLVM, a commence a "
                "travailler sur un nouveau langage de programmation. Le projet etait garde "
                "secret chez Apple, connu de tres peu de personnes en interne. Lattner voulait "
                "creer un langage qui combinerait la performance d'Objective-C avec la securite "
                "et l'expressivite des langages modernes, tout en tirant parti de l'infrastructure "
                "LLVM pour les optimisations. Swift a ete annonce de maniere spectaculaire a la "
                "WWDC 2014 (conference annuelle d'Apple), prenant la communaute des developpeurs "
                "completement par surprise. Apple a fourni un environnement interactif "
                "(Playground) dans Xcode, rendant l'apprentissage du langage immediat et "
                "ludique. Swift 1.0 a ete publie en septembre 2014 avec Xcode 6 et iOS 8. "
                "Swift 2.0 (2015) a apporte la gestion des erreurs avec try/catch, le guard "
                "statement, et les extensions de protocole. En decembre 2015, Apple a rendu "
                "Swift open source sous licence Apache 2.0, incluant le compilateur, la "
                "bibliotheque standard, et le package manager. Swift 3.0 (2016) a ete une "
                "refonte majeure de l'API (grand renommage) pour adopter les conventions "
                "de nommage Swift. Swift 4.0 (2017) a ajoute les Codable pour la "
                "serialisation et les chaines multi-lignes. Swift 5.0 (2019) a marque la "
                "stabilite de l'ABI, signifiant que les applications n'ont plus besoin "
                "d'embarquer le runtime Swift. Swift 5.5 (2021) a introduit la concurrence "
                "structuree (async/await, actors), le plus grand changement depuis la creation "
                "du langage. Swift 5.9 (2023) a ajoute les macros et les ownership features. "
                "Swift 6.0 (2024) a renforce la securite de la concurrence en rendant le "
                "Sendable checking strict par defaut."
            ),
            "architecture": (
                "Swift est un langage compile qui utilise LLVM comme backend de compilation, "
                "produisant du code machine natif optimise. Le compilateur Swift (swiftc) "
                "effectue une analyse de types sophistiquee et des optimisations agressives. "
                "Le processus de compilation inclut le parsing, la verification des types, "
                "la generation de SIL (Swift Intermediate Language, un IR de haut niveau "
                "specifique a Swift pour les optimisations), puis la generation de LLVM IR "
                "et finalement de code machine. SIL permet des optimisations specifiques a "
                "Swift comme l'elimination des retain/release inutiles (ARC optimization), "
                "la devirtualisation des appels de protocole, et la specialisation des "
                "generiques. Le systeme de gestion de la memoire de Swift est base sur l'ARC "
                "(Automatic Reference Counting). Chaque reference forte (strong reference) "
                "a un objet incremente un compteur, et chaque liberation le decremente. "
                "Quand le compteur atteint zero, l'objet est immediatement libere. Ce "
                "modele est deterministe (pas de pauses GC) mais peut creer des cycles "
                "de references que le developpeur doit casser manuellement avec des "
                "references faibles (weak) ou sans-propriete (unowned). Le systeme de "
                "types de Swift distingue les types valeur (struct, enum, tuple) et les "
                "types reference (class). Les types valeur sont copies lors de l'affectation "
                "(avec copy-on-write pour les collections), ce qui simplifie le raisonnement "
                "sur le code concurrent. Les protocoles avec extensions fournissent le "
                "polymorphisme et la reutilisation de code. Les generiques sont monomorphises "
                "quand possible (inline) ou utilisent le witness table pour le dispatch "
                "dynamique. Le modele de concurrence de Swift est base sur les acteurs "
                "(actor isolation) et la concurrence structuree (structured concurrency). "
                "Les acteurs garantissent qu'une seule tache accede a leurs donnees a la fois, "
                "et le compilateur verifie statiquement le respect de ces regles. Le systeme "
                "Sendable marque les types qui peuvent etre partages entre taches concurrentes."
            ),
            "pros_cons": {
                "pros": [
                    "Syntaxe moderne, expressive et agreable a ecrire",
                    "Securite par defaut (optionnels, types valeur, acteurs)",
                    "Performances proches du C grace a LLVM et aux optimisations",
                    "ARC pour une gestion deterministe de la memoire sans pause GC",
                    "Programmation orientee protocole puissante et flexible",
                    "Concurrence structuree avec acteurs et async/await",
                    "Excellent support IDE avec Xcode et autocompletion",
                    "Interoperabilite avec Objective-C et le C"
                ],
                "cons": [
                    "Ecosysteme tres lie a Apple et ses plateformes",
                    "Temps de compilation parfois longs pour les grands projets",
                    "Developpement cote serveur encore marginal par rapport a Java/Go/Python",
                    "Les cycles de references ARC necessitent une attention manuelle",
                    "Le langage evolue rapidement, ce qui peut casser du code existant",
                    "Moins de developpeurs disponibles en dehors de l'ecosysteme Apple",
                    "L'inference de types complexe peut produire des erreurs cryptiques",
                    "Le modele de concurrence strict peut etre complexe a maitriser"
                ]
            },
            "use_cases": (
                "Le cas d'utilisation principal de Swift est le developpement d'applications "
                "pour l'ecosysteme Apple. Les applications iOS, iPadOS, macOS, watchOS, "
                "tvOS, et visionOS (Vision Pro) sont principalement developpees en Swift. "
                "SwiftUI, le framework d'interface declaratif d'Apple (inspire de React et "
                "Flutter), utilise pleinement les fonctionnalites modernes de Swift : les "
                "property wrappers, les result builders, et les generiques avances. UIKit "
                "(framework imperatif plus ancien) est egalement largement utilise avec Swift. "
                "Les applications de realite augmentee (ARKit) et de realite virtuelle "
                "(visionOS/RealityKit) utilisent Swift comme langage principal. Le Machine "
                "Learning sur appareil est accessible via Core ML et Create ML en Swift. "
                "Le developpement cote serveur avec Swift est en croissance, avec des "
                "frameworks comme Vapor (le plus populaire) et Hummingbird offrant des "
                "performances competitives. Swift cote serveur tire parti des memes "
                "fonctionnalites de concurrence (acteurs, async/await) que cote client. "
                "Le developpement d'outils en ligne de commande et de scripts est facilite "
                "par Swift Package Manager et les capabilities systeme de Swift. Le "
                "developpement de frameworks et de bibliotheques pour l'ecosysteme Apple "
                "est presque exclusivement en Swift desormais. La programmation systeme "
                "commence a etre exploree avec Swift, grace aux fonctionnalites d'ownership "
                "et au support embedded (Swift for embedded systems). Les tests automatises "
                "d'applications iOS avec XCTest et les nouveaux Swift Testing framework "
                "utilisent naturellement Swift."
            ),
            "ecosystem": (
                "L'ecosysteme Swift est centre autour des outils Apple et de Swift Package "
                "Manager (SPM), le gestionnaire de paquets officiel. SPM est integre "
                "directement dans Xcode et la ligne de commande swift, offrant la gestion "
                "des dependances, la compilation, et les tests. Le Swift Package Index "
                "(swiftpackageindex.com) reference les paquets disponibles. Xcode est l'IDE "
                "principal et quasi obligatoire pour le developpement Apple, offrant un "
                "editeur de code, un debogueur, un Interface Builder, des instruments de "
                "profiling, et des simulateurs. Pour le developpement UI, SwiftUI est le "
                "framework declaratif moderne d'Apple, tandis que UIKit (iOS) et AppKit "
                "(macOS) sont les frameworks imperatifs plus anciens mais toujours tres "
                "utilises. Combine est le framework reactif d'Apple pour la programmation "
                "reactive. Les frameworks natifs d'Apple sont vastes : Foundation (types "
                "de base), CoreData/SwiftData (persistance), CloudKit (synchronisation "
                "cloud), AVFoundation (multimedia), CoreImage (traitement d'images), et "
                "Metal (GPU). Pour le developpement serveur, Vapor est le framework le plus "
                "populaire, offrant un routage, un ORM (Fluent), et un support WebSocket. "
                "Hummingbird est une alternative plus legere. AsyncHTTPClient et SwiftNIO "
                "fournissent les couches reseau bas niveau. Pour les tests, XCTest est le "
                "framework historique, et Swift Testing (introduit en 2024) est le nouveau "
                "framework moderne. Quick/Nimble offrent des tests de style BDD. Les outils "
                "de linting incluent SwiftLint (le plus populaire) et SwiftFormat. Les "
                "IDE alternatifs incluent VS Code avec l'extension Swift et AppCode "
                "(JetBrains, bien que discontinue). Fastlane est l'outil de reference pour "
                "l'automatisation des builds et du deploiement sur l'App Store."
            ),
            "companies": [
                "Apple (iOS, macOS, tous les produits Apple)",
                "Airbnb (application iOS)",
                "Uber (application iOS, Rider et Driver)",
                "LinkedIn (application iOS)",
                "Lyft (application iOS)",
                "Spotify (application iOS)",
                "Revolut (application bancaire iOS)"
            ],
            "code_example": (
                "import Foundation\n\n"
                "// Protocole avec extension par defaut\n"
                "protocol Descriptible {\n"
                "    var description: String { get }\n"
                "}\n\n"
                "// Enum avec valeurs associees (type algebrique)\n"
                "enum Resultat<T> {\n"
                "    case succes(T)\n"
                "    case erreur(String)\n\n"
                "    func map<U>(_ transform: (T) -> U) -> Resultat<U> {\n"
                "        switch self {\n"
                "        case .succes(let valeur):\n"
                "            return .succes(transform(valeur))\n"
                "        case .erreur(let message):\n"
                "            return .erreur(message)\n"
                "        }\n"
                "    }\n"
                "}\n\n"
                "// Struct avec protocole\n"
                "struct Etudiant: Descriptible {\n"
                "    let nom: String\n"
                "    let notes: [Double]\n\n"
                "    var moyenne: Double? {\n"
                "        guard !notes.isEmpty else { return nil }\n"
                "        return notes.reduce(0, +) / Double(notes.count)\n"
                "    }\n\n"
                "    var description: String {\n"
                "        let moy = moyenne.map { String(format: \"%.2f\", $0) } ?? \"N/A\"\n"
                '        return "\\(nom) - Moyenne: \\(moy)"\n'
                "    }\n"
                "}\n\n"
                "// Fonction generique avec contrainte de protocole\n"
                "func afficher<T: Descriptible>(_ elements: [T]) {\n"
                "    elements.forEach { print($0.description) }\n"
                "}\n\n"
                "// Exemple async/await\n"
                "func chargerNotes(pour nom: String) async -> Resultat<[Double]> {\n"
                "    // Simulation d'un chargement asynchrone\n"
                "    try? await Task.sleep(nanoseconds: 100_000_000)\n"
                "    return .succes([15.5, 14.0, 16.5])\n"
                "}\n\n"
                "let etudiants = [\n"
                '    Etudiant(nom: "Alice", notes: [15.5, 14.0, 16.5]),\n'
                '    Etudiant(nom: "Bob", notes: [8.0, 9.5, 7.0]),\n'
                '    Etudiant(nom: "Claire", notes: [18.0, 17.5, 19.0]),\n'
                "]\n\n"
                "afficher(etudiants)\n"
                "let admis = etudiants.filter { ($0.moyenne ?? 0) >= 10.0 }\n"
                'print("Admis: \\(admis.map(\\.nom))")\n'
            ),
            "performance": {
                "startup_time": "Rapide (compilation native)",
                "throughput": "Eleve (optimisations LLVM agressives)",
                "memory": "Faible-Moyen (ARC, pas de GC)",
                "concurrency_model": "Acteurs, async/await, concurrence structuree, GCD (Grand Central Dispatch)"
            },
            "learning_curve": "Moyenne",
            "community_size": "Grande (ecosysteme Apple)",
            "job_market": "Fort (developpement iOS/macOS, tres demande)"
        },
        "traits": {
            "performance": 8,
            "developer_speed": 6,
            "learning_curve": 5,
            "ecosystem_size": 6,
            "type_safety": 9,
            "concurrency": 7,
            "memory_safety": 8,
            "scalability": 7
        }
    },

    # =========================================================================
    # 11. Kotlin
    # =========================================================================
    "kotlin": {
        "name": "Kotlin",
        "category": "language",
        "year_created": 2011,
        "creator": "JetBrains",
        "paradigm": ["Oriente Objet", "Fonctionnel", "Imperatif"],
        "typing": "Statique fort avec inference",
        "sections": {
            "overview": (
                "Kotlin est un langage de programmation moderne developpe par JetBrains "
                "(l'entreprise derriere IntelliJ IDEA, Android Studio, et d'autres IDE). "
                "Annonce en 2011 et publie en version 1.0 en 2016, Kotlin a ete concu comme "
                "une alternative pragmatique a Java, corrigeant ses defauts historiques tout "
                "en maintenant une interoperabilite totale avec l'ecosysteme Java et la JVM. "
                "En 2017, Google a officiellement annonce le support de Kotlin pour le "
                "developpement Android, et en 2019, Kotlin est devenu le langage recommande "
                "par Google pour Android, un tournant decisif pour son adoption. La philosophie "
                "de Kotlin repose sur la concision, la securite, et la pragmatisme. Le langage "
                "elimine la verbosity excessive de Java tout en ajoutant des fonctionnalites "
                "modernes : null safety integree au systeme de types, data classes, sealed "
                "classes, coroutines pour la programmation asynchrone, extensions functions, "
                "et smart casts. Kotlin est un langage multi-paradigme qui combine la "
                "programmation orientee objet et la programmation fonctionnelle de maniere "
                "fluide. L'une des forces majeures de Kotlin est sa portabilite : il peut "
                "cibler la JVM (Kotlin/JVM), JavaScript (Kotlin/JS), le code natif "
                "(Kotlin/Native via LLVM), et le WebAssembly. Kotlin Multiplatform (KMP) "
                "permet de partager du code entre les plateformes tout en gardant le code "
                "specifique a chaque plateforme. Kotlin est utilise pour le developpement "
                "Android, le backend serveur (avec Spring Boot ou Ktor), et de plus en "
                "plus pour le multiplateforme."
            ),
            "history": (
                "L'histoire de Kotlin commence chez JetBrains en 2010. L'equipe, qui "
                "travaillait quotidiennement avec Java pour developper ses IDE, etait frustree "
                "par les limitations de Java et cherchait un langage plus productif tout en "
                "restant compatible avec la JVM. Apres avoir evalue Scala (juge trop complexe "
                "et avec des temps de compilation trop longs) et d'autres alternatives, "
                "JetBrains a decide de creer son propre langage. Le projet a ete annonce "
                "en juillet 2011, et le nom Kotlin vient de l'ile Kotlin dans le golfe de "
                "Finlande, pres de Saint-Petersbourg ou JetBrains a un bureau. Le "
                "developpement a ete rendu open source des le debut sous licence Apache 2.0. "
                "Kotlin 1.0 est sorti en fevrier 2016 avec la promesse de retrocompatibilite "
                "binaire pour les futures versions. L'evenement decisif a ete la Google I/O "
                "2017, ou Google a annonce le support officiel de Kotlin pour le developpement "
                "Android, aux cotes de Java. L'adoption a explose : en deux ans, plus de 50% "
                "des developpeurs Android professionnels utilisaient Kotlin. A la Google I/O "
                "2019, Google a annonce que Kotlin etait desormais le langage recommande "
                "(Kotlin-first) pour le developpement Android. Kotlin 1.3 (2018) a stabilise "
                "les coroutines, une fonctionnalite fondamentale pour la programmation "
                "asynchrone. Kotlin 1.4 (2020) a ameliore les performances du compilateur "
                "et l'interoperabilite. Kotlin 1.5-1.7 ont affine le langage avec les value "
                "classes, les sealed interfaces, et les ameliorations du compilateur. Kotlin "
                "1.8-1.9 ont ameliore Kotlin Multiplatform et le nouveau compilateur K2. "
                "Kotlin 2.0 (2024) a marque la stabilisation du compilateur K2, offrant des "
                "performances de compilation nettement superieures. Kotlin Multiplatform "
                "(KMP) est devenu stable, permettant le partage de code entre Android, "
                "iOS, desktop, web, et serveur."
            ),
            "architecture": (
                "Kotlin est un langage compile qui peut cibler plusieurs plateformes. Sur "
                "la JVM (le cas d'utilisation le plus courant), le compilateur Kotlin "
                "produit du bytecode Java standard compatible avec la JVM. Cela signifie "
                "que le code Kotlin peut utiliser toutes les bibliotheques Java existantes "
                "et vice versa, sans couche d'abstraction ni surcout de performance. Le "
                "nouveau compilateur K2 (stabilise en Kotlin 2.0) a ete reecrit de zero "
                "pour des performances de compilation jusqu'a 2x plus rapides et une "
                "meilleure architecture extensible. Kotlin/JS compile vers JavaScript, "
                "permettant le developpement web frontend et l'utilisation de bibliotheques "
                "JavaScript. Kotlin/Native utilise LLVM pour compiler directement en code "
                "machine natif, sans JVM, pour les plateformes comme iOS (avec Kotlin "
                "Multiplatform), Linux, Windows, et macOS. Kotlin/Native utilise un "
                "ramasse-miettes automatique (pas l'ARC). Le systeme de types de Kotlin "
                "est plus avance que celui de Java : la null safety est integree au "
                "systeme de types (types nullable T? vs non-nullable T), les smart casts "
                "permettent au compilateur de caster automatiquement les types apres une "
                "verification, les sealed classes/interfaces permettent les hierarchies "
                "de types fermees avec pattern matching exhaustif, et les data classes "
                "generent automatiquement equals, hashCode, toString, et copy. Les "
                "coroutines de Kotlin sont un mecanisme de concurrence cooperatif "
                "implemente via la transformation CPS (Continuation-Passing Style) a la "
                "compilation. Contrairement aux threads, les coroutines sont legeres et "
                "peuvent etre suspendues et reprises sans bloquer de thread. Les flows "
                "(fournissant des streams asynchrones reactifs) et les channels (pour la "
                "communication entre coroutines) completent le modele de concurrence. "
                "Le scope des coroutines (CoroutineScope) fournit la concurrence structuree, "
                "garantissant que les coroutines enfants sont annulees si le parent est "
                "annule."
            ),
            "pros_cons": {
                "pros": [
                    "Null safety integree au systeme de types (elimine les NPE)",
                    "Interoperabilite parfaite avec Java et l'ecosysteme JVM",
                    "Syntaxe concise et expressive (data classes, extensions, smart casts)",
                    "Coroutines pour une programmation asynchrone elegante",
                    "Kotlin Multiplatform pour le partage de code cross-platform",
                    "Langage recommande par Google pour Android",
                    "Excellent support IDE (JetBrains est le createur du langage et des IDE)",
                    "Progressif : adoption facile dans les projets Java existants"
                ],
                "cons": [
                    "Temps de compilation plus lents que Java (en amelioration avec K2)",
                    "La communaute est plus petite que celle de Java",
                    "Certaines fonctionnalites peuvent produire du code difficile a debugger",
                    "Kotlin/Native est moins mature que Kotlin/JVM",
                    "La surcharge d'operateurs peut reduire la lisibilite si mal utilisee",
                    "Les conventions et best practices sont encore en evolution",
                    "Le multiplatform ajoute de la complexite au projet",
                    "La migration de Java vers Kotlin demande un effort d'apprentissage"
                ]
            },
            "use_cases": (
                "Le developpement d'applications Android est le cas d'utilisation principal "
                "de Kotlin. Google recommande Kotlin comme premier langage pour Android, et "
                "les nouvelles API Android (Jetpack Compose pour l'UI declarative, les "
                "Android Architecture Components) sont concues Kotlin-first. La majorite "
                "des applications Android populaires utilisent Kotlin. Le backend serveur est "
                "le second cas d'utilisation majeur. Kotlin s'integre parfaitement avec "
                "Spring Boot (le framework Java le plus populaire), et Ktor (de JetBrains) "
                "est un framework 100% Kotlin pour les serveurs web et les microservices. "
                "Les coroutines de Kotlin sont particulierement adaptees aux services "
                "backend asynchrones. Kotlin Multiplatform (KMP) permet de partager la "
                "logique metier entre Android et iOS, reducisant la duplication de code. "
                "Compose Multiplatform (de JetBrains) etend le framework declaratif "
                "Jetpack Compose a iOS, desktop (Windows, macOS, Linux), et le web. Le "
                "scripting et l'automatisation sont possibles avec les scripts Kotlin "
                "(.kts) et le Kotlin REPL. Gradle utilise Kotlin DSL (build.gradle.kts) "
                "comme alternative au Groovy pour les scripts de build. Le developpement "
                "web frontend est possible via Kotlin/JS et les wrappers React Kotlin. "
                "Le traitement de donnees et le data engineering beneficient des coroutines "
                "et de l'integration avec les bibliotheques Big Data Java. Les tests "
                "automatises utilisent des frameworks Kotlin comme Kotest, MockK, et "
                "les extensions Kotlin pour JUnit. Les DSL (Domain-Specific Languages) "
                "sont un point fort de Kotlin, grace a sa syntaxe flexible (lambdas "
                "avec recepteur, extensions functions)."
            ),
            "ecosystem": (
                "L'ecosysteme Kotlin beneficie directement de l'immense ecosysteme Java "
                "sur la JVM. Toutes les bibliotheques Java sont utilisables en Kotlin sans "
                "modification. Le gestionnaire de dependances principal est Gradle (avec "
                "le DSL Kotlin de plus en plus utilise) ou Maven. Pour le developpement "
                "Android, Jetpack Compose est le framework d'UI declaratif moderne, "
                "remplacant progressivement les layouts XML. Les Android Architecture "
                "Components (ViewModel, LiveData/StateFlow, Room, Navigation) sont les "
                "briques de base. Pour le backend, Spring Boot avec Kotlin offre une "
                "experience first-class grace aux extensions Kotlin, au support des "
                "coroutines, et a la configuration DSL. Ktor est le framework backend "
                "100% Kotlin de JetBrains, leger et base sur les coroutines. Exposed "
                "(JetBrains) est un framework SQL type-safe pour Kotlin. Pour la "
                "serialisation, kotlinx.serialization est la bibliotheque officielle, "
                "offrant la serialisation multi-format (JSON, Protobuf, CBOR) avec un "
                "plugin compilateur. Les coroutines sont fournies par kotlinx.coroutines, "
                "incluant les Flows pour les streams reactifs, les Channels, et les scopes "
                "structures. Pour les tests, Kotest (anciennement KotlinTest) offre des "
                "tests de style BDD, data-driven, et property-based. MockK est la "
                "bibliotheque de mocking idiomatique pour Kotlin. Pour le multiplateforme, "
                "Kotlin Multiplatform fournit les mecanismes expect/actual pour les "
                "implementations specifiques a chaque plateforme. Compose Multiplatform "
                "etend Jetpack Compose au desktop, iOS, et web. Les IDE principaux sont "
                "IntelliJ IDEA et Android Studio (tous deux de JetBrains), offrant le "
                "meilleur support Kotlin possible. Le Kotlin Playground en ligne permet "
                "d'experimenter sans installation."
            ),
            "companies": [
                "Google (Android, services internes)",
                "JetBrains (tous les IDE, services cloud)",
                "Netflix (applications Android, microservices)",
                "Uber (application Android)",
                "Pinterest (migration de Java vers Kotlin pour Android)",
                "Trello/Atlassian (applications mobiles)",
                "Coursera (application Android)"
            ],
            "code_example": (
                "import kotlinx.coroutines.*\n"
                "import kotlinx.coroutines.flow.*\n\n"
                "// Data class avec null safety\n"
                "data class Etudiant(\n"
                "    val nom: String,\n"
                "    val age: Int,\n"
                "    val notes: List<Double>\n"
                ") {\n"
                "    val moyenne: Double?\n"
                "        get() = notes.takeIf { it.isNotEmpty() }?.average()\n\n"
                "    fun estAdmis(seuil: Double = 10.0): Boolean =\n"
                "        moyenne?.let { it >= seuil } ?: false\n"
                "}\n\n"
                "// Extension function\n"
                "fun List<Etudiant>.palmares(): List<Etudiant> =\n"
                "    filter { it.estAdmis() }\n"
                "        .sortedByDescending { it.moyenne }\n\n"
                "// Sealed class pour les resultats\n"
                "sealed class Resultat<out T> {\n"
                "    data class Succes<T>(val donnees: T) : Resultat<T>()\n"
                "    data class Erreur(val message: String) : Resultat<Nothing>()\n"
                "}\n\n"
                "// Coroutine avec Flow\n"
                "fun chargerNotes(): Flow<Etudiant> = flow {\n"
                "    val etudiants = listOf(\n"
                '        Etudiant("Alice", 21, listOf(15.5, 14.0, 16.5)),\n'
                '        Etudiant("Bob", 22, listOf(8.0, 9.5, 7.0)),\n'
                '        Etudiant("Claire", 20, listOf(18.0, 17.5, 19.0)),\n'
                "    )\n"
                "    etudiants.forEach {\n"
                "        delay(100) // Simulation de chargement\n"
                "        emit(it)\n"
                "    }\n"
                "}\n\n"
                "fun main() = runBlocking {\n"
                "    chargerNotes()\n"
                "        .filter { it.estAdmis() }\n"
                "        .collect { etudiant ->\n"
                '            println("${etudiant.nom}: ${etudiant.moyenne?.let { "%.2f".format(it) }}")\n'
                "        }\n"
                "}\n"
            ),
            "performance": {
                "startup_time": "Moyen (JVM) ou rapide (Kotlin/Native)",
                "throughput": "Eleve (identique a Java sur la JVM)",
                "memory": "Moyen (JVM overhead, identique a Java)",
                "concurrency_model": "Coroutines (concurrence structuree), Flows, Channels, threads JVM"
            },
            "learning_curve": "Moyenne (plus facile si Java est connu)",
            "community_size": "Grande (en forte croissance)",
            "job_market": "Fort (Android surtout, backend en croissance)"
        },
        "traits": {
            "performance": 7,
            "developer_speed": 7,
            "learning_curve": 4,
            "ecosystem_size": 7,
            "type_safety": 8,
            "concurrency": 7,
            "memory_safety": 7,
            "scalability": 8
        }
    },

    # =========================================================================
    # 12. Ruby
    # =========================================================================
    "ruby": {
        "name": "Ruby",
        "category": "language",
        "year_created": 1995,
        "creator": "Yukihiro 'Matz' Matsumoto",
        "paradigm": ["Oriente Objet", "Fonctionnel", "Imperatif"],
        "typing": "Dynamique fort (duck typing)",
        "sections": {
            "overview": (
                "Ruby est un langage de programmation dynamique concu pour la productivite "
                "et le plaisir du developpeur. Cree par Yukihiro 'Matz' Matsumoto au Japon "
                "et publie en 1995, Ruby a ete concu avec une philosophie humaniste : le "
                "langage doit etre agreable a utiliser et minimiser le stress du developpeur. "
                "Matz a declare que Ruby etait 'optimise pour le bonheur du programmeur'. "
                "En Ruby, tout est un objet, y compris les nombres, les booleens, et meme "
                "nil. Cette coherence du modele objet rend le langage intuitif et elegant. "
                "Ruby est surtout connu grace a Ruby on Rails, le framework web cree par "
                "David Heinemeier Hansson (DHH) en 2004, qui a revolutionne le developpement "
                "web en introduisant les concepts de 'Convention over Configuration' et "
                "'Don't Repeat Yourself' (DRY). Rails a prouve qu'il etait possible de "
                "developper des applications web complexes extremement rapidement, inspirant "
                "des frameworks similaires dans d'autres langages (Django pour Python, "
                "Laravel pour PHP, etc.). La syntaxe de Ruby est remarquablement expressive "
                "et lisible, souvent comparee a de l'anglais naturel. Les blocs, les "
                "iterateurs, et les methodes chainables permettent d'ecrire du code concis "
                "et elegant. Ruby excelle dans la creation de DSL (Domain-Specific Languages) "
                "grace a sa syntaxe flexible et ses capacites de metaprogrammation. Le langage "
                "permet de modifier les classes existantes a l'execution (monkey patching), "
                "d'intercepter les appels de methodes inexistantes (method_missing), et de "
                "generer du code dynamiquement. Bien que Ruby soit plus lent que les langages "
                "compiles, la productivite de developpement qu'il offre en fait un choix "
                "excellent pour les startups et les projets ou le time-to-market est crucial."
            ),
            "history": (
                "L'histoire de Ruby commence en 1993, lorsque Yukihiro Matsumoto, programme "
                "ur japonais, a commence a concevoir un langage de programmation orientee objet "
                "qui combinerait les meilleurs aspects de ses langages preferes : Perl "
                "(manipulation de texte), Smalltalk (modele objet pur), Eiffel (design by "
                "contract), Ada (fiabilite), et Lisp (programmation fonctionnelle). La "
                "premiere version publique, Ruby 0.95, a ete publiee en decembre 1995 au "
                "Japon. Ruby est reste relativement confidentiel en dehors du Japon pendant "
                "ses premieres annees. La traduction du livre 'Programming Ruby' (le 'Pickaxe "
                "book') en anglais en 2000 a commence a attirer l'attention internationale. "
                "Mais c'est l'emergence de Ruby on Rails en 2004-2005 qui a propulse Ruby "
                "sur la scene mondiale. DHH a cree Rails en extrayant le framework du projet "
                "Basecamp, et sa demonstration de creation d'un blog en 15 minutes a fait "
                "sensation. Twitter, GitHub, Shopify, et Airbnb dans leurs premieres versions "
                "etaient tous construits avec Rails. Ruby 1.8 (2003) a ete la version la "
                "plus longtemps utilisee. Ruby 1.9 (2007) a apporte des ameliorations de "
                "performances significatives avec la machine virtuelle YARV (Yet Another "
                "Ruby VM) et le support natif d'Unicode. Ruby 2.0 (2013) a marque le "
                "20eme anniversaire avec les keyword arguments, les lazy enumerators, et "
                "les refinements. Les versions 2.x successives ont continue a ameliorer les "
                "performances et a ajouter des fonctionnalites. Ruby 3.0 (2020), surnomme "
                "'Ruby 3x3', visait a etre trois fois plus rapide que Ruby 2.0. Il a "
                "introduit Ractor (concurrence basee sur les acteurs), le scheduler de "
                "fibers pour la concurrence cooperative, et RBS (Ruby Signature) pour les "
                "signatures de types. Ruby 3.2-3.3 ont continue les ameliorations de "
                "performance avec YJIT (un compilateur JIT ecrit en Rust), qui offre des "
                "gains significatifs pour les applications Rails."
            ),
            "architecture": (
                "Ruby est un langage interprete qui utilise la machine virtuelle YARV (Yet "
                "Another Ruby VM, integree dans CRuby/MRI depuis Ruby 1.9). Le code source "
                "est parse en un AST (Abstract Syntax Tree), puis compile en bytecode YARV, "
                "qui est ensuite interprete. Depuis Ruby 3.1, YJIT (Yet Another JIT, un "
                "compilateur JIT ecrit en Rust) est inclus et offre des ameliorations de "
                "performance de 15 a 30% pour les applications Rails typiques. CRuby (MRI, "
                "l'implementation de reference de Matz) utilise un ramasse-miettes "
                "generationnel avec compactage (depuis Ruby 2.7). JRuby est une "
                "implementation sur la JVM offrant de meilleures performances de threading "
                "et l'acces a l'ecosysteme Java. TruffleRuby (Oracle) utilise GraalVM pour "
                "des performances proches du C pour certains workloads. Le modele objet de "
                "Ruby est l'un des plus purs de tous les langages : absolument tout est un "
                "objet. Les entiers, les flottants, les booleens, nil, et meme les classes "
                "sont des objets. Chaque objet possede une 'eigenclass' (singleton class) "
                "qui permet de definir des methodes specifiques a une instance. Les modules "
                "servent a la fois de mecanisme de namespace et de mixins (heritage multiple "
                "partiel). La metaprogrammation est une capacite fondamentale de Ruby : "
                "define_method, method_missing, class_eval, instance_eval, et les hooks "
                "(included, inherited, method_added) permettent de generer du code "
                "dynamiquement. Le modele de concurrence de Ruby a longtemps ete limite "
                "par le GVL (Global VM Lock, equivalent du GIL de Python). Ruby 3.0 a "
                "introduit les Ractors, des unites d'execution paralleles qui ne partagent "
                "pas d'etat mutable, offrant un veritable parallelisme. Le scheduler de "
                "fibers permet la concurrence cooperative sans threads OS. Les blocs et "
                "les Proc/Lambda sont des closures qui sont au coeur de l'idiomatique Ruby, "
                "utilises partout pour les iterateurs, les callbacks, et les DSL."
            ),
            "pros_cons": {
                "pros": [
                    "Syntaxe extremement elegante et lisible, optimisee pour le bonheur",
                    "Ruby on Rails pour un developpement web ultra rapide",
                    "Modele objet pur et coherent (tout est un objet)",
                    "Metaprogrammation puissante pour les DSL et les abstractions",
                    "Convention over Configuration reduit la configuration necessaire",
                    "Communaute accueillante et bienveillante",
                    "Excellent pour le prototypage rapide et les startups",
                    "Ecosysteme de gems riche et bien documente"
                ],
                "cons": [
                    "Performances significativement inferieures aux langages compiles",
                    "GVL limitant le parallelisme (en amelioration avec Ractors)",
                    "Popularite en declin relatif par rapport a son apogee (2008-2015)",
                    "Consommation memoire elevee",
                    "La metaprogrammation excessive peut rendre le code difficile a comprendre",
                    "Typage dynamique pouvant masquer des erreurs",
                    "Moins de postes disponibles que Python, JavaScript, ou Java",
                    "Le monkey patching peut creer des bugs difficiles a debugger"
                ]
            },
            "use_cases": (
                "Le cas d'utilisation principal de Ruby est le developpement d'applications "
                "web avec Ruby on Rails. Rails reste l'un des frameworks web les plus "
                "productifs, excellent pour les applications CRUD, les SaaS, les marketplaces, "
                "et les MVPs (Minimum Viable Products). Des entreprises majeures comme "
                "Shopify, GitHub, Basecamp, Airbnb (initialement), et GitLab utilisent Rails "
                "en production a grande echelle. Le prototypage rapide et les startups early-"
                "stage beneficient de la productivite de Rails pour valider rapidement une "
                "idee avec un produit fonctionnel. Les API backend (Rails API mode, Grape) "
                "sont un cas d'utilisation courant. Le scripting et l'automatisation sont "
                "des forces de Ruby, avec des outils comme Rake (equivalent de Make), et "
                "des gems pour diverses taches d'automatisation. L'infrastructure as code "
                "utilise Ruby avec Chef (configuration management) et Vagrant (gestion "
                "d'environnements de developpement). Le testing et le BDD (Behavior-Driven "
                "Development) sont un domaine ou Ruby excelle avec RSpec, Cucumber, et "
                "Capybara. Les tests d'acceptance et les tests end-to-end sont souvent ecrits "
                "en Ruby meme pour des projets dans d'autres langages. La creation de DSL "
                "(Domain-Specific Languages) est une specialite de Ruby : Gemfile (Bundler), "
                "Rakefile (Rake), Vagrantfile (Vagrant), Podfile (CocoaPods), et Fastfile "
                "(Fastlane) sont tous des DSL Ruby. Les sites de contenu et les blogs avec "
                "Jekyll (generateur de sites statiques, utilise par GitHub Pages) et les "
                "systemes de commerce electronique (Solidus, Spree) sont egalement des cas "
                "d'utilisation importants. Le web scraping avec Mechanize et Nokogiri est "
                "courant dans l'ecosysteme Ruby."
            ),
            "ecosystem": (
                "L'ecosysteme Ruby est organise autour de RubyGems (le gestionnaire de "
                "paquets, les paquets sont appeles 'gems') et de Bundler (le gestionnaire "
                "de dependances de projets). RubyGems.org heberge plus de 170 000 gems. "
                "Ruby on Rails est le coeur de l'ecosysteme web, offrant un framework MVC "
                "complet avec ActiveRecord (ORM), ActionView (templates), ActionController "
                "(routage et controleurs), ActionMailer (emails), ActiveJob (taches en "
                "arriere-plan), et ActionCable (WebSockets). En dehors de Rails, Sinatra "
                "est un micro-framework minimaliste, et Hanami est une alternative plus "
                "moderne. Pour les tests, RSpec est le framework BDD dominant, Minitest "
                "est le framework inclus dans la bibliotheque standard, Capybara est "
                "utilise pour les tests d'integration web, et FactoryBot pour la creation "
                "de donnees de test. Pour les taches en arriere-plan, Sidekiq (base sur "
                "Redis) est le standard, et Resque est une alternative. Pour la serialisation "
                "JSON, Oj et MultiJSON sont populaires. Les serveurs web incluent Puma (le "
                "plus utilise, multi-threade), Unicorn, et Falcon (async). Pour le linting, "
                "RuboCop est l'outil de reference, offrant un formatage et une analyse "
                "statique configurables. Sorbet (de Stripe) ajoute un systeme de types "
                "graduel a Ruby, et RBS est le format officiel de signatures de types. "
                "Les IDE incluent RubyMine (JetBrains), VS Code avec Solargraph ou Ruby "
                "LSP, et Vim/Neovim avec des plugins. IRB et Pry sont les REPL interactifs. "
                "Pour le deploiement, Capistrano est l'outil classique, et Docker/Kubernetes "
                "sont de plus en plus utilises. Heroku a historiquement ete tres lie a "
                "l'ecosysteme Ruby."
            ),
            "companies": [
                "Shopify (plateforme e-commerce, Rails a grande echelle)",
                "GitHub (backend Rails, plus grande app Rails au monde)",
                "Basecamp (createurs de Rails)",
                "GitLab (plateforme DevOps, Rails)",
                "Airbnb (initialement tout Rails, encore utilise)",
                "Stripe (Sorbet, outils internes Ruby)",
                "Twitch (anciennement Justin.tv, Rails a l'origine)"
            ],
            "code_example": (
                "# Systeme de gestion de bibliotheque en Ruby idiomatique\n\n"
                "class Livre\n"
                "  attr_reader :titre, :auteur, :annee, :genre\n\n"
                "  def initialize(titre:, auteur:, annee:, genre:)\n"
                "    @titre = titre\n"
                "    @auteur = auteur\n"
                "    @annee = annee\n"
                "    @genre = genre\n"
                "  end\n\n"
                "  def to_s\n"
                '    "#{titre} par #{auteur} (#{annee})"\n'
                "  end\n"
                "end\n\n"
                "class Bibliotheque\n"
                "  include Enumerable\n\n"
                "  def initialize\n"
                "    @livres = []\n"
                "  end\n\n"
                "  def <<(livre)\n"
                "    @livres << livre\n"
                "    self\n"
                "  end\n\n"
                "  def each(&block)\n"
                "    @livres.each(&block)\n"
                "  end\n\n"
                "  def par_genre\n"
                "    group_by(&:genre).transform_values { |livres| livres.map(&:titre) }\n"
                "  end\n\n"
                "  def rechercher(critere)\n"
                "    select { |livre| livre.titre.downcase.include?(critere.downcase) }\n"
                "  end\n"
                "end\n\n"
                "# Utilisation\n"
                "bib = Bibliotheque.new\n"
                'bib << Livre.new(titre: "Le Petit Prince", auteur: "Saint-Exupery",\n'
                '                 annee: 1943, genre: "Conte")\n'
                'bib << Livre.new(titre: "Dune", auteur: "Frank Herbert",\n'
                '                 annee: 1965, genre: "Science-Fiction")\n'
                'bib << Livre.new(titre: "Neuromancien", auteur: "William Gibson",\n'
                '                 annee: 1984, genre: "Science-Fiction")\n\n'
                'puts "=== Par genre ==="\n'
                "bib.par_genre.each do |genre, titres|\n"
                '  puts "#{genre}: #{titres.join(", ")}"\n'
                "end\n\n"
                'puts "\\n=== Livres avant 1970 ==="\n'
                "bib.select { |l| l.annee < 1970 }.each { |l| puts l }\n"
            ),
            "performance": {
                "startup_time": "Moyen-Lent",
                "throughput": "Faible (en amelioration avec YJIT)",
                "memory": "Eleve",
                "concurrency_model": "Ractors (Ruby 3+), Fibers, Threads (limites par le GVL)"
            },
            "learning_curve": "Faible",
            "community_size": "Moyenne (loyale et active)",
            "job_market": "Moyen (Rails reste demande, niche mais bien paye)"
        },
        "traits": {
            "performance": 3,
            "developer_speed": 9,
            "learning_curve": 3,
            "ecosystem_size": 7,
            "type_safety": 3,
            "concurrency": 3,
            "memory_safety": 5,
            "scalability": 5
        }
    },

    # =========================================================================
    # 13. PHP
    # =========================================================================
    "php": {
        "name": "PHP",
        "category": "language",
        "year_created": 1995,
        "creator": "Rasmus Lerdorf",
        "paradigm": ["Oriente Objet", "Procedural", "Fonctionnel"],
        "typing": "Dynamique (typage strict optionnel depuis PHP 7)",
        "sections": {
            "overview": (
                "PHP (PHP: Hypertext Preprocessor) est un langage de scripting cote serveur "
                "concu a l'origine pour le developpement web. Cree par Rasmus Lerdorf en 1995, "
                "PHP est devenu le langage le plus utilise sur le web, alimentant environ 77% "
                "de tous les sites web dont le langage serveur est connu (grace en grande "
                "partie a WordPress, qui represente plus de 40% des sites web). PHP a souffert "
                "d'une mauvaise reputation pendant des annees en raison de son design initial "
                "inconsistant, de ses failles de securite frequentes, et de la qualite variable "
                "du code ecrit en PHP. Cependant, le PHP moderne (7.x et 8.x) est un langage "
                "radicalement different : performances considerablement ameliorees (PHP 7 est "
                "deux fois plus rapide que PHP 5), systeme de types optionnel strict, classes "
                "et interfaces modernes, enumerations, fibers pour la concurrence cooperative, "
                "et des fonctionnalites de programmation fonctionnelle. Le framework Laravel "
                "a largement contribue a la rehabilitation de PHP, offrant une experience de "
                "developpement elegante et moderne comparable a Ruby on Rails. PHP reste le "
                "choix le plus pragmatique pour le developpement web grace a son deploiement "
                "trivial (presque tous les hebergeurs web supportent PHP), son ecosysteme "
                "de CMS mature (WordPress, Drupal, Joomla), et sa courbe d'apprentissage "
                "faible. Les frameworks modernes comme Laravel, Symfony, et les outils comme "
                "Composer ont transforme l'ecosysteme PHP en un environnement de developpement "
                "professionnel et structure. PHP est un langage pragmatique qui privilegie "
                "la facilite de deploiement et la rapidite de developpement web, et malgre "
                "ses detracteurs, il reste un pilier fondamental du web."
            ),
            "history": (
                "L'histoire de PHP est celle d'un outil personnel devenu l'un des langages "
                "les plus utilises au monde. En 1994, Rasmus Lerdorf a cree un ensemble de "
                "scripts CGI en C pour suivre les visiteurs de son CV en ligne. Il les a "
                "appeles 'Personal Home Page Tools'. En 1995, il a publie le code source "
                "de PHP/FI (Forms Interpreter), permettant a d'autres de l'utiliser et de "
                "le modifier. PHP 3.0 (1998) a ete la premiere version a ressembler au PHP "
                "moderne, reecrite par Andi Gutmans et Zeev Suraski (qui ont ensuite fonde "
                "Zend Technologies). PHP 4.0 (2000) a introduit le moteur Zend Engine, "
                "ameliorant significativement les performances. PHP 5.0 (2004) a ete une "
                "revolution avec un modele objet completement redesigne : classes, interfaces, "
                "heritage, visibilite, et exceptions. PHP 5.3 (2009) a ajoute les namespaces, "
                "les closures, et les late static bindings. Le developpement de PHP 6 (qui "
                "devait ajouter le support natif d'Unicode) a ete abandonne apres des annees "
                "d'efforts infructueux. PHP 7.0 (2015) a ete un bond en avant spectaculaire : "
                "performances doublees grace au nouveau moteur Zend Engine 3.0, types de "
                "retour, declarations de types scalaires, et l'operateur null coalescing (??). "
                "PHP 7.4 a ajoute les proprietes typees et les arrow functions. PHP 8.0 (2020) "
                "a introduit le compilateur JIT, les named arguments, les union types, les "
                "match expressions, et les attributs. PHP 8.1 a ajoute les enumerations, les "
                "fibers (pour la programmation asynchrone), les types intersection, et les "
                "readonly properties. PHP 8.2 a apporte les readonly classes et les "
                "Disjunctive Normal Form types. PHP 8.3 a ameliore le typage et les "
                "performances. PHP continue d'evoluer vers un langage de plus en plus type "
                "et moderne, tout en maintenant sa facilite d'utilisation legendaire."
            ),
            "architecture": (
                "PHP est un langage interprete qui utilise le Zend Engine comme moteur "
                "d'execution. Le code source PHP est parse en un AST, compile en opcodes "
                "(bytecode interne), puis execute par la VM Zend. OPcache, une extension "
                "incluse par defaut depuis PHP 5.5, met en cache les opcodes compiles en "
                "memoire partagee, evitant la recompilation a chaque requete et ameliorant "
                "significativement les performances. PHP 8.0 a ajoute un compilateur JIT "
                "(basé sur DynASM) qui compile les opcodes les plus frequents en code machine "
                "natif, offrant des ameliorations de performance pour les workloads CPU-"
                "intensifs. Le modele d'execution traditionnel de PHP est 'shared-nothing' : "
                "chaque requete HTTP demarre un processus (ou un thread) PHP frais, sans "
                "etat partage avec les autres requetes. Ce modele simplifie enormement le "
                "developpement (pas de fuites de memoire cumulatives, pas de gestion de "
                "concurrence) mais limite les performances pour les applications avec "
                "beaucoup de connexions simultanees. PHP-FPM (FastCGI Process Manager) est "
                "le gestionnaire de processus standard, gerant un pool de workers PHP. "
                "Des solutions modernes comme Swoole, OpenSwoole, et FrankenPHP (base sur "
                "Go) offrent des serveurs PHP persistants avec des coroutines, du WebSocket, "
                "et des performances tres superieures au modele traditionnel. RoadRunner "
                "(ecrit en Go) est une alternative populaire. Le systeme de types de PHP "
                "a evolue considerablement : PHP 7+ supporte les declarations de types "
                "pour les parametres, les retours, et les proprietes, avec un mode strict "
                "optionnel (declare(strict_types=1)). PHP 8.0+ ajoute les union types, les "
                "types intersection (8.1), et les Disjunctive Normal Form types (8.2). La "
                "gestion de la memoire utilise un compteur de references avec un ramasse-"
                "miettes cyclique pour detecter les references circulaires. Le modele de "
                "concurrence avec les fibers (PHP 8.1) permet la programmation asynchrone "
                "cooperative au sein d'un processus."
            ),
            "pros_cons": {
                "pros": [
                    "Deploiement extremement simple (presque tous les hebergeurs supportent PHP)",
                    "Courbe d'apprentissage faible, ideal pour les debutants en web",
                    "Ecosysteme web mature (WordPress, Laravel, Symfony)",
                    "Documentation officielle excellente et complete",
                    "PHP moderne (8.x) est rapide, type, et expressif",
                    "Laravel offre une experience de developpement de premier ordre",
                    "Composer a standardise la gestion des dependances",
                    "Enorme base de code existante et communaute active"
                ],
                "cons": [
                    "Reputation historique de langage inconsistant et peu securise",
                    "API standard incoherente (ordre des parametres, nommage)",
                    "Le modele shared-nothing limite la concurrence native",
                    "Moins adapte aux applications non-web que les langages generaux",
                    "La coexistence de PHP procedurale ancien et PHP moderne cree de la confusion",
                    "Le typage optionnel signifie que beaucoup de code reste non type",
                    "Performances inferieures a Node.js ou Go pour les requetes concurrentes",
                    "Moins d'offres d'emploi haut de gamme que Java, Python, ou Go"
                ]
            },
            "use_cases": (
                "Le cas d'utilisation dominant de PHP est le developpement web cote serveur. "
                "WordPress, le CMS le plus utilise au monde (alimentant plus de 40% des sites "
                "web), est ecrit en PHP, creant un ecosysteme massif de themes et de plugins. "
                "Drupal et Joomla sont d'autres CMS PHP majeurs. Les frameworks web modernes "
                "representent l'autre facette de PHP : Laravel est le framework PHP le plus "
                "populaire, offrant une architecture MVC elegante, un ORM puissant (Eloquent), "
                "un systeme de queues, et un ecosysteme riche (Forge, Vapor, Nova). Symfony "
                "est le framework d'entreprise de reference, modulaire et extensible, avec "
                "des composants reutilisables utilises meme en dehors de Symfony (y compris "
                "par Laravel et Drupal). Le commerce electronique est un domaine majeur : "
                "Magento/Adobe Commerce, WooCommerce (plugin WordPress), et PrestaShop sont "
                "tous en PHP. Les SaaS et les applications metier utilisent PHP avec Laravel "
                "ou Symfony pour leur backend. Les API REST et GraphQL sont bien supportees "
                "avec des outils comme API Platform (Symfony) et Lighthouse (Laravel). Les "
                "microservices sont possibles avec des frameworks legers comme Slim, Lumen "
                "(Laravel), ou des outils comme Swoole pour le PHP asynchrone. Le legacy "
                "code PHP est omnipresent dans l'industrie, creant une demande constante de "
                "maintenance et de modernisation. Les applications de gestion interne, les "
                "intranets, et les back-offices sont des cas d'utilisation classiques de PHP "
                "dans les entreprises."
            ),
            "ecosystem": (
                "L'ecosysteme PHP a ete transforme par Composer, le gestionnaire de "
                "dependances qui a standardise la gestion des paquets. Packagist.org est "
                "le registre central des paquets Composer avec plus de 350 000 paquets. "
                "L'autoloading PSR-4 a unifie le chargement des classes. Les standards PSR "
                "(PHP-FIG) ont harmonise les pratiques : PSR-7 (messages HTTP), PSR-12 "
                "(style de code), PSR-14 (event dispatching), PSR-15 (middleware HTTP). "
                "Les frameworks web dominants sont Laravel (le plus populaire, ecosysteme "
                "riche avec Forge, Vapor, Nova, Livewire, Inertia), Symfony (entreprise, "
                "composants reutilisables), et CodeIgniter (leger). Pour les ORM, Eloquent "
                "(Laravel) et Doctrine (Symfony) sont les references. Pour les tests, PHPUnit "
                "est le framework standard, Pest est une alternative moderne au style expressif, "
                "et Mockery est utilise pour le mocking. Les outils d'analyse statique ont "
                "revolutionne la qualite du code PHP : PHPStan et Psalm (de Vimeo) detectent "
                "les erreurs de types, les bugs potentiels, et encouragent le typage strict. "
                "Laravel Pint et PHP CS Fixer formatent le code. Pour les serveurs, PHP-FPM "
                "est le standard, et Swoole/FrankenPHP offrent des performances superieures "
                "avec le PHP persistant. Xdebug est l'outil de debugging standard, et "
                "Blackfire.io (par les createurs de Symfony) est l'outil de profiling de "
                "reference. Les IDE principaux sont PhpStorm (JetBrains, le meilleur IDE "
                "PHP) et VS Code avec Intelephense. Pour le deploiement, Laravel Forge et "
                "Vapor (serverless sur AWS Lambda) simplifient le deploiement. Envoy et "
                "Deployer sont des outils de deploiement generiques pour PHP."
            ),
            "companies": [
                "Meta (Facebook a ete ecrit en PHP, puis Hack)",
                "WordPress.com/Automattic (WordPress, WooCommerce)",
                "Shopify (anciennement, base sur PHP a l'origine)",
                "Wikipedia (MediaWiki est en PHP)",
                "Slack (backend initialement en PHP)",
                "Mailchimp (backend PHP)",
                "Etsy (marketplace, PHP et HHVM)"
            ],
            "code_example": (
                "<?php\n\n"
                "declare(strict_types=1);\n\n"
                "// Enum (PHP 8.1+)\n"
                "enum Statut: string\n"
                "{\n"
                "    case EnCours = 'en_cours';\n"
                "    case Terminee = 'terminee';\n"
                "    case Annulee = 'annulee';\n"
                "}\n\n"
                "// Classe readonly (PHP 8.2+)\n"
                "readonly class Tache\n"
                "{\n"
                "    public function __construct(\n"
                "        public string $titre,\n"
                "        public Statut $statut = Statut::EnCours,\n"
                "        public int $priorite = 0,\n"
                "    ) {}\n"
                "}\n\n"
                "class GestionnaireTaches\n"
                "{\n"
                "    /** @var Tache[] */\n"
                "    private array $taches = [];\n\n"
                "    public function ajouter(Tache $tache): self\n"
                "    {\n"
                "        $this->taches[] = $tache;\n"
                "        return $this;\n"
                "    }\n\n"
                "    /** @return Tache[] */\n"
                "    public function filtrerParStatut(Statut $statut): array\n"
                "    {\n"
                "        return array_filter(\n"
                "            $this->taches,\n"
                "            fn(Tache $t) => $t->statut === $statut\n"
                "        );\n"
                "    }\n\n"
                "    public function resume(): string\n"
                "    {\n"
                "        $compteurs = [];\n"
                "        foreach (Statut::cases() as $statut) {\n"
                "            $compteurs[$statut->value] = count($this->filtrerParStatut($statut));\n"
                "        }\n\n"
                "        return implode(', ', array_map(\n"
                '            fn(string $k, int $v) => "$k: $v",\n'
                "            array_keys($compteurs),\n"
                "            array_values($compteurs)\n"
                "        ));\n"
                "    }\n"
                "}\n\n"
                "// Utilisation avec named arguments (PHP 8.0+)\n"
                "$gestionnaire = new GestionnaireTaches();\n"
                "$gestionnaire\n"
                "    ->ajouter(new Tache(titre: 'Ecrire les tests', priorite: 2))\n"
                "    ->ajouter(new Tache(titre: 'Deployer', statut: Statut::Terminee))\n"
                "    ->ajouter(new Tache(titre: 'Code review', priorite: 1));\n\n"
                "echo $gestionnaire->resume();\n"
            ),
            "performance": {
                "startup_time": "Rapide (avec OPcache)",
                "throughput": "Moyen (PHP 8 avec JIT ameliore)",
                "memory": "Moyen (shared-nothing, pas de leak cumulative)",
                "concurrency_model": "PHP-FPM (processus), Fibers (8.1+), Swoole (coroutines)"
            },
            "learning_curve": "Faible",
            "community_size": "Tres grande (la plus grande pour le web)",
            "job_market": "Fort (WordPress, Laravel, maintenance legacy)"
        },
        "traits": {
            "performance": 4,
            "developer_speed": 7,
            "learning_curve": 3,
            "ecosystem_size": 7,
            "type_safety": 4,
            "concurrency": 3,
            "memory_safety": 5,
            "scalability": 6
        }
    },

    # =========================================================================
    # 14. Elixir
    # =========================================================================
    "elixir": {
        "name": "Elixir",
        "category": "language",
        "year_created": 2011,
        "creator": "Jose Valim",
        "paradigm": ["Fonctionnel", "Concurrent", "Oriente Processus"],
        "typing": "Dynamique fort",
        "sections": {
            "overview": (
                "Elixir est un langage de programmation fonctionnel concu pour construire "
                "des systemes distribues, tolerants aux pannes, et capables de gerer une "
                "concurrence massive. Cree par Jose Valim (ancien contributeur majeur de "
                "Ruby on Rails) en 2011, Elixir s'execute sur la BEAM, la machine virtuelle "
                "d'Erlang, heritant ainsi de plus de 35 ans d'expertise en systemes distribues "
                "et en telecommunications. La BEAM a ete concue par Ericsson pour les systemes "
                "de telephone commutes, ou les exigences de disponibilite sont de 99.9999999% "
                "(neuf 9), soit moins d'une seconde d'interruption par an. Elixir apporte a "
                "la BEAM une syntaxe moderne et agreable (inspiree de Ruby), des macros "
                "puissantes pour la metaprogrammation, un ecosysteme d'outils modernes (Mix, "
                "Hex, ExUnit), et le protocole Protocol pour le polymorphisme ad hoc. Le "
                "modele de concurrence d'Elixir est base sur le modele d'acteurs : chaque "
                "processus BEAM est une unite d'execution legere et isolee, communiquant par "
                "passage de messages. Des millions de processus peuvent coexister sur une "
                "seule machine, chacun avec sa propre memoire et son propre ramasse-miettes. "
                "Si un processus echoue, il est automatiquement redemarree par un superviseur, "
                "suivant la philosophie 'let it crash' (laissez-le planter). Cette approche "
                "rend les systemes Elixir naturellement resiliants et auto-reparants. Elixir "
                "est un langage purement fonctionnel : les donnees sont immutables, les "
                "fonctions sont des citoyens de premiere classe, et le pattern matching est "
                "omnipresent. Phoenix, le framework web d'Elixir, offre des performances "
                "exceptionnelles (capable de gerer des millions de connexions WebSocket "
                "simultanees sur un seul serveur) et une experience de developpement agreable "
                "avec LiveView pour les interfaces reactives en temps reel sans JavaScript."
            ),
            "history": (
                "L'histoire d'Elixir commence avec Jose Valim, un developpeur bresilien "
                "qui etait l'un des contributeurs les plus prolifiques de Ruby on Rails. "
                "Frustre par les limitations de Ruby en matiere de concurrence et de "
                "performance, Valim a commence a explorer d'autres plateformes. Il a "
                "decouvert Erlang et la BEAM, et a ete impressionne par la robustesse et "
                "le modele de concurrence, mais trouvait la syntaxe d'Erlang austere et "
                "l'ecosysteme d'outils moins moderne. En 2011, il a commence a creer "
                "Elixir, un nouveau langage sur la BEAM qui combinerait la puissance de "
                "la plateforme Erlang avec une syntaxe moderne et des outils de "
                "developpement de premier ordre. La premiere version publique d'Elixir a "
                "ete publiee en 2012, et la version 1.0 est sortie en septembre 2014. "
                "Le framework Phoenix, cree par Chris McCord, a ete lance en 2014 et a "
                "rapidement prouve les capacites d'Elixir pour le developpement web haute "
                "performance. La demonstration legendaire de Phoenix Channels gerant 2 "
                "millions de connexions WebSocket simultanees sur un seul serveur a fait "
                "sensation. Phoenix LiveView (2019) a revolutionne le developpement "
                "d'interfaces utilisateur en permettant de creer des UIs riches et "
                "reactives en temps reel sans ecrire de JavaScript, en utilisant les "
                "WebSockets et le rendu cote serveur. Elixir 1.9+ a stabilise les releases "
                "et les Configuration. Les versions recentes ont ameliore les performances, "
                "le systeme de types (travaux sur le set-theoretic type system), et l'experience "
                "de developpement. L'ecosysteme Elixir continue de croitre avec des projets "
                "comme Nerves (IoT et embarque), Nx (calcul numerique et machine learning), "
                "et Livebook (notebooks interactifs). L'adoption par des entreprises comme "
                "Discord, Pinterest, PepsiCo, et Bleacher Report a demontre la viabilite "
                "d'Elixir pour des systemes de production a grande echelle."
            ),
            "architecture": (
                "Elixir s'execute sur la BEAM (Bogdan/Bjorn's Erlang Abstract Machine), la "
                "machine virtuelle d'Erlang. La BEAM est probablement le runtime le mieux "
                "concu au monde pour la concurrence massive et la tolerance aux pannes. Le "
                "code Elixir est compile en bytecode BEAM (.beam), et peut interoperer "
                "directement avec le code Erlang sans surcout. Le modele de concurrence "
                "de la BEAM est base sur le modele d'acteurs. Les processus BEAM (a ne "
                "pas confondre avec les processus OS) sont extremement legers (environ 2 Ko "
                "de memoire chacun) et completement isoles les uns des autres : chaque "
                "processus a sa propre pile, son propre tas, et son propre ramasse-miettes. "
                "La communication entre processus se fait exclusivement par passage de "
                "messages asynchrones. Le scheduler de la BEAM distribue les processus "
                "sur tous les coeurs CPU disponibles (un scheduler par coeur), offrant du "
                "parallelisme reel sans que le developpeur n'ait a s'en soucier. Les "
                "superviseurs forment des arbres de supervision qui surveillent les processus "
                "enfants et les redemarrent selon des strategies predefinies (one_for_one, "
                "one_for_all, rest_for_one). Cette architecture permet la 'programmation "
                "defensive minimale' : au lieu de gerer tous les cas d'erreur possibles, "
                "le code laisse le processus planter et le superviseur le redemarrer dans "
                "un etat propre. Le hot code reloading permet de mettre a jour le code "
                "en production sans arreter le systeme, une fonctionnalite heritee d'Erlang "
                "et des systemes de telecommunications. GenServer (Generic Server) est "
                "l'abstraction de base pour les processus avec etat, encapsulant les "
                "patterns communs de reception de messages, de gestion d'etat, et de "
                "callbacks. Les ETS (Erlang Term Storage) fournissent des tables en memoire "
                "partagee pour le stockage haute performance. Mnesia est la base de donnees "
                "distribuee integree. Les macros d'Elixir (hygienic macros) permettent "
                "de transformer l'AST a la compilation, offrant une metaprogrammation "
                "puissante utilisee extensivement par le framework lui-meme."
            ),
            "pros_cons": {
                "pros": [
                    "Concurrence massive et naturelle via le modele d'acteurs BEAM",
                    "Tolerance aux pannes integree (superviseurs, 'let it crash')",
                    "Scalabilite horizontale et verticale exceptionnelle",
                    "Phoenix LiveView pour des UIs temps reel sans JavaScript",
                    "Syntaxe agreable et moderne inspiree de Ruby",
                    "Pattern matching puissant et omnipresent",
                    "Hot code reloading pour les mises a jour sans interruption",
                    "Immutabilite par defaut eliminant de nombreuses categories de bugs"
                ],
                "cons": [
                    "Ecosysteme plus petit que Python, JavaScript, ou Java",
                    "Marche de l'emploi plus restreint (niche mais en croissance)",
                    "Courbe d'apprentissage pour le paradigme fonctionnel et OTP",
                    "Performances brutes du calcul CPU inferieures a Go ou Rust",
                    "Typage dynamique limitant la detection d'erreurs a la compilation",
                    "Moins de bibliotheques tierces necessitant parfois d'utiliser des libs Erlang",
                    "Le modele fonctionnel pur peut derouter les developpeurs OOP",
                    "Deploiement plus complexe que PHP ou des langages plus mainstream"
                ]
            },
            "use_cases": (
                "Elixir excelle dans les applications necessitant une concurrence massive "
                "et une haute disponibilite. Les applications temps reel sont le domaine de "
                "predilection d'Elixir : chat en direct, notifications push, tableaux de bord "
                "en temps reel, et jeux multijoueur. Discord utilise Elixir pour son "
                "infrastructure de messagerie, gerant des millions d'utilisateurs simultanes. "
                "Phoenix LiveView permet de creer des applications web interactives et "
                "reactives en temps reel sans ecrire de JavaScript client, en utilisant les "
                "WebSockets pour synchroniser l'etat entre le serveur et le navigateur. Les "
                "systemes distribues et les microservices beneficient naturellement de la "
                "BEAM : distribution native entre noeuds, tolerance aux pannes, et "
                "communication entre processus transparente. Les APIs et les services web "
                "haute performance sont un cas d'utilisation courant avec Phoenix, qui offre "
                "des latences de reponse extremement faibles et une capacite de gestion de "
                "connexions simultanees exceptionnelle. L'IoT et les systemes embarques sont "
                "supportes par Nerves, un framework qui permet de deployer des applications "
                "Elixir sur du materiel embarque (Raspberry Pi et autres). Le machine "
                "learning et le calcul numerique emergent avec Nx (Numerical Elixir) et "
                "Livebook (notebooks interactifs, similaires a Jupyter). Les systemes de "
                "streaming de donnees et les pipelines d'evenements utilisent GenStage et "
                "Broadway pour le traitement de messages a haut debit. Les systemes de "
                "telecommunications, le domaine d'origine d'Erlang/BEAM, restent un cas "
                "d'utilisation naturel. Les plateformes SaaS avec des exigences de temps "
                "reel et de haute disponibilite sont de plus en plus construites avec Elixir."
            ),
            "ecosystem": (
                "L'ecosysteme Elixir est organise autour d'outils integres et bien concus. "
                "Mix est l'outil de build et de gestion de projet, fournissant la creation "
                "de projets, la compilation, les tests, et les releases dans un seul outil. "
                "Hex est le gestionnaire de paquets (equivalent de npm/pip), avec hex.pm "
                "comme registre central hebergeant plus de 15 000 paquets. ExUnit est le "
                "framework de test integre, simple et puissant, avec le support des doctests "
                "(tests dans la documentation). Phoenix est le framework web de reference, "
                "offrant un MVC, des WebSockets (Channels), LiveView (UIs reactives sans JS), "
                "et PubSub. Ecto est la bibliotheque d'acces aux donnees et le DSL de "
                "requetes, similaire a un ORM mais fonctionnel, avec des changesets pour "
                "la validation et le casting des donnees. Pour les taches en arriere-plan, "
                "Oban (base sur PostgreSQL) est le standard, offrant des queues de travail "
                "fiables et observables. GenStage et Broadway fournissent des abstractions "
                "pour le traitement de donnees en streaming avec back-pressure. Nerves "
                "permet le developpement IoT et embarque en Elixir. Nx (Numerical Elixir) "
                "et Explorer fournissent le calcul numerique et l'analyse de donnees, avec "
                "Bumblebee pour l'inference de modeles de machine learning. Livebook est un "
                "environnement de notebook interactif pour l'exploration de code et de donnees. "
                "Pour la documentation, ExDoc genere une documentation HTML de qualite "
                "exceptionnelle a partir des commentaires @doc. Credo est l'outil d'analyse "
                "statique et de style de code. Dialyzer (herite d'Erlang) fournit une "
                "analyse de types statique optionnelle. Les IDE principaux sont VS Code avec "
                "ElixirLS (serveur de langage) et les editeurs avec support LSP. IEx est le "
                "REPL interactif puissant, avec l'inspection de processus en direct."
            ),
            "companies": [
                "Discord (infrastructure de messagerie temps reel)",
                "Pinterest (systemes backend haute performance)",
                "PepsiCo (plateforme e-commerce)",
                "Bleacher Report (streaming de contenu sportif temps reel)",
                "Brex (services financiers)",
                "Dockyard (consultancy Elixir, contributeur de LiveView)",
                "Remote.com (plateforme RH globale)"
            ],
            "code_example": (
                "defmodule Universite do\n"
                "  @moduledoc \"\"\"\n"
                "  Module de gestion des etudiants et de leurs notes.\n"
                "  \"\"\"\n\n"
                "  defmodule Etudiant do\n"
                "    @enforce_keys [:nom, :notes]\n"
                "    defstruct [:nom, :age, notes: []]\n\n"
                "    @type t :: %__MODULE__{\n"
                "      nom: String.t(),\n"
                "      age: non_neg_integer() | nil,\n"
                "      notes: [float()]\n"
                "    }\n"
                "  end\n\n"
                "  @spec moyenne(%Etudiant{}) :: {:ok, float()} | :aucune_note\n"
                "  def moyenne(%Etudiant{notes: []}) do\n"
                "    :aucune_note\n"
                "  end\n\n"
                "  def moyenne(%Etudiant{notes: notes}) do\n"
                "    {:ok, Enum.sum(notes) / length(notes)}\n"
                "  end\n\n"
                "  @spec admis?(%Etudiant{}, float()) :: boolean()\n"
                "  def admis?(etudiant, seuil \\\\ 10.0) do\n"
                "    case moyenne(etudiant) do\n"
                "      {:ok, moy} -> moy >= seuil\n"
                "      :aucune_note -> false\n"
                "    end\n"
                "  end\n\n"
                "  @spec palmares([%Etudiant{}]) :: [%Etudiant{}]\n"
                "  def palmares(etudiants) do\n"
                "    etudiants\n"
                "    |> Enum.filter(&admis?/1)\n"
                "    |> Enum.sort_by(fn e ->\n"
                "      case moyenne(e) do\n"
                "        {:ok, moy} -> -moy\n"
                "        _ -> 0\n"
                "      end\n"
                "    end)\n"
                "  end\n"
                "end\n\n"
                "# Utilisation avec le pipe operator\n"
                "etudiants = [\n"
                '  %Universite.Etudiant{nom: "Alice", age: 21, notes: [15.5, 14.0, 16.5]},\n'
                '  %Universite.Etudiant{nom: "Bob", age: 22, notes: [8.0, 9.5, 7.0]},\n'
                '  %Universite.Etudiant{nom: "Claire", age: 20, notes: [18.0, 17.5, 19.0]},\n'
                "]\n\n"
                "etudiants\n"
                "|> Universite.palmares()\n"
                "|> Enum.each(fn e ->\n"
                "  {:ok, moy} = Universite.moyenne(e)\n"
                '  IO.puts("#{e.nom}: #{Float.round(moy, 2)}")\n'
                "end)\n"
            ),
            "performance": {
                "startup_time": "Moyen (demarrage BEAM)",
                "throughput": "Eleve pour I/O concurrent, moyen pour CPU pur",
                "memory": "Moyen (processus legers mais overhead par processus)",
                "concurrency_model": "Processus BEAM (acteurs), GenServer, Task, Agent, supervision trees"
            },
            "learning_curve": "Moyenne a elevee (paradigme fonctionnel, OTP)",
            "community_size": "Petite-Moyenne (en croissance, tres engagee)",
            "job_market": "Niche mais en croissance (postes bien remuneres)"
        },
        "traits": {
            "performance": 6,
            "developer_speed": 6,
            "learning_curve": 6,
            "ecosystem_size": 5,
            "type_safety": 6,
            "concurrency": 10,
            "memory_safety": 7,
            "scalability": 10
        }
    },
}
