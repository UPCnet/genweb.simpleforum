# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone.directives import form
from plone.app.textfield import RichText
from plone import api

from genweb.simpleforum import _
from plone.app.dexterity import PloneMessageFactory as _PMF
from collective import dexteritytextindexer

from plone.app.discussion.interfaces import IConversation
from operator import itemgetter
import calendar
from datetime import datetime, timedelta

from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from plone.app.discussion.interfaces import IDiscussionSettings

from plone.directives import dexterity


def utc_to_local(utc_dt):
    # get integer timestamp to avoid precision lost
    timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)


class IForum(form.Schema):
    """ Forum: contenidor de Post
    """
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_PMF(u'label_title', default=u'Title'),
        required=True
    )

    dexteritytextindexer.searchable('descripcioForum')
    descripcioForum = RichText(
        title=_(u"Forum description"),
        required=False,
    )


class View(grok.View):
    grok.context(IForum)
    grok.template('forum_view')

    def posts(self):
        # llista de posts ordenats de més recent a més antic
        results = []
        mtool = api.portal.get_tool(name='portal_membership')
        brains = self.context.getFolderContents(contentFilter={
            'portal_type': 'genweb.simpleforum.post',
            'sort_on': 'modified',
            'sort_order': 'reverse'})

        for brain in brains:
            conversation = IConversation(brain.getObject())
            total_comments = conversation.total_comments
            comments = conversation.getComments()
            last_comment = None
            for last_comment in comments:
                pass
            if last_comment:
                last_author = last_comment.Creator()
            else:
                last_author = brain.Creator

            # si hi ha comentaris mostrem la data del darrer comentari, si no, la data de modificació del post
            if total_comments > 0:
                modification_date = utc_to_local(conversation.last_comment_date)
            else:
                modification_date = brain.ModificationDate
            modification_date = self.context.toLocalizedTime(modification_date, long_format='%B %d, %Y')

            results.append({
                'title': brain.Title,
                'url': brain.getURL(),
                'author': mtool.getMemberInfo(last_author)['fullname'],
                'modificationDate': modification_date,
                'portrait': mtool.getPersonalPortrait(id=brain.listCreators[0]).absolute_url(),
                'comments': total_comments
            })
            # ordenem els resultas inversament data creació o d'últim comentari
            results = sorted(results, key=itemgetter('modificationDate'), reverse=True)
        # import pdb; pdb.set_trace()
        return results

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
    grok.context(IForum)

    def update(self):
        # hide left column on edit mode
        super(dexterity.EditForm, self).update()
        self.request.set('disable_plone.leftcolumn', 1)
