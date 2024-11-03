extensions = [
  'sphinxcontrib.confluencebuilder',
  'sphinx.ext.autosectionlabel',
              ]

confluence_lang_overrides = {
    'yaml+jinja': 'yaml'
}
version = '1.2.3'
release = '1.2.3'

confluence_publish = True
confluence_server_url = "xxxxxxxxxx-redacted-xxxxxxxxx"
confluence_space_key = "xxxxxxxxxx-redacted-xxxxxxxxx"
confluence_parent_page = "xxxxxxxxxx-redacted-xxxxxxxxx"

confluence_use_index = False
confluence_cleanup_purge = True
confluence_page_hierarchy = True
confluence_publish_orphan = True

confluence_publish_intersphinx = False
confluence_version_comment = 'Automatically generated using '+version
confluence_editor = 'v2'
confluence_permit_raw_html = 'html'
confluence_disable_notifications = True
confluence_prev_next_buttons_location = None
