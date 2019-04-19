import logging
import getpass
from bwproject import BWProject

def create_proj_from_user():
    #set logging level
    logger = logging.getLogger("bwapi")
    #can also set to .DEBUG, .WARN, .ERROR or .CRITICAL (in descending order)
    logger.setLevel(logging.INFO)

    #get username and project from user
    username = input('Enter Brandwatch Username: ')
    projname = input('Enter the Project Name: ')

    #check if we already have a token, if not get password
    try:
        if username in open('tokens.txt').read():
            project = BWProject(username = username,
                                project = projname,
                                token_path = "tokens.txt",
                                grant_type = "partner-password",
                                client_id = "partner-api-client")
    except:
        password = getpass.getpass()
        project = BWProject(username = username,
                            project = projname,
                            password = password,
                            grant_type = "partner-password",
                            client_id = "partner-api-client")

    return(project, username, projname)

def queries_string_to_list(query_string, bw_queries):
    #queries with commas in them will be a problem when uploading rules that have a list of queries from user
    comma_queries = []
    for query in bw_queries.ids:
        if "," in query:
            comma_queries.append(query)

    query_list = []
    for query in comma_queries:
        if query in query_string:
            query_list.append(query)
            if (query+",") in query_string:
                query_string = string.replace(query_string, (query+","), "")
            elif (","+query) in query_string:
                query_string = string.replace(query_string, (","+query), "")
            else:
                query_string = ""
    if query_string:
        for query in query_string.split(","):
            query_list.append(query)

    return(query_list)
