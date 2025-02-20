"""Constants for the Jellyfin integration."""

from typing import Final

from homeassistant.const import __version__ as hass_version

DOMAIN: Final = "jellyfin"

CLIENT_VERSION: Final = hass_version

COLLECTION_TYPE_MOVIES: Final = "movies"
COLLECTION_TYPE_MUSIC: Final = "music"

CONF_CLIENT_DEVICE_ID: Final = "client_device_id"

DATA_CLIENT: Final = "client"

ITEM_KEY_COLLECTION_TYPE: Final = "CollectionType"
ITEM_KEY_ID: Final = "Id"
ITEM_KEY_IMAGE_TAGS: Final = "ImageTags"
ITEM_KEY_INDEX_NUMBER: Final = "IndexNumber"
ITEM_KEY_MEDIA_SOURCES: Final = "MediaSources"
ITEM_KEY_MEDIA_TYPE: Final = "MediaType"
ITEM_KEY_NAME: Final = "Name"

ITEM_TYPE_ALBUM: Final = "MusicAlbum"
ITEM_TYPE_ARTIST: Final = "MusicArtist"
ITEM_TYPE_AUDIO: Final = "Audio"
ITEM_TYPE_LIBRARY: Final = "CollectionFolder"
ITEM_TYPE_MOVIE: Final = "Movie"

MAX_IMAGE_WIDTH: Final = 500
MAX_STREAMING_BITRATE: Final = "140000000"


MEDIA_SOURCE_KEY_PATH: Final = "Path"

MEDIA_TYPE_AUDIO: Final = "Audio"
MEDIA_TYPE_NONE: Final = ""
MEDIA_TYPE_VIDEO: Final = "Video"

SUPPORTED_COLLECTION_TYPES: Final = [COLLECTION_TYPE_MUSIC, COLLECTION_TYPE_MOVIES]

USER_APP_NAME: Final = "Home Assistant"
USER_AGENT: Final = f"Home-Assistant/{CLIENT_VERSION}"
