EasyNewsletter
==============

.. image:: https://secure.travis-ci.org/collective/Products.EasyNewsletter.png?branch=master
    :target: http://travis-ci.org/collective/Products.EasyNewsletter

.. image:: https://coveralls.io/repos/collective/Products.EasyNewsletter/badge.png?branch=master
    :target: https://coveralls.io/r/collective/Products.EasyNewsletter

EasyNewsletter is a simple but powerful newsletter/mailing product for Plone.


Features
========

* Support Text and HTML Newsletter (including images)

* Support manual written Newsletters/Mailings

* Plonish (can use Plone's Collections to collect content)

* Variable templates to generate newsletter content

* Subscribing / Unsubscribing and can use Plone Members/Groups as receivers
  (works also with Membrane)

* support for external subscriber sources (configured through a Zope utility)

* support for external delivery services (other than Plone MailHost)

* TTW customizeable output Template to generate nice HTML Newsletter

* Support personalized mails

* Support for sending daily issues automatically, based on collections
  (by cron or clock-server)

* mass import/export subscribers via csv

* support external filtering/manipulation (filter out or add more subscribers) plugins

Requirements
============

* [inqbus.plone.fastmemberproperties] speed up access of member properties
  (optional, you can installed it with Products.EasyNewsletter[all] in your
  buildout eggs list)

* 4.3 (tested)

Installation
============

1. Add Products.EasyNewsletter to your buildout

2. Run your buildout script

3. Restart zope

4. Install EasyNewsletter via Plone Management Interface

5. Add an "Newsletter Subscriber" portlet and select the EasyNewsletter
   (To this newsletter the subscribers will be added).


Documentation
=============

For more documentation please visit: http://packages.python.org/Products.EasyNewsletter/


Source Code
===========

Source code is at Github: https://github.com/collective/Products.EasyNewsletter

In Dec 2011 the source code repository was moved from `svn-collective <https://svn.plone.org/svn/collective/Products.EasyNewsletter/>`_ (do not use).

Bugtracker
==========

Issue tracker is at Github: https://github.com/collective/Products.EasyNewsletter/issues

There is an old one (do not use) at `plone.org <http://plone.org/products/easynewsletter/issues>`_


Authors
=======

* initial release: Kai Dieffenbach
* Maik Derstappen
* Andreas Jung
* Philip Bauer
* Timo Stollenwerk
* Dinu Gherman
* Peter Holzer
* Jens W. Klein
