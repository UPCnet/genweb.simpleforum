# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone import api

from plone.directives import dexterity
from plone.directives import form
from plone.app.textfield import RichText

from genweb.simpleforum import _
from plone.app.dexterity import PloneMessageFactory as _PMF
from collective import dexteritytextindexer

from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from plone.app.discussion.interfaces import IDiscussionSettings


class IPost(form.Schema):
    """ Post: un tema i les seves respostes
    """

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_PMF(u'label_title', default=u'Title'),
        required=True
    )

    dexteritytextindexer.searchable('text')
    text = RichText(
        title=_(u"Text"),
        required=True,
    )


class View(grok.View):
    grok.context(IPost)
    grok.template('post_view')

    def data(self):
        # dades del tema
        mtool = api.portal.get_tool(name='portal_membership')

        if (self.context.text):
            text = self.context.text.output
        else:
            text = 'Sense text'

        result = {
            'title': self.context.title,
            'author': mtool.getMemberInfo(self.context.Creator),
            'modificationDate': self.context.toLocalizedTime(self.context.ModificationDate(), long_format='%B %d, %Y'),
            'portrait': mtool.getPersonalPortrait(id=self.context.Creator()).absolute_url(),
            'text': text
        }
        return result

    def update(self):
        # hide left column on view mode
        super(grok.View, self).update()
        self.request.set('disable_plone.leftcolumn', 1)

    def show_commenter_image(self):
        # Check if showing commenter image is enabled in the registry
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IDiscussionSettings, check=False)
        return settings.show_commenter_image


class Edit(dexterity.EditForm):
    """A standard edit form.
    """
    grok.context(IPost)

    def update(self):
        # hide left column on edit mode
        super(dexterity.EditForm, self).update()
        self.request.set('disable_plone.leftcolumn', 1)


class Add(dexterity.AddForm):
    """A standard add form.
    """
    grok.name('genweb.simpleforum.post')

    def update(self):
        # hide left column on add mode
        super(dexterity.AddForm, self).update()
        self.request.set('disable_plone.leftcolumn', 1)
