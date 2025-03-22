import os

from NewsPaper.venv import base_dir


class FrontendConfig:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(base_dir(), 'templates'), 'templates']
            ,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',

                    'blog.context_processors.categories',
                ],
            },
        },
    ]

    CKEDITOR_5_CUSTOM_CSS = 'css/ckeditor5/admin_dark_mode_fix.css'
    CKEDITOR_5_CONFIGS = {
        "default": {
            "toolbar": [
                "bold",
                "italic",
                "underline",
                "strikethrough",
                "link",
                'heading', ' | ', 'outdent', 'indent', ' | ',
                "bulletedList",
                "numberedList",
                "blockQuote",
                "imageUpload",  # Enable image upload
                "mediaEmbed",
                'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                'todoList', '|', '|',
                'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'removeFormat',
                'insertTable',
            ],
            "image": {
                "toolbar": [
                    "imageTextAlternative",
                    "imageStyle:full",
                    "imageStyle:side",
                ],
            },
        },
    }
