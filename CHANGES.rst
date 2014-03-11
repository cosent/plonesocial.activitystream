Changelog
=========

0.5.6 (2014-03-11)
------------------

* Bind browserviews to INavigationRoot instead of ISiteRoot [gyst]

* Package distribution was fixed by adding classifiers, dependencies and
  fixing license version number as GPLv2; a MANIFEST.in file was also added.
  [hvelarde]

* Brazilian Portuguese translation was added.
  [hvelarde]

0.5.5 (2013-07-31)
------------------

* fix navigation template base url [gyst]

0.5.4 (2013-07-31)
------------------

* fix invalid zpt view action logic [gyst]

0.5.3 (2013-07-31)
------------------

* Fixed activity stream rendering when a user has been removed
  [thomasdesvenain]

* Activity stream links check we use view action for content
  to avoid direct download.
  [thomasdesvenain]

0.5.2 (2013-07-08)
------------------

* bump version, 0.5.0/0.5.1 sequence got mixed up by pypi upload problems [gyst]

0.5.0 (2013-07-04)
------------------

* update docs [Guido A.J. Stevens]
* tag urls should be global [Guido A.J. Stevens]
* finish IMicroblogContext implementation [Guido A.J. Stevens]
* make active tab check more robust [Guido A.J. Stevens]
* refactor Explore / My network traversal - default to Explore even if plonesocial.network is installed - removes inconsistency between configs - makes following home portal link to @@stream actually show a stream when coldstarting; [Guido A.J. Stevens]
* adapt navigation to presence of plonesocial.network [Guido A.J. Stevens]
* support highlighting of current view in navigation [Guido A.J. Stevens]
* consolidate optional imports into integration [Guido A.J. Stevens]
* move navigationbar from plonesocial.suite to plonesocial.activitystream [Guido A.J. Stevens]
* enable stream view on local microblog contexts [Guido A.J. Stevens]
* filter on users OR microblog context, not both [Guido Stevens]
* pep8 [Guido Stevens]
* fix message folder [tdesvenain]
* french translation [tdesvenain]
* symlink is back [tdesvenain]
* filtering on microblog context works with new API [tdesvenain]
* update changelog [Guido Stevens]
* Don't traceback on missing tag spec, fixes plonesocial.microblog#8 [Guido Stevens]
* If the stream is displayed in a microblog context, filter activity stream on activities within this context.   [tdesvenain]

0.4.3 (2013-04-29)
------------------

* pep8 [Guido Stevens]
* tag view should not filter on network [gyst]
* Plone 4.3 compatibility [thomasdesvenain]
* Dutch translation [maartenkling]

0.4.2 (2012-11-26)
------------------

* update changelog, release
* update travis config to new buildout [gyst]
* provide a virtualenv-enabled Travis buildout that can be debugged on a dev box [gyst]
* ignore dist [gyst]
* Added i18n support for portlets register [macagua]
* Updated contributors file and sync i18n script with plone domain, added i18n support for Generic Setup register Profiles [macagua]
* Updated contributors file and sync i18n script with plone domain, added i18n support for Generic Setup register Profile [macagua]
* Added i18n sync script [macagua]
* Added Manual POT template [macagua]
* Added Spanish l10n [macagua]
* Added more improvements about i18n support [macagua]
* Updated changelog [macagua]
* pep8/pyflakes [hvelarde]
* update Travis CI configuration to include pep8/pyflakes testing [hvelarde]
* update location of extended configuration as the plonetest repo was moved to GitHub [hvelarde]
* update list of ignored objects [hvelarde]
* no hard dependencies, have conditional integration now [gyst]
* bump version [gyst]
* symlink README.txt to mute dist warnings [gyst]
* update docs [gyst]
* Use conditional adaptation to avoid hard microblog dependency [gyst]
* cleanup buildout [gyst]
* add missing required packages [hvelarde]
* add Travis CI configuration [hvelarde]
* document discussion bug [gyst]

0.4.1 (2012-10-09)
------------------

* merge: enable plonesocial.network filters on @@stream [gyst]

0.4 (2012-10-09)
----------------

* update docs [gyst]
* fix dependency [gyst]
* reindent for better pep8 [gyst]
* more styling [gyst]
* catch unresolvable brains [gyst]
* tune styling [gyst]
* document mentions todo [gyst]
* integrate microblog status form into @@stream [gyst]
* refactor and protect against errors on microblog uninstall [gyst]
* provide tag and userid filters API on stream_provider [gyst]
* provide consistency with plonesocial.network @@profile [gyst]
* implement tag view as traversal, not getarg [gyst]
* GS name [gyst]
* extract activity stream rendering to a reusable provider [gyst]
* provide standalone @@stream view and @@stream_provider (noop for now) [gyst]
* rename activity_contentprovider -> activity_provider [gyst]
* encapsulate the portlet-manager-viewlet based activitystream_portal view [gyst]
* expose and filter on hashtags [gyst]
* show content tags [gyst]
* bump version [gyst]


0.3.3 (2012-08-13)
------------------

* arghh. Date is not a DateTime. Sort on max(effective, modified) instead. Refs #1. [gyst]

0.3.2 (2012-08-13)
------------------

* sort on Date, fixes #1: effective 1-1-1000 sorting bug [gyst]

0.3.1 (2012-05-29)
------------------

* fix i18n regression [gyst]

0.3 (2012-05-21)
----------------

* update changelog, readme [gyst]
* use defined accesscontrol, fix portletmanager rename [gyst]
* simplify package layout [gyst]
* extract activity rendering into contentprovider/adapter [gyst]
* activity type filters [gyst]
* adapterize activity stream data structures [gyst]
* tune i18n [gyst]
* switch from annotationstorage to a utility [gyst]
* move separate ZODB shard documentation to plonesocial.microblog [gyst]
* clean up view logic [gyst]
* credit Maurits [gyst]
* refactored storage backend [gyst]
* extract content model to plonesocial.microblog [gyst]
* enable fake data insertion / fix date bug [gyst]
* Added Poi response-like Activities. [maurits]
* Some sample code for using an extra ZODB. [maurits]
* bump version [gyst]

0.2 (2012-05-04)
----------------

* update doc [gyst]
* rename primary view in anticipation of other views in the future [gyst]
* make portlet automatically assignable [gyst]
* get rid of src dir indirection [gyst]
* delegate commentActions translations to p.a.d. [gyst]
* provide i18n for nl [gyst]
* sort on effective; fix date bug; tune styling [gyst]
* force inner aquisition to be safe [gyst]
* pixeltune [gyst]
* tune css [gyst]
* restrict activitystream viewlet to activitystream view, and update doc [gyst]
* backport manageportlets link [gyst]
* Revert "extracted standalone stream view to plonesocial.suite" [gyst]
* sort on created not modified [gyst]
* provide "compact" rendering option [gyst]
* tune doc [gyst]
* update documentation [gyst]
* add basic CSS [gyst]
* prototype implementation of activitystream [gyst]
* rename portletmanager viewlet [gyst]
* provide activitystream portlet [gyst]
* extracted standalone stream view to plonesocial.suite [gyst]
* wrap the portletmanager within the viewlet, register on SiteRoot only [gyst]
* add portletmanager [gyst]
* (empty) activity stream view for homepage [gyst]

0.1dev (unreleased)
-------------------

* initial checkin from ZopeSkel [gyst]
