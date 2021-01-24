from python_rako.bridge import Bridge
from python_rako.model import BridgeInfo, RoomLight, ChannelLight


def test_get_lights_from_discovery_xml(rako_xml):
    lights = Bridge.get_lights_from_discovery_xml(rako_xml)

    expected_lights = [
        RoomLight(room_id=5, room_title='Living Room', channel_id=0),
        ChannelLight(
            room_id=5,
            room_title="Living Room",
            channel_id=1,
            channel_type="Default",
            channel_name="Downlights",
            channel_levels="FF347F3F000000000000000000000000",
        ),
        ChannelLight(
            room_id=5,
            room_title="Living Room",
            channel_id=2,
            channel_type="Default",
            channel_name="Kitchen Downlights",
            channel_levels="FF337F3F000000000000000000000000",
        ),
        RoomLight(room_id=9, room_title='Bedroom 1', channel_id=0),
        ChannelLight(
            room_id=9,
            room_title="Bedroom 1",
            channel_id=1,
            channel_type="Default",
            channel_name="Downlights",
            channel_levels="FFBF7F25000000000000000000000000",
        ),
        ChannelLight(
            room_id=9,
            room_title="Bedroom 1",
            channel_id=2,
            channel_type="Default",
            channel_name="LED",
            channel_levels="FFBF7F00000000000000000000000000",
        ),
    ]
    assert list(lights) == expected_lights


def test_get_bridge_info_from_discovery_xml(rako_xml):
    info = Bridge.get_bridge_info_from_discovery_xml(rako_xml)

    expected_info = BridgeInfo(
        version="2.4.0 RA",
        buildDate="Nov 17 2017 10:01:01",
        hostName="RAKOBRIDGE",
        hostIP="someip",
        hostMAC="somemac",
        hwStatus="05",
        dbVersion="-31",
        requirepassword=None,
        passhash="NAN",
        charset="UTF-8",
    )
    assert info == expected_info
