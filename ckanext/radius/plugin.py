"""
Copyright (c) 2021 Keitaro AB

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class RadiusPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'radius')
        toolkit.add_resource('assets', 'radius_assets')

    # IFacets

    # Removing licenses facet from dataset search page
    def dataset_facets(self, facets_dict, package_type):
        del facets_dict[u'license_id']
        return facets_dict

    # Removing licenses facet from organization page
    def group_facets(self, facets_dict, group_type, package_type):
        del facets_dict[u'license_id']
        return facets_dict

    # Removing licenses facet from group page
    def organization_facets(self, facets_dict, organization_type, package_type):
        del facets_dict[u'license_id']
        return facets_dict
