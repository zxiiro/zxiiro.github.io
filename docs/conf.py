import sphinx_bootstrap_theme

author = 'Thanh Ha'
copyright = '2018, Thanh Ha'
project = u'Thanh Ha'
version = '3.0'
release = version

extensions = []
language = None
master_doc = 'index'
source_suffix = '.rst'
templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

html_static_path = ['_static']
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    # 'analytics_id': 'UA-46385504-1',
    # 'canonical_url': 'http://www.zxiiro.ca/',

    'bootswatch_theme': "readable",
    'navbar_class': "navbar navbar-inverse",
    'navbar_links': [
        ("Resume", "https://docs.google.com/document/d/13R5JxDdB-1fz4w_bhpA6BVraD-Sy4eExp6Cz2s5NrUM/edit?usp=sharing"),
        ("Presentations", "presentations"),
        ("Writings", "writings/index"),
    ],
    'navbar_pagenav': False,
    'navbar_sidebarrel': False,
    'source_link_position': "footer",
}
html_title = 'Thanh Ha - zxiiro.ca'
htmlhelp_basename = 'sitedoc'
