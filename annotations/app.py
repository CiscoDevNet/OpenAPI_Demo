from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

# set openapi.info.title and openapi.info.version
app = APIFlask(__name__, title='Pet API', version='1.0.0', spec_path='/openapi')
app.config['SPEC_FORMAT'] = 'yaml'
app.config['AUTO_OPERATION_ID'] = True

# All the OpenAPI field config can be set with the corresponding attributes of the app instance:
# app.description = '...'

# openapi.info.description
app.config['DESCRIPTION'] = """
The description for this API. It can be very long and **Markdown** is supported.

In this example, the tags is manually set. However, in a real world application, it will be
enough to use the automatic tags feature based on blueprint, see the example for blueprint
tags under the "examples/blueprint_tags" folder:
"""

# openapi.info.contact
app.config['CONTACT'] = {
    'name': 'API Support',
    'url': 'https://developer.cisco.com'
}

# openapi.info.license
app.config['LICENSE'] = {
    'name': 'MIT',
    'url': 'https://opensource.org/licenses/MIT'
}

# openapi.info.termsOfService
app.config['TERMS_OF_SERVICE'] = 'http://example.com'

# The four info fields above can be set with the INFO key:
# app.config['INFO'] = {
#     'description': '...',
#     'termsOfService': 'http://example.com',
#     'contact': {
#         'name': 'API Support',
#         'url': 'http://www.example.com/support',
#         'email': 'support@example.com'
#     },
#     'license': {
#          'name': 'Apache 2.0',
#          'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
#      }
# }

# openapi.tags
app.config['TAGS'] = [
    {'name': 'Hello', 'description': 'The description of the **Hello** tag.'},
    {'name': 'Pet', 'description': 'The description of the **Pet** tag.'}
]

# If you don't need to set tag "description" or tag "externalDocs", just pass a list a string:
# app.config['TAGS'] = ['Hello', 'Pet']

# openapi.servers
app.config['SERVERS'] = [
    {
        'description': 'Development Server',
        'url': 'http://localhost:5000'
    }
]

# openapi.externalDocs
app.config['EXTERNAL_DOCS'] = {
    'description': 'Find more info here',
    'url': 'https://apiflask.com/docs'
}

pets = [
    {'id': 0, 'name': 'Kitty', 'category': 'cat'},
    {'id': 1, 'name': 'Coco', 'category': 'dog'},
    {'id': 2, 'name': 'Flash', 'category': 'cat'}
]


class PetIn(Schema):
    name = String(
        required=True,
        validate=Length(0, 10),
        metadata={'title': 'Pet Name', 'description': 'The name of the pet.'}
    )
    category = String(
        required=True,
        validate=OneOf(['dog', 'cat']),
        metadata={'title': 'Pet Category', 'description': 'The category of the pet.'}
    )


class PetOut(Schema):
    id = Integer(metadata={'title': 'Pet ID', 'description': 'The ID of the pet.'})
    name = String(metadata={'title': 'Pet Name', 'description': 'The name of the pet.'})
    category = String(metadata={'title': 'Pet Category', 'description': 'The category of the pet.'})


@app.get('/')
@app.doc(tags=['Hello'])
def say_hello():
    """Just Say Hello

    It will always return a greeting like this:
    ```
    {'message': 'Hello!'}
    ```
    """
    return {'message': 'Hello!'}


@app.get('/pets/<int:pet_id>')
@app.output(PetOut, description='The pet with given ID')
@app.doc(tags=['Pet'], operation_id='getPetDetails')
def get_pet(pet_id):
    """Get a Pet

    Get details for the pet with `pet_id` identifier.
    """
    if pet_id > len(pets) - 1 or pets[pet_id].get('deleted'):
        abort(404)
    return pets[pet_id]


@app.get('/pets')
@app.output(PetOut(many=True), description='A list of pets')
@app.doc(tags=['Pet'])
def get_pets():
    """Get All Pet

    Get all pets in the database.
    """
    return pets


@app.post('/pets')
@app.input(PetIn)
@app.output(
    PetOut,
    201,
    description='The pet you just created',
    links={'getPetById': {
        'operationId': 'getPet',
        'parameters': {
            'pet_id': '$response.body#/id'
        }
    }}
)
@app.doc(tags=['Pet'])
def create_pet(data):
    """Create a Pet

    Create a pet with given data. The created pet will be returned.
    """
    pet_id = len(pets)
    data['id'] = pet_id
    pets.append(data)
    return pets[pet_id]


@app.patch('/pets/<int:pet_id>')
@app.input(PetIn(partial=True))
@app.output(PetOut, description='The updated pet')
@app.doc(tags=['Pet'])
def update_pet(pet_id, data):
    """Update a Pet

    Update a pet with given data, the valid fields are `name` and `category`.
    """
    if pet_id > len(pets) - 1:
        abort(404)
    for attr, value in data.items():
        pets[pet_id][attr] = value
    return pets[pet_id]


@app.delete('/pets/<int:pet_id>')
@app.output({}, status_code=204, description='Empty')
@app.doc(tags=['Pet'])
def delete_pet(pet_id):
    """Delete a Pet

    Delete a pet with specific ID. The deleted pet will be renamed to `"Ghost"`.
    """
    if pet_id > len(pets) - 1:
        abort(404)
    pets[pet_id]['deleted'] = True
    pets[pet_id]['name'] = 'Ghost'
    return ''

