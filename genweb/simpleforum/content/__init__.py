from zope.interface import implements
from plone.dexterity.content import Item

from genweb.simpleforum.content.post import IPost
from genweb.simpleforum.content.forum import IForum


class Post(Item):
    implements(IPost)


class Forum(Item):
    implements(IForum)
