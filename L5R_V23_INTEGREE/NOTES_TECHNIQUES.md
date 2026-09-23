# Notes techniques V2.3

- Source conservée : `L5R_V2_2_Sumie/L5R4e_V2_2_Sumie.html` et CSS de la V2.2.
- Seul l'onglet `Personnage` reçoit les nouveaux composants illustrés, et tous ses anciens attributs persistent ; les autres blocs restent dans le même document.
- Le script `type="text/worker"` et les cinq `<rolltemplate>` sont recopiés octet pour octet depuis V2.2. L'affichage des maîtrises repose donc sur la logique déjà en place, pas sur de nouvelles formules.
- Les six nouvelles icônes sont des décorations CSS : les `input[type=radio]` des statuts restent inchangés.
- Les cinq images d'Anneaux dans l’HTML reprennent directement les URLs HTTPS de la V1.4, à la demande du créateur.
- La gestion des thèmes continue d'utiliser `attr_ui_clan_theme`, miroir indépendant de `attr_Clan`, et le vert forêt Corbeau `#234939`.
- La bannière des titres est une image sans texte ; le titre reste une vraie chaîne HTML, pour être éditable et traduisible.
- Toutes les URL d'illustrations sont volontairement hors du CSS de base et injectées dans une couche générée après hébergement.
- L’en-tête *peint* possède des mots à l’intérieur de l’image, puisqu’il a été validé comme illustration panoramique. Pour changer ces mots il faudra retoucher l’asset source ou utiliser le fallback HTML sans couche illustrée.
