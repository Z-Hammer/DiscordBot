import CatAPI
import AlcoholAPI
import OuraAPI
import Havenhaven

# Austin username = goob3142#0
# 'kitten' returns Cat Girl
def get_response(user_message: str, message) -> str:
        p_message = user_message.lower()
        p_author = message.author
        
        if p_message == 'cat':
            return (CatAPI.get_cat_image())
        elif p_message == 'drink':
            return (AlcoholAPI.get_alcohol())
        elif p_message[0:2] == 'hh':
            search_phrase = p_message.split('hh')
            return (Havenhaven.haven(search_phrase[1]))
        elif p_message == p_message:
            return (OuraAPI.oura_data(p_message))