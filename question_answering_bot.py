from retrieve_context import retrieve_context
from rewrite_user_query import rewrite_users_query

def get_intent(query):
    # NLU task : user looking for info?
    return 'info'

def manage_query(history, u_query):
    aug_query = ''
    if get_intent(u_query) == "info":
        query = rewrite_users_query(history, u_query)
        context, success = retrieve_context(query)

        if success == 0 :
            # i don't understand.
            aug_query = gen_prompt_for_no_retrieval(u_query)
        elif success == 1 :
            # this is what you are lookin for? use context["Text"] + form context["URL"]
            aug_query = gen_prompt_for_probable_response(context, u_query)
            
        elif success == 2 :
            #respond confidently. use context["Text"] + for more, you can check context["URL"]
            aug_query = gen_prompt_for_confident_response(context, u_query)
    return aug_query
    
def gen_prompt_for_confident_response(context, query):
    augmented_prompt = f""" Answer to the user's question friendly, structural and briefly based on this retrieved context. Refer your response to all the given URLs.
    Context:{context["Text"]}
    Query: {query}
    URLs: {context["URL"]} """
    return augmented_prompt
 
def gen_prompt_for_probable_response(context, query):
    augmented_prompt = f""" respond friendly, structural and briefly to the user. use the retrieved context if needed and Check with the user if this is the data that they are looking for. Refer your response to all the given URLs.
    Context:{context["Text"]}
    Query: {query}
    URLs: {context["URL"]} """
    return augmented_prompt

def gen_prompt_for_no_retrieval(query):
    augmented_prompt = f""" The answer to the user's query is not found in the data. 
    if it is a general question, answer it. if not, ask the user to be more specific about the data that they need.
    Query: {query}"""
    return augmented_prompt

