import pygame
from elements.waiting_lobby_player import waiting_lobby_player

BLIT_LOCS = [
    (16, 140), (232, 140), (448, 140), (664, 140),
    (16, 580), (232, 580), (448, 580), (664, 580),
]

class WaitingRoomMainPanel:
    """
    An object that handles display of the left-side panel on the waiting lobby screen
    
    Mostly used for creating/displaying player components
    from `./elements/waiting_lobby_player.py`
    """
    
    def __init__(self):
        self.surface = pygame.surface.Surface((880, 720), pygame.SRCALPHA)
        
        self.players = [] # list of dicts {"username": str, "color": str, "is_host": bool, "component": Surface}
        
    def add_player(self, username: str, color: str, is_host = False):
        
        comp = waiting_lobby_player(username, color, is_host)
        
        self.players.append({
            "username": username,
            "color": color,
            "is_host": is_host,
            "component": comp
        })
        
        # blit the component on the screen
        
    def remove_player(self, username: str) -> bool:
        
        """
        Removes a player from the screen.
        Returns true if the specified username was found and removed, false otherwise
        """
        
        for player_obj in self.players:
            if player_obj["username"] == username:
                self.players.remove(player_obj)
                
                # Remove the component
                player_obj["component"].set_alpha(0)
                
                return True
            
        return False
    
    def generate_component(self) -> pygame.Surface:
        """
        Re-draw all players on the screen. Best to run this when the player list changes.
        
        Returns the `Surface` component that can be used in other elements.
        """
        
        self.surface = pygame.surface.Surface((880, 720), pygame.SRCALPHA)
        
        index = 0
        for player_obj in self.players:
            self.surface.blit(player_obj["component"], BLIT_LOCS[index])
            index += 1
        
        return self.surface