
from jsonschema import validate

schema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'description': 'Livro',
        'required': ['titulo', 'autor', 'ano', 'preco'],
        'properties': {
            'titulo': {
                'bsonType': 'string',
                'description': 'Titulo do livro'
            },
            'autor': {
                'bsonType': 'string',
                'description': 'Autor do livro',
            },
            'ano': {
                'bsonType': 'int',
                'description': 'Ano de publicacao do livro',
                # sabe-se lá quando se escreveu o primeiro livro a.C.
                'minimum': -10000,
                'maximum': 2023,
            },
            'preco': {
                'bsonType': 'double',
                'description': 'Preco do livro',
                'minimum': 0,
            }
        }
    }
}
