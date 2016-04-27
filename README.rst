====================
genweb.simpleforum
====================


How it works
============

Es tracta d'un fòrum amb funcionalitat simple. 

Els comentaris utilitzen plone.app.discussion, i per tant @@discussion-settings té varies opcions que poden afectar el Forum, per exemple:

- Mostra imatge de perfil
- Habilitar enviament de notificacions per correu

Es mostra a pantalla completa, sense la columna esquerra de portlets.

Té dos tipus de contingut Forum i Post:

Forum:
------
- El Forum és un container de Post, mostra una llista de Posts ordenats cronològicament de més nou a més antic.
- La data d'ordenació és la de l'últim comentari o la de creació si no hi ha comentaris
- Paginat: 10 posts per pàgina
- Cal publicar-lo en intranet, i afegir a 'Comparteix' els usuaris que vulguem amb els rols 'Pot afegir' i 'Pot veure' (és recomanable utilitzar grups)

Post:
-----
- Un tema i a sota els seus comentaris
- Els comentaris es mostren de més nou a més antic




Installation
============

To install `genweb.simpleforum` you simply add ``genweb.simpleforum``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `genweb.simpleforum` using the Add-ons control panel.


Configuration
=============

...

