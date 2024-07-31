import ari

API_URL = 'http://192.168.30.53:8088/'
ARI_USERNAME = 'asterisk'
ARI_PASSWORD = '@Botirjon06'

client = ari.connect(API_URL, ARI_USERNAME, ARI_PASSWORD)


def on_stasis_start(event, channel):
    print(f"Channel {channel.json.get('caller')} entered Stasis app")

    caller = channel.json.get('caller', {}).get('number')
    called = channel.json.get('connected', {}).get('number')
    print(f"Caller: {caller}, Called: {called}")


def on_dial(event):
    print(f"Dial event: {event}")


def on_bridge_enter(event):
    print(f"Channel {event['channel']['id']} entered bride {event['bridge']['id']}")


client.on_channel_event('StasisStart', on_stasis_start)
client.on_event('Dial', on_dial)
client.on_event('BridgeEnter', on_bridge_enter)

client.run_forever()

