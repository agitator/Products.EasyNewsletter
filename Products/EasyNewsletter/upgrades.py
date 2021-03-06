# -*- coding: utf-8 -*-
from logging import getLogger
from nameparser import HumanName
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile


logger = getLogger('Products.EasyNewsletter')


def reinstall_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-Products.EasyNewsletter:default'
    )
    logger.info("Products.EasyNewsletter generic setup profile re-installed")


def fullname_to_first_and_lastname(context):
    """Migrate subscriber fullname to separate fields."""

    catalog = api.portal.get_tool("portal_catalog")
    subscribers = catalog(portal_type='ENLSubscriber')

    for subscriber in subscribers:
        obj = subscriber.getObject()
        name = ''
        try:
            name = HumanName(obj.fullname)
        except:
            logger.info(
                'No splitting necessary for {0}'.format(obj.getTitle()))
        if name:
            if not obj.getLastname():
                obj.setLastname(name.last)
            if not obj.getFirstname():
                obj.setFirstname(name.first)
            if not obj.getName_prefix():
                obj.setName_prefix(name.title)
            obj.reindexObject()
            logger.info(
                'Splitting fullname to first and lastname for {0}'.format(
                    obj.getTitle()
                )
            )

    loadMigrationProfile(
        context,
        'profile-Products.EasyNewsletter:default'
    )


def add_catalog_indexes(context, logger=None):
    """Add aditional indexes to the portal_catalog."""

    catalog = api.portal.get_tool("portal_catalog")

    indexes = catalog.indexes()
    wanted = (('fullname', 'FieldIndex'),
              ('firstname', 'FieldIndex'),
              ('lastname', 'FieldIndex'),
              ('nl_language', 'FieldIndex'),
              ('email', 'FieldIndex'),
              ('organization', 'FieldIndex'),
              )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)
