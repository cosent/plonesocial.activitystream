

Introduction
============

Plonesocial.activitystream is part of the `ploneintranet suite`_.

This package, ploneintranet.activitystream, provides a building block for Plone integrators who want to create a custom social business solution in Plone.

If you're an end-user looking for a pre-integrated solution, you should install `ploneintranet.suite`_ instead.

Credits
-------

|Cosent|_

This package is maintained by Cosent_.

.. _Cosent: http://cosent.nl
.. |Cosent| image:: http://cosent.nl/images/logo-external.png 
                    :alt: Cosent


ploneintranet.activitystream
==========================

Plonesocial.activitystream uses the view ``@@stream`` view (provided by ploneintranet.core) on the SiteRoot.

If you have installed `ploneintranet.network`_ as well, and hit ``@@stream/network`` it will show only updates of people you're following.

A navigation bar is provided which detects the presence of `ploneintranet.network`_, as well as local workspaces that provide a local microblog, and displays nagivation options suitable for the context.

Plonesocial.activitystream also provides an "Activity Portal" view for the SiteRoot.
The Activity Portal view renders a portletmanager viewlet in which you can add an "Activity Stream" portlet (and also a "Microblog" portlet if you installed `ploneintranet.microblog`_.
This may look like a complex construct but it provides integrators with easy customization flex points, and it provides content managers with maximal control over what is rendered where, and in which sequence. Moreover by using a portlet for rendering, content managers can set various rendering options.
You can re-use the viewlet, or the portlet, as you see fit using ZCML overrides. YMMV.

The core rendering component, which is used by all views, is the ``stream_provider`` content provider.
Extracting the display logic to a separate content provider promotes re-use.
``activitystream_provider`` fetches `ploneintranet.microblog`_ updates, if microblog is installed.
It merges those with content creations and plone.app.discussion replies fetched from ZCatalog.
If `ploneintranet.network`_ is installed, it will filter the activity stream by "following" subscription.

To enable loose coupling, ploneintranet.activitystream does not depend on `ploneintranet.microblog`_ 
or `ploneintranet.network`_. Instead, it probes if those components are installed and available, or not.
Depending on the availability of those other ploneintranet components, ploneintranet.activitystream
adapts its behavior.

Plonesocial.activitystream looks nicer if you also install `ploneintranet.theme`_.

Build status
------------

Unit tests
~~~~~~~~~~

.. image:: https://secure.travis-ci.org/cosent/ploneintranet.activitystream.png
    :target: http://travis-ci.org/cosent/ploneintranet.activitystream
.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Social%20Activitystream
    :target: http://jenkins.ploneintranet.net/job/Plone%20Social%20Activitystream/

Robot tests for Plone Social and Plone Intranet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Social%20Suite
   :target: http://jenkins.ploneintranet.net/job/Plone%20Social%20Suite%20Master/badge/

.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Intranet%20Suite%20Master
   :target: http://jenkins.ploneintranet.net/job/Plone%20Intranet%20Suite%20Master/badge/




Roadmap
-------

An extensive roadmap_ for the ploneintranet suite is available on github.

.. _ploneintranet suite: https://github.com/cosent/ploneintranet.suite
.. _ploneintranet.suite: https://github.com/cosent/ploneintranet.suite
.. _ploneintranet.microblog: https://github.com/cosent/ploneintranet.microblog
.. _ploneintranet.activitystream: https://github.com/cosent/ploneintranet.activitystream
.. _ploneintranet.network: https://github.com/cosent/ploneintranet.network
.. _ploneintranet.theme: https://github.com/cosent/ploneintranet.theme
.. _ploneintranet.buildout: https://github.com/cosent/ploneintranet.buildout
.. _roadmap: https://github.com/cosent/ploneintranet.suite/wiki

Copyright (c) Plone Foundation
------------------------------

This package is Copyright (c) Plone Foundation.

Any contribution to this package implies consent and intent to irrevocably transfer all 
copyrights on the code you contribute, to the `Plone Foundation`_, 
under the condition that the code remains under a `OSI-approved license`_.

To contribute, you need to have signed a Plone Foundation `contributor agreement`_.
If you're `listed on Github`_ as a member of the Plone organization, you already signed.

.. _Plone Foundation: https://plone.org/foundation
.. _OSI-approved license: http://opensource.org/licenses
.. _contributor agreement: https://plone.org/foundation/contributors-agreement
.. _listed on Github: https://github.com/orgs/plone/people
