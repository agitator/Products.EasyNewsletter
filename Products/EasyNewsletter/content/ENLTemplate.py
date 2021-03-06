# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.Archetypes import atapi
from Products.CMFCore.utils import getToolByName
from Products.EasyNewsletter import EasyNewsletterMessageFactory as _
from Products.EasyNewsletter import config
from Products.EasyNewsletter.interfaces import IENLTemplate
from Products.TemplateFields import ZPTField
from zope.interface import implementer


schema = atapi.BaseSchema + atapi.Schema((

    ZPTField(
        'body',
        validators=('zptvalidator', ),
        widget=atapi.TextAreaWidget(
            label=_(u'label_body_zpt', default=u'Newsletter Template'),
            description=_(
                'help_body_zpt',
                default=u'This is a Zope Page Template file that is used for \
                     rendering the newsletter mail.'),
            i18n_domain="plone",
            rows=30,
        ),
    ),

    atapi.TextField(
        'description',
        accessor="Description",
        widget=atapi.TextAreaWidget(
            label=_(u"label_description", default=u'Description'),
            description=_(
                u"help_description",
                default=u"Enter a value for description."),
            i18n_domain="plone",
        ),
    ),

), )


@implementer(IENLTemplate)
class ENLTemplate(atapi.BaseContent):
    """Template used for styling newsletter entries.
    """
    security = ClassSecurityInfo()
    schema = schema
    _at_rename_after_creation = True

    def initializeArchetype(self, **kwargs):
        """overwritten hook
        """
        atapi.BaseContent.initializeArchetype(self, **kwargs)
        self.setBody(config.DEFAULT_TEMPLATE)

    @security.public
    def getSourceCode(self):
        """Return body as string
        """
        html = self.getField("body").getRaw(self)
        return html

    @security.public
    def setIssue(self, issue_uid):
        """Sets the newsletter which should be used by the template
        """
        self.issue_uid = issue_uid

    def queryCatalog(self):
        """Delegates queryCatalog to the current issue.
        """
        portal_catalog = getToolByName(self, "portal_catalog")
        try:
            brain = portal_catalog(UID=self.issue_uid)[0]
            issue = brain.getObject()
            return issue.queryCatalog()
        except (AttributeError, IndexError, TypeError):
            return []

    def getSubTopics(self):
        """
        """
        portal_catalog = getToolByName(self, "portal_catalog")
        try:
            brain = portal_catalog(UID=self.issue_uid)[0]
        except (AttributeError, IndexError):
            return []
        else:
            newsletter = brain.getObject()
            return newsletter.getSubTopics()


atapi.registerType(ENLTemplate, config.PROJECTNAME)
