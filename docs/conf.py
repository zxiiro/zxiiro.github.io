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

html_theme = 'alabaster'
html_theme_options = {
    'analytics_id': 'UA-46385504-1',
    'canonical_url': 'http://www.zxiiro.ca/',
}

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

html_static_path = ['_static']
htmlhelp_basename = 'sitedoc'
