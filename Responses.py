import CatAPI
import AlcoholAPI
import OuraAPI

def get_response(user_message: str, message) -> str:
        p_message = user_message.lower()
        p_author = message.author
        
        if p_message == 'cat':
            return (CatAPI.get_cat_image())
        elif p_message == 'drink':
            return (AlcoholAPI.get_alcohol())
        elif p_message == p_message:
            return (OuraAPI.oura_data(p_message))
