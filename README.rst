.. contents::

Introduction
============

Plonesocial.activitystream is part of the `plonesocial suite`_.

This package provides a building block for Plone integrators who want to create
a custom social business solution in Plone.

If you're an end-user looking for a pre-integrated solution,
you should install `plonesocial.suite`_ instead.


plonesocial.activitystream
==========================

Plonesocial.activitystream provides an "Activity Portal" view for the SiteRoot.

The Activity Portal view renders a viewlet in AboveContent in which a portletmanager lives in which you can add an "Activity Stream" portlet (and also a "Microblog" portlet if you installed plonesocial.microblog.

This may look like a complex construct but it provides integrators with easy customization flex points, and it provides content managers with maximal control over what is rendered where, and in which sequence. Moreover by using a portlet for rendering, content managers can set various rendering options.

You can re-use the viewlet, or the portlet, as you see fit using
ZCML overrides. YMMV.

status
------

Alpha. This package is under active development and changes in backward-incompatible and forward-incompatible ways.


Plonesocial
===========

Plonesocial consists of:

`plonesocial.suite`_
 An out-of-the-box social business experience integrating all of the plonesocial.* packages.
 If you're an end user, this is what you're looking for.

`plonesocial.microblog`_
 Status updates

`plonesocial.activitystream`_
 Lists content changes, discussion replies, and status updates

plonesocial.network
 Follow/unfollow of users

plonesocial.like
 Favoriting of content

`plonesocial.buildout`_
 Developer buildout. Not a Python package. Intended for Plonesocial developers only.

.. _plonesocial suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.microblog: https://github.com/cosent/plonesocial.microblog
.. _plonesocial.activitystream: https://github.com/cosent/plonesocial.activitystream
.. _plonesocial.suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.buildout: https://github.com/cosent/plonesocial.buildout

