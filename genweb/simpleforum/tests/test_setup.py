# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from genweb.simpleforum.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of genweb.simpleforum into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if genweb.simpleforum is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('genweb.simpleforum'))

    def test_uninstall(self):
        """Test if genweb.simpleforum is cleanly uninstalled."""
        self.installer.uninstallProducts(['genweb.simpleforum'])
        self.assertFalse(self.installer.isProductInstalled('genweb.simpleforum'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IGenwebsimpleforumLayer is registered."""
        from genweb.simpleforum.interfaces import IGenwebsimpleforumLayer
        from plone.browserlayer import utils
        self.failUnless(IGenwebsimpleforumLayer in utils.registered_layers())
