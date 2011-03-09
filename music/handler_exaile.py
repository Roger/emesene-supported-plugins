import songretriever
import DBusBase

class ExaileHandler(DBusBase.DBusBase):
    '''Handler for exaile'''
    NAME = 'Exaile'
    DESCRIPTION = 'Music handler for exaile'
    AUTHOR = 'Karasu'
    WEBSITE = 'www.emesene.org'

    def __init__(self, main_window = None,
                 iface_name = 'org.exaile.Exaile',
                 iface_path = '/org/exaile/Exaile'):
        DBusBase.DBusBase.__init__(self, main_window, iface_name, iface_path)

    def is_playing(self):
        '''Returns True if a song is being played'''
        if self.is_running():
            track_info = str(self.iface.Query())
            status = track_info.split(", ")[0]
            if status == "status: playing":
                return True
        return False

    def get_current_song(self):
        '''Returns the current song in the correct format'''
        if self.is_playing():
            artist = self.iface.GetTrackAttr('artist')
            if artist == None:
                artist = ""
            album = self.iface.GetTrackAttr('album')
            if album == None:
                album = ""
            title = self.iface.GetTrackAttr('title')
            if title == None:
                title = ""
            return songretriever.Song(artist, album, title)

