# L5R 4e — V2.3 Sumi-e intégrée

Cette livraison transforme **l’onglet Personnage** en une composition illustrée fondée sur la maquette approuvée. La couleur du **Clan du Corbeau est le vert forêt `#234939`**. Elle reprend les éléments graphiques validés : fond parchemin, en-tête panoramique, titres sur coups de pinceau **sans texte incorporé à l'image**, six icônes de la Voie du samouraï et paysage en bas de page (sans phrase d'ambiance).

L'HTML conserve les 5 adresses HTTPS des anneaux déjà employées en V1.4, plutôt que d'utiliser de nouveaux anneaux générés. La V2.2 est la base fonctionnelle : ses champs, ses macros, ses sections répétables et son script ne sont pas remplacés.

## Consulter le véritable rendu avant mise en ligne

Ouvrez `APERCU_LOCAL_V2_3.html` **depuis le ZIP extrait**, avec le dossier `assets` présent à côté. Les illustrations locales doivent alors s'afficher. Les valeurs visibles dans cet aperçu (`Morigami Kaori`, etc.) sont **fictives** et ne sont jamais écrites dans l’HTML livré pour Roll20.

Les captures `APERCU_LARGE.png`, `APERCU_ROLL20.png` et `APERCU_BAS_DE_PAGE.png` permettent de comparer les proportions. Les captures proviennent d'un navigateur statique et ne constituent pas un test dans le moteur Roll20.

## Mettre les images en ligne (nécessaire pour le même résultat sur Roll20)

**Vous n'avez rien à héberger pour les Anneaux** : leurs 5 URL d'origine V1.4 se trouvent déjà dans `L5R4e_V2_3_Sumie.html`.

Publiez les **12** illustrations du tableau ci-dessous dans un emplacement publiquement accessible en HTTPS, sans authentification, avec de préférence une URL permanente et sans expiration. Assurez-vous que chaque adresse permet d'ouvrir directement l'image PNG dans un navigateur privé et non une page HTML d'aperçu.

| Fichier `assets/…` | Clé dans le fichier de configuration | Rôle |
|---|---|---|
| fond-parchemin.png | fond-parchemin | Fond parchemin avec paysages discrets |
| entete-peint.png | entete-peint | En-tête Sumi-e complet |
| pinceau-titres.png | pinceau-titres | Pinceau noir sans texte, réutilisable pour tous les titres |
| bas-de-page.png | bas-de-page | Paysage final sans citation |
| icone-honneur.png | icone-honneur | Statut : Honneur |
| icone-gloire.png | icone-gloire | Statut : Gloire |
| icone-infamie.png | icone-infamie | Statut : Infamie |
| icone-statut.png | icone-statut | Statut : Statut |
| icone-souillure.png | icone-souillure | Statut : Souillure |
| icone-ombre.png | icone-ombre | Statut : Ombre |
| sceau-corbeau.png | sceau-corbeau | Mon du Corbeau vert foncé |
| corbeau-peint.png | corbeau-peint | Illustration du Corbeau sur sa branche |

Les autres PNG `preview-anneau-…` servent **uniquement à l’aperçu hors ligne**, pas à Roll20. `paysage-doux.png` est une réserve artistique non utilisée dans cette version.

## Générer la feuille CSS intégrale

1. Dans `ASSETS_A_HEBERGER.json`, remplacez chaque valeur `""` par l'adresse **HTTPS directe** de l'illustration correspondante. Les clés doivent rester inchangées.
2. À l'endroit où vous avez extrait le ZIP, exécutez `python GENERER_CSS_ROLL20.py` (Python 3). Le script vérifie qu'aucune illustration obligatoire ne manque. Il ne téléverse **rien** et n'accède pas à Internet.
3. Récupérez le fichier `L5R4e_V2_3_ROLL20_COMPLET.css` créé dans le même dossier. **C'est ce CSS qui restitue tous les visuels.**

`L5R4e_V2_3_BASE.css` seul est un filet de sécurité : il conserve l’interface, les couleurs et des titres sombres, mais il ne contient aucun lien vers les nouvelles peintures. `ART_LAYER_TEMPLATE.css` n'est pas destiné à être collé directement dans Roll20 : ses marqueurs d'images doivent être remplacés par le générateur.

## Installation dans Roll20

1. **Dupliquez la campagne et conservez votre version actuellement fonctionnelle** avant toute modification.
2. Dans les paramètres de la campagne de test, éditez la feuille personnalisée. Copiez tout `L5R4e_V2_3_Sumie.html` dans l'éditeur HTML et tout `L5R4e_V2_3_ROLL20_COMPLET.css` dans l'éditeur CSS.
3. Sauvegardez. Rouvrez la fiche et vérifiez les six points : les sept onglets restent cliquables ; chaque trait reprend sa valeur ; le Clan du Corbeau devient vert forêt ; l'initiative et le ND se recalculent ; les pistes Honneur/Gloire/etc. changent et restent conservées ; les maîtrises de compétences déjà présentes sont toujours accessibles.
4. Vérifiez enfin le résultat graphique dans votre vraie fenêtre Roll20. Pour un affichage proche de la maquette, une fenêtre large améliore la disposition des cinq cartes d'Anneaux. Une fenêtre plus étroite réorganise la grille.

### Périmètre et limites

La **présente livraison est la refonte intégrée de Personnage** : les autres onglets restent sur leur version fonctionnelle précédente, dans le même HTML. Les contrôles automatiques vérifient la compatibilité statique et la navigation en navigateur, **pas** l'exécution du moteur Roll20. Le portrait de l'illustration et les paysages sont décoratifs ; le portrait du personnage du Journal Roll20 n'est pas injecté automatiquement dans la feuille.
