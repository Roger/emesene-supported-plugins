import songretriever
import DBusBase

class BansheeHandler(DBusBase.DBusBase):
    '''Handler for banshee'''
    NAME = 'Banshee'
    DESCRIPTION = 'Music handler for banshee'
    AUTHOR = 'Adolfo Fitoria'
    WEBSITE = 'www.emesene.org'

    def __init__(self, main_window = None,
                 iface_name = 'org.bansheeproject.Banshee',
                 iface_path = '/org/bansheeproject/Banshee/PlayerEngine'):
        DBusBase.DBusBase.__init__(self, main_window, iface_name, iface_path)

    def is_playing(self):
        '''Returns True if a song is being played'''
        if self.is_running():
            if self.iface.GetCurrentState() == "playing":
                return True
        return False

    def get_current_song(self):
        '''Returns the current song in the correct format'''
        if self.is_playing():
            info = self.iface.GetCurrentTrack()
            return songretriever.Song(info.get('artist', '?'),
                info.get('album', '?'),
                info.get('name', '?'))

        return None

