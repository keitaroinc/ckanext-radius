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
    def group_facets(self, facets_dict, package_type):
        del facets_dict[u'license_id']
        return facets_dict

    # Removing licenses facet from group page
    def organization_facets(self, facets_dict, package_type):
        del facets_dict[u'license_id']
        return facets_dict
