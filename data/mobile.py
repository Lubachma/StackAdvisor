"""
Donnees sur les frameworks de developpement mobile.
Chaque entree documente un framework avec son histoire, son architecture,
ses cas d'usage et ses caracteristiques techniques.
"""

TECHNOLOGIES = {
    "react_native": {
        "name": "React Native",
        "category": "mobile",
        "year_created": 2015,
        "creator": "Facebook",
        "paradigm": ["declaratif", "composants", "reactif", "fonctionnel"],
        "typing": "dynamique (JavaScript) / statique optionnel (TypeScript)",
        "sections": {
            "overview": (
                "React Native est un framework open source cree par Facebook permettant\n"
                "de developper des applications mobiles natives en utilisant JavaScript\n"
                "et React. Contrairement aux solutions hybrides classiques comme Cordova,\n"
                "React Native ne s'appuie pas sur une WebView : il traduit les composants\n"
                "React en widgets natifs reels de la plateforme cible (UIKit sur iOS,\n"
                "Android Views sur Android). Cette approche offre un compromis interessant\n"
                "entre la productivite du developpement web et les performances d'une\n"
                "application native.\n\n"
                "Le principe fondamental de React Native repose sur le concept de 'learn\n"
                "once, write anywhere' plutot que 'write once, run anywhere'. Cela signifie\n"
                "que les developpeurs utilisent les memes concepts React mais adaptent\n"
                "certaines parties du code a chaque plateforme quand c'est necessaire.\n"
                "Le framework fournit un ensemble de composants de base (View, Text,\n"
                "Image, ScrollView, etc.) qui s'adaptent automatiquement a la plateforme.\n\n"
                "React Native utilise un pont (bridge) asynchrone pour communiquer entre\n"
                "le thread JavaScript et le thread natif. Depuis 2022, la nouvelle\n"
                "architecture (Fabric et TurboModules) remplace ce pont par une interface\n"
                "synchrone basee sur JSI (JavaScript Interface), ameliorant\n"
                "considerablement les performances et reduisant la latence des appels\n"
                "entre les couches JavaScript et native."
            ),
            "history": (
                "L'histoire de React Native commence en 2013, lors d'un hackathon interne\n"
                "chez Facebook. A cette epoque, Facebook avait deja tente l'approche HTML5\n"
                "pour son application mobile, une decision que Mark Zuckerberg qualifia\n"
                "plus tard de 'plus grande erreur strategique de l'entreprise'. Face a ce\n"
                "constat, l'equipe cherchait un moyen de combiner la rapidite du\n"
                "developpement web avec les performances natives.\n\n"
                "Jordan Walke, le createur de React, a presente un prototype qui permettait\n"
                "de generer des elements d'interface natifs iOS a partir de code JavaScript.\n"
                "Ce prototype a immediatement suscite l'interet de la direction.\n\n"
                "En janvier 2015, Facebook a presente React Native lors de la React.js\n"
                "Conference. La version iOS a ete publiee en mars 2015 en open source,\n"
                "suivie de la version Android en septembre de la meme annee. L'adoption\n"
                "a ete fulgurante : en quelques mois, des milliers de developpeurs\n"
                "contribuaient au projet.\n\n"
                "Entre 2016 et 2020, React Native a connu une croissance massive, adopte\n"
                "par des entreprises majeures comme Airbnb, Uber Eats, Discord et\n"
                "Instagram. Cependant, certaines entreprises comme Airbnb ont fini par\n"
                "abandonner React Native en 2018, citant des problemes de maintenance\n"
                "et de performances dans les cas complexes.\n\n"
                "En 2022, Meta a lance la nouvelle architecture de React Native,\n"
                "comprenant Fabric (nouveau systeme de rendu), TurboModules (nouveau\n"
                "systeme de modules natifs) et le moteur JavaScript Hermes, devenu\n"
                "le moteur par defaut. Cette refonte majeure adresse de nombreuses\n"
                "limitations historiques du framework."
            ),
            "architecture": (
                "L'architecture de React Native repose sur plusieurs couches distinctes\n"
                "qui cooperent pour transformer du code JavaScript en interfaces natives.\n\n"
                "Couche JavaScript : C'est la ou reside la logique applicative. Le code\n"
                "React est execute dans un moteur JavaScript (Hermes par defaut depuis\n"
                "React Native 0.70). Le Virtual DOM de React gere la reconciliation\n"
                "des changements d'interface de maniere optimisee.\n\n"
                "Ancienne architecture - Le Bridge : Historiquement, React Native\n"
                "utilisait un pont asynchrone serialisant les messages en JSON entre\n"
                "le thread JS et le thread natif. Ce bridge etait un goulot\n"
                "d'etranglement car chaque communication passait par une serialisation\n"
                "et deserialisation JSON couteuse.\n\n"
                "Nouvelle architecture - JSI (JavaScript Interface) : JSI permet au\n"
                "code JavaScript d'appeler directement des fonctions C++ sans passer\n"
                "par le bridge. Cela elimine la serialisation JSON et permet des\n"
                "appels synchrones quand necessaire.\n\n"
                "Fabric : Le nouveau systeme de rendu qui remplace l'ancien UIManager.\n"
                "Fabric permet le rendu concurrent, les mises a jour synchrones de\n"
                "l'interface et une meilleure interoperabilite avec les vues natives\n"
                "de la plateforme hote.\n\n"
                "TurboModules : Remplacement du systeme de modules natifs. Les\n"
                "TurboModules sont charges a la demande (lazy loading) plutot que\n"
                "tous au demarrage, ce qui ameliore significativement le temps de\n"
                "lancement de l'application.\n\n"
                "Le threading dans React Native implique generalement trois threads :\n"
                "le thread JavaScript, le thread de rendu natif (UI thread) et le\n"
                "thread Shadow (calcul de la mise en page via Yoga, le moteur de\n"
                "layout flexbox)."
            ),
            "pros_cons": {
                "pros": [
                    "Partage de code significatif entre iOS et Android (60-90%)",
                    "Enorme communaute et ecosysteme de bibliotheques tierces",
                    "Hot Reload pour un cycle de developpement extremement rapide",
                    "Acces aux API natives via des modules natifs quand necessaire",
                    "Reutilisation des competences web React existantes",
                    "Support de TypeScript pour un typage statique optionnel",
                    "Nouvelle architecture (Fabric/TurboModules) ameliorant les performances",
                    "Soutenu activement par Meta avec des mises a jour regulieres"
                ],
                "cons": [
                    "Performances inferieures aux applications purement natives",
                    "Debugging complexe entre les couches JS et native",
                    "Dependance aux bibliotheques tierces pour des fonctionnalites courantes",
                    "Mises a jour majeures parfois penibles (breaking changes)",
                    "Taille des applications plus importante qu'en natif pur",
                    "Navigation complexe necessitant des bibliotheques externes",
                    "Animations complexes difficiles a optimiser",
                    "Fragmentation de l'ecosysteme (Expo vs CLI, navigation, etc.)"
                ]
            },
            "use_cases": (
                "React Native excelle dans le developpement d'applications mobiles\n"
                "multiplateforme a contenu riche : applications de e-commerce,\n"
                "reseaux sociaux, applications de messagerie, tableaux de bord,\n"
                "applications de livraison, et prototypes rapides. Il est\n"
                "particulierement adapte aux equipes ayant deja des competences\n"
                "React/JavaScript et souhaitant livrer sur iOS et Android avec\n"
                "un seul codebase. Expo simplifie encore davantage le developpement\n"
                "pour les cas d'usage standards."
            ),
            "ecosystem_size": (
                "L'ecosysteme React Native est vaste et mature. Expo fournit un\n"
                "ensemble d'outils et services qui simplifient le developpement,\n"
                "le build et le deploiement. React Navigation est la solution\n"
                "de navigation standard. Pour la gestion d'etat, Redux, Zustand\n"
                "et MobX sont les choix populaires. Les bibliotheques d'UI comme\n"
                "React Native Paper et NativeBase offrent des composants prets\n"
                "a l'emploi. Le testing est supporte via Jest et React Native\n"
                "Testing Library. Fastlane facilite le deploiement automatise."
            ),
            "companies": [
                "Meta (Facebook, Instagram, Messenger)",
                "Microsoft (Office, Outlook, Xbox)",
                "Shopify",
                "Discord",
                "Bloomberg",
                "Uber Eats",
                "Walmart",
                "Pinterest"
            ],
            "code_example": (
                "import React, { useState } from 'react';\n"
                "import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';\n\n"
                "const Compteur = () => {\n"
                "  const [compte, setCompte] = useState(0);\n\n"
                "  return (\n"
                "    <View style={styles.container}>\n"
                "      <Text style={styles.titre}>Compteur : {compte}</Text>\n"
                "      <TouchableOpacity\n"
                "        style={styles.bouton}\n"
                "        onPress={() => setCompte(compte + 1)}\n"
                "      >\n"
                "        <Text style={styles.texteBouton}>Incrementer</Text>\n"
                "      </TouchableOpacity>\n"
                "    </View>\n"
                "  );\n"
                "};\n\n"
                "const styles = StyleSheet.create({\n"
                "  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },\n"
                "  titre: { fontSize: 24, marginBottom: 20 },\n"
                "  bouton: { backgroundColor: '#007AFF', padding: 15, borderRadius: 8 },\n"
                "  texteBouton: { color: '#fff', fontSize: 18 },\n"
                "});"
            ),
            "performance": {
                "startup_time": "Temps de demarrage moyen : 1-3 secondes selon la complexite. Hermes et les TurboModules ameliorent significativement ce delai.",
                "throughput": "Rendu fluide a 60 FPS pour la plupart des interfaces. Les animations complexes peuvent provoquer des saccades si elles transitent par le bridge.",
                "memory": "Consommation memoire superieure de 20-40% par rapport au natif pur en raison du moteur JavaScript et du runtime React.",
                "concurrency_model": "Modele asynchrone base sur la boucle d'evenements JavaScript. Trois threads principaux : JS, UI natif et Shadow. La nouvelle architecture permet des appels synchrones via JSI."
            },
            "learning_curve": (
                "La courbe d'apprentissage de React Native est moderee. Les developpeurs\n"
                "web connaissant React peuvent etre productifs rapidement. Cependant,\n"
                "la maitrise complete necessite de comprendre les specificites mobiles :\n"
                "navigation, gestion du cycle de vie, optimisation des performances,\n"
                "et potentiellement l'ecriture de modules natifs en Swift/Kotlin."
            ),
            "community_size": "Plus de 115 000 etoiles sur GitHub, des milliers de packages npm, une communaute tres active sur Discord, Stack Overflow et Reddit.",
            "job_market": "Tres forte demande sur le marche de l'emploi. React Native reste le framework cross-platform le plus demande en 2025, avec de nombreuses offres en freelance et CDI."
        },
        "traits": {
            "performance": 5,
            "developer_speed": 8,
            "learning_curve": 4,
            "ecosystem_size": 8,
            "type_safety": 5,
            "concurrency": 5,
            "memory_safety": 5,
            "scalability": 6
        }
    },

    "flutter": {
        "name": "Flutter",
        "category": "mobile",
        "year_created": 2017,
        "creator": "Google",
        "paradigm": ["declaratif", "composants", "reactif", "oriente objet"],
        "typing": "statique (Dart)",
        "sections": {
            "overview": (
                "Flutter est un framework open source developpe par Google pour creer\n"
                "des applications multiplateformes compilees nativement a partir d'un\n"
                "seul codebase. Contrairement a React Native qui utilise les composants\n"
                "natifs de la plateforme, Flutter dessine entierement son interface via\n"
                "son propre moteur de rendu graphique (Skia, puis Impeller).\n\n"
                "Cette approche donne a Flutter un controle total sur chaque pixel\n"
                "affiche a l'ecran, garantissant une coherence visuelle parfaite entre\n"
                "les plateformes. Le framework utilise le langage Dart, egalement cree\n"
                "par Google, qui offre un typage statique fort, la compilation AOT\n"
                "(Ahead-of-Time) pour les performances en production et la compilation\n"
                "JIT (Just-in-Time) pour le Hot Reload en developpement.\n\n"
                "Flutter ne se limite pas au mobile : il cible egalement le web, le\n"
                "desktop (Windows, macOS, Linux) et les systemes embarques. Cette\n"
                "vision multiplateforme unifiee est l'un de ses atouts majeurs.\n\n"
                "Le systeme de widgets de Flutter est extremement riche. Tout est\n"
                "widget : les elements visuels, les mises en page, les animations,\n"
                "les gestes, et meme les themes. Cette philosophie de composition\n"
                "permet de construire des interfaces complexes en assemblant des\n"
                "widgets simples. Flutter fournit des implementations Material Design\n"
                "et Cupertino (iOS) prets a l'emploi, tout en permettant une\n"
                "personnalisation totale."
            ),
            "history": (
                "Le projet Flutter a ete initie en 2015 au sein de Google sous le nom\n"
                "de code 'Sky'. L'objectif initial etait de creer un framework capable\n"
                "de rendre 120 images par seconde de maniere constante, un objectif\n"
                "ambitieux dans le monde du developpement mobile.\n\n"
                "La premiere version alpha a ete presentee au Google I/O 2017, suscitant\n"
                "un vif interet dans la communaute. Flutter 1.0, la premiere version\n"
                "stable, a ete publiee en decembre 2018 lors du Flutter Live Event.\n\n"
                "En 2019, Flutter a etendu son support au web (beta) et au desktop\n"
                "(alpha), marquant l'ambition de Google de faire de Flutter une\n"
                "plateforme de developpement universelle. Flutter 2.0, sorti en\n"
                "mars 2021, a apporte le support stable du web et une amelioration\n"
                "significative des performances.\n\n"
                "Flutter 3.0, publie en mai 2022, a marque un tournant avec le support\n"
                "stable de macOS et Linux en plus de Windows, completant ainsi la\n"
                "couverture desktop. Google a egalement introduit le support des\n"
                "applications embarquees.\n\n"
                "En 2023, Google a presente Impeller, un nouveau moteur de rendu\n"
                "remplacant Skia, specifiquement concu pour Flutter et eliminant\n"
                "les problemes de compilation de shaders qui causaient des saccades.\n"
                "Impeller est devenu le moteur par defaut sur iOS et progresse\n"
                "rapidement sur Android.\n\n"
                "L'adoption de Flutter a connu une croissance exponentielle, depassant\n"
                "React Native en nombre d'applications publiees sur les stores en 2023\n"
                "selon plusieurs etudes de marche."
            ),
            "architecture": (
                "L'architecture de Flutter se decompose en trois couches principales :\n\n"
                "1. Couche Framework (Dart) : C'est la couche avec laquelle les\n"
                "developpeurs interagissent directement. Elle comprend les widgets,\n"
                "le systeme de rendu, les animations, les gestes et les fondations.\n"
                "Les widgets sont organises en un arbre de composition ou chaque\n"
                "widget decrit une partie de l'interface.\n\n"
                "2. Couche Engine (C++) : Le moteur Flutter, ecrit principalement en\n"
                "C++, fournit le support de bas niveau : rendu graphique (via Impeller\n"
                "ou Skia), composition de texte (via la bibliotheque txt et HarfBuzz),\n"
                "gestion du reseau, acces au systeme de fichiers et le runtime Dart.\n\n"
                "3. Couche Embedder : Specifique a chaque plateforme, l'embedder\n"
                "fournit un point d'entree, gere la boucle d'evenements de la\n"
                "plateforme, le rendu de surface, et l'accessibilite.\n\n"
                "Le systeme de rendu de Flutter est unique : plutot que d'utiliser\n"
                "les widgets natifs de la plateforme, Flutter dessine tout lui-meme\n"
                "sur un canvas. L'arbre de widgets est traduit en un arbre d'elements,\n"
                "puis en un arbre de RenderObjects qui calculent la mise en page et\n"
                "effectuent le dessin.\n\n"
                "Le pipeline de rendu suit ces etapes : Build (construction de l'arbre\n"
                "de widgets) -> Layout (calcul des tailles et positions) -> Paint\n"
                "(dessin des pixels) -> Composite (composition des couches).\n\n"
                "Les Platform Channels permettent la communication bidirectionnelle\n"
                "entre Dart et le code natif de la plateforme (Kotlin/Swift) pour\n"
                "acceder aux API specifiques."
            ),
            "pros_cons": {
                "pros": [
                    "Performances excellentes grace a la compilation native AOT",
                    "Hot Reload instantane accelerant enormement le cycle de developpement",
                    "Controle total sur le rendu, coherence pixel-perfect entre plateformes",
                    "Dart est un langage moderne avec typage statique et null safety",
                    "Bibliotheque de widgets extremement riche et personnalisable",
                    "Support multiplateforme unifie : mobile, web, desktop et embarque",
                    "Documentation officielle de tres haute qualite",
                    "Impeller elimine les problemes de saccades lies aux shaders"
                ],
                "cons": [
                    "Taille des applications plus importante qu'en natif (minimum ~5-8 Mo)",
                    "Dart est un langage de niche, moins connu que JavaScript ou Kotlin",
                    "L'interface ne respecte pas toujours les conventions natives de la plateforme",
                    "Moins de packages disponibles que dans l'ecosysteme npm de React Native",
                    "Le support web, bien que stable, reste en retard sur les performances mobiles",
                    "Accessibilite parfois en retrait par rapport aux composants natifs",
                    "Consommation memoire elevee sur les appareils d'entree de gamme"
                ]
            },
            "use_cases": (
                "Flutter est ideal pour les applications necessitant une interface\n"
                "riche et personnalisee : applications fintech, e-commerce, applications\n"
                "de streaming, tableaux de bord interactifs, jeux 2D simples et\n"
                "applications d'entreprise multiplateformes. Il excelle quand la\n"
                "coherence visuelle entre iOS et Android est prioritaire sur le\n"
                "respect des conventions natives de chaque plateforme. Les startups\n"
                "l'apprecient pour sa capacite a cibler mobile, web et desktop\n"
                "depuis un seul codebase."
            ),
            "ecosystem_size": (
                "L'ecosysteme Flutter est en pleine expansion. Le gestionnaire de\n"
                "packages pub.dev heberge plus de 35 000 packages. Les bibliotheques\n"
                "essentielles incluent : Provider/Riverpod/Bloc pour la gestion d'etat,\n"
                "GoRouter pour la navigation declarative, Dio pour les requetes HTTP,\n"
                "Freezed pour la generation de code, Hive/Isar pour le stockage local,\n"
                "et Flutter Hooks pour la gestion de l'etat local. Firebase propose\n"
                "une integration officielle FlutterFire. Le testing est supporte\n"
                "nativement avec des outils de test unitaire, widget et d'integration."
            ),
            "companies": [
                "Google (Google Pay, Google Ads, Google Earth)",
                "BMW",
                "Alibaba (Xianyu)",
                "Nubank",
                "Toyota",
                "eBay",
                "Tencent",
                "ByteDance (TikTok)"
            ],
            "code_example": (
                "import 'package:flutter/material.dart';\n\n"
                "void main() => runApp(const MonApplication());\n\n"
                "class MonApplication extends StatelessWidget {\n"
                "  const MonApplication({super.key});\n\n"
                "  @override\n"
                "  Widget build(BuildContext context) {\n"
                "    return MaterialApp(\n"
                "      title: 'Demo Compteur',\n"
                "      home: const PageCompteur(),\n"
                "    );\n"
                "  }\n"
                "}\n\n"
                "class PageCompteur extends StatefulWidget {\n"
                "  const PageCompteur({super.key});\n\n"
                "  @override\n"
                "  State<PageCompteur> createState() => _PageCompteurState();\n"
                "}\n\n"
                "class _PageCompteurState extends State<PageCompteur> {\n"
                "  int _compte = 0;\n\n"
                "  @override\n"
                "  Widget build(BuildContext context) {\n"
                "    return Scaffold(\n"
                "      appBar: AppBar(title: const Text('Compteur Flutter')),\n"
                "      body: Center(\n"
                "        child: Text('Valeur : $_compte', style: const TextStyle(fontSize: 24)),\n"
                "      ),\n"
                "      floatingActionButton: FloatingActionButton(\n"
                "        onPressed: () => setState(() => _compte++),\n"
                "        child: const Icon(Icons.add),\n"
                "      ),\n"
                "    );\n"
                "  }\n"
                "}"
            ),
            "performance": {
                "startup_time": "Demarrage rapide grace a la compilation AOT : generalement sous 1-2 secondes. Le pre-chauffage de Skia/Impeller peut ajouter un leger delai au premier lancement.",
                "throughput": "Rendu cible a 60/120 FPS. Impeller elimine les saccades de compilation de shaders. Les animations complexes restent fluides grace au controle direct du pipeline graphique.",
                "memory": "Consommation memoire moderee a elevee selon la complexite. Le runtime Dart et le moteur de rendu occupent un plancher de ~30-50 Mo.",
                "concurrency_model": "Modele base sur les Isolates de Dart : chaque Isolate a sa propre memoire, elimine les data races. Communication par passage de messages. Les futures et streams gerent l'asynchronisme."
            },
            "learning_curve": (
                "La courbe d'apprentissage de Flutter est moderee. Dart est un langage\n"
                "accessible pour les developpeurs venant de Java, Kotlin, Swift ou\n"
                "TypeScript. Le systeme de widgets est intuitif une fois les concepts\n"
                "de base maitrises (StatelessWidget vs StatefulWidget, BuildContext).\n"
                "La complexite augmente avec la gestion d'etat avancee et les\n"
                "interactions avec le code natif via les Platform Channels."
            ),
            "community_size": "Plus de 165 000 etoiles sur GitHub, communaute mondiale tres active avec des meetups dans de nombreuses villes. Plus de 35 000 packages sur pub.dev.",
            "job_market": "Demande en forte croissance. Flutter est de plus en plus recherche dans les entreprises, notamment dans la fintech et le e-commerce. Le marche s'elargit avec le support desktop et web."
        },
        "traits": {
            "performance": 7,
            "developer_speed": 7,
            "learning_curve": 4,
            "ecosystem_size": 6,
            "type_safety": 7,
            "concurrency": 5,
            "memory_safety": 6,
            "scalability": 7
        }
    },

    "swiftui": {
        "name": "SwiftUI",
        "category": "mobile",
        "year_created": 2019,
        "creator": "Apple",
        "paradigm": ["declaratif", "composants", "reactif", "protocol-oriented"],
        "typing": "statique (Swift)",
        "sections": {
            "overview": (
                "SwiftUI est le framework d'interface utilisateur declaratif d'Apple,\n"
                "introduit a la WWDC 2019. Il represente un changement de paradigme\n"
                "majeur par rapport a UIKit (imperatif) en adoptant une approche\n"
                "declarative ou le developpeur decrit 'quoi' afficher plutot que\n"
                "'comment' l'afficher.\n\n"
                "SwiftUI tire pleinement parti des fonctionnalites avancees du langage\n"
                "Swift : result builders (les ViewBuilders), property wrappers\n"
                "(@State, @Binding, @ObservedObject, @EnvironmentObject), generiques\n"
                "et types opaques (some View). Ces mecanismes permettent une syntaxe\n"
                "concise et expressive tout en conservant la securite du typage statique.\n\n"
                "Le framework est profondement integre a l'ecosysteme Apple et cible\n"
                "toutes les plateformes : iOS, macOS, watchOS, tvOS et visionOS.\n"
                "Cette integration native offre un acces direct a toutes les capacites\n"
                "du systeme sans couche d'abstraction intermediaire.\n\n"
                "SwiftUI utilise un systeme de diffing automatique : quand l'etat\n"
                "change, le framework determine automatiquement quelles parties de\n"
                "l'interface doivent etre redesssinees, optimisant les mises a jour.\n"
                "Les previews Xcode permettent de visualiser les modifications en\n"
                "temps reel directement dans l'editeur, accelerant considerablement\n"
                "le cycle de developpement.\n\n"
                "Avec l'introduction de Swift 5.9 et les macros Swift, SwiftUI\n"
                "a encore simplifie son API, notamment avec la macro @Observable\n"
                "qui remplace le protocole ObservableObject et les property\n"
                "wrappers associes."
            ),
            "history": (
                "L'histoire de SwiftUI est intimement liee a celle de Swift lui-meme.\n"
                "Apple a lance Swift en 2014 comme remplacement moderne d'Objective-C.\n"
                "Pendant les cinq premieres annees, les developpeurs Apple utilisaient\n"
                "UIKit (iOS) et AppKit (macOS) avec Swift, des frameworks imperatifs\n"
                "herites de l'ere Objective-C.\n\n"
                "A la WWDC 2019, Apple a surpris la communaute en devoilant SwiftUI,\n"
                "un framework entierement nouveau adoptant le paradigme declaratif\n"
                "popularise par React. L'annonce a ete accueillie avec enthousiasme\n"
                "mais aussi prudence, car la premiere version presentait de nombreuses\n"
                "limitations.\n\n"
                "SwiftUI 2.0 (2020, iOS 14) a corrige de nombreuses lacunes : ajout\n"
                "de LazyVStack/LazyHGrid pour les listes performantes, le cycle de\n"
                "vie des applications (@main, App protocol), et de nombreux nouveaux\n"
                "composants. SwiftUI 3.0 (2021, iOS 15) a introduit le support\n"
                "d'async/await, les listes tirees vers le bas, et le Markdown dans\n"
                "les textes.\n\n"
                "SwiftUI 4.0 (2022, iOS 16) a apporte NavigationStack remplacant\n"
                "NavigationView, les Charts natifs et les transferables. SwiftUI 5.0\n"
                "(2023, iOS 17) a marque un tournant avec la macro @Observable,\n"
                "les animations par keyframes, et le support de visionOS.\n\n"
                "En 2024 et 2025, Apple a continue d'enrichir SwiftUI avec des\n"
                "composants toujours plus avances, rendant le framework mature\n"
                "pour la majorite des cas d'usage. L'interoperabilite avec UIKit\n"
                "reste disponible pour les cas complexes."
            ),
            "architecture": (
                "L'architecture de SwiftUI repose sur plusieurs concepts fondamentaux\n"
                "qui forment un systeme coherent et performant :\n\n"
                "Vues declaratives : Chaque vue est une struct conformant au protocole\n"
                "View, avec une propriete calculee 'body' retournant le contenu.\n"
                "Les vues sont des valeurs (value types), pas des objets, ce qui\n"
                "les rend legeres et eliminables sans cout.\n\n"
                "Gestion de l'etat : SwiftUI propose une hierarchie de property\n"
                "wrappers pour gerer l'etat : @State pour l'etat local, @Binding\n"
                "pour les references partagees parent-enfant, @Observable (macro)\n"
                "pour les modeles observables, et @Environment pour l'injection\n"
                "de dependances.\n\n"
                "Systeme de layout : SwiftUI utilise un systeme de negociation\n"
                "de taille unique. Le parent propose une taille a l'enfant,\n"
                "l'enfant choisit sa taille, puis le parent positionne l'enfant.\n"
                "Ce systeme est plus intuitif que l'Auto Layout d'UIKit.\n\n"
                "Arbre de rendu : En coulisses, SwiftUI maintient un graphe\n"
                "d'attributs (AttributeGraph) qui suit les dependances entre\n"
                "les vues et les donnees. Quand une donnee change, seules les\n"
                "vues directement dependantes sont recalculees et redesssinees.\n\n"
                "Diffing structurel : SwiftUI compare les arbres de vues via\n"
                "leur type structurel plutot que par identite d'objet, permettant\n"
                "un diffing tres performant a la compilation.\n\n"
                "Integration plateforme : Les composants SwiftUI sont traduits\n"
                "en elements UIKit/AppKit natifs sous le capot, garantissant\n"
                "les performances et l'accessibilite natives."
            ),
            "pros_cons": {
                "pros": [
                    "Syntaxe declarative concise et expressive grace aux fonctionnalites de Swift",
                    "Performances natives optimales sans couche d'abstraction intermediaire",
                    "Integration parfaite avec l'ecosysteme Apple (CoreData, CloudKit, HealthKit)",
                    "Previews Xcode pour un retour visuel instantane pendant le developpement",
                    "Securite du typage statique de Swift avec null safety integre",
                    "Support natif de l'accessibilite et des technologies adaptatives Apple",
                    "Animations fluides et declaratives integrees au framework",
                    "Support de toutes les plateformes Apple incluant visionOS"
                ],
                "cons": [
                    "Limite exclusivement a l'ecosysteme Apple",
                    "Necessite iOS 13 minimum, les API modernes requierent iOS 16+",
                    "Documentation officielle parfois lacunaire sur les concepts avances",
                    "Comportements internes opaques rendant le debugging difficile",
                    "Certains composants UIKit n'ont pas encore d'equivalent SwiftUI",
                    "Le marche de l'emploi est limite aux entreprises ciblant Apple",
                    "Les changements d'API entre versions peuvent casser le code existant"
                ]
            },
            "use_cases": (
                "SwiftUI est le choix optimal pour toute application ciblant\n"
                "exclusivement l'ecosysteme Apple. Il excelle pour les applications\n"
                "iOS natives, les applications Apple Watch, les widgets d'ecran\n"
                "d'accueil, les applications visionOS (Vision Pro), les extensions\n"
                "systeme et les applications macOS. Il est particulierement adapte\n"
                "aux entreprises souhaitant offrir l'experience utilisateur la plus\n"
                "native et performante possible sur les produits Apple."
            ),
            "ecosystem_size": (
                "L'ecosysteme SwiftUI beneficie de l'integration profonde avec\n"
                "les outils et frameworks Apple. Xcode fournit un IDE complet\n"
                "avec les previews interactives. Swift Package Manager gere les\n"
                "dependances. Les frameworks Apple (CoreData, SwiftData, CloudKit,\n"
                "Combine, async/await, Core ML, ARKit, RealityKit) s'integrent\n"
                "nativement. Des bibliotheques tierces populaires incluent\n"
                "The Composable Architecture (TCA), Kingfisher pour les images,\n"
                "et SwiftLint pour le linting."
            ),
            "companies": [
                "Apple (toutes les applications systeme)",
                "Airbnb (application iOS)",
                "Spotify (certaines vues)",
                "Netflix (application iOS)",
                "Lyft",
                "Revolut",
                "N26"
            ],
            "code_example": (
                "import SwiftUI\n\n"
                "struct PageCompteur: View {\n"
                "    @State private var compte = 0\n\n"
                "    var body: some View {\n"
                "        VStack(spacing: 20) {\n"
                "            Text(\"Compteur\")\n"
                "                .font(.largeTitle)\n"
                "                .fontWeight(.bold)\n\n"
                "            Text(\"\\(compte)\")\n"
                "                .font(.system(size: 72, weight: .bold))\n"
                "                .foregroundStyle(.blue)\n\n"
                "            HStack(spacing: 20) {\n"
                "                Button(\"Decrementer\") {\n"
                "                    compte -= 1\n"
                "                }\n"
                "                .buttonStyle(.bordered)\n\n"
                "                Button(\"Incrementer\") {\n"
                "                    compte += 1\n"
                "                }\n"
                "                .buttonStyle(.borderedProminent)\n"
                "            }\n"
                "        }\n"
                "        .padding()\n"
                "    }\n"
                "}\n\n"
                "#Preview {\n"
                "    PageCompteur()\n"
                "}"
            ),
            "performance": {
                "startup_time": "Demarrage quasi instantane, identique a une application UIKit native. Aucun moteur intermediaire a initialiser.",
                "throughput": "Rendu a 60/120 FPS natif. SwiftUI exploite directement Core Animation et Metal pour un rendu GPU optimal.",
                "memory": "Consommation memoire minimale. Les vues sont des structs (value types) allouees sur la pile, pas le tas. L'empreinte memoire est comparable a UIKit pur.",
                "concurrency_model": "Modele de concurrence moderne de Swift : async/await, acteurs, taches structurees. Swift 5.5+ offre une concurrence securisee a la compilation avec le checking strict de la concurrence."
            },
            "learning_curve": (
                "La courbe d'apprentissage est moderee a elevee. La syntaxe declarative\n"
                "est intuitive pour les interfaces simples, mais la maitrise des property\n"
                "wrappers, du systeme de layout et de la gestion d'etat avancee demande\n"
                "du temps. Les developpeurs venant d'UIKit doivent changer de paradigme\n"
                "mental. La comprehension de Swift (generiques, protocols, value types)\n"
                "est un prerequis important."
            ),
            "community_size": "Communaute en forte croissance, portee par l'ecosysteme Apple. Des milliers de tutoriels, cours et conferences dedies. Le forum Swift et les communautes iOS sont tres actifs.",
            "job_market": "Forte demande pour les developpeurs iOS matrisant SwiftUI, particulierement dans les startups et entreprises tech. Les salaires sont parmi les plus eleves du developpement mobile."
        },
        "traits": {
            "performance": 9,
            "developer_speed": 6,
            "learning_curve": 5,
            "ecosystem_size": 6,
            "type_safety": 9,
            "concurrency": 7,
            "memory_safety": 8,
            "scalability": 7
        }
    },

    "jetpack_compose": {
        "name": "Jetpack Compose",
        "category": "mobile",
        "year_created": 2021,
        "creator": "Google",
        "paradigm": ["declaratif", "composants", "reactif", "fonctionnel"],
        "typing": "statique (Kotlin)",
        "sections": {
            "overview": (
                "Jetpack Compose est le toolkit moderne de Google pour la construction\n"
                "d'interfaces utilisateur natives sur Android. Lance en version stable\n"
                "en juillet 2021, il represente la reponse de Google a SwiftUI d'Apple\n"
                "et marque l'abandon progressif de l'ancien systeme de vues XML\n"
                "qui definissait le developpement Android depuis sa creation.\n\n"
                "Compose adopte un paradigme declaratif ou l'interface est definie\n"
                "comme une fonction du state de l'application. Les developpeurs\n"
                "ecrivent des fonctions composables (annotees @Composable) qui\n"
                "decrivent l'interface. Quand l'etat change, Compose recompose\n"
                "intelligemment uniquement les parties affectees de l'arbre d'interface.\n\n"
                "Le framework est entierement ecrit en Kotlin et exploite les\n"
                "fonctionnalites avancees du langage : fonctions d'extension, lambdas\n"
                "avec recepteur, coroutines, DSLs de type-safe et la programmation\n"
                "fonctionnelle. Cette synergie entre Kotlin et Compose produit un\n"
                "code extremement concis et lisible.\n\n"
                "Compose s'integre parfaitement avec l'ecosysteme Jetpack existant :\n"
                "ViewModel, Room, Navigation, Hilt, et les autres bibliotheques\n"
                "Architecture Components. L'interoperabilite bidirectionnelle avec\n"
                "le systeme de vues classique permet une migration progressive.\n\n"
                "Google a egalement lance Compose Multiplatform via JetBrains,\n"
                "etendant Compose au desktop (Windows, macOS, Linux), au web\n"
                "et a iOS (en alpha), elargissant significativement sa portee."
            ),
            "history": (
                "Le developpement de Jetpack Compose a debute en 2018, quand l'equipe\n"
                "Android de Google a commence a repenser fondamentalement la facon\n"
                "dont les interfaces sont construites sur Android. Le systeme de vues\n"
                "XML, bien que mature, presentait de nombreuses limitations : verbosity\n"
                "excessive, difficulte a maintenir la coherence etat-vue, et complexite\n"
                "des RecyclerViews.\n\n"
                "Google a annonce Compose pour la premiere fois lors du Google I/O 2019\n"
                "comme un projet en pre-alpha. L'annonce a genere un enorme interet\n"
                "mais aussi des inquietudes quant a la fragmentation de l'ecosysteme\n"
                "Android deja complexe.\n\n"
                "La version alpha est arrivee en aout 2020, suivie de la beta en\n"
                "fevrier 2021. Chaque version apportait des ameliorations\n"
                "significatives en termes de performances, d'API et de stabilite.\n\n"
                "En juillet 2021, Compose 1.0 est sorti en version stable,\n"
                "accompagne du support de Material Design 3 et d'outils ameliores\n"
                "dans Android Studio. Google a annonce que Compose serait desormais\n"
                "l'approche recommandee pour le developpement d'interfaces Android.\n\n"
                "Depuis sa sortie, Compose a connu des mises a jour regulieres :\n"
                "Compose 1.2 a ameliore les performances de la lazy composition,\n"
                "Compose 1.4 a introduit de nouveaux composants Material 3, et\n"
                "Compose 1.5 a apporte des optimisations significatives du\n"
                "compilateur Compose.\n\n"
                "En parallele, JetBrains a lance Compose Multiplatform, utilisant\n"
                "le meme modele de programmation pour cibler le desktop et le web,\n"
                "avec un support iOS en cours de maturation."
            ),
            "architecture": (
                "L'architecture de Jetpack Compose repose sur un compilateur Kotlin\n"
                "specialise et un runtime sophistique qui gerent la recomposition\n"
                "intelligente de l'interface.\n\n"
                "Compilateur Compose : Un plugin du compilateur Kotlin transforme les\n"
                "fonctions @Composable en code genere qui gere automatiquement la\n"
                "recomposition. Le compilateur insere des groupes de suivi qui\n"
                "permettent au runtime de savoir quelles parties de l'arbre doivent\n"
                "etre mises a jour.\n\n"
                "Runtime Compose : Le runtime maintient une Slot Table, une structure\n"
                "de donnees en memoire qui stocke l'etat courant de l'arbre de\n"
                "composition. Lors de la recomposition, seules les fonctions dont\n"
                "les entrees ont change sont reexecutees.\n\n"
                "Recomposition intelligente : Compose utilise la stabilite positionnelle\n"
                "pour determiner si un composable doit etre recompose. Les parametres\n"
                "stables (val, data class, types primitifs) permettent au compilateur\n"
                "de sauter la recomposition quand les entrees n'ont pas change.\n\n"
                "Phases de rendu : Le pipeline de Compose comprend trois phases :\n"
                "Composition (execution des fonctions composables), Layout (mesure\n"
                "et placement des elements) et Drawing (dessin sur le canvas).\n"
                "Chaque phase peut etre optimisee independamment.\n\n"
                "Gestion de l'etat : Compose propose remember {} pour la persistance\n"
                "d'etat entre les recompositions, mutableStateOf() pour les\n"
                "observables reactifs, et derivedStateOf {} pour les calculs\n"
                "derives. Le state hoisting est le pattern recommande pour\n"
                "la separation des responsabilites.\n\n"
                "Effets de bord : Les effets (LaunchedEffect, DisposableEffect,\n"
                "SideEffect) permettent d'executer du code non composable de\n"
                "maniere securisee dans le contexte de la composition."
            ),
            "pros_cons": {
                "pros": [
                    "Syntaxe declarative eliminant la verbosity du systeme de vues XML",
                    "Kotlin idiomatique avec typage statique fort et null safety",
                    "Recomposition intelligente optimisant les performances automatiquement",
                    "Previews interactives dans Android Studio pour un feedback immediat",
                    "Interoperabilite totale avec le systeme de vues existant (migration progressive)",
                    "Integration native avec l'ecosysteme Jetpack (ViewModel, Navigation, Room)",
                    "Material Design 3 integre avec theming dynamique et complet",
                    "Compose Multiplatform etend la portee au desktop et web via JetBrains"
                ],
                "cons": [
                    "Limite principalement a Android (le multiplateforme est en maturation)",
                    "Courbe d'apprentissage pour les developpeurs habitues au systeme de vues XML",
                    "Les performances peuvent se degrader avec des recompositions excessives mal optimisees",
                    "L'outillage de debugging de la recomposition est encore en cours d'amelioration",
                    "Certains composants avances manquent encore par rapport a l'ecosysteme View",
                    "La documentation sur les patterns avances (custom layouts, modifiers) est incomplete",
                    "La taille de la bibliotheque ajoute du poids a l'APK final"
                ]
            },
            "use_cases": (
                "Jetpack Compose est recommande pour tout nouveau projet Android.\n"
                "Il excelle dans les applications necessitant des interfaces\n"
                "dynamiques et reactives : applications de e-commerce, reseaux\n"
                "sociaux, applications de productivite, tableaux de bord, et\n"
                "applications Material Design 3. Avec Compose Multiplatform,\n"
                "il devient pertinent pour les projets ciblant Android et desktop.\n"
                "Les equipes migrant des applications existantes peuvent adopter\n"
                "Compose progressivement grace a l'interoperabilite."
            ),
            "ecosystem_size": (
                "L'ecosysteme Compose s'appuie sur Jetpack, la suite de bibliotheques\n"
                "Android recommandees par Google. Compose Navigation pour la navigation,\n"
                "Compose Material 3 pour les composants UI, Hilt/Koin pour l'injection\n"
                "de dependances, Coil/Glide pour le chargement d'images, Room pour\n"
                "la persistance locale, Retrofit/Ktor pour les appels reseau.\n"
                "L'outillage Android Studio offre des previews interactives, un\n"
                "layout inspector, et un profiler de recomposition."
            ),
            "companies": [
                "Google (Play Store, Maps, Messages)",
                "Twitter/X",
                "Airbnb",
                "Square/Block",
                "Lyft",
                "Monzo",
                "Reddit",
                "Dropbox"
            ],
            "code_example": (
                "import androidx.compose.foundation.layout.*\n"
                "import androidx.compose.material3.*\n"
                "import androidx.compose.runtime.*\n"
                "import androidx.compose.ui.Alignment\n"
                "import androidx.compose.ui.Modifier\n"
                "import androidx.compose.ui.unit.dp\n"
                "import androidx.compose.ui.unit.sp\n\n"
                "@Composable\n"
                "fun PageCompteur() {\n"
                "    var compte by remember { mutableIntStateOf(0) }\n\n"
                "    Column(\n"
                "        modifier = Modifier.fillMaxSize(),\n"
                "        verticalArrangement = Arrangement.Center,\n"
                "        horizontalAlignment = Alignment.CenterHorizontally\n"
                "    ) {\n"
                "        Text(\n"
                "            text = \"Compteur\",\n"
                "            style = MaterialTheme.typography.headlineLarge\n"
                "        )\n"
                "        Spacer(modifier = Modifier.height(16.dp))\n"
                "        Text(\n"
                "            text = \"$compte\",\n"
                "            fontSize = 72.sp,\n"
                "            color = MaterialTheme.colorScheme.primary\n"
                "        )\n"
                "        Spacer(modifier = Modifier.height(16.dp))\n"
                "        Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {\n"
                "            OutlinedButton(onClick = { compte-- }) {\n"
                "                Text(\"Decrementer\")\n"
                "            }\n"
                "            Button(onClick = { compte++ }) {\n"
                "                Text(\"Incrementer\")\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "}"
            ),
            "performance": {
                "startup_time": "Temps de demarrage comparable aux vues classiques Android. Le compilateur Compose optimise le code genere pour minimiser l'overhead.",
                "throughput": "Rendu a 60/90/120 FPS selon l'ecran. La recomposition intelligente evite les recalculs inutiles. Les Lazy lists offrent des performances excellentes pour les grandes listes.",
                "memory": "Consommation memoire legerement superieure au systeme de vues classique en raison de la Slot Table. L'optimisation de la stabilite des parametres reduit la surcharge.",
                "concurrency_model": "Base sur les coroutines Kotlin. Les effets (LaunchedEffect) lancent des coroutines dans le scope du composable. Le dispatcher Main gere les mises a jour UI de maniere thread-safe."
            },
            "learning_curve": (
                "La courbe d'apprentissage est moderee. Les developpeurs Kotlin s'adaptent\n"
                "rapidement a la syntaxe composable. Les concepts de recomposition,\n"
                "de state hoisting et d'effets de bord demandent de la pratique.\n"
                "Les developpeurs venant du systeme de vues XML doivent abandonner\n"
                "les reflexes imperatifs. La maitrise de Kotlin (coroutines, lambdas,\n"
                "DSL) est essentielle pour etre productif."
            ),
            "community_size": "Communaute en croissance rapide, soutenue par Google et JetBrains. Des milliers d'articles, tutoriels video et projets open source. La communaute Kotlin Android Developers est tres active.",
            "job_market": "Demande croissante et souvent exigee pour les postes Android en 2025. Les entreprises migrent activement vers Compose. La maitrise de Compose est un atout majeur sur le marche de l'emploi Android."
        },
        "traits": {
            "performance": 8,
            "developer_speed": 7,
            "learning_curve": 5,
            "ecosystem_size": 7,
            "type_safety": 8,
            "concurrency": 7,
            "memory_safety": 7,
            "scalability": 7
        }
    }
}
