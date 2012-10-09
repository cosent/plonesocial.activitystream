Introduction
============

Plonesocial.activitystream is part of the `plonesocial suite`_.

This package, plonesocial.activitystream, provides a building block for Plone integrators who want to create a custom social business solution in Plone.

If you're an end-user looking for a pre-integrated solution, you should install `plonesocial.suite`_ instead.


plonesocial.activitystream
==========================

Plonesocial.activitystream provides a standalone ``@@stream`` view on the SiteRoot.
If you have installed `plonesocial.network`_ as well, ``@@stream`` will show only updates of people you're following.
If you have not installed `plonesocial.network`_, or if you hit ``@@stream/explore``, it will show the unfiltered full site activity feed.

Plonesocial.activitystream also provides an "Activity Portal" view for the SiteRoot.
The Activity Portal view renders a portletmanager viewlet in which you can add an "Activity Stream" portlet (and also a "Microblog" portlet if you installed `plonesocial.microblog`_.
This may look like a complex construct but it provides integrators with easy customization flex points, and it provides content managers with maximal control over what is rendered where, and in which sequence. Moreover by using a portlet for rendering, content managers can set various rendering options.
You can re-use the viewlet, or the portlet, as you see fit using ZCML overrides. YMMV.

The core rendering component, which is used by all views, is the ``activitystream_provider`` content provider.
Extracting the display logic to a separate content provider promotes re-use.
``activitystream_provider`` fetches `plonesocial.microblog`_ updates, if microblog is installed.
It merges those with content creations and plone.app.discussion replies fetched from ZCatalog.
If `plonesocial.network`_ is installed, it will filter the activity stream by "following" subscription.

To enable loose coupling, plonesocial.activitystream does not depend on `plonesocial.microblog`_ 
or `plonesocial.network`_. Instead, it probes if those components are installed and available, or not.
Depending on the availability of those other plonesocial components, plonesocial.activitystream
adapts its behavior.


TODO
----

Link @username mentions for integration with `plonesocial.network`_ as soon as `plonesocial.microblog`_ supports @mentions indexes.


.. _plonesocial suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.microblog: https://github.com/cosent/plonesocial.microblog
.. _plonesocial.activitystream: https://github.com/cosent/plonesocial.activitystream
.. _plonesocial.network: https://github.com/cosent/plonesocial.network
.. _plonesocial.buildout: https://github.com/cosent/plonesocial.buildout

