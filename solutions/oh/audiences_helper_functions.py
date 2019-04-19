import json
import requests


def create_search_query_child(search_term_list, search_field, bool_operator='AND'):
    """ 
    given a list of search terms, and a search field to, 
    this function generates and a dict containing a 
    well-formed child query for the audiences app.

    search_term_list: a list of string values to search for
    search_field: a string, one of 'BIO', 'INTERESTS', 'TWEETS'...
    bool_operator: a string, one of ['AND', 'OR']

    returns: a dict containing a well formed child query.    
    """
    bool_operator = bool_operator.upper()
    if bool_operator not in ['AND','OR']:
        print('error. illegal operator', bool_operator)
        return []
    grandchildren = [] # initialise list for collection of search terms
    for search_term in search_term_list:
        grandchild = {"operator":"OR",     # <--- not used?
                      "field":search_field, 
                      "value":[search_term] 
                     }
        grandchildren.append(grandchild)
    child = {"operator":bool_operator, "children":grandchildren}
    return child


def add_search_term_to_query_child(query_child, search_term, search_field):
    """
    TO BE COMPLETED (tested):
    given a query child dict (assumed to be well-formed),
    add a search term and search field to it. 
    note that the operator applied to the terms is not changed.
    """
    grandchildren = query_child['children']
    new_grandchild = {'operator':'OR',     # <--- not used?
                      'field':search_field, 
                      'value':[search_term] }
    
    grandchildren.append(new_grandchild)
    query_child['children'] = grandchildren

    return query_child


def create_search_query_payload(list_of_children, query_id = None):
    """
    given a list of query children (in the form of dicts),import r
    this function packs them into a dict framework required 
    for the query payload
    """
    search_query = {
        'id':query_id, 
        'query':{
            'operator':'AND',   # obligatory top level operator
            'children':list_of_children
        }
    }
    return search_query


def create_search_query_payload_json(list_of_children, query_id = None):
    """
    given a list of query children (in the form of dicts),import r
    this function packs them into the framework required 
    for the payload and casts it to a json string.
    """
    query = {
        'id':query_id, 
        'query':{
            'operator':'AND',   # obligatory top level operator
            'children':list_of_children
        }
    }
    query_payload = json.dumps(query) # converts dicts to json string
    return query_payload


def get_search_query_response(request_url, authorisation_key, payload, user_id=None):
    """
    sends payload (assumed to be a well formed query) to audience's request url
    and returns the response object.
    if you want to control the number of accounts returned, you need to edit 
    the request url.
    """
    char_count = str(len(payload))
    request_headers={
        'Authorization': f'bearer {authorisation_key}', 
        'Content-Type': 'application/json',
        'Content-Length': char_count,
        #       'userId': user_id
        }
    response = requests.post(request_url, headers=request_headers, data=payload)
    return response


def create_save_query_payload(search_query, query_name):
    """
    given a search query (assumed to be well-formed and 
    contain a list of ) this code
    returns the payload string needed to save the query under 
    the given name (query_name)
    """
    save_query  = {'name': query_name, 'query': search_query}
    return save_query


def create_save_query_payload_json(search_query, query_name):
    """
    given a search query (assumed to be well-formed and 
    contain a list of ) this code
    returns the payload string needed to save the query under 
    the given name (query_name)
    """
    save_query  = {'name': query_name, 'query': search_query}
    return json.dumps(save_query)


def save_audience_search(save_payload, authorisation_key, char_count, user_id):
    """
    sends payload (assumed to be a well formed query) to request url
    and returns the response object.
    if you want to limit the number of accounts returned, 
    """

    char_count = str(len(save_payload))
    url = 'https://audiences.brandwatch.com/api/audiences/audiences?newFormat=true'
    response = requests.post(
        url, 
        headers={'Authorization': f'bearer {authorisation_key}', 
                 'Content-Type': 'application/json', 
                 'Content-Length': char_count, 
                 'userId':user_id}, 
        data=save_payload)
    return response



