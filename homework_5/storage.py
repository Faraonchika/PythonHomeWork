# -*- coding: utf-8 -*-
import datetime


BLOG_ENTRIES = [
    {
        'key': '1',
        'title': 'It\'s first entry',
        'text': """The term normalisation comes from the database world. It refers to transforming the schema of a 
        database to remove redundant information. Also, redundant information means the same data that is stored in more 
        than one place.""",
        'created_at': datetime.datetime.now(),
        'comments': [
            {
                'name': 'Julius Koronci',
                'text': 'Nice article'
            },
            {
                'name': 'Alexander Shirokov',
                'text': 'Thanks for good article'
            }
        ]
    },
{
        'key': '2',
        'title': 'It\'s second entry',
        'text': """The term normalisation comes from the database world. It refers to transforming the schema of a 
        database to remove redundant information. Also, redundant information means the same data that is stored in more 
        than one place.""",
        'created_at': datetime.datetime.now(),
        'comments': [
        ]
    }
]
